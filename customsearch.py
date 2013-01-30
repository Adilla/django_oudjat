#!/usr/bin/python2.7



"""Simple command-line example for Custom Search.

Command-line application that does a search.
"""

__author__ = 'adilla.susungi@gmail.com (Adilla Susungi)'


import pprint
from apiclient.discovery import build

def main():
    service = build("customsearch", "v1",
                  developerKey="AIzaSyBGCWOxtQZomkXAVSLmyg1XI_obyTe5P4E")

    res = service.cse().list(
        q='etudiant',
        cx='006966613857663466729:qjigtwbyr7o',
        ).execute()
    pprint.pprint(res)

if __name__ == '__main__':
    main()


