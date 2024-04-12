string = 'ABCDEFGHIJKLIMNOQRSTUZ'
subStringLength = 2
for i in range(0,int(len(string)/subStringLength)):
    substring = string[(i*subStringLength):(i*subStringLength)+subStringLength]
    print(substring)
    print(i,i*subStringLength,(i*subStringLength)+subStringLength)
print(i*subStringLength+subStringLength)
print(string[i*subStringLength+subStringLength:])