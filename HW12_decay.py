#hw12 Decay

import numpy as np
import matplotlib.pyplot as plt
import time as time

def decay(tau,timestep = 1):
    """
    Returns the value of decay probability in 1 second given the half-life value of the element
    """
    return 1 - 2**(-timestep/tau)
    
if __name__ == "__main__":
    NBi213 = 10000 #starting atoms
    NPb = 0
    NTl = 0
    NBi209 = 0
    
    tau_Bi = 46*60 #half life of Bismuth_213 in seconds
    tau_Tl = 2.2 * 60 #half life of thallium in seconds
    tau_Pb = 3.3 * 60 #half life of Lead in seconds
    timestep = 1 #second
    tmax = 20000 #max time
    ts = np.arange(0, tmax, timestep)#time range
    #open lists to collect how many atoms exist at each timestep
    Bi213 = []
    Pb = []
    Tl = []
    Bi209 = []
    start = time.time()
    for t in ts:
        #log number of remaning elements
        Bi213.append(NBi213)
        Pb.append(NPb)
        Tl.append(NTl)
        Bi209.append(NBi209)
        #step through # of Bi213 atoms remaining
        for i in range(NBi213):
            #if atom decays
            if np.random.random()<decay(tau_Bi):
                if np.random.random()<= 2.09/100:
                    NBi213 -= 1
                    NTl += 1
                else:
                    NBi213 -=1
                    NPb += 1
        #step through # of Tl atoms remain
        for i in range(NTl):
            if np.random.random() < decay(tau_Tl):
                NTl -=1
                NPb +=1
        #steps through # of lead atoms remain
        for i in range(NPb):
            if np.random.random() < decay(tau_Pb):
                NPb -= 1
                NBi209 += 1
    print('Time to compute:',time.time()-start)
    #code for plot
    plt.plot(ts, Bi213, 'k.', label = 'Bi213')
    plt.plot(ts, Pb, 'r.', label = 'Pb')
    plt.plot(ts,Tl, 'c.',label = 'Tl')
    plt.plot(ts,Bi209,'m.',label = 'Bi209')
    plt.xlabel('Time [s]')
    plt.ylabel('Number of atoms')
    plt.yscale('log')
    #plt.xscale('log')
    plt.title('Radioactive Decay')
    plt.legend()
    plt.show()
