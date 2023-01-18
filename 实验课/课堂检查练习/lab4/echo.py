import socket

def echo():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('127.0.0.1', 7890))
    sock.listen(10)
    sock.settimeout(0.5)
    while True:
        try:
            conn, address = sock.accept()
            while True:
                data = conn.recv(2048)
                if data and data != b'exit':
                    # data1 = data.decode()
                    # conn.send(("\r\r"+data1+"\r\n").encode())
                    conn.send(data)
                    print(data)
                else:
                    conn.close()
                    break
        except socket.timeout:
            continue

  
if __name__ == "__main__":
    try:
        echo()
    except KeyboardInterrupt:
        pass