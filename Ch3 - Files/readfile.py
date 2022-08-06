# Read file

def main():
# read the file
    myfile = open("textfile.txt", "r")
    if myfile.mode == 'r':
        contents = myfile.read()
        print(contents)


if __name__ == "__main__":
    main()