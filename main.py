import os
from collections import defaultdict
import pandas as pd

def extract_last_n_chars(directory, n):
    # Get the absolute path of the script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the absolute path to the target directory
    directory_path = os.path.join(script_dir, directory)

    # Check if the specified directory exists
    if not os.path.exists(directory_path):
        print(f"Error: Directory '{directory_path}' not found.")
        return

    # Change directory to the specified directory
    os.chdir(directory_path)

    # Loop through all files in the directory
    for filename in os.listdir(directory_path):
        # Check if the item is a file (not a directory)
        if os.path.isfile(filename):
            # Extract the last n characters from the filename (file extension and quarter)
            extracted = filename[:-n]

            num = "" # keep track of course number
            for i in range(3, len(extracted)):
                if extracted[i].isnumeric():
                    num += extracted[i]
                else:
                    break
            if num != '':
                course = int(num)

                if course > 200: # found a graduate course
                    print(filename + " in " + directory_path)
                    os.remove(filename) # remove all grad classes

            # Append the extracted string to the result dictionary
            if extracted != '':
                classes[extracted].append(pd.read_csv(filename))
def saver(dictex):
    for key, val in dictex.items():
        val.to_csv("data_{}.csv".format(str(key)))

    with open("keys.txt", "w") as f: #saving keys to file
        f.write(str(list(dictex.keys())))

def loader():
    """Reading data from keys"""
    with open("keys.txt", "r") as f:
        keys = eval(f.read())

    dictex = {}
    for key in keys:
        dictex[key] = pd.read_csv("data_{}.csv".format(str(key)))

    return dictex

# Specify the directory and the value of n
paths = ["f22", "w23", "s23", "f23", "w24"]
n_value = 8
classes = defaultdict(list) # keep track of classes

# Call the function
for p in paths:
    extract_last_n_chars(p, n_value)

saver(classes)

# opening classes
classes = loader()
