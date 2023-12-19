#!/bin/bash

# clone the repos and call rename script
svn checkout https://github.com/UCSD-Historical-Enrollment-Data/2022Fall/trunk/overall
mv overall/ f22/
bash rename.sh f22/ "f22"

svn checkout https://github.com/UCSD-Historical-Enrollment-Data/2023Winter/trunk/overall
mv overall/ w23/
bash rename.sh w23/ "w23"

svn checkout https://github.com/UCSD-Historical-Enrollment-Data/2023Spring/trunk/overall
mv overall/ s23/
bash rename.sh s23/ "s23"

svn checkout https://github.com/UCSD-Historical-Enrollment-Data/2023Fall/trunk/overall
mv overall/ f23/
bash rename.sh f23/ "f23"

svn checkout https://github.com/UCSD-Historical-Enrollment-Data/2024Winter/trunk/overall
mv overall/ w24/
bash rename.sh w24/ "w24"
