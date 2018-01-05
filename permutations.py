'''
The function below takes in an list of four operators, namely +, - , x , / and returns an list which
has all possible permutations of the four operators. Since we can enter only three operators in between
four operands, the total elements in the resultant list will be 4^3=64 elements.
So it consists of three for loops, nested.

'''
def permut_operators(x):
	permuted = []
	for i in x:
		for j in x:
			for k in x:
				permuted.append([i,j,k])

	permuted.remove(['*','*','*'])
	permuted.remove(['+','+','+'])
                    
	return(permuted)
	
'''
The function permut_nums takes in an list of the four number entered by the user and returns the possible
permutations of those numbers. There are 4 numbers, so there will be 4!=24 permutations in all.
Therefore, the list permuted will contain 24 elements.
'''
def permut_nums(x):

        permuted = []
        
        for i in range(4):
                for j in range(4):
                        for k in range(4):
                                for l in range(4):
                                        if(l!= k and l!= j and l!= i):                                             #this ensures that all four elements
                                                if(k!= j and k!= i):                                               #will be pointing to different locations in the list,
                                                        if( j!= i ):                                               #even if they hold the same values.
                                                                permuted.append((x[i]+x[j]+x[k]+x[l]))
                                                                
 
        permuted = list(set(permuted))

        for i in range(len(permuted)):
                permuted[i] = list(permuted[i])
        
        return permuted
                                  


