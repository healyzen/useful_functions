"""
a collection of file editing functions and user input functions
jesse.naumanen@tuni.fi
"""
def read_integer_to_input(prompt = "Awaiting input: "):
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

def write_input_to_file(target_file):
    """
    write_input_to_file, writes user input to file in rows
    :return:
    """
    while True:
        u_input = input()
        if u_input == "":
            return
        print(f"{u_input}", file = target_file)

def get_file(filename):
    """
    getFile, fetches a file from same directory
    :param filename: the name of the file
    :return: target file, if possible to read
    """
    try:
        file = open(filename, mode="r")
    except OSError:
        print(f"There was an error in reading the file.")
        return 0
    file.close()
    return file

def write_file(filename):
    """
    writeFile, creates a file in write format
    :param filename: name of file
    :return:
    """
    try:
        file = open(filename, mode="w")
    except OSError:
        print(f"Writing the file {filename} was not successful.")
        return 0
    print("Enter rows of text. Quit by entering an empty row.")
    write_input_to_file(file)
    print(f"File {filename} has been written.")
    file.close()
    return

#main for testing purposes
def main():
    print("This is fiEdiTool")

if __name__ == "__main__":
    main()
