from modules import *
import os, csv, re, sys
import numpy as np
import pandas as pd
from pymongo import MongoClient


# Dependant on position of data, update this as needed
cellColumn = 9


ourArray = csv_to_arr('./clients.AutomatedSMS_ReviewRequests_Copy.csv')
for i in range(1, len(ourArray)):
    if not re.match("[0-9]{10}", ourArray[i][cellColumn]):
        this = ourArray[i][cellColumn]
        this = this.replace("(", "")
        this = this.replace(")", "")
        this = this.replace("-", "")
        this = this.replace(" ", "")
        ourArray[i][cellColumn] = this

make_csv('./clients.AutomatedSMS_ReviewRequests.csv', ourArray)

# Outputs array with gaps between every entry. Mongo ignores empty rows, so it works