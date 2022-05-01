import sys

def main(argv):
    if argv[1] != '-it':
        print('Error: Second command must be -it')
    if len(argv) == 3 and argv[2] != '--rm':
        print('Error: third command must be --rm (--rm is an optional command)')
    elif len(argv) == 3 and argv[2] == '--rm':
        print(input() + " you dumbass")
        print('Goodby')
    else:
        print(input() + " you dumbass")

    sys.exit()

main(sys.argv)

