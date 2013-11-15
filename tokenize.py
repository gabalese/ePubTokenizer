import sys
import os
from src.epub import EPUB, InvalidEpub
from cStringIO import StringIO
from src.functions import toText, tokenize

if __name__ == "__main__":
    for i in sys.argv[1:]:
        try:
            epubfile = EPUB(os.path.abspath(i))
        except InvalidEpub:
            pass
        for k in epubfile.contents:
            text = toText(epubfile.read(k.values()[0]))
            text = StringIO(text.encode('UTF-8'))
            for i in text.readlines():
                for i in tokenize(i):
                    if len(i) > 0:
                        print i

