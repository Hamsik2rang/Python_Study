import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("192.168.63.46", 8000))  # 접속할 서버의 ip주소와 포트번호를 입력.
sock.send("Hello Server!".encode())  # 내가 전송할 데이터를 보냄.
