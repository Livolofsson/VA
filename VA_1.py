"""
Solutions to module VA 1
Student: 
Mail:
"""
from time import perf_counter as pc
import sys

def exchange(target, coins) -> list: 
    """ Count possible way to exchange a with the coins in coins. Use memoization"""
    mem = {}
    
    def exchange_mem(a, index):
        if (a, index) in mem:
            return mem[(a, index)]
        elif a == 0: 
            return 1 
        elif a < 0 or index >= len(coins): 
            return 0 

        mem[(a, index)] = exchange_mem(a, index + 1) + exchange_mem(a - coins[index], index)
        return mem[(a, index)]
    
    return exchange_mem(target, 0) 

def exchange0(a, coins): 
    if a == 0: 
        return 1 
    elif a < 0 or not coins: 
        return 0 
    return exchange0(a, coins[1:]) + exchange0(a - coins[0], coins)

def time_execution(func, a, coins):
    start = pc()
    result = func(a, coins)
    end = pc()
    return result, end - start

def zippa(l1: list, l2: list) -> list: 
    """ Returns a new list from the elements in l1 and l2 like the zip function"""
    if not l1 and not l2: 
        return []
    elif not l1 or not l2: 
        if len(l1) < len(l2): 
            return l2[len(l1):]
        return l1[len(l2):]
    return [l1[0], l2[0]] + zippa(l1[1:], l2[1:])

def main():
    sys.setrecursionlimit(2000)
    print('\nCode that demonstrates my implementations\n')

    # # Compare exchange0 (without memoization) and exchange (with memoization)
    
    # Testing for a = 11, coins = [1, 2, 5]
    print("Comparing exchange0 (no memoization) and exchange (with memoization)")
    #print("Test case: a = 11, coins = [1, 2, 5]")

    # Exchange0 without memoization
    result0, time0 = time_execution(exchange0, 1000, [1, 5, 10, 50, 100])
    print(f"exchange0 result = {result0}, time = {time0:.6f} seconds")

    # Exchange with memoization
    result_memo, time_memo = time_execution(exchange, 1000, [1, 5, 10, 50, 100])
    print(f"exchange result (memoization) = {result_memo}, time = {time_memo:.6f} seconds")

    # Testing for a = 4, coins = [1, 2, 3]
    print("\nTest case: a = 4, coins = [1, 2, 3]")

    # Exchange0 without memoization
    result0, time0 = time_execution(exchange0, 2000, [1, 5, 10, 50, 100])
    print(f"exchange0 result = {result0}, time = {time0:.6f} seconds")

    # Exchange with memoization
    result_memo, time_memo = time_execution(exchange, 2000, [1, 5, 10, 50, 100])
    print(f"exchange result (memoization) = {result_memo}, time = {time_memo:.6f} seconds")

if __name__ == "__main__":
    main()

####################################################

"""
  Answers to the none-coding tasks
  ================================
  
  
  Exercise 1

What time did it take to calculate large sums such as 1000 and 2000? 

What happens if you try to calculate e.g. 10000?
  
"""
