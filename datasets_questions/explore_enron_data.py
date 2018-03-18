#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print "The total number of person in Enron dataset is "+str(len(enron_data))+"."
print "The total number of features included in Enron dataset is "+str(len(enron_data['METTS MARK']))+"."

num_POI = 0
for key in enron_data:
	if enron_data[key]["poi"] == 1:
		num_POI += 1
print "The total number of person of interest is "+str(num_POI)+"."

print "The total stock value of James Prentice is "+str(enron_data["PRENTICE JAMES"]["total_stock_value"])+"."

print "The number of messages from this person to poi is "+str(enron_data["COLWELL WESLEY"]["from_this_person_to_poi"])+"."

print "The value of stock option exercised by Jeff Skilling is "+str(enron_data["SKILLING JEFFREY K"]["exercised_stock_options"])+"."


print enron_data["LAY KENNETH L"]["total_payments"]
print enron_data["SKILLING JEFFREY K"]["total_payments"]
print enron_data["FASTOW ANDREW S"]["total_payments"]


print enron_data["METTS MARK"]
num_with_salary_data = 0
num_known_email_adress = 0
num_total_payments_with_NaN = 0
num_total_payments_with_NaN_for_POI = 0
for key, value in enron_data.items():
	if str(value["salary"]).isdigit():
		num_with_salary_data += 1
	if value["email_address"] != "NaN":
		num_known_email_adress += 1
	if value["total_payments"] == "NaN":
		num_total_payments_with_NaN += 1
	if value["poi"] == 1 and value["total_payments"] == "NaN":
		num_total_payments_with_NaN_for_POI += 1

print "The number of folks who have qualified salary in the dataset is "+str(num_with_salary_data)+"."
print "The number of folks who have email adress known from the dataset is "+str(num_known_email_adress)+"."
print "The percentage of people in the dataset have NaN for their total payments is "+str(1.0*num_total_payments_with_NaN/len(enron_data))+"."
print "The percentage of people in the dataset have NaN for their total payments is "+str(num_total_payments_with_NaN)+"."
print "The percentage of POI in the dataset have NaN for their total payments is "+str(1.0*num_total_payments_with_NaN_for_POI/num_POI)+"."
