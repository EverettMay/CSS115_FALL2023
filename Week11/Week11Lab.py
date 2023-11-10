import random

def isNumberEven(aNumber):
    return aNumber % 2 == 0

def isNumberPrime(aNumber):
    if aNumber == 1:
        return False
    for i in range(2, aNumber):
        if aNumber % i == 0:
            return False
    return True
#-------------------------

def main():
    print("Week 11 lab")

    result = []
    for i in range(10):
        random_number = random.randint(1,10)
        result.append(isNumberEven(random_number))
    print(result)

if __name__ == "__main__":
    main()