import os
import shutil

basepath = 'C:\\Users\\petur\\testDir'

try:
    os.mkdir(basepath + "\\Text Documents\\")
    os.mkdir(basepath + "\\Images\\")
    os.mkdir(basepath + "\\Music\\")
    os.mkdir(basepath + "\\Shortcuts\\")
except FileExistsError as exc:
    print(exc)





with os.scandir(basepath) as entries:
    for entry in entries:
        if entry.is_file():
            if entry.name.endswith('.txt'):
                shutil.move(entry.path, basepath + "\\Text Documents\\" + entry.name)
            elif entry.name.endswith('.jpg'):
                shutil.move(entry.path, basepath + "\\Images\\" + entry.name)
            elif entry.name.endswith('.mp4'):
                shutil.move(entry.path, basepath + "\\Music\\" + entry.name)


