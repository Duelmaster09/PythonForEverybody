'''In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers.

Data Files
We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/regex_sum_42.txt (There are 90 values with a sum=445833)
Actual data: http://py4e-data.dr-chuck.net/regex_sum_1108393.txt (There are 76 values and the sum ends with 206)'''

import re

file_name="regex_sum_1108393.txt"
handle=open(file_name)

total=0

for line in handle:
    line=line.strip()
    fetched_numbers=re.findall('[0-9]+',line)
    if len(fetched_numbers)>0:
        fetched_numbers=[int(i) for i in fetched_numbers]
        total+=sum(fetched_numbers)

print(total)