#!/usr/bin/env python3
import http.server
import socketserver
import webbrowser
import os
from pathlib import Path
import socket

class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        # Suppress default logging for 404 errors (e.g., favicon.ico)
        if "404" not in format:
            super().log_message(format, *args)

    def handle_one_request(self):
        try:
            super().handle_one_request()
        except (BrokenPipeError, ConnectionResetError):
            # Silently handle broken pipe or connection reset errors
            pass

def main():
    # Define the directory containing the web content
    web_dir = Path.home() / "rmis_interface_ws/src/rmis_interface"
    if not web_dir.exists():
        print(f"Error: Directory {web_dir} does not exist.")
        print("Please ensure the 'rmis_interface' directory exists with web content.")
        return

    # Change to the directory containing the web content
    os.chdir(web_dir)

    # Set up the HTTP server
    PORT = 8000

    # Create TCPServer with SO_REUSEADDR to avoid port conflicts
    class ReusableTCPServer(socketserver.TCPServer):
        allow_reuse_address = True

    try:
        with ReusableTCPServer(("", PORT), QuietHandler) as httpd:
            print(f"Serving at http://localhost:{PORT}")
            # Open the default web browser
            webbrowser.open(f"http://localhost:{PORT}")
            # Start the server
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("Shutting down the web server...")
        httpd.server_close()
    except OSError as e:
        print(f"Error starting server: {e}")
        print("Port may be in use. Try closing other applications or changing the PORT in the script.")

if __name__ == "__main__":
    main()