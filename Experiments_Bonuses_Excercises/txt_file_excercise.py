member = input("add a new member")

file = open("Members.txt", 'r')
existing_members = file.readlines()
file.close()

existing_members.append(member + "\n")

file = open("Members.txt", 'w')
existing_members = file.writelines(existing_members)
file.close()
