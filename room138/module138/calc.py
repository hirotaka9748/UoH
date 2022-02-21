import pandas as pd
import csv
from decimal import Decimal
import shutil
import glob
import os
import math

def toCSV(pico_path1,pico_csv_path):
    read_text_file = pd.read_csv (pico_path1)
    read_text_file.to_csv (pico_csv_path, index=None)
    
def mean(num,pico_csv_path,pico_path1,mean_path):
    detect_time = num
    df = pd.read_csv(pico_csv_path, header=None)
    for i in range(0,sum([1 for _ in open(pico_path1)]),detect_time):
        num = round(df[i:i + detect_time].sum()/detect_time,8)
        data = num.iloc[-1]
        with open(mean_path, 'a') as f:
            print(data, file=f)
            
def arctan(mean_path1,mean_path2,atan_path):   
    csvfile1 = open(mean_path1)
    csvfile2 = open(mean_path2)
    data1 = csvfile1.readlines()
    data2 = csvfile2.readlines()
    for i in range(0,sum([1 for _ in open(mean_path1)])):
        atan = math.degrees(math.atan(float(data1[i])/float(data2[i])))
        with open(atan_path, 'a') as f:
                print(atan, file=f)
            
def diff(atan_path,diff_path):            
    csvfile = open(atan_path)
    data = csvfile.readlines()
    first_low = data[0]
    last_low = data[sum([1 for _ in open(atan_path)])-1]
    diff_gosa = (float(first_low) - float(last_low))/(sum([1 for _ in open(atan_path)])-1)
    diff = round(diff_gosa,9)
    df2 = pd.read_csv(atan_path, header=None)
    for i in range(0,sum([1 for _ in open(atan_path)])):
        num2 = df2[i:i+1].sum()
        data2_gosa = num2.iloc[-1] + (diff*i)
        data2 = round(data2_gosa,9)
        with open(diff_path, 'a') as f:
            print(data2, file=f)
            
def motorStatus(status_path,status_csv_path):
    csvfile = open(status_path)
    data = csvfile.readlines()
    for i in range(0,sum([1 for _ in open(status_path)])):
        x = float(data[i])*0.0025*2
        with open(status_csv_path, 'a') as f:
            print(x, file=f)
            
def kerr(diff_path,kerr_path):
    df = pd.read_csv(diff_path,header=None)
    rows = df[0]
    max = rows.max()
    min = rows.min()
    mean = round((max + min)/2,10)
    csvfile = open(diff_path)
    data = csvfile.readlines()
    for i in range(0,sum([1 for _ in open(diff_path)])):
        x = (float(data[i]) - float(mean))
        kerr = round(x,10)
        with open(kerr_path, 'a') as f:
                print(kerr, file=f) 
                
def diff_kerr(atan_path,kerr_path):
    csvfile = open(atan_path)
    data = csvfile.readlines()
    first_low = data[0]
    for i in range(0,sum([1 for _ in open(atan_path)])):
        diff_data = data[i]-data[0]
        data2 = round(diff_data,9)
        with open(kerr_path, 'a') as f:
            print(data2, file=f)
            
def norm(diff_path,norm_path):
    df = pd.read_csv(diff_path,header=None)
    rows = df[0]
    max = rows.max()
    min = rows.min()
    mean = round((max + min)/2,10)
    csvfile = open(diff_path)
    data = csvfile.readlines()
    for i in range(0,sum([1 for _ in open(diff_path)])):
        x = (float(data[i]) - float(mean))/(float(max) - float(mean))
        norm = round(x,10)
        with open(norm_path, 'a') as f:
                print(norm, file=f)
            
def floatCurr(mean_path,curr_path,curr_tesla,tesla_path):
    for i in range(0,sum([1 for _ in open(mean_path)])):
        with open(curr_path) as f:
            data11 = f.readlines()[i]
            data22 = float(data11[0:12])
            data33 = data22 * curr_tesla
            with open(tesla_path, 'a') as f:
                print(data33, file=f)
                
def copyTesla(tesla_path,calc):
    shutil.copy(tesla_path,calc+"delete_tesla.csv")
    
def copyStatus(status_path,calc):
    shutil.copy(status_path,calc+"delete1_status.csv")
    
def copyPico1(pico_path,calc):
    shutil.copy(pico_path,calc+"delete2_pico1.csv")
    
def copyPico2(pico_path,calc):
    shutil.copy(pico_path,calc+"delete3_pico2.csv")
    
def copyDiff(norm_path,calc):
    shutil.copy(norm_path,calc+"delete_znorm.csv")
    
def link(calc,calc_path):
    csv_files = glob.glob(calc+'*.csv')
    for a in csv_files:
        print(a)
    data_list = []
    for file in csv_files:
        data_list.append(pd.read_csv(file))
    df = pd.concat(data_list, axis=1, sort=True)
    df.to_csv(calc_path,index=False)
    
def removeTesla(calc):
    os.remove(calc+"delete_tesla.csv")
    
def removeDiff(calc):
    os.remove(calc+"delete_znorm.csv")
    
def removeStatus(calc):
    os.remove(calc+"delete1_status.csv")
    
def removePico1(calc):
    os.remove(calc+"delete2_pico1.csv")
    
def removePico2(calc):
    os.remove(calc+"delete3_pico2.csv")

def move(calc_path,result):
    shutil.move(calc_path, result)
    
def sum_status(motor1_path,motor2_path,motor_path):
    for i in range(0,sum([1 for _ in open(motor1_path)])):
        with open(motor1_path) as f:
            data1 = f.readlines()[i]
            data11 = int(data1)
        with open(motor2_path) as f:
            data2 = f.readlines()[i]
            data22 = int(data2)    
            data_sum = data11 + data22
            with open(motor_path, 'a') as f:
                print(data_sum, file=f)
