# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

    # I can be placed before V (5) and X (10) to make 4 and 9. 
    # X can be placed before L (50) and C (100) to make 40 and 90. 
    # C can be placed before D (500) and M (1000) to make 400 and 900.

# Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

# Example 1:

# Input: "III"
# Output: 3

# Example 2:

# Input: "IV"
# Output: 4

# Example 3:

# Input: "IX"
# Output: 9

# Example 4:

# Input: "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.

# Example 5:

# Input: "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.




def romanToInt(x):
    #let's create a dictionary of all of the letters and value
    romanLetters = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

    #value we are going to return
    sum = 0

    #need to iterate through the string and check the keys and add to sum variable
    #if RomanLetter is less than the next letter in the string, we substract it from the sum
    #for each IV will be -1 during the first iteration and then 4 during the second iteration
    for value in range(0, len(x)-1):
        #pull the key-value of the current letter and compare it to the next
        if(romanLetters[x[value]] <  romanLetters[x[value+1]]):
            #current roman numeral is smaller so we substract
            sum -= romanLetters[x[value]]
        else:
            #add the roman numeral value to the sum
            sum += romanLetters[x[value]]

    return sum + romanLetters[x[-1]]

print(romanToInt("I")) #1
print(romanToInt("II")) #2
print(romanToInt("III")) #3
print(romanToInt("IV")) #4
print(romanToInt("VI")) #6
print(romanToInt("XCIX")) #99
print(romanToInt("CMXCIX")) #9999