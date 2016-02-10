# Dealing with messy data
import numpy as np
import pandas as pd
pd.read_stata("state_names.dta")
pd.read_stata("state_names.dta", encoding="utf-8")
#Out:        
#    r               r_name
#    1          Aguascalientes
#   ...     
#   15             MA@xico ~~~~Mexico
#   16             Ocampo  


import chardet # check encoding should use
chardet.detect(rawdata)
# Output: {'encoding': 'EUC-JP', 'confidence': 0.99}

# Unix file
#$ file boston_python_is_awesome.tsv
#boston_python_is_awesome.tsv: UTF-8 Unicode English text

from unidecode import unidecode
print u'H\xeb\xe4vy M\xebt\xe4l'
unidecode(u'H\xeb\xe4vy M\xebt\xe4l') 
# 'Heavy Metal'

# Taking a peak
df = pd.read_excel("1033-program-foia-may-2014.xlsx")
df.columns
df.describe()
df.info()

# 
x = pd.read_csv(StringIO("a,b\n5,6.0\n,"))
x
x.info()

# Merging on different types makes data disappear
# Converting types
pd.read_csv(..., dtype={"column_1": int, "column_2": object})
# or
df.column = df.column.astype(int)

# The Semantics of Types
# Kinds of nothing
# No data available: None
# Nully values: "", 0

# Identifiers (Not numbers)
# 617-555-1234
# 721-07-1426
# 01605

# Categoricals (Not strings!)
# red, green, blue, orange
# A, B, AB, 0
# noun, verb, adjective, adverb

# Ordinals (Also not strings!)
# low, medium, high
# star, star star, star star star, star star star star
# high school, undergrad, graduate

# Dealing with Missing Data
## Converting custom N/A values
pd.read_csv(..., na_values=['N/A', 'Unknown'])
# or
df.replace('N/A', None)

## Dropping nulls
df.dropna(axis=1)
df.dropna(axis=1,  how="all")

## fill na
df.fillna(method="bfill")

# Playing with data
df.state
df['Item Name']
## Selecting multiple columns
df[['State', 'Country']]

# Indexing
expensive_stuff = df['Acquisition Cost'] > 100000
expensive_stuff
# Out: 
#0  False
#1  False
#2  False
#3  False
#4  False
#5  False
df[expensive_stuff] # Output only rows with True value
df[expensive_stuff].count()
## What were the highest cost items?
df.sort('Acquisition Cost', ascending=False) \
[['Item Name', 'Acquisition Cost']]
df.sort('Quantity', ascending=False) \ 
[['Item Name', 'Quantity', 'UI']]
## df.UI.value_counts() 
df.UI.value_counts()

df = df.replace({'UI': ['EA', 'EACH', 'PR' ...]}, {'UI':['Each', 'Each', 'Pair' ...]})
df = df.replace({'UI':'Unknown'}, {'UI': np.NaN})
df.UI.value_counts()[20:]
dontcare = df.UI.value_counts()[20:]
df = df[~df.UI.isin(dontcare.index)]

# Regexes and other string functions
df.column[df.column.str.contains('(\d{4} - \d{2} - \d{2})')]
df['Item Name'].str.lower()

# Pivoting
df.pivot(index='date', columns='variable', values='values')

# Grouping
df.groupby('State')[['Acquisition Cost']].sum()

# Transforming data with functions
df4 
f = lambda x: len(str(x))
df3['one'].map(f)

# Merging dataset
# Bane of everyone's exsitence
# Make sure the types match
# Check dataframe size before and after
# Try with how=inner and how=outer
ages
weights
pd.merge(ages, weights, left_on='cats', right_on='cats') # how=inner
pd.merge(ages, weights, left_on='cats', right_on='cats', how = 'outer')

# fuzzywuzzy and jellyfish
from fuzzywuzzy import fuzz
fuzz.ratio('this is a test', 'this is a test!') # return match percentage

# Graphs!
# ggplot
# bokeh
# seaborn
# matplotlib
# glue

# PDFs suck! tabula

# Scaling up
# Don't let notebooks get in the way of reusable code
# Sometimes repeatability matters
# Build tools: Make, tup
# Data pipelines: OKFN Bubbles, Storm, Spark etc

#1. Wrangle data
#2. Run calculations on standardized data
#3. ???
#4. Profit!!!

# Be conscious about what you load into memory
pd.read_csv(..., usecols=['blah'])
pd.read_csv(..., iterator=True, chunksize=100000)

# Push things down into the pandas / numpy layer

# Blaze
# Pandas-y interface for querying large datasets

# Takeaways
## Use the proper types for things
## Data has a tendency to be used in unanticipated ways
## Documentation matters
## Fix data before you need it fixed!
## Data cleaning is a necessary evil


