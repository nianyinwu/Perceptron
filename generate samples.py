import random
import numpy as np
import matplotlib.pyplot as plt

def generate(m, b, num=2):
    x0 = []
    xdata = []
    ydata = []
    label = []
    # positive and negtive point number
    pos = int(num / 2) 
    neg = num - pos 
    for i in range(pos): # positive
        x = random.randint(0, num)
        r = random.randint(2, num) #no samples on the line
        y = m * x + b - r
        x0.append(1)
        xdata.append(x)
        ydata.append(y)
        label.append(1 if m >= 0 else -1)

    for i in range(neg): # negative
        x = random.randint(0, num)
        r = random.randint(2, num)
        y = m * x + b + r
        x0.append(1)
        xdata.append(x)
        ydata.append(y)
        label.append(-1 if m >= 0 else 1)
    return x0, xdata, ydata, label

if __name__ == '__main__':  
    m, b = 3, 10 # set the value of m and b
    print("the num of total samples : ")
    samples = int(input()) # the num of samples
    x = np.arange(samples)
    y = m * x + b
    plt.plot(x, y)
    half = int(samples / 2)
    x0, xdata, ydata, label = generate(m, b,num=samples)
    dataset = list(zip(x0,xdata,ydata)) 
    dataset = list(zip(dataset,label))
    np.savez('dataset',a=x0,b=xdata,c=ydata,z=label)
    for i in range(samples):
        print(xdata[i],ydata[i],label[i])
    b = np.dstack((x0,xdata,ydata))
    plt.plot(xdata[:half], ydata[:half], '.', color='blue',label='positive')
    plt.plot(xdata[half:], ydata[half:], 'x', color='red', label='negative')
    plt.legend(loc='upper left');
    plt.show()
