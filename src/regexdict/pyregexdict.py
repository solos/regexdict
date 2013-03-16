#!/usr/bin/python
#coding=utf-8

import re
import json

def redict(regex, words):
    r = re.compile(regex)
    match_words = filter(r.match, words)
    return match_words


if __name__ == '__main__':
    dic = json.loads(open('dict.json', 'r').read())
    words = set(dic.keys())
    print map(lambda word: {word:dic[word]}, redict('.*gnu.*', words))
