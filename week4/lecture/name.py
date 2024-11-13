import sys

# Check for errors
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")


# Print the name
print("Hello, my name is", sys.argv[1])
