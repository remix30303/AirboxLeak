import argparse
import requests
import re

def ExtractDHCP(ip):
	url='http://{}/goform/getWlanClientInfo?rand='.format(ip)
	r = requests.get(url)
	html = str(r.content)
	print(html)
	
if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Aribox DHCP extract')
	parser.add_argument('-ip', action ='store', dest='ip', help="IP of router",default=max)
	results = parser.parse_args()
	ExtractDHCP(results.ip)
