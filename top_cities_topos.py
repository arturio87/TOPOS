#!/usr/bin/env python
# coding: utf-8

# In[344]:


from bs4 import BeautifulSoup
import requests
import pandas as pd
from itertools import cycle
from collections import defaultdict
import re

#URL for the assignment
url = 'https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population'

#Download page in html
page = requests.get(url)

#Parse downloaded page using web-scraper
soup = BeautifulSoup(page.text, 'html.parser')

#Locate the table to be scraped
tab = soup.find('table', class_= 'wikitable sortable')

#Create two empty lists
a = []
b = []

#Locate and clean headers that will be used as columns. Add to the list A
for row in tab.find_all('tr'):
    for cell in row.find_all('th'):
        a.append(cell.text.rstrip('\n').upper())

#Locate and clean rows. Add to the list B
for row in tab.find_all('tr'):
    for cell in row.find_all('td'):
        b.append(cell.text.rstrip('\n'))

#Drop square brackets with characters inside, that appear in few rows
a = [re.sub(r"\[\w+\]","",x) for x in a]

#Insert whitespace between numbers and characters, that appear in few columns names
a = [re.sub(r"(\d+)\B(\D+)","\\1 \\2", x) for x in a]

#Drop metric values
b = [x for x in b if "km2" not in x]

#Drop square brackets with characters inside, that appear in few rows
b = [re.sub(r"\[\w+\]","",x) for x in b]
#b = [re.sub(r"\D+\B\D","",x) for x in b]

#Merge two lists, and repeating the short one several times to create list of tuple pairs
c = list(zip(cycle(a), b))

#Create default dictionary
d = defaultdict(list)

#Convert merged list with tuples into dictionary with keys
for k, v in c:
    d[k].append(v)
    
#Create data frame from dictionary
df = pd.DataFrame.from_dict(d)
df = df.set_index('2018 RANK')

#Clean data and convert to integers, and drop location data since it useless in the table.
df = df.drop(['LOCATION'], axis=1)
df['2016 LAND AREA'] = df['2016 LAND AREA'].str.replace(r"\D+", '', regex=True).astype('int64', errors='ignore')
df['2016 POPULATION DENSITY'] = df['2016 POPULATION DENSITY'].str.replace(r"\D+", '', regex=True).astype('int64', errors='ignore')
df['2018 ESTIMATE'] = df['2018 ESTIMATE'].str.replace(r"\D+", '', regex=True).astype('int64', errors='ignore')
df['2010 CENSUS'] = df['2010 CENSUS'].str.replace(r"\D+", '', regex=True).astype('int64', errors='ignore')
df.rename(columns={'2016 POPULATION DENSITY':'2016 POPULATION DENSITY PER SQ MI', '2016 LAND AREA':'2016 LAND AREA SQ MI'}, inplace = True)


# In[327]:


path = str(input("Enter the directory, for example: /users/username/Desktop/filename.csv"))


# In[346]:


df.to_csv(path, encoding='utf-8-sig')

