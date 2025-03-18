## secrets, passwords, apikey, username, sensitive information we can store in the env file

import os # os module

## directly from terminal or cmd line we fetch the values in code and see the output in the output panel
print(os.getenv('pass')) # customize pass the secret
print(os.getenv('apikey'))

## 2 ## inside inbuilt env we fetch the values
print(os.getenv('HOME'))
print(os.getenv('SHELL'))
print(os.getenv('USER'))
print(os.getenv('PWD'))