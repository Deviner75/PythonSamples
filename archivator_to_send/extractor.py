
# Python Extractor

from zipfile import ZipFile
import os
import sys

trg = os.path.join(os.path.dirname(sys.argv[1]), 'extracted')

zf = ZipFile(sys.argv[1], 'r')
for f in zf.namelist():
    full = os.path.join(trg, f)
    d = os.path.dirname(full)
    if d:
        if not os.path.exists(d):
            os.makedirs(d)
    if os.path.basename(f):
        print 'Write', full
        out = open(full, 'wb')
        out.write(zf.read(f))
        out.close()
zf.close()