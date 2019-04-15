#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 22:09:49 2018

@author: Xiaohui Guo  UNI: xg2225
"""
import numpy as np
import pandas as pd
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from IrisMatching import L1_distance,L2_distance,Euclidean_Norm,cosine_similarity_distance,IrisMatching



# calcuate the accuracy
def CRR_accuracy(ground_truth,prediction):
    corect_prediction_count= 0 
    # coun the correct prediction
    for i in range(len(ground_truth)):
        if ground_truth[i] == prediction[i]:
            corect_prediction_count += 1
    # calculate accuracy number of correct prediction devided by the total number
    accuracy = corect_prediction_count/len(ground_truth)

    return accuracy

# function to create table 3
def create_table3(training_matrix,testing_matrix):
    
    # testing dataset class list
    y_test = []
    for i in range(1,109):
        y_test.append(i)
        y_test.append(i)
        y_test.append(i)
        y_test.append(i)
    
    # set fround truth
    ground_truth = y_test
    
    # calculate the prediction based on l1 l2 cosine distance measure
    l1_prediction = IrisMatching(training_matrix, testing_matrix, L1_distance, 'No')
    l2_prediction = IrisMatching(training_matrix, testing_matrix, L2_distance, 'No')
    cosine_similarity_prediction = IrisMatching(training_matrix, testing_matrix, cosine_similarity_distance, 'No')

    # calculate the prediction accuracy
    
    l1 = CRR_accuracy(ground_truth,l1_prediction)
    l2 = CRR_accuracy(ground_truth,l2_prediction)
    consine = CRR_accuracy(ground_truth,cosine_similarity_prediction)
    
    # when reduce the dimension of features, calcualte the prediction, set the dimension to be 107
    l1_prediction_reduced = IrisMatching(training_matrix, testing_matrix, L1_distance, 107)
    l2_prediction_reduced = IrisMatching(training_matrix, testing_matrix, L2_distance, 107)
    cosine_similarity_prediction_reduced = IrisMatching(training_matrix, testing_matrix, cosine_similarity_distance, 107)


    # calculate the prediction
    l1_recuded = CRR_accuracy(ground_truth,l1_prediction_reduced)
    l2_reduced = CRR_accuracy(ground_truth,l2_prediction_reduced)
    consine_reduced = CRR_accuracy(ground_truth,cosine_similarity_prediction_reduced)
    
    # create list to make tables
    distance_name = ['L1 distance measure','L2 distance measure','Cosine Similarity measure']
    distance_name_df = pd.DataFrame(distance_name, columns =['Similarity measure'] )
    
    # create list to make tables
    original_feature_set = [l1,l2,consine]
    original_feature_set_df = pd.DataFrame(original_feature_set, columns = ['Original feature set correct recognition rate'] )
    
    # create list to make tables
    reduced_feature_set = [l1_recuded,l2_reduced,consine_reduced]
    reduced_feature_set_df = pd.DataFrame(reduced_feature_set, columns = ['Reduced feature set correct recognition rate'] )

    # create list to make tables
    table_prepare = pd.concat([distance_name_df, original_feature_set_df], axis=1)
    Recognition_result_table = pd.concat([table_prepare, reduced_feature_set_df], axis=1)
    Recognition_result_table = Recognition_result_table.set_index(['Similarity measure'])

    return Recognition_result_table


# function to draw the plot
def draw_plot(index_for_dimension_reduction,training_matrix,testing_matrix):
    # fround truth test classification
    y_test = []
    for i in range(1,109):
        y_test.append(i)
        y_test.append(i)
        y_test.append(i)
        y_test.append(i)
    
    # y value for y asix in the plot
    # calculate the accuracy when dimension is in different value
    y =[]
    for item in index_for_dimension_reduction:
        prediction = IrisMatching(training_matrix, testing_matrix, cosine_similarity_distance, item)
        y_value = CRR_accuracy(y_test,prediction)
        y.append(y_value)
    # plot the graph
    plt.plot(index_for_dimension_reduction, y, '-o')
    plt.xlabel('Dimensionality of the feature vector')
    plt.ylabel('Correct recognition rate')
    plt.title('Recognition results using features of different dimensionality')
    plt.show()
    
    return plt.show()


def LDA_prediciton_using_sklearn(train_X,test_X,n_componetns):
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
    
    train_y = np.array(y_train)
    test_y = np.array(y_test)
    
        
    clf = LinearDiscriminantAnalysis(n_components = n_componetns)
    clf.fit(train_X, train_y)

    value = clf.score(test_X,test_y)
    
    return value
