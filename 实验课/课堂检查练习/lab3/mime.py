import mimetypes as mt
import os

path = 'E:\\Desktop\\test'

allFiles = os.listdir(path)

print('%-25s %-25s'%('File Name', 'MIME Type'))

for f in allFiles:
    print('%-25s %-25s'%(f, mt.guess_type(f)[0]))
