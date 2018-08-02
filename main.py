import sys

def Token(object):
    pass

# Takes: file-descriptor
def main(fd):
    fcontents = fd.read()
    print(fcontents)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        fd = open(sys.argv[1], 'rb') # open read/binary
    else:
        fd = sys.stdin
    main(fd)

