
numberOfStars = int(input(''))

maxcharacters = numberOfStars+(numberOfStars-1)

for num in range(numberOfStars):
        numberOfSpaces =int( (maxcharacters-(2*num-1))/2)
        lineToBePrinted=''
        for space in range(numberOfSpaces):
            lineToBePrinted+=' '
        for star in range(num):
            lineToBePrinted+='* '
        print(lineToBePrinted)
