# Creat a list
results = ["Mario", "Luigi", "Princess", "Yoshi"]

# Add an element to a list
results.append("Princess")
print("Version 1:", results)

# Add a list of elements to a list
results.append(["Yoshi", "Toad"])
print("Version 2:", results)

# Remove an element from the list
results.remove(["Yoshi", "Toad"])
print("Version 3:", results)

# Add multiple of elements to the list
results.extend(["Yoshi", "Toad"])
print("Version 4:", results)

# Add an element to a specific position in the list
results.insert(0, "Bowser")
print("Version 5:", results)
