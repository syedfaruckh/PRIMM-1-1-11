"""
PRIMM: 1+1 = 11
This program takes 2 numbers and instead of giving the sum it just puts them together.
Syed September 2024
"""

def main():
    
    #This asks the user for a number
    num1: float = float(input("Enter a number: "))
    #This asks the user another number
    num2: float = float(input("Enter another number: "))
    #This takes the 2 numbers from the user and shows it as 1 number + another
    total: float = num1+num2

    #This code takes the two numbers and puts them together like 1+1=11 
    print(f"{num1} + {num2} = {total}")
    print(f"{num1} - {num2} = {num1-num2}")
    print(f"{num1} + {num2} = {num1+num2}")
    print(f"{num1} * {num2} = {num1*num2}")  
    print(f"{num1} ** {num2} = {num1**num2}") 
    print(f"{num1} / {num2} = {num1/num2}")
    print(f"{num1} // {num2} = {num1//num2}") 
    print(f"{num1} % {num2} = {num1%num2}")  


if __name__ == "__main__":
  main()
