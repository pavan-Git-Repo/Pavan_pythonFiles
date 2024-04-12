x = "aaajjjkkkrrqqaa"
#x = "aaaaaaaaaaaaaaa"
previous = x[0]
output = ''
c=1
i=1
while i<len(x):
    if x[i]==previous:
        c=c+1
    else:
        output=output+str(c)+previous
        previous=x[i]
        c=1
    if i==len(x)-1:
        output=output+str(c)+previous

    i=i+1
print(output)