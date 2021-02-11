from http.server import HTTPServer, BaseHTTPRequestHandler
import win32api

PORT = 8000

code = {
    'volume_down': 0xAE,
    'volume_up': 0xAF,
    'track_next': 0xB0,
    'track_prev': 0xB1,
    'play_pause': 0xB3,
}

cmds = {
    'volume_down': { 'code': win32api.MapVirtualKey(code['volume_down'], 0), 'range': True },
    'volume_up': { 'code': win32api.MapVirtualKey(code['volume_up'], 0), 'range': True },
    'track_next': { 'code': win32api.MapVirtualKey(code['track_next'], 0), 'range': False },
    'track_prev': { 'code': win32api.MapVirtualKey(code['track_prev'], 0), 'range': False },
    'play_pause': { 'code': win32api.MapVirtualKey(code['play_pause'], 0), 'range': False }
}

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        path = [a for a in self.path.split('/') if len(a) > 0]

        if len(path) > 0:

            cmd = str(path[0])
            num = int(path[1]) if len(path) > 1 else 2
            if cmd in cmds: [win32api.keybd_event(code[cmd], cmds[cmd]['code']) for _ in range(0, num if cmds[cmd]['range'] else 1)]

        self.send_response(200)
        self.end_headers()

        self.wfile.write(b'OK')

httpd = HTTPServer(('', PORT), SimpleHTTPRequestHandler)
httpd.serve_forever()
