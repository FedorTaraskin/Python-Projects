##1. What does the code for an empty dictionary look like?
emptyDictionary = {}
print(type(emptyDictionary))

##2. What does a dictionary value with a key 'foo' and a value 42 look like?
dict2 = {"foo": 42, "poo": 69}

##3. What is the main difference between a dictionary and a list?
##Dictionaries are unordered, and have pairs of keys-values attached to each other.

##4. What happens if you try to access spam['foo'] if spam is {'bar': 100}?
##Error lmao? I'll test it out
spam = {"bar": 100}
try:
    print(spam["foo"])
except:
    print("Error indeed on number 4.")

##5. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?
##Ugh, it's the same. Calling .keys() just uses a bit more resources by converting all of the keys from the dictionary into a separate list.
spam = {"pet": "cat"}
print(str("cat" in spam), str("cat" in spam.keys()))
spam = {"cat": "pet"}
print(str("cat" in spam), str("cat" in spam.keys()))

##6. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.values()?
##The first one searches for "cat" as a key, the second one does so but searching for a value.

##7. What is a shortcut for the following code?
if 'color' not in spam:
    spam['color'] = 'black'
##It is:
spam.get("color", "black")

##8. What module and function can be used to “pretty print” dictionary values?
##It is pprint:
import pprint
pprint.pprint(dict2)
print(dict2)