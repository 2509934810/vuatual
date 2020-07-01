import socket


conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

url = "182.61.200.7"
port = 80

conn.connect((url, port))

conn.send("hello".encode("utf-8"))

print(conn.recv(1024))
