string=input()
count=0

for i in string:
    if i in "aeiouAEIOU":
        count+=1

print(count)