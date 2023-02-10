def is_palindrome(s):
    char= [s[i] for i in range(len(s))]
    char.reverse()
    s1 = ''.join(char)
    if(s1==s):
        print("Palindrome")
    else:
        print("Not Palindrome")
s=input()
is_palindrome(s)
