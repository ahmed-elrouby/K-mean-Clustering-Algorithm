# Reading an excel file using Python
import xlrd
from random import sample
import math
#import numpy as np
def EclidianDistanse(centroid,node):
    sum=0
    for i in range(len(centroid)):
        a=(centroid[i]-node[i])*(centroid[i]-node[i])
        sum=sum+a
    return math.sqrt(sum)
def Mean(list_of_elment):
    list1=[]
    outer_size=len(list_of_elment)
    inner_size=len(list_of_elment[0])
    sum=0
    mean=0
    for i in range(inner_size):
        for j in range(outer_size):
            sum+=list_of_elment[j][i]
        mean=sum/outer_size
        list1.append(mean)
        sum=0
        mean=0
    return list1
def Make_cluster_list(data,centroid_List):
    cluster_list=[]
    listitems1=[]
    listitems2=[]
    listcomparison=[]
    Min=100000000000
    dataindex=[]
    centroidindex=[]
    for i in data:
        for j in centroid_List:
            #calculat Eclidaian distance and but in list
            dis=EclidianDistanse(j,i)
            if dis<Min:
                Min=dis
                dataindex=i
                centroidindex=j
            listcomparison=(list((centroid_List.index(j),data.index(i),dis))).copy()
            listitems1.append(listcomparison)
        listitems2.append(listitems1)
        listitems1=[]
        listcomparison=[]
        cluster_list.append(list((centroid_List.index(centroidindex),data.index(dataindex),Min)))
        Min=100000000000
    
    return cluster_list

def Make_New_Centroid(cluster_list,data,C_len):
    temp_list=[]
    for i in range(C_len):
        for j in range(len(cluster_list)):
            if cluster_list[j][0]==i:
                temp_list.append(data[cluster_list[j][1]])
        Centroid_List[i]=Mean(temp_list)
        temp_list=[]
    return Centroid_List

def read_excel_file(FileName,val):
    # To open Workbook
    wb = xlrd.open_workbook(FileName)
    sheet = wb.sheet_by_index(0)
    row_num=sheet.nrows
    num=float(val)
    x=float(num/100)
    z=int(x*row_num)
    # read row from file 
    list2=[]
    for i in range(z):
        if i==0:
            continue
        else:
            list1=sheet.row_values(i)
            del list1[0]
            list2.append(list1)
    return list2
#size of recored that we will works on
per=int(input("Enter the precetage of data that you want read it:"))
#the number of Key 
key=int(input("enter the key:"))
# Give the location of the file
loc = ("Absenteeism_at_work.xls")
Data=read_excel_file(loc,per)
Centroid_List=sample(Data,key)
initial_cluster_list=Make_cluster_list(Data,Centroid_List).copy()
final_cluster_list=[]
centriod_len=len(Centroid_List)
#print(len(initial_cluster_list))
    
while(True):
    Centroid_List=Make_New_Centroid(initial_cluster_list,Data,centriod_len)
    final_cluster_list=Make_cluster_list(Data,Centroid_List).copy()
    if(initial_cluster_list==final_cluster_list):
        break
    else:
        initial_cluster_list=final_cluster_list.copy()
        final_cluster_list=[]
        
        
for i in range(len(Centroid_List)):
        print("Cluster ",end="")
        print(i+1)
        for j in range(len(final_cluster_list)):
            if final_cluster_list[j][0]==i:
                print(Data[final_cluster_list[j][1]])