'''
A regEx Ex is a sequence of character that forms  Ssearch pattern

RegEx can be used to check if a string contain the specified search pattern

Regex - module - built in package called  re




'''

import re

txt = "The rain in spain"

x = re.search("^The. *Spain$", txt)
print(x)


x=re.split("\s", txt)
print(x)