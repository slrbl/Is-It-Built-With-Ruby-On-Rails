import sys
import requests


def usage():
	print "Usage: "+sys.argv[0]+" <URL> <TIMEOUT>"
	sys.exit(1)

if len(sys.argv)<3:
	usage()

URL=sys.argv[1]
timeout=float(sys.argv[2])

RorTypicalRoutingError="No route matches [GET]"
WeirdRoute='/my/very/weird/odd/route'

if "http" in URL:
	URL=URL+WeirdRoute
else:
	URL="http://"+URL+WeirdRoute

r=requests.get(URL,timeout=timeout)
if RorTypicalRoutingError in r.text:
	sys.exit(0)
else:
	sys.exit(1)