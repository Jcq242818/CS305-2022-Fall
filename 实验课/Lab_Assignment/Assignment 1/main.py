import json
import random
import string
from typing import *
from urllib import request
from xmlrpc.client import Server
import config
import mimetypes
# We must initialize the mimetypes here, or we should have an error reading the .js file
from framework import HTTPServer, HTTPRequest, HTTPResponse


def random_string(length=20):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))


def default_handler(server: HTTPServer, request: HTTPRequest, response: HTTPResponse):
    response.status_code, response.reason = 404, 'Not Found'
    print(f"calling default handler for url {request.request_target}")


def task2_data_handler(server: HTTPServer, request: HTTPRequest, response: HTTPResponse):
    # TODO: Task 2: Serve static content based on request URL (20%)
    # get the request url from thr request message
    request_target = request.request_target
    if request.method == "GET":
        # match that request_target if our local url have this request_target url, so we should firstly try to open our local file
        try: 
            f = open("." + request_target, 'rb') 
            response.add_header("Content-Type", mimetypes.guess_type(request_target)[0])
            # If there is not any except(file is exist), we should return the response code "200"
            response.status_code, response.reason = 200, 'OK'
            response.body = f.read()
            response.add_header("Content-Length" , str(len(response.body)))
            f.close()
        except FileNotFoundError :
            # If the file doesn't exist we should return the response code "404"
            response.status_code, response.reason = 404, 'Not Found'
        print(f"calling task2_data_handler for url {request_target}")
    elif request.method == "HEAD":
        # match that request_target if our local url have this request_target url, so we should firstly try to open our local file
        try: 
            f = open("." + request_target, 'rb') 
            response.add_header("Content-Type", mimetypes.guess_type(request_target)[0])
            # If there is not any except(file is exist), we should return the response code "200"
            response.status_code, response.reason = 200, 'OK'
            response.add_header("Content-Length" , str(len(f.read())))
            f.close()
        except FileNotFoundError :
            # If the file doesn't exist we should return the response code "404"
            response.status_code, response.reason = 404, 'Not Found'
        print(f"calling task2_data_handler for url {request_target}")
    pass


def task3_json_handler(server: HTTPServer, request: HTTPRequest, response: HTTPResponse):
    # TODO: Task 3: Handle POST Request (20%)
    response.status_code, response.reason = 200, 'OK'
    if request.method == 'POST':
        binary_data = request.read_message_body()
        # str转化为调用json.loads是必须里面的键值对都用双引号括起来，否则会报错，因此前面read_message_body()需要对收到的实体体进行切片处理
        obj = json.loads(binary_data)
        # TODO: Task 3: Store data when POST
        server.task3_data = str(obj["data"])
        real_data = ("{"+ f"'data': '{server.task3_data}'" + "}").replace('\'', '"')
        with open(".\\post","w") as f:
            f.write(real_data)
        pass
    elif request.method == "GET":
        obj = {'data': server.task3_data}
        json_return = json.dumps(obj)
        response.add_header("Content-Type", mimetypes.guess_type("json_return.json")[0])
        return_binary = json_return.encode()
        response.add_header("Content-Length", str(len(return_binary)))
        response.body = return_binary
    elif request.method == "HEAD":
        obj = {'data': server.task3_data}
        json_return = json.dumps(obj)
        response.add_header("Content-Type", mimetypes.guess_type("json_return.json")[0])
        return_binary = json_return.encode()
        response.add_header("Content-Length", str(len(return_binary)))
        pass
   



def task4_url_redirection(server: HTTPServer, request: HTTPRequest, response: HTTPResponse):
    # TODO: Task 4: HTTP 301 & 302: URL Redirection (10%)
    response.status_code, response.reason = 302, 'Found'
    response.add_header("Location", "http://127.0.0.1:8080/data/index.html")
    pass


def task5_test_html(server: HTTPServer, request: HTTPRequest, response: HTTPResponse):
    response.status_code, response.reason = 200, 'OK'
    with open("task5.html", "rb") as f:
        response.body = f.read()


def task5_cookie_login(server: HTTPServer, request: HTTPRequest, response: HTTPResponse):
    # TODO: Task 5: Cookie, Step 1 Login Authorization
    obj = json.loads(request.read_message_body())
    if obj["username"] == 'admin' and obj['password'] == 'admin':
        response.status_code, response.reason = 200, 'OK'
        response.add_header("Set-Cookie", "Authenticated=yes")
        pass
    else:
        response.status_code, response.reason = 403, 'Forbidden'
        pass


def task5_cookie_getimage(server: HTTPServer, request: HTTPRequest, response: HTTPResponse):
    # TODO: Task 5: Cookie, Step 2 Access Protected Resources
    # 检查请求头部有没有Cookie，如果有就返回相应的图片资源
    if request.method == "GET":
        for h in request.headers:
            if f"{h.name}" == "Cookie" and f"{h.value}" == "Authenticated=yes":
                response.status_code, response.reason = 200, 'OK'
                with open(".\\data\\test.jpg", 'rb') as f : 
                    response.add_header("Content-Type", mimetypes.guess_type(".\\data\\test.jpg")[0])
                    response.body = f.read()
                    response.add_header("Content-Length" , str(len(response.body)))
            else:
                response.status_code, response.reason = 403, 'Forbidden'
    elif request.method == 'HEAD':
         for h in request.headers:
            if f"{h.name}" == "Cookie" and f"{h.value}" == "Authenticated=yes":
                response.status_code, response.reason = 200, 'OK'
                with open(".\\data\\test.jpg", 'rb') as f : 
                    response.add_header("Content-Type", mimetypes.guess_type(".\\data\\test.jpg")[0])
                    response.add_header("Content-Length" , str(len(f.read())))
            else:
                response.status_code, response.reason = 403, 'Forbidden'
    pass


def task5_session_login(server: HTTPServer, request: HTTPRequest, response: HTTPResponse):
    # TODO: Task 5: Cookie, Step 1 Login Authorization
    obj = json.loads(request.read_message_body())
    if obj["username"] == 'admin' and obj['password'] == 'admin':
        response.status_code, response.reason = 200, 'OK'
        session_key = random_string()
        while session_key in server.session:
            session_key = random_string()
        pass
        server.session = {"SESSION_KEY=":f"{session_key}"}
        response.add_header("Set-Cookie", "SESSION_KEY="+ f"{session_key}")
    else:
        response.status_code, response.reason = 403, 'Forbidden'


def task5_session_getimage(server: HTTPServer, request: HTTPRequest, response: HTTPResponse):
    # TODO: Task 5: Cookie, Step 2 Access Protected Resources
    # 检查请求头部有没有Cookie，如果有就返回相应的图片资源
    if request.method == "GET":
        for h in request.headers:
            if f"{h.name}" == "Cookie" and f"{h.value}" == "SESSION_KEY="+ server.session["SESSION_KEY="]:
                response.status_code, response.reason = 200, 'OK'
                with open(".\\data\\test.jpg", 'rb') as f : 
                    response.add_header("Content-Type", mimetypes.guess_type(".\\data\\test.jpg")[0])
                    response.body = f.read()
                    response.add_header("Content-Length" , str(len(response.body)))
            else:
                response.status_code, response.reason = 403, 'Forbidden'
    elif request.method == 'HEAD':
         for h in request.headers:
            if f"{h.name}" == "Cookie" and f"{h.value}" == "SESSION_KEY="+ server.session["SESSION_KEY="]:
                response.status_code, response.reason = 200, 'OK'
                with open(".\\data\\test.jpg", 'rb') as f : 
                    response.add_header("Content-Type", mimetypes.guess_type(".\\data\\test.jpg")[0])
                    response.add_header("Content-Length" , str(len(f.read())))
            else:
                response.status_code, response.reason = 403, 'Forbidden'
    pass


# TODO: Change this to your student ID, otherwise you may lost all of your points
YOUR_STUDENT_ID = 11911303

http_server = HTTPServer(config.LISTEN_PORT)
http_server.register_handler("/", default_handler)
# Register your handler here!
http_server.register_handler("/data", task2_data_handler, allowed_methods=['GET', 'HEAD'])
http_server.register_handler("/post", task3_json_handler, allowed_methods=['GET', 'HEAD', 'POST'])
http_server.register_handler("/redirect", task4_url_redirection, allowed_methods=['GET', 'HEAD'])
# Task 5: Cookie
http_server.register_handler("/api/login", task5_cookie_login, allowed_methods=['POST'])
http_server.register_handler("/api/getimage", task5_cookie_getimage, allowed_methods=['GET', 'HEAD'])
# Task 5: Session
http_server.register_handler("/apiv2/login", task5_session_login, allowed_methods=['POST'])
http_server.register_handler("/apiv2/getimage", task5_session_getimage, allowed_methods=['GET', 'HEAD'])

# Only for browser test
http_server.register_handler("/api/test", task5_test_html, allowed_methods=['GET'])
http_server.register_handler("/apiv2/test", task5_test_html, allowed_methods=['GET'])


def start_server():
    try:
        http_server.run()
    except Exception as e:
        http_server.listen_socket.close()
        print(e)


if __name__ == '__main__':
    start_server()
