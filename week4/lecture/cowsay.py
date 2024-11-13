import cowsay
import sys

if len(sys.argv) < 2:
    print("Too few arguments")

cowsay.say(("My name is " + sys.argv[1]))
