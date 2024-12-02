"""
TASK 3
PASSWORD GENERATOR
A password generator is a useful tool that generates strong and
random passwords for users. This project aims to create a
password generator application using Python, allowing users to
specify the length and complexity of the password.
User Input: Prompt the user to specify the desired length of the
password.
Generate Password: Use a combination of random characters to
generate a password of the specified length.
Display the Password: Print the generated password on the screen
"""
import random,string
def password_generator(len):
    digits="9876543210"
    specialsymbol="@#$"
    tool=string.ascii_letters+digits+specialsymbol
    generatepassword1="".join(random.choices(tool,k=len))
    print(f"Generated password : {generatepassword1}")

password_generator(int(input("Enter the length of the password :")))