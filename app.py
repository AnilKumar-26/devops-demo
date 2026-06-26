from http.server import HTTPServer, BaseHTTPRequestHandler
import os

VERSION = os.environ.get("APP_VERSION", "2.0")
ENV = os.environ.get("ENVIRONMENT", "local")

class H(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        msg = f"Anil DevOps Engineer | version: {VERSION} | env: {ENV} | CAPSTONE COMPLETE"
        self.wfile.write(msg.encode())
    def log_message(self, *args):
        pass

HTTPServer(('', 8080), H).serve_forever()
