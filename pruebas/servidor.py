import os
import socket
import subprocess
import threading

def ejecutar_comando(comando):
    subprocess.run(comando)

def iniciar_servidor_aux():
    comando1 = ["python", "servidor_aux1.py"]
    hilo1 = threading.Thread(target=ejecutar_comando, args=(comando1,))
    hilo1.start()

    comando2 = ["python", "servidor_aux2.py"]
    hilo2 = threading.Thread(target=ejecutar_comando, args=(comando2,))
    hilo2.start()

    hilo1.join()
    hilo2.join()

#si cliente 1 envia imagen a cliente 2
def handle_client(client_socket):
    print(f"Conexión establecida con el cliente 1")
    # Crear la carpeta del cliente si no existe

    # Ruta completa al archivo de imagen en la carpeta del cliente
    image_path = os.path.join(f"ImagenEnviada1.jpg")

    # Manejo de la conexión con el cliente
    with open(image_path, "wb") as file:
        while True:
            # Recibir los datos del cliente
            image_data = client_socket.recv(4096)
            if not image_data:
                break

            # Guardar los datos de la imagen en el archivo
            file.write(image_data)

    print(f"Imagen recibida del cliente 1")

    # Cerrar la conexión con el cliente
    client_socket.close()
    print(f"Conexión cerrada con el cliente 1")

#si cliente 2 envia imagen a cliente 1
def handle_client2(client_socket):
    print(f"Conexión establecida con el cliente 2")
    # Crear la carpeta del cliente si no existe

    # Ruta completa al archivo de imagen en la carpeta del cliente
    image_path = os.path.join(f"ImagenEnviada2.jpg")

    # Manejo de la conexión con el cliente
    with open(image_path, "wb") as file:
        while True:
            # Recibir los datos del cliente
            image_data = client_socket.recv(4096)
            if not image_data:
                break

            # Guardar los datos de la imagen en el archivo
            file.write(image_data)

    print(f"Imagen recibida del cliente 2")

# Configuración del servidor
#host = '192.168.100.122'
#host = '192.168.137.221'
host = 'localhost'
port = 12345
max_clients = 10

# Crear un socket del servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(max_clients)

iniciar_servidor_aux()
print("Servidor en espera de conexiones...")


client_count = 0

while client_count < max_clients:
    # Esperar una conexión entrante
    client_socket, addr = server_socket.accept()
    client_count = int.from_bytes(client_socket.recv(1), byteorder='big')

    if client_count == 1:
        handle_client(client_socket)
    elif client_count == 2:
        handle_client2(client_socket)
    else:
        print("Cliente desconocido")