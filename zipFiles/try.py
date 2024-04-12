try:
    result = 10 + '10'
except:
    print("hey it looks like you aren't adding correctly!")
else:
    print("Adding went well")
    print(result)

try:
    result = 10 + 10
except:
    print("hey it looks like you aren't adding correctly!")
else:
    print("Adding went well")
    print(result)

1 # if the code don't had an os error
try:
    f = open('testfile', 'w')
    f.write("write a test line")
except TypeError:
    print("There was a typeerror!")
except OSError:
    print("Hey you have an OS error")
finally:
    print("I always run")

2 # if the code had an os error
try:
    f = open('testfile', 'r')
    f.write("write a test line")
except TypeError:
    print("There was a typeerror!")
except OSError:
    print("Hey you have an OS error")
finally:
    print("I always run")

3 #if there is an error
try:
    f = open('testfile', 'r')
    f.write("write a test line")
except:
    print("There was a typeerror!")
finally:
    print("I always run")

4 # when there is error describe error
try:
    for i in ['a','b','c']:
        print(i**2)
except:
    print("Type error! Watch out")

5
try:
    x=5
    y=0
    z=x/y
except:
    print("Error!")
finally:
    print("All done")