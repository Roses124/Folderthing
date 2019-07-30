#Opens a file. You can now look at each line in the file individually with a statement like "for line in f:
f = open("dictionary.txt","r")

print(type(f))
print("Can your password survive a dictionary attack?")

#Take input from the keyboard, storing in the variable test_password
#NOTE - You will have to use .strip() to strip whitespace and newlines from the file and passwords
test_password = input("Type in a trial password: ")
password = test_password.lower()
found = False
password = test_password.strip()
#lets_to_nums = {"4:a", "1:l", "3:e", "0:o"}
#other_nums = ["2", "5", "6", "7", "8", "9"]
#len_password = int(password)
for row in f:

    if password == row.strip():
        print("The password " + str(password) + " is weak!")
        found = True
        break


if found == False:
    print("Very nice! Your password is strong!")

#Write logic to see if the password is in the dictionary file below here:
