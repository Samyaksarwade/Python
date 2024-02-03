#Using len() function :

string = "Python is Object-Oriented Language!"
string_length = len(string)

print(string_length)

#using Count()

string = "Apple a day Keeps a doctor away!"
a_count = string.count("a")
print(a_count) 


#using for loop :

def string_length(s):
    count = 0
    for char in s:
        count += 1
    return count

str = 'Custard'
print(string_length(str))



#using while loop :

def string_length(s):
    count = 0
    while s:
        count += 1
        s = s[:-1]
    return count

cric = 'Virat kohli'
print(string_length(cric))