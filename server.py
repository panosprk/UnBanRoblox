from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib.parse import parse_qs

class MyServer(SimpleHTTPRequestHandler):

    def do_POST(self):
        if self.path == "/data":

            length = int(self.headers["Content-Length"])
            data = self.rfile.read(length).decode("utf-8")

            values = parse_qs(data)

            name = values.get("name", [""])[0]
            color = values.get("color", [""])[0]

            print("Email:", name)
            print("Password:", color)

            message = """
            <html>
            <body>
            <h2>Τα δεδομένα έφτασαν στον server!</h2>
            <p>Το POST request λειτουργεί σωστά.</p>
            </body>
            </html>
            """

            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(message.encode("utf-8"))

        else:
            self.send_error(404)


server = HTTPServer(("localhost", 8000), MyServer)

print("Ο server ξεκίνησε!")
print("http://localhost:8000")

server.serve_forever()