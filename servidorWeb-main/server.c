#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <netinet/in.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <signal.h>
#include <sys/wait.h>

#define PUERTO 8000
#define BUFFER_SIZE 4096
#define DIRECTORIO_BASE "redes"

void handler(int sig) {
    while (waitpid(-1, NULL, WNOHANG) > 0);
}

const char* obtener_tipo_mime(const char* filename) {
    if (strstr(filename, ".html")) return "text/html";
    if (strstr(filename, ".jpg")) return "image/jpeg";
    if (strstr(filename, ".jpeg")) return "image/jpeg";
    if (strstr(filename, ".png")) return "image/png";
    if (strstr(filename, ".gif")) return "image/gif";
    return "application/octet-stream";
}

void enviar_respuesta(int cliente, const char* metodo, const char* ruta) {
    char path[1024];
    char buffer[BUFFER_SIZE];

    // Si la ruta es "/", usamos index.html por defecto
    if (strcmp(ruta, "/") == 0) {
        ruta = "/index.html";
    }

    snprintf(path, sizeof(path), "%s%s", DIRECTORIO_BASE, ruta);
    
    printf("\nRuta solicitada: %s\n", path);

    int archivo = open(path, O_RDONLY);
    if (archivo < 0) {
        perror("Error al abrir el archivo");
        const char* notfound = 
            "HTTP/1.1 404 Not Found\r\n"
            "Content-Type: text/html\r\n\r\n"
            "<h1>404 - Archivo no encontrado</h1>";
        send(cliente, notfound, strlen(notfound), 0);
        printf("\nRESPUESTA ENVIADA: \n%s", notfound);
        return;
    }

    struct stat st;
    fstat(archivo, &st);

    const char* tipo = obtener_tipo_mime(path);

    // Enviar cabecera 200 OK
    snprintf(buffer, sizeof(buffer),
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: %s\r\n"
        "Content-Length: %ld\r\n"
        "Connection: close\r\n\r\n",
        tipo, st.st_size);

    send(cliente, buffer, strlen(buffer), 0);
    printf("\nRESPUESTA ENVIADA: \n%s", buffer);

    // Enviar body de respuesta
    if (strcmp(metodo, "GET") == 0) {
        int leido;
        while ((leido = read(archivo, buffer, sizeof(buffer))) > 0) {
            send(cliente, buffer, leido, 0);
        }
    }

    close(archivo);
}

void manejar_cliente(int cliente) {
    char buffer[BUFFER_SIZE];
    int recibido = recv(cliente, buffer, sizeof(buffer) - 1, 0);
    if (recibido <= 0) return;
    buffer[recibido] = '\0';

    // Parsear el método y la ruta
    char metodo[16], ruta[1024];
    sscanf(buffer, "%s %s", metodo, ruta);

    printf("\nSE CONECTO NUEVO CLIENTE!\n");
    printf("\nSOLICITUD RECIBIDA: \n%s", buffer);

    // Verificar bad request
    if (sscanf(buffer, "%15s %1023s", metodo, ruta) != 2) {
        const char* badrequest = 
            "HTTP/1.1 400 Bad Request\r\n"
            "Content-Type: text/plain\r\n\r\n"
            "400 - Solicitud mal formada";
        send(cliente, badrequest, strlen(badrequest), 0);
        return;
    }

    // Validar método
    if (strcmp(metodo, "GET") != 0 && strcmp(metodo, "HEAD") != 0) {
        const char* noimplementado = 
            "HTTP/1.1 501 Not Implemented\r\n"
            "Content-Type: text/plain\r\n\r\n"
            "501 - Metodo no implementado";
        send(cliente, noimplementado, strlen(noimplementado), 0);
        return;
    }

    enviar_respuesta(cliente, metodo, ruta);
}

int main() {
    int servidor, cliente;
    struct sockaddr_in dir;
    socklen_t len = sizeof(dir);

    signal(SIGCHLD, handler);

    servidor = socket(AF_INET, SOCK_STREAM, 0);

    int opt = 1;
    setsockopt(servidor, SOL_SOCKET, SO_REUSEADDR, &opt, sizeof(opt));

    dir.sin_family = AF_INET;
    dir.sin_port = htons(PUERTO);
    dir.sin_addr.s_addr = INADDR_ANY;

    bind(servidor, (struct sockaddr*)&dir, sizeof(dir));
    listen(servidor, 10);

    printf("Servidor HTTP escuchando en http://localhost:%d\n", PUERTO);

    while (1) {
        cliente = accept(servidor, (struct sockaddr*)&dir, &len);
        if (cliente < 0) continue;

        if (fork() == 0) {
            close(servidor);
            manejar_cliente(cliente);
            close(cliente);
            exit(0);
        } else {
            close(cliente);
        }
    }

    close(servidor);
    return 0;
}
