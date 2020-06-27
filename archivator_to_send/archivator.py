
# Python Archivator

from zipfile import ZipFile
import os
import sys

folder = sys.argv[1]
folderName = os.path.basename(folder) + '.zip'
extList = ['.pyc', '.tmp', '.zip']

placeInput = raw_input('Do you want to make an archive in this folder? y/n  ').lower()
if placeInput.startswith('n'):
    place = os.path.dirname(folder)
else:
    place = folder


zf = ZipFile(os.path.join(place, folderName), 'w')
for path, dirs, files in os.walk(folder):
    [zf.write(os.path.relpath(os.path.join(path, f))) for f in dirs]
    for f in files:
        ext = os.path.splitext(f)[-1]
        zfpath = os.path.relpath(os.path.join(path, f))
        if ext not in extList:
            zf.write(zfpath)
zf.close()
