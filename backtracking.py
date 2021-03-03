x = input("backtrack no: ")
import itertools
letters = {'2':'abc', '3':'def','4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs','8':'tuv', '9':'wxyz'}

def letterCombinations(digits):
    return ["".join(combo) for combo in itertools.product(*[letters[d] for d in digits])]

print(letterCombinations(x))


'''for loop
    d = characters(a,b,c)
    digits = 2,3
    itertools.products = inbuilt module can accept multiple lists
    * = to unpack the iterable into positional arguments
    joins = joins all items in a tuples'''
