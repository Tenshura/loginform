name = str(input("Enter Your Name : "))
surname = str(input("Enter Your Surname : "))
email = str(input("Enter Your Email : "))
password = str(input("Enter Your Password : "))
confPassword = str(input("Confirm Your Password : "))
  
if(password == confPassword):
      print("User Accepted!")

else:
      print("User Rejected! Invalid Password Combination")

      
