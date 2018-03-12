#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
#features_train = features_train[:len(features_train)/100] 
#labels_train = labels_train[:len(labels_train)/100] 
def svm_classifier(C=1.0):
	from sklearn.svm import SVC
	clf = SVC(C=C, kernel = "rbf")
	t0 = time()
	clf.fit(features_train, labels_train)
	print "training_time", round(time()-t0, 3), "s"
	t0 = time()
	pred = clf.predict(features_test)
	print "prediction_time", round(time()-t0, 3), "s"
	from sklearn.metrics import accuracy_score
	acc = accuracy_score(pred, labels_test)
	print "For C = "+str(C)+": accuracy is "+str(acc)
	return pred

#for C in [1.0,10.0,100.0,1000.0,10000.0]:
pred = svm_classifier(C=10000.0)
print "There are "+str(sum(pred))+"events "+"predicted to be in the Chris(1) class."
#answer=[pred[10],pred[26],pred[50]]
#print answer
#########################################################


