import BaseHTTPServer
import lirc_commander

PORT = 10000

class SmallRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        commander = lirc_commander.LircCommander()
        commander.send(lirc_commander.TV, lirc_commander.POWER_OFF)
    def do_POST(self):
        print "Post"

def main():
    server = BaseHTTPServer.HTTPServer(('', PORT),
                                       SmallRequestHandler)
    print "Starting Server on %s" % PORT
    server.serve_forever()

if __name__ == "__main__":
    main()
