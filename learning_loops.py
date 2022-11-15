num =0
'''Python keyword while has a conditional expression followed by the : symbol to start a block with an increased indent.
 This block has statements to be executed repeatedly.
 Such a block is usually referred to as the body of the loop.
 The body will keep executing till the condition evaluates to True.
 If and when it turns out to be False,
 the program will exit the loop. The following example demonstrates a while loop.'''
while num < 5:
    num = num + 1
    print('num = ', num)

'''Here the repetitive block after the while statement involves incrementing the value of an integer variable and printing it. 
Before the block begins, the variable num is initialized to 0. 
Till it is less than 5, num is incremented by 1 and printed to display the sequence of numbers, as above.

All the statements in the body of the loop must start with the same indentation, otherwise it will raise a IndentationError.'''

'''num =0
while num < 5:
    num = num + 1
      print('num = ', num)'''


num = 0
'''Use the break keyword to exit the while loop at some condition.
 Use the if condition to determine when to exit from the while loop, as shown below'''   
while num < 5:
    num += 1   # num += 1 is same as num = num + 1
    print('num = ', num)
    if num == 3: # condition before exiting a loop
        #use break to exit the loop
        break
 
num = 0
'''Use the continue keyword to start the next iteration and skip the statements after the continue statement on some conditions, as shown below.'''  
while num < 5:
	num += 1   # num += 1 is same as num = num + 1
	if num > 3: # condition before exiting a loop
		continue
	print('num = ', num)  
'''The following Python program successively takes a number as input from the user and calculates the average,
 as long as the user enters a positive number. Here,
 the repetitive block (the body of the loop) asks the user to input a number,
 adds it cumulatively and keeps the count if it is non-negative.'''    
num=0
count=0
sum=0

while num>=0:
    num = int(input('enter any number .. -1 to exit: '))
    if num >= 0:
        count = count + 1 # this counts number of inputs
        sum = sum + num # this adds input number cumulatively.
avg = sum/count
print('Total numbers: ', count, ', Average: ', avg)
