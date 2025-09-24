from http.server import HTTPServer, BaseHTTPRequestHandler
import subprocess
import os

class StreamlitHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        # Start Streamlit
        subprocess.Popen(['streamlit', 'run', 'Home.py'])
        
        # Redirect to Streamlit port
        self.wfile.write(b'<meta http-equiv="refresh" content="0;url=http://localhost:8501">')