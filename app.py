n=input("Enter a number:")
n=int(n)
def find_survivor(n):
    if n == 1:
        return 1
    else:
        return (find_survivor(n - 1) + 1) % n + 1
    print(find_survivor(n)
          
### it words

## Make stars like a  triangle
for i in range(5,0,-1):
    for k in range(1,6-i):
        print(" ",end="")
    for j in range (1,(2*i-1)+1):
        print("*",end="")
    print("\n")
    
    