#  Let's say; you left a message in the past that prints a password you need. To see the password you wrote, you need to enter your name and the program should recognize you.
#  Write a program that 

#  Takes the first name from the user and compares it to yours,
#  Then if the name the user entered is the same as yours, print out such as : "Hello, Joseph! The password is : W@12",
#  If the name the user entered is not the same as yours, print out such as : "Hello, Amina! See you later."


print("Hi! We have received the message you sent, enter your first name in the box below to get your password\n")
name=input("Please enter your first name so we can recognize you  ").lower()
joseph="W@12"
if name=="joseph":
  print("Hello, {}! The password is : {}".format(name.title(), joseph))
else:
  print("\nHello, {}! See you later.".format(name.title()))

  
  
  
  
