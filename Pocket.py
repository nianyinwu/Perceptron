import matplotlib.pyplot as plt
import numpy as np
import random
import time
from numpy import loadtxt
    
# check error Pocket   
def check_errorP(w, x ,label):
    if int(np.sign(w.T.dot(x))) != label:
        return True
    else :
        return False
        
# get num of total error in dataset        
def sum_error(w, dataset):
    errors = 0
    for x, label in dataset:
        if check_errorP(w, x, label):
            errors += 1
    return errors

# Pocket演算法實作
def pocket(dataset):
    w = np.zeros(3) 
    iterp = 0
    premisclassified = sum_error(w,dataset)
    bestw = 0
    
    for iterp in range(0,100000):
        misclassified = None
        while True:
            x, label = random.choice(dataset) # random choose samples
            if check_errorP(w,x,label):
                x = np.array(x)
                w = w + label * x
                misclassified = sum_error(w,dataset)
                break
    
        if misclassified < premisclassified: # misclassified smaller than premisclassified
            bestw = w
            premisclassified = misclassified
    
        iterp = iterp + 1 
        #w = bestw
        if premisclassified == 0:
            break
        print("iter: %d , misclassified: %d , best misclassified: %d" % (iterp,misclassified , premisclassified))
    if premisclassified == 0 :
        print("!!halt!! iter: %d , misclassified: %d , best misclassified: %d" % (iterp,misclassified , premisclassified))
    else :
        print("!!iter done!! iter: %d , misclassified: %d , best misclassified: %d" % (iterp,misclassified , premisclassified))
    print("Accuracy :" , ((samples-premisclassified)/samples)*100, "%")
    return bestw , iterp 

if __name__ == '__main__':  
    m, b = 3, 10 # set the value of m and b
    print("the num of total samples : ")
    samples = int(input()) # the num of samples
    x = np.arange(samples)
    y = m * x + b
    plt.plot(x, y,'-y',label = 'Original')
    half = int(samples / 2)
    data = np.load('dataset.npz')
    dataset = list(zip(data['a'],data['b'],data['c'])) 
    dataset = list(zip(dataset,data['z']))
    x0 = data['a']
    xdata = data['b']
    ydata = data['c']
    label = data['z'] 
    print("Pocket:") 
    start1 = time.time()    
    wbest , iterp = pocket(dataset)
    end1 = time.time()
    print("num of iterations: ",iterp)
    print("執行時間：%f 秒"% float(end1-start1))
    l = np.arange(samples)
    ap,bp = -wbest[1]/wbest[2], -wbest[0]/wbest[2]
    print("m: %f, b: %f" % (ap,bp))
    plt.plot(l, ap*l + bp, 'g-',label = 'Pocket')
    plt.plot(xdata[:half], ydata[:half], '.', color='blue',label='positive')
    plt.plot(xdata[half:], ydata[half:], 'x', color='red',label='negative')
    plt.legend(loc='upper left');
    plt.show()
