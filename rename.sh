#!/bin/bash

# check for args
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <directory> <suffix>"
    exit 1
fi

# cd into the right directory
cd "$1" || exit 1

# Loop through all files in the current directory
for file in *; do
    # Check if the item is a file (not a directory)
    if [ -f "$file" ]; then
        # Remove spaces from the filename
        newname="${file// /}"

        # Append "_f22" before the file extension
        newname="${newname%.*}_$2.${newname##*.}"

        # Rename the file
        mv "$file" "$newname"

        echo "Renamed: $file -> $newname"
    fi
done
