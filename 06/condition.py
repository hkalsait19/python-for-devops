# Conditional Statements
# /usr/local/bin/python3 /Users/yourname/pathofyourfile/condition.py t2.micro - run this command in terminal
import sys

type = sys.argv[1]

# only IF statement:

# if type == "t2.micro":
#     print("Free tier eligible, We will create it for you soon!")

# IF with ELSE statement:

# if type == "t2.micro":
#     print("Free tier eligible, We will create it for you soon!")
# else:
#     print("NOT free tier eligible, please choose t2.micro instaed others")


# IF with ELIF and ELSE statement:

if type == "t2.micro":
    print("Free tier eligible, We will create it for you soon!")
elif type == "t2.small":
    print("NOT free tier eligible, You will charge 2$ per day")
elif type== "t2.medium":
    print("NOT free tier eligible, You will charge 4$ per day")
elif type== "t2.large":
    print("NOT free tier eligible, You will charge 8$ per day")
elif type== "t2.xlarge":
    print("NOT free tier eligible, You will charge 16$ per day")
else:
    print("NOT free tier eligible, please choose 't2.micro' instaed others")