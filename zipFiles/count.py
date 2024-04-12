
def counter_list(lst):
    count = 0
    for item,num in enumerate(lst):
        if item!=num:
            count = 1
        else:
            count+=1
            return count
   # return count
print(counter_list([1,2,3,2,4,5,6,4,3,2,4,5]))

# counter
from collections import Counter
sentence = 'hi hello What are you doing'
print(Counter(sentence.split()))
print(Counter(sentence.lower().split()))
print(Counter(sentence.upper().split()))

from collections import Counter
s= 'hi hello What are you doing'
s = Counter(s)
print(s.most_common(2))
#most_common returns most repeated letters

