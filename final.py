
class Chore:
    def __init__(self, name, minutes):
        self.name = name
        self.minutes = self.check_minutes(minutes)
#Basically sets up the chore as a variable and makes name and minutes important
    def check_minutes(self, minutes):
        if minutes < 0:
            print("Minutes can't be negative, goofy! Please set to 0")
            return 0.0
        return minutes
# resets the time to 0 if someone puts a negative or something
    def get_info(self):
        return f"{self.name} - {self.minutes} mins"

class DailyChore(Chore):
    def __init__(self, name, minutes, time):
        super().__init__(name, minutes)
        self.time = time
#Creats a daily chore (another varibale) and sets it so it doesnt collide with the other classes
    def get_info(self):
        return f"[Daily] {super().get_info()} | Time of Day: {self.time}"

class WeeklyChore(Chore):
        def __init__(self, name, minutes, day):
            super().__init__(name, minutes)
            self.day = day

        def get_info(self):
            return f"[Weekly] {super().get_info()} | Day: {self.day}"
#Similar to the daily chore it makes a weekly chore as a variable, seperating from other classes
class ChoreTracker:
        def __init__(self):
            self.chores = [ DailyChore("Make your bed NOW", 5, "Morning"), DailyChore("Wash the Dishes pretty pleasee", 15, "Night"), WeeklyChore("Mow Lawn", 45, "Saturday"),  WeeklyChore("Clean that stinky bathroom", 30, "Sunday")]
#It tracks the chores
        def add_chore(self):
             chore_type = input("Hi, this is the chore tracker, and this app is here to remind you what you should be doing today! Daily or Weekly? (d/w): ")
             name = input("Chore name: ")
             minutes = float(input("Minutes needed: "))
#Basically sets it so the user/ player has to put something in to set the "reminder"
             if chore_type == "d":
                  time = input("Time of day( example, Morning): ")
                  self.chores.append(DailyChore(name,minutes,time))

             else:
                  day = input("Time of week ( example, Saturday): ")
                  self.chores.append(WeeklyChore(name, minutes, day))
#prints out examples to help user type whatever they put basically the "input"

        def display_all(self):
            for chore in self.chores:
                print(chore.get_info())
#Loops the chores and prints
tracker = ChoreTracker()
tracker.add_chore()
tracker.display_all()

#runs it


