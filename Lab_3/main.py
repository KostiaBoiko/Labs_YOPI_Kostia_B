import math
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

File = open("result.txt", "w+")
averagex, averagey = 0.0, 0.0
def connect_txt(nameoffile):
    inputdata = []
    input = open(nameoffile)
    input.seek(1)
    for line in input:
        inputdata.append(input.read(3))
        input.read(1)
        inputdata.append(input.read(2))
    for i in range(int(len(inputdata))):
        inputdata[i] = inputdata[i].replace(',', '.')
    data = [[0 for i in range(2)] for j in range(int(len(inputdata) / 2))]
    index0 = 0
    index1 = 0
    for i in range(int(len(inputdata))):
        if i % 2 == 0:
            data[index0][0] = float(inputdata[i])
            index0 +=1
        elif i % 2 != 0:
            data[index1][1] = int(inputdata[i])
            index1 += 1
    return data

def dataX(data):
    inputdatadata = []
    for i in range(len(data)):
        inputdatadata.append(data[i][0])
    return inputdatadata

def dataY(data):
    inputdatadata = []
    for i in range(len(data)):
        inputdatadata.append(data[i][1])
    return inputdatadata


def trend(data):
    if max(data) == data[len(data)-1]:
        print("Trend of data is positive")
        File.write("\nTrend of data is positive")
    elif min(data) == data[len(data)-1]:
        print("Trend of data is negative")
        File.write("\nTrend of data is negative")
    else:
        print("The data does not have any trend")
        File.write("\nThe data does not have any trend")

def centerofweight(x, y):
    chis = 0
    znam = 0
    for i in range(len(data)):
        chis += x[i]*y[i]
        znam += x[i]
    centerofweight = chis/znam
    print("\nGravitycenter = " + str(centerofweight))
    File.write("\n\nGravitycenter = " + str(centerofweight))


def covariance(x, y):
    global averagex, averagey
    covarience = 0.0
    for i in range(len(x)):
        averagex += x[i]
        averagey += y[i]
    averagex = averagex / len(x)
    averagey = averagey / len(y)
    for i in range(len(x)):
        covarience += (x[i] - averagex) * (y[i] - averagey)
    covarience = covarience / (len(x)-1)
    print("Covarince: ", covarience)
    File.write("Covarince: " + str(covarience))


def correlation(x, y):
    global averagex, averagey
    corcoef, sum1, sum2, sum3 = 0.0, 0.0, 0.0, 0.0
    for i in range(len(x)):
        sum1 += (x[i] - averagex) * (y[i] - averagey)
        sum2 += (x[i] - averagex) * (x[i] - averagex)
        sum3 += (y[i] - averagey) * (y[i] - averagey)
    sum2 = sum2 * sum3
    corcoef = sum1/math.sqrt(sum2)
    print("Correlation coefficient:", corcoef)
    File.write("\nCorrelation coefficient:" + str(corcoef))


def lineofregression(X, Y):
    global averagex, averagey
    byx, sumx, sumy, sumxy, sumx2, sumy2 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
    for i in range(len(X)):
        sumx += X[i]
        sumy += Y[i]
        sumxy += X[i] * Y[i]
        sumx2 += X[i] * X[i]
        sumy2 += Y[i] * Y[i]
    byx = (len(X) * sumxy - (sumx * sumy)) / ((len(X) * sumx2) - sumx**2)
    x, y = sp.symbols("x,y")
    line = sp.Eq(y-averagey, byx*(x-averagex))
    linex = sp.solve(line, y)
    liney = sp.solve(line, x)
    x1 = np.linspace(0, 9)
    y1 = byx * (x1 - averagex) + averagey
    plt.plot(x1, y1)
    strlinex = str(linex)
    strliney = str(liney)
    strlinex = strlinex.replace("[", "")
    strlinex = strlinex.replace("]", "")
    strliney = strliney.replace("[", "")
    strliney = strliney.replace("]", "")
    print("Line of regression of y on x")
    print("x = " + strliney)
    print("y = " + strlinex, "\t(y on x)")
    File.write("Line of regression of y on x\n")
    File.write("x = " + strliney)
    File.write("\ny = " + strlinex + "\t(y on x)")


nameoffile = input("Input the name of input file: ")
data = connect_txt(nameoffile)
data = sorted(data)
infoX = dataX(data)
infoY = dataY(data)
print("Sorted data: ", data)
File.write("Sorted data: " + str(data))
print("\n")
File.write("\n\n")
trend(data)
print("\n")
File.write("\n\n")
centerofweight(infoX, infoY)
covariance(infoX, infoY)
correlation(infoX, infoY)
print("\n")
File.write("\n\n")
lineofregression(infoX, infoY)
plt.scatter(infoX, infoY)
plt.grid()
plt.show()