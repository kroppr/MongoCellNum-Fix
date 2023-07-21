import os
import csv

def go_to(path):
	dir = os.listdir(path)
	return dir

def make_csv(c,arr):
	with open(c,'w') as file:
		mywriter=csv.writer(file)
		mywriter.writerows(arr)

def csv_to_arr(c):
	arr=[]

	with open(c,'r') as file:
		pulled=csv.reader(file)
		for rows in pulled:
			arr.append(rows)
	return arr

def search(dir,tag):
	tag=str(tag)
	arr=[]
	for file in dir:
		if tag in file:
			arr.append(file)
	return arr

def freesurferSetup():
	os.system('export FREESURFER_HOME=/usr/apps/engineering/FreeSurfer/freesurfer')
	os.system('source $FREESURFER_HOME/SetUpFreeSurfer.csh')
	os.system('export SUBJECTS_DIR=/projects/abv/TRANSLATIONAL_IMAGING/M15_562/MissingStats/')

def bubble(arr):
	for i in range(len(arr)-1):
		for j in range(1,len(arr)-i-1):
			if float(arr[j])>float(arr[j+1]):
				a=arr[j]
				arr[j]=arr[j+1]
				arr[j+1]=a
	return arr
		

def statFinder(text, method):
	t=open(text, method)
	line=t.readline()
	while line:
		line=t.readline()
		if 'Your Target' in line:
			stat=float(line[53:60]) # Wherever in line
	return (stat)
