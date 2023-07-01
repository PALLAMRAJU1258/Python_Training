#Write a program for math tables
n=int(input("Enter a value for a multiplication table to print from range 1-10:"))
print("Multiplication table of",n)
print("-----------------------")
for i in range(1,11):
    print("{0}x{1}={2}".format(n,i,n*i))
