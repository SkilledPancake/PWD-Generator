

#I am trying to create a strong password in the terminal, depending on some user settings. 
#I will take input from the user and finally return their very own customized password.
#This is a project made my me so please give credits if you use it. 
#extremely lightweight project


# necessary imports
import secrets
import string


# fix password length
pwd_length = int(input("How long should the password be? "))


#fix the constraints of password

pwd_constraints=input("Do you want special characters in the password? (Y or N) ")


# define the alphabet
letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation


if pwd_constraints=='N':
    alphabet = letters + digits
elif pwd_constraints=="Y":
    alphabet=letters+digits+special_chars


# generate a password string
pwd = ''
for i in range(pwd_length):
  pwd += ''.join(secrets.choice(alphabet))

print(pwd)

# generate password meeting constraints
while True:
  pwd = ''
  for i in range(pwd_length):
    pwd += ''.join(secrets.choice(alphabet))

  if (any(char in special_chars for char in pwd) and 
      sum(char in digits for char in pwd)>=2):
          break
print('__________________')
print(pwd)
print('__________________')


































