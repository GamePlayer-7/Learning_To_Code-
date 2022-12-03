dict1 = {'Hello': 'one', 'I': 'two', 'am': 'three', 'Python': 'four', 'Developer': 'five'}
dict2 = {'Hello': 'six', 'I': 'seven', 'am': 'eight', 'Software': 'nine', 'Developer': 'ten'}

print("First dictionary = ", dict1)
print("Second dictionary = ", dict2)

intersectdicts = {k: dict1[k] for k in dict1 if k in dict2} # for loop to see if K in dict1 also exists in dict2

print("Intersection of the given two dictionaries = ", (intersectdicts))

# Below is the Output :

First dictionary =  {'Hello': 'one', 'I': 'two', 'am': 'three', 'Python': 'four', 'Developer': 'five'}
Second dictionary =  {'Hello': 'six', 'I': 'seven', 'am': 'eight', 'Software': 'nine', 'Developer': 'ten'}
Intersection of the given two dictionaries =  {'Hello': 'one', 'I': 'two', 'am': 'three', 'Developer': 'five'}
