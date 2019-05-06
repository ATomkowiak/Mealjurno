data=[]
t=[]
food=[]
fl=[data,t,food]
while True:
    print("To add new meal press 1")
    print("To edit a meal press 2")
    print("To show all meals press 3")
    print("To show one meal press 4")
    print("To close programme press 5")
    x=int(input())
    if x == 1:
        print("meal date")
        ndata=input()
        print("meal time")
        nt=input()
        print("what did you eat")
        nfood=input()
        data.append(ndata)
        t.append(nt)
        food.append(nfood)
    elif x == 2:
        print("Which meal you want to edit")
        temp=int(input())-1
        while True:
            print("To change date press 1")
            print("To change time press 2")
            print("To change products in the meal press 3")
            print("To edit whole meal press 4")
            print("To get back to the menu press 5")
            y=int(input())
            if y==1:
                data[temp]=input()
            elif y==2:
                t[temp]=input()
            elif y == 3:
                food[temp]=input()
            elif y == 4:
                print("enter date")
                data[temp]=input()
                print("enter time")
                t[temp]=input()
                print("enter products in the meal")
                food[temp]=input()
            else:
                break
    elif x == 3:
        print(fl)
    elif x == 4:
        print("Press a number of a meal you would like to see")
        temp2=int(input())-1
        print(data[temp2], t[temp2], food[temp2])
    elif x== 5:
        break
