#Input interger
n=int(input())
#If n is Odd Print Weird
if n%2!=0:
    print("Weird")
#If n is even & range of 2 to 5
elif n <= 5:
    if n%2==0:
        print("Not Weird")
#If n is even & range of 6 to 20
elif n>=6 and n<=20:
    if n%2==0:
        print("Weird")
#If n is even & greater than 20
elif n>20:
    if n%2==0:
        print("Not Weird")
