import regex as re
allinform = re.findall("inform","we need to inform him with the latest information")
for i in allinform:
    print(i)
#
str = "we need to inform him with the latest information"
for i in re.finditer("inform", str):
    loctup = i.span()
    print(loctup)
#
str = "Sat, hat, mat, pat"
allstr = re.findall("[Shmp]at",str)
for i in allstr:
    print(i)
import re
str = "Sat, hat, mat, pat"
allstr = re.findall("[h-m]at",str)
for i in allstr:
    print(i)
#
result = re.search(r'cat|dog', 'The cat is here')
print(result)
#see the difference when we add the dots
reslt = re.findall(r'.at','The cat in the hat sat there.')
print(reslt)
rslt = re.findall(r'...at','The cat in the hat sat there.')
print(rslt)
answer = re.findall(r'..at..','The cat in the hat sat there.')
print(answer)
#
import re
str = "Sat, hat, mat, pat"
allstr = re.findall("[^h-m]at",str)
for i in allstr:
    print(i)
#
import re
my_str= "Sat, rat, mat, pat"
regex = re.compile("[r]at")
my_str= regex.sub("food", my_str)
print(my_str)
#
import re
randstr = "here is \\drogba"
print(randstr)
#
import re
randstr = "here is \\drogba"
print(re.search(r"\\drogba",randstr))
#
import re
randstr = '''
Keep the blue flag
flying high
chelsea
'''
print(randstr)
regex = re.compile("\n")
randstr = regex.sub("", randstr)
print(randstr)

import re
randstr = "123456"
print("Matches:", len(re.findall("\d",randstr)))

import re
randstr = "123456"
print("Matches:", len(re.findall("\d{5}",randstr)))

import re
randstr = "123456"
print("Matches:", len(re.findall("\d{7}",randstr)))

import re
number = "12 1234 13245 345678 2345678"
print("Matches:", len(re.findall("\d{5,7}",number)))

import re
number = "12 1234 13245 345678 2345678"
pattern = "12"
match = re.search(pattern,number)
print(match)
print(match.span())
print(match.start())
print(match.end())

# \d  digit    \w Alphanumeric   \s White space
#\D  non_digit  \W Non-alphanumeric  \S Non-whitespace

import regex as re
answer = re.findall(r'^\d','2 is a number')
answr =  re.findall(r'^\d','the 2 is a number')
ansr =  re.findall(r'\d$','the num number is 2')
#see the difference 
print(answer)
print(answr)
print(ansr)
#
import regex as re
phrase = 'There are 3 numbers 34 inside 5 this sentence'
pattern = r'[^\d]'
print(re.findall(pattern,phrase))
pattern = r'[^\d]+'
print(re.findall(pattern,phrase))
test_phrase = 'This is a string! But it has punctuation. How can we remove it?'
clean = re.findall(r'[^!.?]+',test_phrase)
print(clean) 
#see the difference there is we added space
clean = re.findall(r'[^!.? ]+',test_phrase)
print(clean)
print(' '.join(clean))

#
import regex as re
text = 'Only find hypen-words in this sentence. But you do not know how long-ish they  are'
pattern = r'[\w]+'
print(re.findall(pattern,text))
pattern = r'\w+-\w+'
print(re.findall(pattern,text))