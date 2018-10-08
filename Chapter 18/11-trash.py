import os


def get_dirlist(path):
    """
      Return a sorted list of all entries in path.
      This returns just the names, not the full path to the names.
    """
    dirlist = os.listdir(path)
    dirlist.sort()
    return dirlist


# create trash.py in every sub-directories in a given directory tree
def trash(path):
    dirlist = get_dirlist(path)
    for f in dirlist:
        fullname = os.path.join(path, f)
        if os.path.isdir(fullname):
            handler = open(fullname + "\\trash.py", "w")
            handler.write("print('this is trash')\ninput()")
            handler.close()
            trash(fullname)


trash("C:\\users\\hanzh\\desktop\\1\\")
