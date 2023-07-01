"""Write a program that accepts a string from a user & redisplays the same string
after removing vowels from it"""
String_Name=input("Enter the String:")
Vowels="aeiou"
string=""
for i in String_Name:
    if i not in Vowels:
        string+=i
print(string)


#Another way of displaying the string after removing vowels from it
for i in String_Name:
    if i not in Vowels:
        print(i,end="")

 
