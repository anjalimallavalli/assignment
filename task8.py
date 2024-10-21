#create a guessing game by using python
import random
print("welcome to the guessing game")
print("try guess the numbet in between 1 to 100")
number=random.randit(1,100)
guess=-1
if guess!=number:
    guess_num=input("enter your number")
    guess=int(guess_num)
    if guess<number:
        print("too low,try again")
        elif guess>number:
            print("too high,try again")
            else:
                print("congractulations! you guessed the number correctly")
                #adding an item to dmart shopping bill

                def function(dict_in,dict_price):
                    n=int(input())
                    for i in range(n):
                        function_1(dict_in)
                        count=0
                        for i,j in dict_in.items():
                            for a,b in dict_price.items():
                                if i==a:
                                    count+=int(j)*int(b)
                                    return count
                                    def function_1(dict_in):
                                        dict_in[input()]=input()


                                        dict_in=eval(input())
                                        dict_price=eval(input())
                                        a=function(dict_in,dict_price)
                                        print(a)

