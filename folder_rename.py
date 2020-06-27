import os

root = os.path.dirname(__file__)
files = os.listdir(root)
arg = []
for f in files:
    path = os.path.join(root, f)
    if os.path.isdir(path) and not f.startswith('.'):
        dfiles = os.listdir(path)
        for i in dfiles:
            if os.path.splitext(i)[-1] == '.txt':
                arg.append(os.path.join(path, i))
print(arg)

newName = raw_input('Enter name: ')

if newName:
    for i, f in enumerate(arg):
        d = os.path.dirname(f)
        name, ext = os.path.splitext( os.path.basename(f) )
        fName = newName + '_' + str(i+1).zfill(3) + ext
        fullPath = os.path.join(d, fName)
        os.rename(f, fullPath)

        f = open(f, 'w+')
        f.write("smtg")
        f.close()

input()