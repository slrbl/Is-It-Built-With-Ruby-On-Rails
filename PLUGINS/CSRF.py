import sys
import requests

def usage():
	print "Usage: "+sys.argv[0]+" <URL> <TIMEOUT>"
	sys.exit(1)

if len(sys.argv)<3:
	usage()


url=sys.argv[1]
timeout=float(sys.argv[2])

data = {"username":"white", "password":"angel"}

possible_login_routes=['/login','/signin','/sign_in','/connexion','/profile/login','/profile/signin','/profile/sign_in','/profile/connexion']

if not "http" in url:
	url="http://"+url

s = requests.session()

for login_route in possible_login_routes:
	current_url=url+login_route
	r = s.post(current_url, data=data,timeout=timeout)
	print current_url
	if 'authenticity_token' in r.text:
		sys.exit(0)
sys.exit(1)



