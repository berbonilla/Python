def factorial(x):
    if x == 0:
        return 1
    else:
        return (int) (x * factorial(x-1)) 

def count_repeating_chars(x):
    char_count = {}
    for char in x:
        if char in char_count:
            char_count[char] += 1
            has_repeating_chars = True
        else:
            char_count[char] = 1
    repeating_chars = {char: count for char,count in char_count.items() if count > 1}
    num_repeating_chars = len(repeating_chars)
    has_repeating_chars = any(count > 1 for count in char_count.values())
    return repeating_chars, num_repeating_chars, has_repeating_chars

def permutations(length,r):
    permRes = factorial(length)/(factorial(length-r))
    return print("Permutation Count:", combinations(length,r))   

def combinations(length,r):
    combRes = factorial(length)/(factorial(length-r)*factorial(r))
    return print("Combinations Count:", combRes) 

x = list(map(str, input("Enter multiple values: ").lower()))
r = int(input("Input r: "))

length = len(x)
result, num_repeating_chars, has_repeating_chars = count_repeating_chars(x)

if x.__contains__(" "):
    print("Input should be one word")

else:
    
    if has_repeating_chars:
        repVal = 1
        for i in result:
            repVal *= (factorial(result[i]))

        print("Factorial:",int(factorial(length)/repVal))
    else:
        print("Factorial:", factorial(length))
        
         
