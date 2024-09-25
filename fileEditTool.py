"""
a collection of file editing functions
jesse.naumanen@tuni.fi
"""
def readIntegerInput(prompt = "Awaiting input: "):
    """
    input reader, for integers
    :prompt: input prompt
    :return: first int passed
    """
    i = input(prompt)
    while True:

        try:
            i = int(i)
            if i > 0:
                return i
        except ValueError:
            i = input(prompt)

def writeInputToFile(fileToWrite):
    """
    writeInputToFile, writes user input to file in rows
    :return:
    """
    while True:
        uInput = input()
        if uInput == "":
            return
        print(f"{uInput}", file = fileToWrite)

def getFile(fileName):
    """
    getFile, fetches a file from same directory
    :param fileName: the name of the file
    :return: the file, if possible to read
    """
    try:
        file = open(fileName, mode="r")
    except OSError:
        print(f"There was an error in reading the file.")
        return 0
    file.close()
    return file

def writeFile(fileName):
    """
    writeFile, creates a file in write format
    :param fileName: name of file
    :return:
    """
    try:
        file = open(fileName, mode="w")
    except OSError:
        print(f"Writing the file {fileName} was not successful.")
        return 0
    print("Enter rows of text. Quit by entering an empty row.")
    writeInputToFile(file)
    print(f"File {fileName} has been written.")
    file.close()
    return

def main():
    print()

if __name__ == "__main__":
    main()
