# Telepathy_Labs_Assessment

Time needed to infect all patients at a hospital.

The approach for this problem is to travese the matrix using BFS.
First we define the function to traverse through the wards in the hospital and then we call this function in the final function that calculates time to infect all wards.
We initialise 2 lists (queues), one to store time of infection and another to store position of infected wards at 1 unit time.
There are 4 directions up (-1,0), down (1,0), left (0,-1) and right(0,1) hence we define the direction arrows accordingly.
Then we traverse to nearby wards in these directions, If the value at cell (i, j) = 2, then push that cell into the queue with the time of infection as 0. Whenever new infection happens, time is increased by 1 unit (time[m][n] = time of infection of current infected ward+1).
Once all the infected wards are visited, i.e. the time of infection of all the infected wards is non-negative, then we calculate the time to infect all wards possibly. If any ward remains uninfected then we output result as '-1'.
