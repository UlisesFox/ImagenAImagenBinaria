import socket

def obtener_imagen2():
    with open('ImagenEnviada1.jpg', 'rb') as file:
        imagen_bytes = file.read()
    return imagen_bytes

def servidor2():
    # Configuración del socket
    host = 'localhost'
    port = 9000

    # Crear un socket TCP/IP
    servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Enlace del socket
    servidor_socket.bind((host, port))

    # Escuchar las conexiones entrantes (hasta 1 cliente)
    servidor_socket.listen(1)
    
    print('Esperando una conexión...')

    while True:
        # Esperar una conexión
        cliente_socket, cliente_direccion = servidor_socket.accept()
        print('Conexión establecida desde:', cliente_direccion)
        # Obtener la imagen
        imagen_bytes = obtener_imagen2()

        # Enviar los datos de la imagen al cliente
        cliente_socket.sendall(imagen_bytes)

        # Cerrar la conexión con el cliente
        cliente_socket.close()

if __name__ == '__main__':
        print("Iniciciando servidor_aux2.py\n")
        servidor2()
    