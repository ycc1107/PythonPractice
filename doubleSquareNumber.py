#A double-square number is an integer X which can be expressed as the sum of two perfect squares. For example, 10 is a double-square because 10 = 3^2 + 1^2. Your task in this problem is, given X, determine the number of ways in which it can be written as the sum of two squares.

#For example, 10 can only be written as 3^2 + 1^2 (we don't count 1^2 + 3^2 as being different). On the other hand, 25 can be written as 5^2 + 0^2 or as 4^2 + 3^2. 
#NOTE: Do NOT attempt a brute force approach. It will not work. The following constraints hold: 
#0 <= X <= 2147483647 
#1 <= N <= 100

import math
def doubleSquareNumber(x):
    result = 0
    end = 0
    first = int(math.sqrt(x))
    for i in range(first,2,-1):
        second = math.sqrt(x - i*i)
        if i <= end: break
        if second == int(second):
            result += 1
            end = int(second)
    return result if x != 1 else 1

