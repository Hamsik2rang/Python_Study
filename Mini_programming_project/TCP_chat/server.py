import socketserver
import threading

# Loopback IP Address
HOST = "127.0.0.1"
PORT = 8000
lock = threading.Lock()


class UserManager:
    def __init__(self):
        self.users = {}

    def add_user(self, username, connect, address):
        if username in self.users:
            connect.send("이미 등록된 닉네임입니다.\n".encode())
            return None

        lock.acquire()
        self.users[username] = (connect, address)
        lock.release()

        self.send_message_to_all(f"[{username}]님이 입장하셨습니다.")
        print(f"현재 대화 참여자 수 :[{len(self.users)}]")

        return username

    def remove_user(self, username):
        if username not in self.users:
            return

        lock.acquire()
        del self.users[username]
        lock.release()

        self.send_message_to_all(f"[{username}]님이 퇴장하셨습니다.")
        print(f"현재 대화 참여자 수 :[{len(self.users)}]")

    def message_handler(self, username, msg):
        if msg[0] != "/":
            self.send_message_to_all(f"[{username}]: {msg}")
            return

        if msg.strip() == "/quit":
            self.remove_user(username)
            return -1

    def send_message_to_all(self, msg):
        for connect, address in self.users.values():
            connect.send(msg.encode())


class TCPHandler(socketserver.BaseRequestHandler):
    user_manager = UserManager()

    def handle(self):
        print(f"[{self.client_address[0]}]")

        try:
            username = self.register_username()
            msg = self.request.recv(1024)
            while msg:
                print(msg.decode())
                if self.user_manager.message_handler(username, msg.decode()) == -1:
                    self.request.close()
                    break
                msg = self.request.recv(1024)
        except Exception as e:
            print(e)
        print(f"[{self.client_address[0]}] 접속 종료.")
        self.user_manager.remove_user(username)

    def register_username(self):
        while True:
            self.request.send("닉네임을 설정하세요: ".encode())
            username = self.request.recv(1024)
            username = username.decode().strip()
            if self.user_manager.add_user(username, self.request, self.client_address):
                return username


class ChattingServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


def run_server():
    print("채팅 서버를 시작합니다.")
    print("채팅 서버를 종료하려면 Ctrl+C를 입력하세요.")

    try:
        server = ChattingServer((HOST, PORT), TCPHandler)
        server.serve_forever()
    except KeyboardInterrupt:
        print("채팅 서버를 종료합니다.")
        server.shutdown()
        server.server_close()


run_server()