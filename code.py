import csv
import numpy as np 


def getDataSource(data_path):
    marks_in_percentage = []
    days_present = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            marks_in_percentage.append(float(row["Marks In Percentage"]))
            days_present.append(float(row["Days Present"]))

    return {"x" : marks_in_percentage, "y": days_present}


def findCorrelation(ds):
    #correlation coefficient
    c = np.corrcoef( ds["x"],ds["y"])
    print( c[0,1] )

def setter():
    dp = "Student Marks vs Days Present.csv"
    ds = getDataSource(dp)
    findCorrelation(ds)

setter()

# correlation coefficient = 1 :  closely correlated
# 0 : not correlated
# -1 : inversely correlated