import os
import sys
path = r'F:' + r'/Work/projects/' + input('Enter client name: ').title()


folders = \
[ ['abc',[]], 
  ['caches',[] ],
  ['flipbook',[] ],
  ['geo',[] ],
  ['precomp',[] ],
  ['textures',[] ],
  ['work',[] ],
  ['render',[] ],
  ]


def createFolder(path):
    if not os.path.exists(path):
        os.mkdir(path)

def build(root, data):
    if data:
        for d in data:
            name = d[0]
            path = os.path.join(root, name)
            createFolder(path)
            build(path, d[1])

projectname = r'/' + input('Enter projectname name: ').title()

if projectname:
    input("Done, Press Enter to continue...")
    fullPath = os.path.normpath(os.path.join(path, projectname))
    input("Done, Press Enter to continue...")
    createFolder(fullPath)
    build(fullPath, folders)

print (fullPath)

input("Done, Press Enter to continue...")