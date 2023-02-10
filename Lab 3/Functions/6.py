def reverse(sentence):
    words = sentence.split()
    words.reverse()
    print(' '.join(words))
s = input()
reverse(s)