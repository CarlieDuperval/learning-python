
def main():
    myfile = open("textfile.txt", "r")
    if myfile.mode == "r":
        fl = myfile.readline()
        for x in fl:
            print(x)
if __name__ == "__main__":
    main()