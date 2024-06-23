import socket

def guardar_imagen(imagen_bytes, nombre_archivo):
    with open(nombre_archivo, 'wb') as file:
        file.write(imagen_bytes)

def cliente2():
    # Configuración del socket
    #host = '192.168.100.122'
    #host = '192.168.137.221'
    host = 'localhost'
    port = 9000

    # Crear un socket TCP/IP
    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Conectar al servidor
    cliente_socket.connect((host, port))

    # Recibir los datos de la imagen
    imagen_bytes = b''
    while True:
        datos = cliente_socket.recv(1024)
        if not datos:
            break
        imagen_bytes += datos

    # Guardar la imagen con un nombre específico
    guardar_imagen(imagen_bytes, 'Recibida1.jpg')

    # Cerrar la conexión con el servidor
    cliente_socket.close()

if __name__ == '__main__':
    cliente2()