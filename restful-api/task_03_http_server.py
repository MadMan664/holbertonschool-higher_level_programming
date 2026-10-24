#!/usr/bin/python3
"""A simple API built with the http.server module."""
import http.server
import json


class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    """Handle the GET requests of the API."""

    def _send(self, code, content_type, body):
        data = body.encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        """Route the request according to its path."""
        if self.path == "/":
            self._send(200, "text/plain", "Hello, this is a simple API!")
        elif self.path == "/data":
            data = {"name": "John", "age": 30, "city": "New York"}
            self._send(200, "application/json", json.dumps(data))
        elif self.path == "/status":
            self._send(200, "text/plain", "OK")
        elif self.path == "/info":
            info = {"version": "1.0",
                    "description": "A simple API built with http.server"}
            self._send(200, "application/json", json.dumps(info))
        else:
            self._send(404, "text/plain", "Endpoint not found")


def run(port=8000):
    """Start the server on the given port."""
    server = http.server.HTTPServer(("", port), SimpleAPIHandler)
    print("Serving on port {}".format(port))
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    run()
