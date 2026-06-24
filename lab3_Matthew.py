# Matthew |lab 3| intro to python

# Ticket 1 


username = "Matthew"
#Predict: Matthew is 6 letters so it will print 7
#Explain:len() counts the amount of letters in a string 
print (len(username))

#ticket 2
name = "Matthew"

#Predict: M and W will print out as it counts 0 1 2 3 4 5 6
#Explain: The last index len(name) is minus 1 because it starts from zero.

print(name[0])
print(name[6])

#ticket 3
#Concatenation
first_name = "Matthew"
last = "Le"
full = first_name +" "+ last
print(full) 
name = "Matthew"
print(f"Welcome to Loop, {name}")

# Predict: The lines won't be similar as "urhandle"will be my name
# Explain:I think the f-string is a lot easier to type and memorize than concatenation


#ticket 4
#username[0] = "X" # run this, it breaks on purpose
#    TypeError: 'str' object does not support item assignment
username = "Matthew"
print(username.upper())
# Predict: I think if I run the broken line it will give me an error code
#Explain: Immutable means that the variable cannot be changed because the error code explains ' str' object does not support item assignment


#ticket 5
feed = ["hey, there. Still alive!", "In my happy place", "Present moment"]
print(len(feed))
print(feed[0])
#Predict: it should print out "3"
#Explain: I used print(feed[0])

#ticket 6
feed.append("Look at this toilet!")
print(feed)
#Predict: it should be the 3rd index.
#Explain: The fourth post is at index 3 because when counting index it starts from 0.

#ticket 7 
feed.pop(0)
feed.sort()
print(feed)
#predict: The "hey there. Still alive!" is removed, and the order should go from A-Z
#Explain:I used . pop(0) which removed the first string which is the 0 index, and also used .sort which sorts the strings or lists from A-Z.

#ticket 8

profile = {"username": "Matthew", "followers": 47, "verified": False}
print(profile["followers"])
#profile[0] #run this, it breaks on purpose
#KeyError: 0
#prediciton: it will print 47 followers, and I think profile[0] will cause an error because nothing is listed "0"
# Explanation: dictionaries look things up by key name because it's more special or destinctive rather than 0-100

#ticket 9
profile["followers"]+ 50
profile["bio"] = "Coding me summer away"
print(profile)
print(profile.get("age"))

#predict: It'll probably just print nothing since nothing is there to begin with
#explain: .get is safer because it doesn't crash if a key is missing.