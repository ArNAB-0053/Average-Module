lists = []
def countNum(num):
    count = 0
    for i in range(num):
        count+=1
    return count

def add(num):   
    for i in range(num):
        a = int(input("Enter number: "))
        lists.append(a)
    # print(lists)  
    Sum = sum(lists)
    # print(Sum)
    return Sum

num = int(input("How many number you want to add: "))
print(f"The average of {countNum(num)} lists is: ",add(num)/countNum(num))