# Part 1 
#Bug 1
def send_vibe():
    print("VibeCheck says: good energy only")
#Bug 2
def welcome_user():
    print("Welcome to VibeCheck!")
#Part 2 
#Bug 3
def show_mood():
   mood = "hyped"
   print(f"Today's mood is {mood}")
#Part 3
def make_shoutout(name, mood):
    return f"{name} is feeling {mood} today!"
#Part 4 
#Bug 4
def count_hype(likes, shares):
    total = likes +shares
    return total 
#Bug 5
send_vibe()
welcome_user()
show_mood()
#Bug 6
print(make_shoutout("Jordan", "creative"))
#Bug 7
print(make_shoutout("Alex", "happy"))
#Bug 8
print(count_hype(10, 5))

def final_message():
    print("Thanks for using VibeCheck!")
final_message()



