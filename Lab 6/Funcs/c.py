b = input()
b = [i for a,i in enumerate(b)]
c = list(reversed(b))

if b==c:
    print("Palindrome")
else:
    print("Not palindrome")
    

