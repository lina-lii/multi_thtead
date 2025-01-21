import socket

# Настройки сервера
SERVER_HOST = 'localhost'  # IP-адрес сервера
SERVER_PORT = 9090         # Порт сервера

# Подключение к серверу
def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((SERVER_HOST, SERVER_PORT))
        print(f"Подключён к серверу {SERVER_HOST}:{SERVER_PORT}")
        
        while True:
            message = input("Введите сообщение (или 'exit' для выхода): ")
            if message.lower() == 'exit':
                print("Отключение от сервера...")
                break
            client_socket.send(message.encode())  # Отправка сообщения серверу
            response = client_socket.recv(1024)  # Получение ответа от сервера
            print(f"Ответ от сервера: {response.decode()}")
    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        client_socket.close()
        print("Клиент завершил работу")

if __name__ == "__main__":
    start_client()
