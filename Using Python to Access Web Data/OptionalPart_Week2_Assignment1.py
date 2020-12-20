'''redacted version of two-line version of this Week2_Assignment1 using list comprehension'''

import re
print(sum([int(i) for i in re.findall('[0-9]+',open("regex_sum_1108393.txt").read())]))