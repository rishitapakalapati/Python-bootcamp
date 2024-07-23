#3.X goes to market ,he buys 10 apples,2 dozen bananas.8 oranges
#1 apple=15
#1 banana=4
#1 orange=5
#x has 700rs . 

cost_apple=15
cost_banana=4
cost_orange=5
n=int(input("enter the amount given by mother"))
no_apple=int(input("Enter no.of apples"))
no_banana=int(input("Enter no.of bananas"))
no_orange=int(input("Enter no.of oranges"))
total_cost=(no_apple*cost_apple)+(no_banana*cost_banana)+(no_orange*cost_banana)
if(total_cost>n):
    print("you have been cheated")
else:
    print("you are safe")