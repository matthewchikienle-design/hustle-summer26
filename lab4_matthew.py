#Matthew Le | Lab 4 | intro to Python

# Ticket 1 
#prediction: The code will deny any age younger than 13 while granting access to ages over 13
ages =[17, 11, 25,13, 9]

for age in ages:
    if age >=13:
        print(f"{age}: Permission Granted")
    else:
        print(f"{age}: Permission Denied")
#Explain: The "age" variable in code holds an individual integer, this is also checked by the "<=13" which is where we can be granted or denied access

#Ticket 2
#Prediction: After typing "no" the system should stop because "no" is like the command to stop for "yes"
keep_checking = "yes"

while keep_checking == "yes":
    # Ask the user to enter an age
    age = int(input("enter an age to check: "))
    # Check if age is 13 or older and print the result
    if age >= 13:
        print (f"{age}: Access Granted")
    else:
        print(f"{age}: Access Denied")
    # Ask if they want to check another age
    # Store their answer in keep_checking
    keep_checking = input("Check another?") #Update it
#Explain: A while loop is the right choice because I believe it detects "unknown variables" so like whatever the suggested individual types

#Ticket 3
#Prediction: if you forget to break the statement the code will run infinitely
while True:
    entry = input("Enter something or type stop: ")
    if entry == "stop":
        break  #exits loop
    #otherwise keep going 
    age = int(entry)
    if age >= 13:
        print("Permission Granted")
    else: 
        print("Permission Denied")
    # Explain: instead of stopping from one order it loops continously

    #Ticket 4
def can_access(age):
    if age >=13:
        return True
    else: 
        return False 
    #List of Ages
    ages = [17, 11, 25, 13, 9]
if can_access(age):
    print(f"{age}: Access Granted ✅ ")
else:
    print(f"{age}: Access Denied ❌")
    #Explain: I'm not really sure, maybe because it shortens code or it helps out with repeat typing I'm not sure

    #Ticket 5
signups =[22, 10, 15, 8, 19, 13]
def signup_report(age_list):
    approved = 0
    print("- - - StreamPass Signup Report - - -")
    for n, age in enumerate(age_list, start=1):
        if can_access(age):
          print(f"Signup #{n}| age{age} - Access Granted") 
          approved += 1
        else: 
           print(f"Signup #{n}| age{age} - Access Denied")
    print(f"Approved: {approved} out of {len(age_list)}")
      

signup_report(signups)
#prediction: 4 should approve out of 6
#Explain: Lists, Functions, loops, string, operators