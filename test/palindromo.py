# A palindrome is a word that is the same forwards and backwards. For example, "radar" is a palindrome. Write a function that takes a string and returns True if the string is a palindrome and False if it is not. The function should work for both uppercase and lowercase letters.
# implement the function is_almost_palindrome(string word). 
# The function returns the string yes if the word is a palindrome OR if it is possible to make the word a palindrome by modifying one character. Otherwise, the function returns the string no.
# Assume that all caracters will be received in lower case.

def is_almost_palindrome(word):
    if word == word[::-1]:
        return "yes"
    else:
        for i in range(len(word)):
            if word[i] != word[-i-1]:
                new_word = word[:i] + word[-i-1] + word[i+1:]
                if new_word == new_word[::-1]:
                    return "yes"
                else:
                    return "no"
    
    
word = input()

out_ = is_almost_palindrome(word)
print(out_)

# Question 2:
# Develop a function to calculate the average distance among three especified points,
# which are represented by their coordinates (xi, yi). The function output should be rounded to 2 decimal places.

def average_distance(x1, y1, x2, y2, x3, y3):
    distance1 = ((x2-x1)**2 + (y2-y1)**2)**0.5
    distance2 = ((x3-x2)**2 + (y3-y2)**2)**0.5
    distance3 = ((x1-x3)**2 + (y1-y3)**2)**0.5
    return round((distance1 + distance2 + distance3)/3, 2)

# Question 3:
# Write a function that receives 2 parameters:
    # parameter 1: an array of positive integers with values between 1 and 5000
    # parameter 2: The length of the array
    
# The function should return the number that appears the most in the array. If there is a tie, the function should return the SMALLEST number.

def numMasPopular(n, arr):
    count = [0]*5001
    for i in range(n):
        count[arr[i]] += 1
    max_count = 0
    res = -1
    for i in range(5001):
        if count[i] > max_count:
            max_count = count[i]
            res = i
    return res

# question 3 version 2
def numMasPopular(n, arr):
    count = [0]*5001
    for i in range(n):
        count[arr[i]] += 1
    max_count = 0
    res = -1
    for i in range(5001):
        if count[i] > max_count:
            max_count = count[i]
            res = i
        elif count[i] == max_count and i < res:
            res = i
    return res