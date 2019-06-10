# Web-Scraping Wikipedia

https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population

[1] Requirements:

BeautifulSoup,
Pandas,
Re,
Itertools,
Requests

*Ideally Anaconda package installed*

[2] Steps:

Request and parse html page using BeautifulSoup and Requests. 
After inspecting the source locate tags which contain necessary data. 
Separate headers and rows into two lists and use Regex to briefly clean data.
Combine two lists into one to create list that close to key/value structure and eventually transform the merged list into dictionary.
Create data frame from dictionary using Pandas. 
Next stage of data cleaning with focus on specific issues of dataframe columns, and transforming some column data into integers
As a result we get a dataframe, ready for further data analysis.
