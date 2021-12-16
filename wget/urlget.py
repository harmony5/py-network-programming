#!/usr/bin/python3
import urllib.request
import os
import sys


def f_save(filename, content, binary=True):
    """Creates a new file named filename."""

    mode = 'w'
    if binary:
        mode = 'wb'

    with open(filename, mode) as file:
        b = file.write(content)

    return b


def urlread(url):
    """Return the contents of a url. Raises IOError if couldn't read url."""
    try:
        urlfile = urllib.request.urlopen(url)
        return urlfile.read()
    except IOError as e:
        print("[!] Error reading url:", url)
        print(e.message)
        sys.exit(1)


def webget(url, name=None):
    """Save the content of a url to a file."""
    urlfile = urllib.request.urlopen(url)  # url file-like object

    filename = os.path.basename(urlfile.geturl())  # basename of the url
    if name:
        filename = name

    b = f_save(filename, urlfile.read())
    return b


if __name__ == '__main__':
    def main():
        args = sys.argv[1:]
        if not args:
            print("usage: urlget [-p path][-n filename] 'url'")
            sys.exit(1)

        path = ''
        if '-p' in args:
            path = args[args.index('-p') + 1]
            args.remove('-p')
            args.remove(path)

        name = ''
        if '-n' in args:
            name = args[args.index('-n') + 1]
            args.remove('-n')
            args.remove(name)

        if len(args) == 0:
            print("error: must specify one url")
            sys.exit(1)

        url = args[0]

        if path:
            if not os.path.exists(path):
                print("Building path:", path)
                os.makedirs(path)
            print("Moving to path:", path)
            os.chdir(path)

        if name:
            print("Retrieveing url '{}' to file '{}'".format(url, name))
            webget(url, name)
        else:
            print("Retrieving url '{}'".format(url))
            webget(url)
    main()
