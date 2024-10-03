n=input("Enter a number:")
n=int(n)
def find_survivor(n):
    if n == 1:
        return 1
    else:
        return (find_survivor(n - 1) + 1) % n + 1
    print(find_survivor(n)
          
### it words