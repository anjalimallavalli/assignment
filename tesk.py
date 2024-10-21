# print the reverse string
def function(x):
    return x[::-1]
    s="learning python is very easy"
    print(function(s))

    #reverse of reverse the string
    str="learning python is very easy"
    str1=str.split()
    11=lambda str1:str1[::-1]
    p=11(str1)
    a=""
    for i in p:
        a+=i+""
        print(a)

        #To sort a couple based on second element of each tuple.
        t=eval(input("Enter the Tuple"))
        tupl=sorted(t,key=lamda x:x[1])
        print(tuple(tup1))
        
        #To find a max and min element in a tuple of integers.
        t=(10,20,5,40,25)
        max_val=t[0]
        min_val=t[0]
        for i in range (len(t)):
            if t[i]>max_val:
                max_val=t[i]
                if t[i]<min_val:
                    min_val=t[i]
                print("maximum value is:",max_val)
                print("minimum value is:",min_val)

                #Nested tuple flatting in into single tuple
                tuple_1=eval(input("Enter the tuple"))
                list1=[]
                for i in tuple_1:
                    str1=str(i)
                    if len(str1)==1:
                        list1.append(int(str1))
                        else:
                            str1=list(i)
                            fir i in str1:
                            list1.append(i)
                            tuple_1=tuple(list1)
                            print(tuple_1)

                            #dictionary where keys are tuple coordinates(x,y) and values are city names.
                            def function(dict_1,dict_2):
                                for i,j in dict_1.items():
                                    b=eval(i)
                                    if b=dict_2:
                                        print(j)
                                        dict_1=eval(input())
                                        dict_2=eval(input())
                                        function(dict_1,dict_2)

                