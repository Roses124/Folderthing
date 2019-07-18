
ending = ("You made it to grandma's house. Great job!")
print("You are sitting in your room when your mom comes barging in with a pair")
print("of your grandmothers reading glasses in her hands.")
import time
time.sleep(1.5)
print("You say: What do you want mom?")
import time
time.sleep(2)
print("She replies: I need you to return these to your grandma for me.")
import time
time.sleep(2)
print("You reluctantly agree and head out of your house. ")
import time
time.sleep(3)
print("You get out of your house.")
import time
time.sleep(2)
answer1 = input("Which way to go, left or right? Type left or right. ")
if answer1 == "left":
    import time
    time.sleep(2)
    print("You arrive at a nice meadow. You are greeted by the fox.")
    import time
    time.sleep(2)
    print("The fox says: I would like to help you go to your grandma's house.")
    import time
    time.sleep(2)
    answer= input("Fox: Will you let me guide you? Type yes or no. ")
    if answer == "yes":
        print("Fox: Come with me. Muahahah...")
        import time
        time.sleep(2)
        print("The fox lied to you, and you have been eaten. You lost.")
    else:
        print("Fox: Fine okay hope you die.")
        import time
        time.sleep(2)
        print("You slowly continue walking along the path.")
        import time
        time.sleep(1)
        print(ending)
else:
    import time
    time.sleep(2)
    print("You arrive at a dangerous looking mountain, but you continue on.")
    import time
    time.sleep(2)
    print(ending)
