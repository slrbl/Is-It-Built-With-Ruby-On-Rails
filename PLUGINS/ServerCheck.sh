

usage() {
  echo "Usage: $0 <URL> <TIMEOUT>"
  exit 1
}

if [ "$1" = "" -o "$2" = "" ]; then
  usage
  
fi

url=$1
timeout=$2

curl --connect-timeout 2 -I $url | grep -i 'passenger\|WEBrick\|Unicorn\|Thin\|Mongrel'
