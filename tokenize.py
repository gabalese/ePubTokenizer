import sys
import os

from src.epub import EPUB, InvalidEpub
from src.functions import tweets

import lxml.html

if __name__ == "__main__":
    twit = []
    try:
        epubfile = EPUB(os.path.abspath(sys.argv[1]))
    except InvalidEpub:
        pass
    for k in epubfile.contents:
        text = lxml.html.document_fromstring(epubfile.read(k.values()[0])).text_content()
        twit.extend(tweets(text))
    for i in twit:
        print i
