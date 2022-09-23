import numpy as np

#traverse the hospital from 1 ward to another in only 4 directions up, down, left, right
def infect_hospital(hospital):
    row = len(hospital) 
    col = len(hospital[0])
    
    infection_map = [[0 for _ in range(col)] for _ in range(row)] #define the infection map to traverse
    
    #traversing in the directions up (-1,0), down (1,0), left (0,-1), right (0,1)
    for i in range(row):
        for j in range(col):
            if hospital[i][j] == 2:            
                infection_map[i][j] = 2
                
                if hospital[i][min(j+1, col-1)] != 0:
                    infection_map[i][min(j+1, col-1)] = 2
                
                if hospital[i][max(j-1, 0)] != 0:
                    infection_map[i][max(j-1, 0)] = 2
                
                if hospital[max(i-1,0)][j] != 0:                               
                    infection_map[max(i-1,0)][j] = 2
                
                if hospital[min(i+1,row-1)][j] != 0:
                    infection_map[min(i+1,row-1)][j] = 2
             
    propogation = np.maximum(hospital,infection_map).tolist() #after a round of infection, how the matrix looks like
    
    # print("Hospital\n{}\nPropogation\n{}\n".format(np.matrix(hospital),np.matrix(propogation)))
    
    return propogation

def minTime(hospital):
  rounds = 0 #rounds = each unit of time, in other words each round of propagation

  while True:
    rounds = rounds+1
    print("\n\nRound{}".format(rounds))
    infected_hospital_iter = infect_hospital(hospital)
    #we break propagation when we cannot change the matrix anymore, i.e, no more new 2s can be formed
    if infected_hospital_iter == hospital: 
      print("No more propagation possible, breaking the loop")
      break
    else: #continue with propagation
      hospital = infected_hospital_iter.copy()

  row = len(hospital)
  col = len(hospital[0])

  for i in range(row):
    for j in range(col):
      if hospital[i][j] == 1: #in the final matrix after propagation cannot go on, if we encounter a 1 then return '-1'
        return '-1'
      res = rounds-1
      result = str(res)
  return result

