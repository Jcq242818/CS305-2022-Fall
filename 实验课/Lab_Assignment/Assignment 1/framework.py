from ast import For
from cgitb import reset
from concurrent.futures import process
from itertools import count
from re import S, sub
import socket
import threading
import traceback
from collections import namedtuple
from typing import *
from unittest import result
from xmlrpc.client import boolean

HTTPHeader = namedtuple('HTTPHeader', ['name', 'value'])


class HTTPRequest:
    def __init__(self, rsocket: socket.socket):
        """
            Read RFC7230: https://datatracker.ietf.org/doc/html/rfc7230#section-3

            3.  Message Format
            HTTP-message  = start-line
                              *( header-field CRLF )
                              CRLF
                              [ message-body ]

            start-line     = request-line / status-line

            3.1.1.  Request Line
                request-line   = method SP request-target SP HTTP-version CRLF
        """
        self.socket = rsocket
        # HTTP request fields
        self.headers: List[HTTPHeader] = list()
        self.method: str = ''
        self.request_target: str = ''  # We only need to handle absolute-path here.
        self.http_version: str = ''
        # HTTP request body info
        self.body_length = 0
        self.buffer = bytearray()

    def read_headers(self):
        """
        Read these structures from `self.socket`, format them and fill HTTPRequest object fields.

        HTTP-message   = method SP request-target SP HTTP-version CRLF
                         *( header-field CRLF )
                         CRLF

        :return:
        """
        # TODO: Task1, read from socket and fill HTTPRequest object fields
        # read from socket and get the url of the request
        recv_data: bytes = b''
        count: int = 1
        body_count: int = 0
        body: str = ""
        # we wait for all the data is received, then we can resolve the request message
        while True:
            recv_sub_data = self.socket.recv(2048)
            recv_data = recv_data + recv_sub_data
            if len(recv_sub_data) < 2048:
                break
        data = recv_data.decode().split('\r\n')
        self.method = data[0].split(' ')[0]
        self.request_target = data[0].split(' ')[1]
        self.http_version = data[0].split(' ')[2]
        for sub_data in data[1:]:
            # print(sub_data)
            sub_data_spilt = sub_data.split(' ')
            # print(sub_data_spilt)
            if sub_data_spilt[0] != "":
                self.headers.append(HTTPHeader(sub_data_spilt[0].split(":")[0], sub_data_spilt[1]))
                count = count + 1
            else: 
                count = count + 1
                break
        # Then came the entity part, and began to analyze the message
        for sub_body_data in data[count:]:
            if sub_body_data == data[-1]:
                # body_count +=1
                body = body + sub_body_data
                continue
            else:
                body = body + sub_body_data + "\r\n"
        # print(body_count)
        self.buffer = body.encode()
        # self.buffer = data[count:][0].encode()
        # Debug: print http request
        print(f"{self.method} {self.request_target} {self.http_version}")
        for h in self.headers:
            print(f"{h.name}: {h.value}")
        print()
        print(self.buffer.decode())

    def read_message_body(self) -> bytes:
        #这一套代码是这种写法 curl -v http://127.0.0.1:8080/post --data "{"data":"test", "junk":"ignore"}"
        # result: str = "{"
        # # TODO: Task 3: complete read_message_body here
        # process = self.buffer.decode()
        # print(process)
        # process_new = process.replace("{","")
        # process_newest = process_new.replace("}","")
        # process_newest = process_newest.replace(" ","")
        # print(process_newest)
        # processing = process_newest.split(",")
        # print(processing)
        # for h in processing:
        #     sub_proc = h.split(":")
        #     if h != processing[-1]:
        #         result = result + f"'{sub_proc[0]}':'{sub_proc[1]}', "
        #     else:
        #         result = result + f"'{sub_proc[0]}':'{sub_proc[1]}'" + "}"
        # print(result)
        # result = result.replace('\'', '"')
        # return result
        return self.buffer

    def get_header(self, key: str) -> Union[str, None]:
        for h in self.headers:
            if h.name == key:
                return h[1]
        return None


class HTTPResponse:
    def __init__(self, wsocket: socket.socket):
        self.socket = wsocket
        """
        status-line = HTTP-version SP status-code SP reason-phrase CRLF
        """
        self.http_version = "HTTP/1.1"
        self.status_code: int = 400
        self.reason: str = 'Bad Request'
        self.headers: List[HTTPHeader] = list()
        # store Header in this format: "Host: 127.0.0.1:8080" -> ('Host', '127.0.0.1')
        self.body: bytes = b''
        self.response = b''
    def write_all(self):
        """
        set status_line, and write status_line, headers and message body (if exists) into self.socket
        :return:
        """
        # TODO: Task1, construct response from fields and write binary data to socket
        self.response = '{} {} {}\r\n'.format(self.http_version, self.status_code, self.reason).encode()
        self.socket.send(self.response) # send response 
        for h in self.headers:
            self.socket.send('{}: {}\r\n'.format(h.name, h.value).encode()) # send response headers
        self.socket.send(b'\r\n') # send response \r\n for response body
        # Then if have any file we should transmit them
        self.socket.send(self.body)
        pass

    def add_header(self, name: str, value: str):
        self.headers.append(HTTPHeader(name, value))


class HTTPServer:
    def __init__(self, listen_port: int):
        self.listen_addr = "127.0.0.1"
        self.listen_port = listen_port
        self.host = f'{self.listen_addr}:{self.listen_port}'
        self.server_path = "data/"
        self.listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.listen_socket.bind((self.listen_addr, self.listen_port))
        self.router: List[Route] = list()
        # Task 3: Store POST data in this bucket.
        self.task3_data: str = ""
        # Task 5: Session Bucket
        self.session: Dict[str, Any] = dict()

    def run(self):
        self.listen_socket.listen()
        print(f"Server start listening at http://{self.host}/")
        while True:
            client, src = self.listen_socket.accept()
            print(f"[Server] Server accept connection from {src[0]}:{src[1]}")
            threading.Thread(target=self.__client_run__, args=[client, src]).run()

    def register_handler(self, path: str, handler, allowed_methods=None):
        if allowed_methods is None:
            allowed_methods = ['GET', 'HEAD', 'POST']
        self.router.append(Route(path, allowed_methods, handler))

    def __client_run__(self, client_socket: socket.socket, source_address):
        try:
            request = HTTPRequest(client_socket)
            request.read_headers()
            host = request.get_header("Host")
            response = HTTPResponse(client_socket)
            # To simplify the implementation of the HTTP server, we require clients not to reuse TCP connections
            response.add_header("Connection", "close")
            if host == self.host:
                path = request.request_target.split('?', maxsplit=1)[0]
                # print(path)
                route = self.__match_route__(path)
                if route:
                    if request.method in route.allowed_methods:
                        route.handler(self, request, response)
                    else:
                        (response.status_code, response.reason) = 405, "Method Not Allowed"
                else:
                    (response.status_code, response.reason) = 404, "Not Found"
            else:
                (response.status_code, response.reason) = 400, "Bad Request"
            # if request.method != "HEAD":
            response.write_all()
            # else: # Do not write the entity body if the request method is HEAD!
            #     response.response = '{} {} {}\r\n'.format(response.http_version, response.status_code, response.reason).encode()
            #     response.socket.send(response.response) # send response 
            #     for h in response.headers:
            #         response.socket.send('{}: {}\r\n'.format(h.name, h.value).encode()) # send response headers
            #         # response.socket.send(b'\r\n') # send response \r\n for response body
        except Exception:
            print(traceback.format_exc())
        finally:
            client_socket.close()
            print(f"[Server] Connection from {source_address} closed.")

    def __match_route__(self, path: str):
        """
        Match Route
        :param path: Request URL
        :return: matched Route instance
        """
        # match path
        ps = path.split('/') # split the request url into components, ps is a list 
        matched_len, matched_route = 0, None
        for route in self.router: # Pre-register urls
            rps = route.path.split('/') # split the Pre-register urls into components, rps is also a list 
            cnt = 0
            while cnt < min(len(rps), len(ps)):
                if rps[cnt] != ps[cnt]: # if the same level pieces is not equal, we should exit this loop
                    break
                cnt += 1
            if cnt > matched_len and cnt == len(rps):
                matched_len, matched_route = cnt, route
        # print(matched_route.path)
        return matched_route


class Route(NamedTuple):
    path: str
    allowed_methods: List[str]
    handler: Callable[[HTTPServer, HTTPRequest, HTTPResponse], None]
