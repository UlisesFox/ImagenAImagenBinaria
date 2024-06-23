import os
import socket

#si cliente 1 envia imagen a cliente 2
def handle_client(client_socket):

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

    # Cerrar la conexión con el cliente
    client_socket.close()

#si cliente 2 envia imagen a cliente 1
def handle_client2(client_socket):

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

    # Cerrar la conexión con el cliente
    client_socket.close()

# Configuración del servidor
host = '192.168.100.122'
#host = '192.168.137.221'
#host = 'localhost'
port = 12345
max_clients = 10

# Crear un socket del servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(max_clients)

print("\nServidor en espera de conexiones...")

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
        print("Error")