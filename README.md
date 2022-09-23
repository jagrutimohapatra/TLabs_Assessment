# Telepathy_Labs_Assessment

Time needed to infect all patients at a hospital.

The approach for this problem is to travese the matrix.
First we define the function to traverse through the wards in the hospital and then we call this function in the final function that calculates time to infect all wards.
In this we define a matrix called propagation matrix that will store the result of infection after each unit time.
There are 4 directions up (-1,0), down (1,0), left (0,-1) and right(0,1) hence we navigate the matrix accordingly.
Whenever new infection happens, time is increased by 1 unit (round = round+1).
Everytime we check if further propagation can happen. If not then we break the loop. If any ward remains uninfected then we output result as '-1'.
Time complexity = O(M * N) for a MXN matrix.
To run the code:
1. Download the whole folder using the command:  git clone https://github.com/jagrutimohapatra/TLabs_Assessment.git
2. Open terminal and navigate to the folder (give the path to where you have downloaded the folder with its files and stored in your local) for example you have cloned in the root folder and to navigate to the TLabs_Assessment file just use the command: cd TLabs_Assessment/
3. Check if all the files have been downloaded i.e., main.py, README.md and test_main.py
4. Run the test file with the command : python test_main.py, you can see the tests have passed
5. I have commented the print statements, to see how the propagation happens please make sure to uncomment the print statements
