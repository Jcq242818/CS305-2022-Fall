import socket

ok200 = [b'HTTP/1.0 200 OK\r\n',
         b'Connection: close'
         b'Content-Type:text/html; charset=utf-8\r\n',
         b'\r\n',
         b'<html><body>Hello World!<body></html>\r\n',
         b'\r\n']

noContent204 = [b'HTTP/1.0 204 No Content\r\n',
                b'Connection: close'
                b'Content-Type:text/html; charset=utf-8\r\n',
                b'\r\n',
                b'<html><body>204 No Content<body></html>\r\n',
                b'\r\n']

badRequest400 = [b'HTTP/1.0 400 Bad Request\r\n',
                 b'Connection: close'
                 b'Content-Type:text/html; charset=utf-8\r\n',
                 b'\r\n',
                 b'<html><body>400 Bad Request<body></html>\r\n',
                 b'\r\n']

notFound404 = [b'HTTP/1.0 404 Not Found\r\n',
               b'Connection: close'
               b'Content-Type:text/html; charset=utf-8\r\n',
               b'\r\n',
               b'<html><body>404 Not Found<body></html>\r\n',
               b'\r\n']

intern500 = [b'HTTP/1.0 500 Internal server error\r\n',
             b'Connection: close'
             b'Content-Type:text/html; charset=utf-8\r\n',
             b'\r\n',
             b'<html><body>500 Internal server error<body></html>\r\n',
             b'\r\n']

service503 = [b'HTTP/1.0 503 Service unavailable\r\n+',
              b'Connection: close'
              b'Content-Type:text/html; charset=utf-8\r\n',
              b'\r\n',
              b'<html><body>503 Service unavailable<body></html>\r\n',
              b'\r\n']


def web():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('127.0.0.1', 8080))
    sock.listen(10)
    while True:
        conn, address = sock.accept()
        data = conn.recv(2048).decode().split('\r\n')
        print(data[0])
        print(data[0].split(' '))
        res = notFound404

        s = data[0].split(' ')[1]
        if s == '/':
            res = ok200
        elif s == '/bad-request':
            res = badRequest400
        elif s == '/no-content':
            res = noContent204
        elif s == '/internal':
            res = intern500
        elif s == '/service':
            res = service503

        for line in res:
            conn.send(line)
        conn.close()


if __name__ == "__main__":
    try:
        web()
    except KeyboardInterrupt:
        pass
