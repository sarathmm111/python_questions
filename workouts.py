def fizzbizz(n):
    for i in range(1,n+1):
        if i%15 == 0:
            print("fizzbizz")
        elif i%5 == 0:
            print("bizz")
        elif i%3 == 0:
            print("fizz")
        else:
            print(i)
fizzbizz(50)


def palindrome(s):
    s=s.replace(" ","").lower()
    return s == s[::-1]

print(palindrome("malayalam"))


def panagram(s):
    alphabets='abcdefghijklmnopqrstuvwxyz'
    for i in alphabets:
        if i in s.lower():
            return True
    return False
print(panagram("the quick brown fox jumps over the lazy dog"))
