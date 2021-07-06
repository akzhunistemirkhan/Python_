import string, os
if not os.path.exists("alphabit"):
   os.makedirs("alphabit")
for alpha in string.ascii_uppercase:
   with open(alpha + ".txt", "w") as file:
       file.writelines(alpha)