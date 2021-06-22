'''
Challenge 14: Build a ZIP archive

Input: input directory path, list of file extensions, output path

Output: a ZIP file

>>> zip_all('.\\my_stuff', ['.jpg','.txt'], 'my_stuff.zip')
'''

import os
from zipfile import ZipFile

def zip_all(path, ext, output):
    with ZipFile(output,'w') as zipObj:
        for root, dirs, files in os.walk(path):
            rel_path = os.path.relpath(root, path)
            for file in files:
                name, ext = os.path.splitext(file)
                if ext.lower() in ext:
                    zipObj.write(os.path.join(root, file), arcname=os.path.join(rel_path,file))
                    

path = 'E:/c14Files'
output = 'E:/c14Files'
zip_all(path,['.txt','.jpg'],output)   
