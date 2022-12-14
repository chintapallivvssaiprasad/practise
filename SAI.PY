product_1 = int(input("Enter a number : "))
product_2 = int(input("Enter a number : "))
product_3 = int(input("Enter a number : "))
total = product_1*product_2*product_3
s = open("Data-1.txt","a")
if(product_1 > 0) and (product_2 >0) and (product_3 >0):
    print("total value is : ",total)
    print("total value is : ",total,file=s)
else:
    print("enter a right value")