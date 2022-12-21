import os, sys


# Create directories in the current working directory
def create_dirs():
    for i in range(1, 10):
        new_path = os.path.join(os.getcwd(), 'dir_{}'.format(i))
        os.mkdir(new_path)


# Deleting directories create above
def delete_dirs():
    for i in range(1, 10):
        path = os.path.join(os.getcwd(), 'dir_{}'.format(i))
        os.rmdir(path)


# delete_dirs()
