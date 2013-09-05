print("Hello would you like to see how long you've lived in days, minutes, and seconds?")

input()

print("Okay first whats your name?")

name = input()

print("Hello",name, "Now enter your age.")

age = int(input())

days = age * 365

minutes = age * 525948     

seconds = age * 31556926

print(name, "Has been alive for", days,"days", minutes, "minutes and", seconds, "seconds!")

input("\nPress enter to exit.")
