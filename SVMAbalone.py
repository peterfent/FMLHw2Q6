import scipy, csv, random
import numpy as np
from libsvm.svmutil import *
import graphingfunctions as g  

def main():
    ftrain = open("trainingdata.txt", "w")
    ftest = open("testingdata.txt", "w")

    trainNum = 3133
    testNum = 1044

    abalone = open("abalone.data.txt")
    lines = abalone.readlines()
    line_count = 0
    for row in lines:
        genderBits = "3"
        if row[0] == "M":
            genderInt = "2"
        elif row[0] == "F":
            genderInt = "1"
        elif row[0] == "I":
            genderInt = "0"
        newRow = genderInt + row[1:]

        if line_count < trainNum:
            line_count = line_count+1

            toAdd = ""
            splitter = newRow[:-1].split(",")
            if int(splitter[-1]) < 10:
                toAdd = toAdd + "+1"
            else:
                toAdd = toAdd + "-1"
            for i in range(8):
                toAdd = toAdd + " " + str(i+1) + ":" + splitter[i]
            toAdd = toAdd + "\n"
            ftrain.write(toAdd)
        elif line_count-trainNum < testNum:
            line_count = line_count+1

            toAdd = ""
            splitter = newRow[:-1].split(",")
            if int(splitter[-1]) < 10:
                toAdd = toAdd + "+1"
            else:
                toAdd = toAdd + "-1"
            for i in range(8):
                toAdd = toAdd + " " + str(i+1) + ":" + splitter[i]
            toAdd = toAdd + "\n"
            ftest.write(toAdd)
        else:
            break

    y1, x1 = svm_read_problem("trainingdata.txt", return_scipy=True)
    scale_param = csr_find_scale_param(x1, lower=0)
    scaled_training = csr_scale(x1, scale_param)
    y2, x2 = svm_read_problem("testingdata.txt", return_scipy=True)
    scaled_testing = csr_scale(x2, scale_param)

    print(y1)
    print("break")
    print(x1)

    
    subset1 = []
    subset2 = []
    subset3 = []
    subset4 = []
    subset5 = []
    

    for item in scaled_training:
        randy = random.randint(1, 5)
        if randy == 1:
            subset1.append(item)
        elif randy == 2:
            subset2.append(item)
        elif randy == 3:
            subset3.append(item)
        elif randy == 4:
            subset4.append(item)
        elif randy == 5:
            subset5.append(item)

    y = [1, -1]
    prob1 = svm_problem(y, subset1)
    prob2 = svm_problem(y, subset2)
    prob3 = svm_problem(y, subset3)
    prob4 = svm_problem(y, subset4)
    prob5 = svm_problem(y, subset5)

    k = 5, m
    for d in range(1, 6):
        for cexp in range(-1*k, k+1):
            C = 1
            if cexp < 0:
                C = 1.0/(3**cexp)
            elif cexp > 0:
                C = 3.0**cexp
            param = svm_parameter('-t 1 -d %f -c %f', d, C)
            if d == 1:
                m = svm_train(prob1, param)
            if d == 2:
                m = svm_train(prob2, param)
            if d == 3:
                m = svm_train(prob3, param)
            if d == 4:
                m = svm_train(prob4, param)
            if d == 5:
                m = svm_train(prob5, param)

            
                

if __name__ == "__main__":
    main()
        
