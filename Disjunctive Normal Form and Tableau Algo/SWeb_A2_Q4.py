# '#' for Disjunction
# '.' for Conjunction
# '`' for Negation
# '*' for Implication
# '$' for Bi-implication
# Use '+' to indicate it as True
# Use '-' to indicate as False

## Alpha-Beta logic is written in this method,Based on the 
#  boolean function, two or one path is returned along with the 
#  expressions(along with values of expressions) in the paths.
def actualSplit(expr,splitIndex,booleanType,exprValue):
	# exprValue indicates whether the expression is with True or False
	# expr is the actual expression which we have to split
	# booleanType is the boolean operation to be considered for split
	# splitIndex indicates on which index we have to split the expression
	# As we do not know into how many paths the expression gets splitted,we maintain
	# two lists to store the items of two paths if any.
	list1 = []
	list2 = []
	# If operation is implication
	if booleanType == '*':
		# If the value of expression is False
		if exprValue == '-':
			str1,str2 = splitOn(expr,splitIndex)
			str1 = deleteExtraBrackets(str1)
			str2 = deleteExtraBrackets(str2)
			# When implication is False, We know that the first part is True
			# AND second part is False and both has to be in same path
			# so we have to add them into same list
			str1 = '+'+str1
			str2 = '-'+str2
			list1.append(str1)
			list1.append(str2)
		# If the value of expression is True
		else:
			str1,str2 = splitOn(expr,splitIndex)
			str1 = deleteExtraBrackets(str1)
			str2 = deleteExtraBrackets(str2)
			# When implication is True, We know that, the first part can be False
			# OR the second part can be True, These split into two different paths,
			# So we have to add them into different lists
			str1 = '-'+str1
			str2 = '+'+str2
			list1.append(str1)
			list2.append(str2)
	#If the operation is Disjunction
	if booleanType == '#':
		#If the value of expression is False
		if exprValue == '-':
			str1,str2 = splitOn(expr,splitIndex)
			str1 = deleteExtraBrackets(str1)
			str2 = deleteExtraBrackets(str2)
			# When disjunction is False, it means that both of them have to be False,
			# As both needed to be False, There will be only single path for this,
			# We will be adding them into same list
			str1 = '-'+str1
			str2 = '-'+str2
			list1.append(str1)
			list1.append(str2)
		# If the value of expression is True
		else:
			str1,str2 = splitOn(expr,splitIndex)
			str1 = deleteExtraBrackets(str1)
			str2 = deleteExtraBrackets(str2)
			# When the Disjunction is True, it means that anyone of the both needs to
			# be True, As as one of it being True is sufficient, We have to add them 
			# into seperate lists
			str1 = '+'+str1
			str2 = '+'+str2
			list1.append(str1)
			list2.append(str2)
	#If the operation is Conjunction
	if booleanType == '.':
		#If the value of expression is False
		if exprValue == '-':
			str1,str2 = splitOn(expr,splitIndex)
			str1 = deleteExtraBrackets(str1)
			str2 = deleteExtraBrackets(str2)
			# When the Conjunction is False, it means that anyone of the both needs to
			# be False, As as one of it being False is sufficient, We have to add them 
			# into seperate lists
			str1 = '-'+str1
			str2 = '-'+str2
			list1.append(str1)
			list2.append(str2)
		#If the value of expression is True
		if exprValue == '+':
			str1,str2 = splitOn(expr,splitIndex)
			str1 = deleteExtraBrackets(str1)
			str2 = deleteExtraBrackets(str2)
			# When Conjunction is True, it means that both of them have to be True,
			# As both needed to be True, There will be only single path for this,
			# We will be adding them into same list
			str1 = '+'+str1
			str2 = '+'+str2
			list1.append(str1)
			list1.append(str2)
	# if booleanType == '`':
	# 	if exprValue == '-':

	return list1,list2


## This method splits the expression based on the index passed.
def splitOn(expr,i):
	str1 = ""
	str2 = ""
	print(expr)
	print(type(expr))
	str1 = expr[:i]
	str2 = expr[i+1:len(expr)]
	return str1,str2

## After Splitting, Sometimes we would be having extra brackets,
#  this method removes those extra brackets in the expression passed to it.
def deleteExtraBrackets(str1):
	open_brackets = 0
	closed_brackets = 0
	for i in range(len(str1)):
		if str1[i] == '(':
			open_brackets+=1
		elif str1[i] == ')':
			closed_brackets+=1
	if open_brackets == closed_brackets:
		return str1
	elif open_brackets+1 == closed_brackets:
		if str1[len(str1)-1] == ')':
			str1 = str1[:-1]
			return str1
	elif closed_brackets+1 == open_brackets:
		if str1[0] == '(':
			str1 = str1[1:]
			return str1

## Every expression contains '-' or '+' in the begining, representing whether 
#  they are 'False' or 'True' respectively. We seperate this value from
#  expression in this method.
def seperateValueFromExpression(expr):
	# print(expr)
	# print(type(expr))
	# print(expr[0])
	if expr[0] == '+':
		value = '+'
		expr = expr[1:]
	else:
		value = '-'
		expr = expr[1:]
	return value,expr

## Method for getting the splitIndex and SplitSymbol from Postfix expression
def getSplitIndex(postfixExpression):
	size = len(postfixExpression)
	symbol = postfixExpression[size-1][0]
	index = postfixExpression[size-1][1]
	return symbol,index

def isSimple(expr):
	if len(expr) == 2:
		return True
	else:
		return False

def isListSimple(l1):
	flag = 0   # 0 means simple as of now
	for i in l1:
		if isSimple(i) == False:
			flag = 1
			return False
	if flag == 0:
		return True

def checkForClosed(ans_tt):
	closed = True
	for ll in ans_tt:
		row_done = 0
		for i in range(len(ll)-1):
			flag = 0         #represnts whether the match found or not
			sign = ll[i][0]
			literal = ll[i][1]
			if sign == '+':
				wanted_sign = '-'
			else:
				wanted_sign = '+'
			for j in range(i+1,len(ll)):
				if ll[j] == wanted_sign+literal :
					flag = 1
					row_done = 1
					break
			if flag == 1:
				break
		if row_done == 0:
			closed = False
	return closed



##Class Definition for converting Infix expression to Postfix expression
##Reference:-
## geeksforgeeks.org/stack-set-2-infix-to-postfix/
#  Our postfix expression contains symbols along with the index of that 
#  particular symbol in the initial expression. We use these indexes for 
#  splitting.
class InfixToPostfix:

	##For initialising the class variables
	def __init__(self,capacityOfStack):
		self.topOfStack = -1
		self.capacityOfStack = capacityOfStack
		#stack for conversion
		self.stackArray = []
		#for storing the output_expr
		self.output_expr = []
		#for presedence setting
		self.op_precedence = {'#':1, '.':1, '*':2, '$':2, '`':3}

	##For checking whether the stack is empty or not
	def isEmpty(self):
		return True if self.topOfStack ==-1 else False

	##For getting the top value of the stack
	def peek(self):
		dummy = self.stackArray[-1]
		return dummy[0]

	##For removing the top most element of the stack
	def pop(self):
		#checking whether the stack is empty or not
		if not self.isEmpty():
			self.topOfStack -= 1
			return self.stackArray.pop()
		#if stack is empty return this character which says that the
		#stack is empty 
		else:
			return "$"

	##For inserting elements into the Stack
	def push(self,op):
		duplicate_list = []
		#incrementing the value of top indeed increments the capacity of stack
		self.topOfStack +=1
		#inserting new element
		self.stackArray.append(op)


	##Checking whether the character passed is Operand or not
	def isOperand(self,ch):
		return ch.isalpha()


	##Checking whether the operator precedence is strictly lessthan the
	##operator present at the top of the stack
	def notGreater(self,i):
		try:
			a = self.op_precedence[i]
			b = self.op_precedence[self.peek()]
			return True if a <= b else False
		except KeyError:
			return False

	##Function to convert an infix expression to
	##Postfix expression
	def infixToPostfix(self,exp):

		#Traversing through the expression
		for i in range(len(exp)):
			if self.isOperand(exp[i]):
				duplicate_list1 = []
				duplicate_list1.append(exp[i])
				duplicate_list1.append(i)
				self.output_expr.append(duplicate_list1)

			#if the current symbol is open paranthesis we are pushing it
			#on to the stack
			elif exp[i] == '(':
				duplicate_list1 = []
				duplicate_list1.append(exp[i])
				duplicate_list1.append(i)
				self.push(duplicate_list1)

			#when current symbol is closed paranthesis
			elif exp[i] == ')':
				#popping all the elements of the stack still we encounter a
				#open paranthesis
				while ((not self.isEmpty()) and self.peek() != '('):
					a = self.pop()
					self.output_expr.append(a)
				if (not self.isEmpty() and self.peek() != '('):
					return -1
				else:
					self.pop()

			else:
				while(not self.isEmpty() and self.notGreater(exp[i])):
					self.output_expr.append(self.pop())
				duplicate_list1 = []
				duplicate_list1.append(exp[i])
				duplicate_list1.append(i)
				self.push(duplicate_list1)

		while not self.isEmpty():
			self.output_expr.append(self.pop())

		#printing the final converted expression
		#print(self.output_expr)
		return self.output_expr

b = input("Enter the consequence:-  ")
a = input("Enter the statements:- ")
expr = '('+a+'*'+b+')'
#expr = "((a*(b*c))*((a*b)*(a*c)))"
print("The combined statement is:- ")
print(expr)
# For proving validity, we assume the given expression as False,
expr = '-'+expr
print(expr)
initial_path = []
initial_path.append(expr)
final_tree = []
final_tree.append(initial_path)
print("The final tree list is:- ")
print(final_tree)

def myMain(final_tree):
	for list1 in final_tree:
		flag1 = 0
		print(list1)
		for i in range(len(list1)):
			if isSimple(list1[i]) == False:
				value,expression = seperateValueFromExpression(list1[i])
				print("The value of the expression is:-  "+value)
				print("The expression after deleting its value is:- "+str(expression))
				obj = InfixToPostfix(len(expression))
				postexpr = obj.infixToPostfix(expression)
				print("The postfix expression is:- ")
				print(postexpr)
				symbol,index = getSplitIndex(postexpr)
				print("The symbol of split is:- "+symbol)
				print("The index of split is:- "+str(index))
				p1,p2 = actualSplit(str(expression),index,str(symbol),str(value))
				print("The path1 is:- ")
				print(p1)
				print("The path2 is:- ")
				print(p2)
				if len(p1) == 0 and len(p2) == 0:
					continue;
				elif len(p2) == 0:
					for ele in p1:
						list1.append(ele)
					list1.remove(list1[i])
				else:
					dummy1 = []
					for j in range(len(list1)):
						if j != i:
							dummy1.append(list1[j])
					for ele in p1:
						dummy1.append(ele)

					dummy2 = []
					for j in range(len(list1)):
						if j != i:
							dummy2.append(list1[j])
					for ele in p2:
						dummy2.append(ele)
					list1.clear()
					list1.append(dummy1)
					list1.append(dummy2)
					final_tree.remove(list1)
					flag1 = 1
					break
					
			print("The list1 is ")
			print(list1)
		if flag1 == 1:
			for dad in list1:
				if dad not in final_tree:
					final_tree.append(dad)
		#final_tree.append(list1)
		print("The final tree is ")
		print(final_tree)
	# Trying for recursion
	for lists in final_tree:
		if isListSimple(lists) == False:
			myMain(final_tree)
	return final_tree

ans_tree = myMain(final_tree)
print()
print()
print()
print("All possible paths are:- ")
for ll in ans_tree:
	print(ll)
print()
print()
print()

Nikhil = checkForClosed(ans_tree)
if Nikhil == True:
	print("All paths are closed..!")
	print("Our assumption is wrong..!")
	print(b+" is logical consequence of "+a)
	print("!!!!!!! TRUE !!!!!!!!")
else:
	print("All paths are not closed...!")
	print(b+" is not a logical consequence of "+a)
	print("!!!!!!! FALSE !!!!!!!!")
