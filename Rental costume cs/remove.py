
# txt = "rtt banana"

# x = txt.strip("rt")

# print(x)


from ntpath import join
import string


name = "Tulsi"
list=[]
for i in name:
    if i == 'l':
        continue
    else:
        list.append(i)
string=" ".join(list)
print(string) 
