'''
Challenge 15:
Write a Python function to download and save sequence of files

Input: URL for first item, output directory path

URL: http://699340.youcanlearnit.net/image001.jpg
        ...
     http://699340.youcanlearnit.net/image001.jpg
'''


import requests

def download_files(URL, output_path):

    for i in range(1,51):
        filename = 'image'+str(i).zfill(3) +'.jpg'
        print('Downloading '+filename, end = '')
        try:
            file = requests.get(URL+ filename)
            open(output_path+filename,'wb').write(file.content)
            print('\t\t...Complete')
        except:
            print('Error while downloading '+filename)


URL = 'http://699340.youcanlearnit.net/'
output_path = 'C:/Users/Akshay Chavan/Desktop/Python Challenges/c15Files/'

download_files( URL, output_path)
