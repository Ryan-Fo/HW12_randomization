#HW12 Monte Carlo / Randomizers

import numpy as np
import matplotlib.pyplot as plt
import time as time

if __name__ == "__main__":
	
    count_all_6 = 0
    count_sum_11 = 0
    total_rolls = 100000
    sumlist = []
    start = time.time()
    
    for t in range(total_rolls):
        x = np.random.randint(1,7)
        y = np.random.randint(1,7)
        z = np.random.randint(1,7)
        total = x + y + z
        sumlist.append(total)
        
        if x == 6 and y == 6 and z == 6:
            count_all_6 += 1
        if x + y + z == 11:
            count_sum_11 += 1
        t+=1

    #probabilities
    all_6_odds = count_all_6 / total_rolls * 100
    sum_11_odds = count_sum_11 / total_rolls * 100
    print('Time to compute 100,000 dice rolls:',time.time() - start,'seconds.')
    print('Odds to roll all 6:',all_6_odds,'%')
    print('Odds to roll sum of 11:',sum_11_odds,'%')
    
    
    #plotting code
    plt.hist(sumlist,bins = 15,density = True,color = 'dodgerblue')
    plt.ylabel('Probability of Total Rolled')
    plt.xlabel('Total of Rolling 3 Dice')
    plt.title('Total Dice Value for 100k rolls')
    plt.show()