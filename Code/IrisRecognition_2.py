#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 22:40:21 2018

@author: earthaguo
"""
import numpy as np
import pandas as pd
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from IrisMatching import L1_distance,L2_distance,Euclidean_Norm,cosine_similarity_distance,IrisMatching
from PerformanceEvaluation import CRR_accuracy,create_table3,draw_plot,LDA_prediciton_using_sklearn

# function to show table 3 and plot
def IrisRecognition_2(train_matrix,test_matrix,n_components):
    import numpy as np
    import pandas as pd
    from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
    import matplotlib.pyplot as plt
    from sklearn.metrics import accuracy_score
    from IrisMatching import L1_distance,L2_distance,Euclidean_Norm,cosine_similarity_distance,IrisMatching
    from PerformanceEvaluation import CRR_accuracy,create_table3,draw_plot

    
    # import dataset
    training_matrix_df = pd.read_csv(train_matrix,header = None)
    testing_matrix_df = pd.read_csv(test_matrix,header = None)
    training_matrix = np.array(training_matrix_df)
    testing_matrix = np.array(testing_matrix_df)
   
    # calculate the ground truth
    y_test = []
    for i in range(1,109):
        y_test.append(i)
        y_test.append(i)
        y_test.append(i)
        y_test.append(i)
    ground_truth = y_test

    # dimension selection
    index_for_dimension_reduction = [1,10,20,30,40,50,60,70,80,90,107]
    
    # show table 3
    table3 = create_table3(training_matrix,testing_matrix)
    print(table3)
    
    prediction_by_lda_sklearn = LDA_prediciton_using_sklearn(training_matrix,testing_matrix,n_components)
    
    print('The prediction accuracy calculated by sklearn package function is ', prediction_by_lda_sklearn)
    # draw plot
    draw_plot(index_for_dimension_reduction,training_matrix,testing_matrix)
    
    return

    