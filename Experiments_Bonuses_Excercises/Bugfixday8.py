#this output gives "Hello You 0" but should be "Hello You 9"
# THE CONTENT OF file.txt is HELLO YOU (THE SPACE COUNTS AS A LENGTH CHARACTER duh)

#with open("helloyou.txt", 'r') as file:
#    print(file.read())
#    print(len(file.read()))

with open("helloyou.txt", 'r') as file:
    content = file.read()

print(content)
print(len(content))

#IT NEEDED TO HAVE THE VARIABLE "CONTENT" SO THAT WAY WE COULD MANIPULATE AND USE IT THROUGHOUT THE SCRIPT