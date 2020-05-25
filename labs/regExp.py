"""
Nate Koch
Lab 8
CIS 211
"""

import re

# Exercise 1
#result = re.search(r'pattern', 'string')
#print(result.group(0))
#print(result[0])

# A
result = re.search(r'[A-Z]*211', 'CIS210 CIS211 CIS212')
print(result.group(0)) #CIS211
print(result[0]) #CIS211

# B
result = re.search(r'(xy){2}', 'xy xyxy xyxyxy')
print(result.group(0)) #xyxy
print(result[0]) #xyxy

# C
result = re.match(r'[A-Z|a-z]+211\.', 'Cis211.  CIS210 CIS211')
print(result.group(0)) #Cis211.
print(result[0]) #Cis211.

# D
'''
re.search finds where pattern is located in the string object and returns that portion of the string.
re.match looks only at the beginning of a string and returns the string object at the beginning if it matches the pattern.
'''


#Exercise 2
result = re.match(r'(?P<course1>[A-Z|a-z]*210) (?P<course2>.*211)', 'Cis210 CIS211 CIS212')
print(result.groupdict()) #{'course1': 'Cis210', 'course2': 'CIS211'}
# returns a dict with the specified keys and courses that matched the patterns as values.


# Challenge
result = re.match(r'a*b*', 'abb')
print(result)