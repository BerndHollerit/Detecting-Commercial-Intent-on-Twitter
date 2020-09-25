'''
Created on 29.07.2011

@author: Bernd
Takes POS-tagged tweets with annotations and creates an .arff
Tweets should be in the following format:
0this_DT auction_NN is_VBZ going_VBG to_TO be_VB funny_JJ ._.
1np_NN pink_JJ fridayi_NNS think_VBP im_NN going_VBG to_TO buy_VB it_PRP tomorrow_NN ._.
'''

import string

input_name = raw_input("Please enter input name: ")
parsed_input_name = 'c://hack/' + input_name + '.txt'
fh = open(parsed_input_name)
output_name = raw_input("Please enter output name: ")
parsed_output_name = 'c://hack/' + output_name + '.arff'

wholefile = """@relation is_ci
@attribute tweet string
@attribute postags string
@attribute ci{yes,no}
@data
"""

for line in fh.readlines():
    if '_V' in line: #only Tweets containing a verb
        s = line
        a = 1
        untaggedtweet = ""
        tags = ""
        ci = "no"
    
        if s[0] == "1":
            ci = "yes"
        s = s[1:]
    
        a = string.find(s, '_')
        b = string.find(s, ' ')
        while b != -1:
            untaggedtweet = untaggedtweet + s[:a] + " "
            tags = tags + s[a+1:b] + " "
            s = s[b+1:]
            a = string.find(s, '_')
            b = string.find(s, ' ')
    
        untaggedtweet = untaggedtweet.rstrip()
        untaggedtweet = untaggedtweet.lower()
        tags = tags.rstrip()
        arff = "'" + untaggedtweet + "','" + tags + "'," + ci
        print arff
        wholefile = wholefile + arff + "\n"
    
filename = parsed_output_name
file = open(filename, 'w')
file.write(wholefile)
file.close()
