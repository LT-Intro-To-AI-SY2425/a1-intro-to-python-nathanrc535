# Complete your individualized AI problems here

# Write a program that checks if a given string is a palindrome (reads the same forwards and backwards).
def palindrome(w: str):
    for x in range(len(w) // 2):
        if w[x] != w[len(w)-x-1]:
            return print("This is SOOOOO not a palindrome")
    return print("This is the best palindrome I have ever seen. Thank you for this splended experience. Have a great day.")

(palindrome("Chicken"))
(palindrome("racecar"))

def fizbuzz(input_num):
    if(input_num%3==0):
        if(input_num%5==0):
            return 'FizzBuzz'
        return 'Fizz'
    elif(input_num%5==0):
        return 'Buzz'
    else:
        return input_num

assert fizbuzz(1) == 1, "fizzbuzz 1 test"
assert fizbuzz(3) == "Fizz", "fizzbuzz 3 test"
assert fizbuzz(4) == 4, "fizzbuzz 4 test"
assert fizbuzz(5) == "Buzz", "fizzbuzz 5 test"
assert fizbuzz(6) == "Fizz", "fizzbuzz 6 test"
assert fizbuzz(15) == "FizzBuzz", "fizzbuzz 15 test"

