## ADD WHATEVER ARGUMENTS ARE NECESSARY TO THE MAIN FUNCTION
## IN THE SAME ORDER AS THE ARGUMENTS ARE TAKEN FROM THE
## COMMAND LINE SPECIFIED BELOW

import sys
def main(x):

	## YOU CODE SHOULD START HERE AST THE SAME
	## IDENTATION AS THIS COMMENT

	i = x
	e = 0
	y = 0
	j = x - 1

	while i > 0:	
        	if x % i == 0:
                	y = y + 1
        	i = i - 1
	while j > 0 and e < y:
		k = 1
		e = 0
		while k <= j:
			if j % k == 0:
                		e = e + 1
			k = k + 1
		j = j - 1
	if e >= y:
        	return("not antiprime")
	else:
        	return("antiprime")

	## THE LAST LINES OF YOUR CODE SHOULD EITHER
	## RETURN THE VALUE "anti-prime" or "not anti-prime"
	## REPLACE THE FOLLOWING LINE BY WHATEVER LINES
	## OF CODE ALLOW THIS FUNCTION TO RETURN THE VALUE
	## "anti-prime" or "not anti-prime"
	
## DO NOT REMOVE THIS LINE BELOW

if __name__ == "__main__" :

	## MODIFY THE LINE BELOW AND ADD BEFORE WHATEVER LINES ARE NECESSARY
	## TO RUN THIS PROGRAM AS, FOR INSTANCE:
	## $ python antiprime.py 6
	## WHERE THE FIRST ARGUMENT IS A POSITIVE INTEGER NUMBER FOR WHICH
	## YOU WANT TO FIGURE OUT WHETHER IS ANTI-PRIME OR NOT
	
	#print(main(x))
	if len(sys.argv) == 2:
		x = int(sys.argv[1])
		if x > 0:
			print(main(x))
