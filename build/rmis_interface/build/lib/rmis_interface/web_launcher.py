# ~/rmis_interface_ws/src/rmis_interface/rmis_interface/web_launcher.py

import os
import http.server
import socketserver
import webbrowser
from ament_index_python.packages import get_package_share_directory
def main():
    port = 8000
    package_share_dir = get_package_share_directory('rmis_interface')
    web_dir = os.path.join(package_share_dir, 'web')
    os.chdir(web_dir)

    handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(("", port), handler)

    print(f"Starting web server at http://localhost:{port}")
    webbrowser.open(f"http://localhost:{port}")
    httpd.serve_forever()
