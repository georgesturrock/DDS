import sqlite3 as lite
import sys

con = lite.connect('population.db')

with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE Population(id INTEGER PRIMARY KEY, country TEXT, population INT)")
    cur.execute("INSERT INTO Population VALUES(NULL,'Germany',81197537)")
    cur.execute("INSERT INTO Population VALUES(NULL,'France', 66415161)")
    cur.execute("INSERT INTO Population VALUES(NULL,'Spain', 46439864)")
    cur.execute("INSERT INTO Population VALUES(NULL,'Italy', 60795612)")
    cur.execute("INSERT INTO Population VALUES(NULL,'Spain', 46439864)")

#############################################################################
# Had to install pandas
# sudo pip install pandas
#
import pandas as pd
import sqlite3

conn = sqlite3.connect('population.db')
query = "SELECT country from Population WHERE population > 50000000;"

df = pd.read_sql_query(query, conn)

for country in df['country']:
    print(country)

#############################################################################
# had to install python-tk and xlrd
# sudo apt-get install python-tk
# sudo pip install xlrd

from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt
import pandas as pd

file = r'/home/gsturrock/MSDS6303/Presidents.xls'
df2 = pd.read_excel(file)

# plot occupation in a pie chart
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'red', 'green', 'orange', 'white', 'brown', 'purple']
df2['Occupation'].value_counts().plot(kind='pie', title='Occupation by President', colors=colors)
plt.show()

# plot popularity in a histogram
df3 = df2[df2['% popular'] != 'NA()']

print(df3['% popular'])
df3['% popular'].plot(kind='hist', bins=8, title='Popularity by President', edgecolor='black', alpha=0.5, normed=1)
plt.show()