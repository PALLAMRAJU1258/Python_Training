"""Sunny is a raw agent who is working at iran and he got a information that
there is an attack against india,he must send a msg to india regarding the
information safely so he using ceaser cipher"""
msg=str(input("Enter the message:"))
j=0
while j<len(msg) :
    letter=msg[j]
    print(chr(ord(letter)+2),end="")
    j+=1
