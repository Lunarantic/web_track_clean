#!/usr/local/bin/python3

from urllib.parse import urlsplit
from urllib.parse import parse_qs
from urllib.parse import urlunsplit
import sys


keep_args = ['www.youtube.com']
debug = False


def parse(safe_link):
	us = urlsplit(safe_link)
	if debug:
		print(us)
	usq = us.query
	if debug:
		print(usq)
	pq = parse_qs(usq)
	if debug:
		print(pq)
	url = pq['url']
	if debug:
		print(url)
	url0 = url[0]
	if debug:
		print(url0)
	us = urlsplit(url0)
	if debug:
		print(us)
	if us.netloc in keep_args:
		print(url0)
		return
	else:
		usq = list(us)[:3]
		if debug:
			print(usq)
		uus = urlunsplit(usq+['', ''])
		print(uus)
	pass


def parse_link_list(link_list):
	for link in link_list:
		parse(link)
		print()
	pass


if __name__=="__main__":
	if len(sys.argv) < 2:
		print('Error')

	print()
	parse_link_list(sys.argv[1:])

