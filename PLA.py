import matplotlib.pyplot as plt
import numpy as np
import random
import time
from numpy import loadtxt

def pla(dataset):
    w = np.zeros(3)
    error = 1
    iter = 0
    while error : # and iter < 1000000:
        error = 0
        for x,s in dataset:
            x = np.array(x)
            if int(np.sign(w.T.dot(x))) != s:
                w = w + s * x
                error = 1
                iter = iter + 1
                #print("iter : ",iter)
        if not error:
            break
    return w , iter
    
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
    #print(dataset)
    x0 = data['a']
    xdata = data['b']
    ydata = data['c']
    label = data['z']
    start = time.time()
    w , iter= pla(dataset)
    end = time.time()
    print("PLA:")
    print("num of iterations: ",iter)
    print("執行時間：%f 秒" % float(end-start))
    l = np.arange(samples)
    a,b = -w[1]/w[2], -w[0]/w[2]
    print("m: %f ,b: %f" % (a,b))
    plt.plot(l, a*l + b, 'b-',label = 'PLA')
    plt.plot(xdata[:half], ydata[:half], '.', color='blue',label='positive')
    plt.plot(xdata[half:], ydata[half:], 'x', color='red',label='negative')
    plt.legend(loc='upper left');
    plt.show()
