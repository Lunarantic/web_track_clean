#!/usr/local/bin/python3

from urllib.parse import *
import sys


keep_args = ['www.youtube.com','library.stevens.edu']
for_q = [('www.google.com', '/search')]
red_q =  [('www.youtube.com', '/redirect')]
debug = False


def _check(n, p, fq):
    for q in fq:
        if n == q[0] and p == q[1]:
            return True
    return False

def _parse(url):
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
    try:
        url = pq['url']
        _parse(url)
    except KeyError:
        if _check(us.netloc, us.path, for_q):
            q = pq['q']
            if debug:
                print(q)
            usq = list(us)[:3]
            if debug:
                print(usq)
            uus = urlunsplit(usq + ['q='+quote_plus(q[0]), ''])
            print(uus)
        elif _check(us.netloc, us.path, red_q):
            try:
                url = pq['q']
                _parse(url)
            except KeyError:
                print('Re Oops')
        else:
            print('Oops')
    pass


def parse_link_list(link_list):
    for link in link_list:
        parse(link)
        print()
    pass


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Error')

    print()
    parse_link_list(sys.argv[1:])
