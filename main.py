# define a function to traverse the matrix

def traverseGrid(i, j, grid, time):
	r = len(grid)
	c = len(grid[0])
	# position visited
	grid[i][j] = 0

# create a queue (list) to store all the positions of infected wards in 1 unit time
	infection_queue = []

# direction arrays, only up,down,right,left allowed
	row = [-1, 0, 0, 1]
	col = [0, -1, 1, 0]

# traversal to adjacent wards
	for k in range(4):
		m = i+row[k]
		n = j+col[k]

		if m >= 0 and m < r and n >= 0 and n < c and grid[m][n] == 1:
			grid[m][n] = 0
			infection_queue.append((m, n)) #queue updated

# store time at which the ward got infected
			time[m][n] = time[i][j]+1

	return infection_queue


# define a function to calculate minimum time to infect all possible wards
def minTime(hospital):
	r = len(hospital)
	c = len(hospital[0])

	# array to store the time at which the wards got infected
	time = [[0 for i in range(c)] for j in range(r)]

# initialise queue to store newly infected wards
	inf_q = []

# initial run
	for i in range(r):
		for j in range(c):
			if hospital[i][j] == 2:
				inf_q += traverseGrid(i, j, hospital, time)

# we need to iterate till all wards that can be possibly infected are infected
	while(len(inf_q) != 0):
		for x, y in inf_q:
			temp = traverseGrid(x, y, hospital, time)
		inf_q = temp

# calculate minimum time to infect all possible wards
	res = 0
	for i in range(r):
		for j in range(c):

			# check if there is any uninfected ward
			if hospital[i][j] == 1:
				return '-1'
			res = max(res, time[i][j])
			result = str(res) #time complexity = O(M*N)

            

	return result

