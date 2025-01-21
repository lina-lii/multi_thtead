import socket
import threading

# Настройки сервера
HOST = ''  # Слушать на всех доступных интерфейсах
PORT = 9090  # Порт сервера

# Функция для обработки клиента
def handle_client(client_socket, client_address):
    print(f"Подключён новый клиент: {client_address}")
    try:
        while True:
            # Приём данных от клиента
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"Получено от {client_address}: {data.decode()}")
            
            # Отправляем данные обратно клиенту (эхо)
            client_socket.send(data)
            print(f"Отправлено клиенту {client_address}: {data.decode()}")
    except Exception as e:
        print(f"Ошибка с клиентом {client_address}: {e}")
    finally:
        print(f"Клиент отключён: {client_address}")
        client_socket.close()

# Создание сокета и запуск сервера
def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)  # Максимум 5 подключений в очереди
    print(f"Сервер запущен и слушает порт {PORT}...")

    try:
        while True:
            # Ожидание подключения клиента
            client_socket, client_address = server_socket.accept()
            # Создание нового потока для клиента
            client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
            client_thread.start()
    except KeyboardInterrupt:
        print("\nСервер остановлен вручную")
    finally:
        server_socket.close()
        print("Сервер полностью остановлен")

if __name__ == "__main__":
    start_server()
