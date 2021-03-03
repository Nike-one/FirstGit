#access to string functions by importing re

#Search()- to search a string
import re
txt = "I am Nike-ONE ----> Nikhil Singh"
x = re.search("ONE",txt)
print(x)

#Output <_sre.SRE_Match object; span=(10, 13), match='ONE'> 

#Sub() - to replace a string with another
import re
y = re.sub("ONE","Here",txt)
print(y)

#Output I am Nike-Here ----> Nikhil Singh

#findall() - returns a list of all matched words
import re 
text = "Here you go go"
z = re.findall("go",text)
print(z)

#output ['go', 'go']

#split() - returns list for place you want split
import re
tex = "be the hustler"
a = re.split(" ",tex)
print(a)

#output ['be', 'the', 'hustler']

