#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("C:/Users/Daneel/GitHub/for-fun/top_words")
from top_words import top_words

def download_articles():
    """ Downloads the articles by Pablo Iglesias at elpais.com,
        which are listed in pablo_iglesias_elpais.txt.
        Some character replacements need to be done to the downloaded
        files so they can be properly processed by extract_articles().
        Otherwise, some unicode coding error will pop up """

    import urllib
    testfile = urllib.URLopener()

    article_num = 0
    f = open("iglesias_elpais.txt","rb")
    for line in f.readlines():
        address=line.split(',')[0]
        if address.startswith('"http'):
            article_num += 1
            address = address.replace('"','')
            print address
            testfile.retrieve(address,"article_%i.html" % article_num)

def extract_articles():
    """ Extract the text of the articles downloaded as article_X.html,
        where X is a positive integer """

    import os
    import codecs
    listing = os.listdir('.')
    article_list = []
    isCuerpo=False
    prevline = ""
    for art in listing:
        if art.startswith('article_') and art.endswith('.html'):
            article_list.append("")
            for line in codecs.open(art,'r','utf8').readlines():
                if "Las revistas " in line or "Para poder comentar" in line:
                    isCuerpo = False
                if isCuerpo and line == "</div>" and prevline == "</div>":
                    isCuerpo = False
                    break
                if isCuerpo and line.startswith('<p>'):
                    article_list[-1] += " " + line.split('>')[1].split('<')[0]
                if 'cuerpo_' in line:
                    isCuerpo = True
                prevline = line

    return article_list

# download_articles()
artlist = extract_articles()

for ii,art in enumerate(artlist):
    print "----------------- ARTICLE ",ii+1," ------------------"
    print art
    print "Most common words on article",ii+1
    top_words(art,"spanish")

print ""
print "Most common words on all the articles"
top_words(" ".join(artlist),"spanish")
