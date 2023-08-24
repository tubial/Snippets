from os import listdir
from os.path import isfile, join

drive = "E:\\"
folder = "OneDrive - School District 38"

print([f for f in listdir(join(drive, folder)) if isfile(join(drive, f))])
