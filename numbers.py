'''
        WELCOME.
        This is program based on numbers. The user enters four numbers and a result.
        All possible arithmetic operations (+,-,x,/)  are performed on those four numbers.
        Only those combinations which will evaluate to that result are displayed.

        ex: User enters 5, 5, 1, 4 and a result 99

        So the output of the program will be:
        5*5*4-1 =  99
        4*5*5-1 =  99
        5*4*5-1 =  99

 '''


import permutations  #importing module permutations.py whoch has functions for
                     #returning permuted lists for operarotrs and operands

        
print("WELCOME.\nThis is program based on numbers.\nThe user enters four numbers and a result.\
\nAll possible arithmetic operations (+,-,x,/) are performed on those four numbers.\
\nOnly those combinations which will evaluate to that result are displayed.")


        
condition = True
while(condition):

        per_lis = []

        '''
        For loop below inputs 4 numbers and appensd it to empty list per_lis[]. 
        '''
        print()
        print("Please enter the required positive single digit numbers  :\n")
        for i in range(4):
                                flag = True
                                while(flag):
                                        try :
                                                print("Enter element number",i+1, ":  ", end = '')
                                                k = input("")
         
                                                a=int(k)/2

                                                if(len(k)!=1):
                                                        a = 's'/2                                       #error rising statement
                                        except :
                                                print("\nINVALID INPUT. [ input must be a positive single digit number ]")
                                                print("\nPlease re-enter the number . \n")
                
                                        else :
                                                flag = False

                                per_lis.append(k)
                                
        flag = True
        while flag:
                try:
                        res = int(input("\nEnter the result : "))   	#inputs probable result from use
                        res1 = int(res)/2
                except:
                        print("invaild input.")
                else:
                        flag = False
         
                
        lis_opr = ['/','+','-','*']            #list containing four operators




        pop_per = (permutations.permut_nums(per_lis))
        '''
        pop_per is a list which contains all possible permutations of the 4 numbers entered by the user.
        Function permut_nums lies in module permutaions.py and is imported here.
        '''

        pop_opr = list(permutations.permut_operators(lis_opr))

        '''
        pop_opr is a list which contains all possible permutations of the 4 operators.
        Function permut_operators lies in module permutaions.py and is imported here.
        '''

        lst = []  #empty list
        test =''   #empty string
        for i in pop_per:
                for j in pop_opr:
                        test=i[0]+j[0]+i[1]+j[1]+i[2]+j[2]+i[3]
                        if(('/0' in test)):
                                continue
                        result=eval(test)
                        if result==res:
                                lst.append(test)

        for i in pop_per:
                if(eval(i[0]+'*' + i[1] + '*' + i[2] + '*' + i[3]) == res):
                        lst.append(i[0]+'*' + i[1] + '*' + i[2] + '*' + i[3])
                        break
        for i in pop_per:
                if(eval(i[0] + '+' + i[1] + '+' + i[2] + '+' + i[3]) == res):
                        lst.append(i[0]+'+' + i[1] + '+' + i[2] + '+' + i[3])
                        break

                    
        lst = list(set(lst))

        if(len(lst) == 0):
                print("\nNo possible combination yeilds to the required result !!")

        else:
          print("\nThe possible combinations that give rise to the required result are  :-\n")
          for i in lst:
             print(i+" = ",res)     #prints only those expressions which evaluates to res
             for j in range(9990):
                     pass

          print("\nWOW  thats a total of ", len(lst) ," combinations !!!")             

        choice = input("\nDo you want to continue (y/n) : ")
        if(choice == 'n'):
            condition = False
                   
