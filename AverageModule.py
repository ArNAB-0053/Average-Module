class Average():
    def __init__(self, number_of_element = 3):
        self.num = number_of_element

    def average(self, defaultStyle = True): 
        print('''
                        ---------------------------------------------
        By default input for entering numbers is given, you just have to give numbers in input
                    ---------------------------------------------------------''')
        lists = []  
        count = 0
        i=0
        for i in range(self.num):
            count+=1
        # print("Enter numbers: ")  
        print("\n", end='')  
        for i in range(self.num):
            if defaultStyle == True:
                a = int(input(f"Enter numbers ({i+1}): "))
            else:    
                a = int(input())
            lists.append(a)
        # print(lists)  
        Sum = sum(lists)
        # print(Sum)
        avg = Sum/count
        return avg