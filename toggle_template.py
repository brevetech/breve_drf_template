import os
import re
import sys

from binaryornot.check import is_binary


def replace_text_in_file(selected_file, text_to_find, replace_text):
    """Replaces specified text with specified replace text in selected file

    :param selected_file: the selected file
    :type selected_file: str
    :param text_to_find: the selected text to find
    :type text_to_find: str
    :param replace_text: the selected text to replace with
    :type replace_text: str
    :returns(bool): True if file was modified, false otherwise
    """
    print(selected_file)
    if os.path.basename(selected_file) not in ["Procfile", ".env"]:
        if os.path.splitext(selected_file)[1] not in [".py", ".iml", ".xml"]:
            return

    print(f"Working on file: {selected_file}")
    with open(selected_file, "r") as file:
        data = file.read()
        if data != "":
            data = data.replace(text_to_find, replace_text)
            with open(selected_file, "w") as writefile:
                writefile.write(data)
                return True

    return False


def find_and_replace_in_directory(dir_name, text_to_find, replace_text):
    """Finds occurrences for a specified text in all files inside a directory
    and its subdirectories and replaces it with a specified replace text.

    :param(str) dir_name: Directory to navigate
    :param(str) text_to_find: Text to find
    :param(str) replace_text: Text to replace with
    :returns(int): number of files modified
    """

    # Get the list of all files in directory tree at given path
    file_list = []
    modified_files = 0
    for (dirpath, dirnames, filenames) in os.walk(dir_name):
        file_list += [os.path.join(dirpath, file) for file in filenames if os.path.join(dirpath, file) != __file__]

    # Print the files
    for file in file_list:
        if replace_text_in_file(file, text_to_find, replace_text):
            modified_files += 1

    return modified_files


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Incorrect usage. Use like: python toggle_template.py enable | disable")
        sys.exit(-1)

    if (x := sys.argv[1]) not in ["enable", "disable"]:
        print("Incorrect argument. Allowed values: [\"enable\", \"disable\"]")
        sys.exit(-1)

    print(x)

    y = find_and_replace_in_directory(os.getcwd(),
                                      r"{{project_name}}" if x == "disable" else "project_name",
                                      r"project_name" if x == "disable" else "{{project_name}}")

    print(f"Total files modified: {y}")
