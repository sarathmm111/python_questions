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
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    s = s.lower()

    for letter in alphabets:
        if letter not in s:
            return False 
    return True

input = "the quick brown fox jumps over the lazy dog"
output = panagram(input)
print(output)



def freq(s):
    frequency = {}
    for i in s:
        if i in frequency:
            frequency[i] += 1
        else:
            frequency[i] = 1
    return frequency

print(freq("hello"))
