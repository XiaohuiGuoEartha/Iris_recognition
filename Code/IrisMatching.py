#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 22:06:45 2018

@author: Xiaohui Guo   UNI xg2225

"""

import numpy as np
import pandas as pd
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import matplotlib.pyplot as plt

# function to calculate l1 distance
# input: vector1 and vector 2
# return the l1 distance of vector 1 and vector 2
def L1_distance(vector1,vector2):
    value = sum(abs(vector1 - vector2))
    return value


# function to calculate l2 distance
# input: vector 1 and vector 2
# return l2 distance
def L2_distance(vector1,vector2):
    value = sum((vector1 - vector2)**2)
    return value

# function to calculate euclidean norm, which is used to calculate cosine similarity distance
# input a vector return the euclidean norm
def Euclidean_Norm(vector):
    value = np.sqrt(sum(vector**2))
    return value

# function to calculate the cosine similarity distance
# input: two vectors
# output the cosine similarity distance
def cosine_similarity_distance(vector1,vector2):
    value = 1-np.dot(vector1,vector2)/(Euclidean_Norm(vector1)*Euclidean_Norm(vector2))
    return value

# function to make prediction
# input train matrix, test matrix, , which distance function you want to use, the desired dimension
def IrisMatching(training_matrix, test_matrix, distance_function, dimension_after_LDA):
    
    # if input of dimension_after_LDA is "No", then make prediction on the original non dimension reduced matrix.
    # input the desired number of featuer dimension, then do feature reduction using LDA
    
    if dimension_after_LDA == 'No':
        train_transform = training_matrix
        test_transform = test_matrix
    else:
        
        # class for train dataset
        y_train = []
        for i in range(1,109):
            y_train.append(i)
            y_train.append(i)
            y_train.append(i)
        # class for test dataset
        y_test = []
        for i in range(1,109):
            y_test.append(i)
            y_test.append(i)
            y_test.append(i)
            y_test.append(i)
    
        # reduce the dimension of training matrix
        train_X = training_matrix
        train_y = np.array(y_train)
    
        clf = LinearDiscriminantAnalysis(n_components = dimension_after_LDA)
        clf.fit(train_X, train_y)
        
        # train matrix after feature reduction
        train_transform = clf.transform(train_X)
    
        # reduce the dimension of testing matrix
        # test matrix after feature reduction, this is created based on the trained model
        test_transform = clf.transform(test_matrix)
    
    
    
    # Create index for y_train in original dataset
    y_train = []
    for i in range(1,109):
        y_train.append(i)
        y_train.append(i)
        y_train.append(i)
    
    # the list is to contain the predicted classification result
    prediction_list = []
    # this loop is to calcualte the prediction  for each eye in test dataset
    for j in range(0,len(test_transform)):
        # this list is to contain the distance value 
        distance_list = []
        
        for i in range(0,len(train_transform)):
            distance = L1_distance(train_transform[i,:],test_transform[j,:])
            distance_list.append(distance)   
        # find min distance value
        minimum_distance = min(distance_list)
        # find index of the eye
        index = distance_list.index(minimum_distance)
        # find the class according of the index
        class_name = y_train[index]
    
        prediction_list.append(class_name)

        
    return prediction_list



