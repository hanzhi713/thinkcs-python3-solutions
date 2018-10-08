import os


def get_dirlist(path):
    """
      Return a sorted list of all entries in path.
      This returns just the names, not the full path to the names.
    """
    dirlist = os.listdir(path)
    dirlist.sort()
    return dirlist


# remove trash.py in every sub-directories in a given directory tree
def clean(path):
    dirlist = get_dirlist(path)
    for f in dirlist:
        fullname = os.path.join(path, f)
        if os.path.isdir(fullname):
            os.remove(fullname + "\\trash.py")
            clean(fullname)


clean("Z:\\服务器客户端\\")
