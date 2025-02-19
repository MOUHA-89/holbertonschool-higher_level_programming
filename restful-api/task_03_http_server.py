#!/usr/bin/python3

import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class SimpleAPIHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print(f"Received GET request for {self.path}")

        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == '/data':
            self.send_response(200)
            self.send_header("Content-type", "application/json; charset=utf-8")
            self.end_headers()
            response_data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(response_data).encode("utf-8"))
        elif self.path == '/status':
            self.send_response(200)
            self.send_header("Content-type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(json.dumps({"status": "OK"}).encode("utf-8"))
        elif self.path == '/info':
            self.send_response(200)
            self.send_header("Content-type", "application/json; charset=utf-8")
            self.end_headers()
            info_data = {"version": "1.0",
                         "description": "A simple API built with http.server"}
            self.wfile.write(json.dumps(info_data).encode("utf-8"))
        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(json.dumps({"error": "Endpoint not found"})
                             .encode("utf-8"))

    def do_POST(self):
        self.send_response(405)  # Method Not Allowed
        self.send_header("Content-type", "application/json; charset=utf-8")
        self.end_headers()
        self.wfile.write(json.dumps({"error": "POST method not allowed"})
                         .encode("utf-8"))


if __name__ == "__main__":
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, SimpleAPIHandler)
    print("Starting server on port 8000...")

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down the server...")
        httpd.server_close()
