# Code your solution here

str1 = "This is a test."
str2 = "This is only a test."
num = 2
STR_ARITHMETIC = 0

if str1 + str2:
    STR_ARITHMETIC+=1

if str1 + num:
    STR_ARITHMETIC+=1

if str1 - str2:
    STR_ARITHMETIC += 1

if str1 - num:
    STR_ARITHMETIC+=1
    
if str1 * str2:
    STR_ARITHMETIC += 1

if str1 * num:
    STR_ARITHMETIC += 1
    
if str1 / str2:
    STR_ARITHMETIC += 1

if str1 ** str2:
    STR_ARITHMETIC += 1

if str1 ** num:
    STR_ARITHMETIC += 1

if str1 // str2:
    STR_ARITHMETIC += 1

if str1 // num:
    STR_ARITHMETIC += 1

if str1 % str2:
    STR_ARITHMETIC += 1

if str1 % num:
    STR_ARITHMETIC += 1
