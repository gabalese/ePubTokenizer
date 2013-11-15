import re
from cStringIO import StringIO
import xml.etree.ElementTree as ET

from htmlentitydefs import entitydefs
from settings import MAX_LENGHT, MIN_LENGHT


def toText(textfile):
    textfile = textfile.replace('<br/>', ' ')
    parser = ET.XMLParser()
    parser.parser.UseForeignDTD(True)
    parser.entity.update(entitydefs)
    source = StringIO(textfile)
    root = ET.parse(source, parser)
    name = root.find(".//{http://www.w3.org/1999/xhtml}body")
    output = "".join([t for t in list(name.itertext())])
    return output


def tokenize(line):
    rephrase = re.compile(r'(?<!\w\s)[A-Z].{%d,%d}[!\?\.]' % (MIN_LENGHT, MAX_LENGHT))
    a = rephrase.findall(line)
    return a
