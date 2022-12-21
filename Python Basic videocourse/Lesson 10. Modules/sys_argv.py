import os, sys


def ping():
    print('pong')


def get_dir_info():
    print(os.listdir())


def hello(name):
    print('Hello, %s' % name)


command = sys.argv[1]

if command == 'ping':
    ping()
elif command == 'list':
    get_dir_info()
elif command == 'greet':
    name = sys.argv[2]
    hello(name)
