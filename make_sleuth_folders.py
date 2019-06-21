import os

# get current directory
currentPath = os.getcwd()

print("Files are created in the working directory.")
print("Which folders do you want to create?" )

# prompt user for input and repeat if invalid
answer = 0
validInputs = ["a", "r", "p", "x"]
while answer not in validInputs:
	answer = input("(A)ll (R)ookie (P)ro, or e(X)it: ")
	answer = answer.lower()

# Create rookie folder function
def create_rookie():

	# create arrays for parent folders and sub folders
	rookieParent = [101, 201, 202, 301, 302, 303, 401, 402, 403]
	rookieSub = [1, 2, 3, 4]

	# loop for creating 9 parent folders, each 4 with sub folders
	for i in range(0, len(rookieParent), 1):
		rookieParentPath = currentPath + "/%s" % rookieParent[i]
		os.mkdir(rookieParentPath)

		for j in range(0, len(rookieSub), 1):
			rookieSubPath = rookieParentPath + "/%s" % rookieSub[j]
			os.mkdir(rookieSubPath)

# Create pro folder function
def create_pro():

	# create arrays for parent folders and sub folders
	proParent = [501, 502, 601, 701, 702, 801, 802]
	proSub = [1, 2, 3, 4]

	# loop for creating 7 parent folders, each 4 with sub folders
	for i in range(0, len(proParent), 1):
		proParentPath = currentPath + "/%s" % proParent[i]
		os.mkdir(proParentPath)

		for j in range(0, len(proSub), 1):
			proSubPath = proParentPath + "/%s" % proSub[j]
			os.mkdir(proSubPath)

# execute functions according to user input
if __name__ == '__main__':
	if answer == "a":
		create_rookie()
		create_pro()
		print("Complete")
	elif answer == "r":
		create_rookie()
		print("Complete")
	elif answer == "p":
		create_pro()
		print("Complete")
	elif answer == "x":
		exit()
