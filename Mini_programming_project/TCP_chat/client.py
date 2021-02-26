import socket
import threading

# Loopback IP Address
HOST = '127.0.0.1'
PORT = 1216


def recv_msg(sock):
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                raise Exception
            print(data.decode())
        except:
            pass


def run_chat():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        thread = threading.Thread(target=recv_msg, args=(sock,))
        thread.daemon = True
        thread.start()

        while True:
            msg = input()
            if msg == "/quit":
                sock.send(msg.encode())
                break

            sock.send(msg.encode())


run_chat()