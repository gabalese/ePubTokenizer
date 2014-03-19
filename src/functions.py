import re
from StringIO import StringIO
from settings import MAX_LENGHT, MIN_LENGHT


def tokenize(line):
    rephrase = re.compile(r'(?<!\w\s)[A-Z].{%d,%d}[!\?\.]' % (MIN_LENGHT, MAX_LENGHT))
    tokens = rephrase.findall(line)
    return tokens


def tweets(text):
    tweets_list = []
    if not isinstance(text, StringIO):
        text = StringIO(text.encode('UTF-8'))
    for line in text.readlines():
        tokens = tokenize(line)
        if len(tokens) > 0:
            tweets_list.extend(tokens)
    else:
        return tweets_list
