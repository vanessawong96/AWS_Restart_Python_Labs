import math
import time;

def getPrimeList1():
    findPrime = int(input("Input the number to find the prime numbers smaller or equal to it : "))
    time_1 = time.time()
    primeList = []
    palindromList = []
    for x in range(2, findPrime+1):
        x_str = str(x)
        if x_str == x_str[::-1]:
            palindromList.append(x)
        
        sqrtNum = math.floor(math.sqrt(x))
        primeNum = True
        for a in primeList:
            if a > sqrtNum:
                break
            if x % a == 0:
                primeNum = False
                break
        
        if primeNum == True:
            primeList.append(x)
    
    time_2 = time.time()
    time_interval = time_2 - time_1
    print("time taken to load: ", time_interval)
    input("press Enter to display prime numbers and palindrome numbers")
    print("list of prime numbers:")
    print(primeList)
    print("")
    print("list of palindrome numbers:")
    print(palindromList)
    
getPrimeList1()