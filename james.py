import re
print(" welcome to univrsity of brighton login details") 

# this String welcomes the user to login
userName=input('enter username:')
# this username will allow the  user to input username when he runs the code

password=input('enter password:')
# this input will allow the user to enter the username when the user runs it
while len(userName)== 0 or len(password)== 0:
    print("error: ensure that both username and password are being entered")
    
# if there is no string entered and the user press on the login button directly it will print error: no string entered
while len(userName)<12 or len (password) <12:
    print("username or password is incorrect: please re-login")
    #if a user inputs a password that is less than 12 it will print the username is incorrect: please re-login  
    userName=input()
    password=input()
# it allows the user to rerun the program until the user re enters the correct login details.
# it also does not end the program when the user enters a wrong log in details 
if re.search("[a-z]", password) and re.search("[A-Z]", password) and re.search("[0-9]", password):
 print("Password is strong")
else:
   username=input()
   password=input()
password2=input("confirm password:  ")
while password2!=password:
    print("input type error!")
    password2=input("confirm password:  ")
# if the user enters the correct password it ask the user to confirm the password to make sure that the user did not guessed the password
print("congratulations! you can access Brighton Materials")
# if the user enters the correct password and logged in succesfully it will print congratulations! you can access brighton materials