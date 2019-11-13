


# SepalLengthCm  SepalWidthCm  PetalLengthCm  PetalWidthCm  Species
def readFile(name):
    with open(name) as file:
        rows = file.read().splitlines()
    print(rows)




def main():
    data = readFile("iris.txt")


if __name__ == "__main__":
    main()