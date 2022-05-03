from http.server import HTTPServer, CGIHTTPRequestHandler

HOST = ""
PORT = 9000

if __name__ == "__main__":
    print(f"!local server started! on http://localhost:{PORT}")
    httpd = HTTPServer((HOST, PORT), CGIHTTPRequestHandler)
    httpd.serve_forever()

