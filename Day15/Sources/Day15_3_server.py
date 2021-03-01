import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("192.168.63.46", 8000))  # ip주소, 포트번호 지정

server_socket.listen(0)  # 클라이언트의 연결요청을 기다리는 상태
client_socket, addr = server_socket.accept()  # 연결 요청을 수락함. 그러면 아이피주소, 포트등 데이터를 return
data = client_socket.recv(
    65535
)  # 클라이언트로 부터 데이터를 받음. 출력되는 버퍼 사이즈. (만약 2할 경우, 2개의 데이터만 전송됨)
print("받은 데이터:", data.decode())  # 받은 데이터를 해석함.
