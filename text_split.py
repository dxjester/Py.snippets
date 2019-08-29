txt = "welcome to the jungle"
x = txt.split()
print(x)


#split on specific character
txt = "apple#banana#cherry#orange"
x = txt.split("#")
print(x)

# split one the first string
txt = "apple#banana#cherry#orange"
# setting the max parameter to 1, will return a list with 2 elements!
x = txt.split("#", 1)
print(x)
# >>> ['apple', 'banana#cherry#orange']
