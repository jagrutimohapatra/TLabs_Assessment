# Telepathy_Labs_Assessment

Time needed to infect all patients at a hospital.

The approach for this problem is to travese the matrix using BFS.
First we define the function to traverse through the wards in the hospital and then we call this function in the final function that calculates time to infect all wards.
We initialise 2 lists (queues), one to store time of infection and another to store position of infected wards at 1 unit time.
There are 4 directions up (-1,0), down (1,0), left (0,-1) and right(0,1) hence we define the direction arrows accordingly.
Then we traverse to nearby wards in these directions, If the value at cell (i, j) = 2, then push that cell into the queue with the time of infection as 0. Whenever new infection happens, time is increased by 1 unit (time[m][n] = time of infection of current infected ward+1).
Once all the infected wards are visited, i.e. the time of infection of all the infected wards is non-negative, then we calculate the time to infect all wards possibly. If any ward remains uninfected then we output result as '-1'.

To run the code:
1. Download the whole folder using the command:  git clone https://github.com/jagrutimohapatra/TLabs_Assessment.git
2. Open terminal and navigate to the folder (give the path to where you have downloaded the folder with its files and stored in your local) for example you have cloned in the root folder and to navigate to the TLabs_Assessment file just use the command: cd TLabs_Assessment/
3. Check if all the files have been downloaded i.e., main.py, README.md and test_main.py
4. Run the test file with the command : python test_main.py, you can see the tests have passed
