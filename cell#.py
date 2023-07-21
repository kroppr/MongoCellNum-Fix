from modules import *
import os, csv, re, sys
import numpy as np
import pandas as pd
from pymongo import MongoClient



ourArray = csv_to_arr('./clients.AutomatedSMS_ReviewRequests_Copy.csv')
for i in range(1, len(ourArray)):
    if re.search("[0-9]{10}", ourArray[i][9]) == None:
        this = ourArray[i][9]
        this = this.replace("(", "")
        this = this.replace(")", "")
        this = this.replace("-", "")
        this = this.replace(" ", "")
        ourArray[i][9] = this

make_csv('./clients.AutomatedSMS_ReviewRequests.csv', ourArray)
