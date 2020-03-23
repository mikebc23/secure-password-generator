from random import choice
import sys

def generate(lenght):
	#generating a random string based on the following characters
  return ''.join([choice('abcdefghijkmnopqrstuvwxyzABCDEFGHIJKLMNPQRSTUVWXYZ123456789~@#$%^&*+-/[]') for i in range(lenght)])

default = 24 #default 
flag = '' #default

#Determinating if the argument is valid
if len(sys.argv) >= 2 and sys.argv[1].isdigit() and int(sys.argv[1]) <= 256:
	user_length = sys.argv[1]
else:
	user_length = default
	flag = "\t\t*Invalid entry, using default settings"

print generate(int(user_length)) + flag
