'''
Created on 29.07.2011

@author: Bernd
Takes tweets, removes punctuation, sets them to lowercase
and appends " ."
'''

import re

input_name = raw_input("Please enter input name: ")
parsed_input_name = 'c://hack/' + input_name + '.txt'
fh = open(parsed_input_name)
output_name = raw_input("Please enter output name: ")
parsed_output_name = 'c://hack/' + output_name + '.txt'

#fh = open('c://hack/t1.txt')
wholefile = ""

for line in fh.readlines():
    s = line
    
    #removes all characters except for A-Z, a-z, 0-9 and spaces
    s = re.sub(r'[^\w ]', '', s)
    s = s.lower()
    s = re.sub(r"\s+", " ", s) #replaces multiple spaces by one space
    s = s.strip()
    s = s + " . "
    
    wholefile = wholefile + s + "\n"
    #print line
    #print s

print wholefile
    
filename = parsed_output_name
file = open(filename, 'w')
file.write(wholefile)
file.close()
