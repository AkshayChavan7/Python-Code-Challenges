'''
Challenge 12: Write a Python function to merge multiple CSV files into one

Input: List of input files, output file path
>>> merge_csv(['class1.csv','class2.csv'],'all_students.csv')
'''

import os, glob
import pandas as pd

def merge_csv(i_files,o_path ):
    all_df = []
    for f in i_files:
        df = pd.read_csv(f, sep=',')
        df['file'] = f.split('/')[-1]
        all_df.append(df)
    merged_df = pd.concat(all_df, ignore_index=True, sort=True)
    merged_df.to_csv(o_path+'merged.csv')


f1 = 'C:/Users/Akshay Chavan/Desktop/Python Challenges/c12Files/file1.csv'
f2 = 'C:/Users/Akshay Chavan/Desktop/Python Challenges/c12Files/file2.csv'

merge_csv([f1,f2],'C:/Users/Akshay Chavan/Desktop/Python Challenges/c12Files/')
