#!/usr/local/bin/python3
  
from urllib.parse import urlsplit
from urllib.parse import parse_qs
from urllib.parse import urlunsplit
import sys

def parse(safelink):
        print(urlunsplit(list(urlsplit(parse_qs(urlsplit(safelink).query)['url'][0]))[:3]+['','']))
        pass

def parselist(linklist):
        for link in linklist:
                parse(link)
                print()
        pass

if __name__=="__main__":
        if len(sys.argv) < 2:
                print('Error')

        print()
        parselist(sys.argv[1:])

