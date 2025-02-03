def rev_no(n):
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10

    print(rev)
    
n = int(input("Enter Number:"))
rev_no(n)


def rev_string(s):
    rev = ""
    for char in s:
        rev = char+rev

    print(rev)

s = input("Enter String:")
rev_string(s)
