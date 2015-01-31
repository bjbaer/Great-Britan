import pandas as pd
from scipy import stats
data = '''Region, Alcohol, Tobacco
North, 6.47, 4.03
Yorkshire, 6.13, 3.76
Northeast, 6.19, 3.77
East Midlands, 4.89, 3.34
West Midlands, 5.63, 3.47
East Anglia, 4.52, 2.92
Southeast, 5.89, 3.20
Southwest, 4.79, 2.71
Wales, 5.27, 3.53
Scotland, 6.08, 4.51
Northern Ireland, 4.02, 4.56'''

# First, split the string on the (hidden characters that indicate) newlines
data = data.splitlines() # we could also do data.split('\n')

# Then, split each item in this list on the commas
# the bracketed expression is a list comprehension
data = [i.split(', ') for i in data] 

# Now, convert create a pandas dataframe
column_names = data[0] # this is the first row
data_rows = data[1::] # these are all the following rows of data
df = pd.DataFrame(data_rows, columns=column_names)
df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)

meanalc = df['Alcohol'].mean() #calculate the mean pounds spent on alcohol across GB
print "The mean pounds spent on alcohol is %s" % meanalc
meantob = df['Tobacco'].mean() #calculate the mean pounds spent on tobacco across GB
print "The mean pounds spent on tobacco is %s" % meantob
medalc = df['Alcohol'].median()#calculate the median pounds spent on tobacco across GB
print "The median pounds spent on alcohol is %s" % medalc
medtob = df['Tobacco'].median()#calculate the median pounds spent on tobacco across GB
print "The median pounds spent on tobacco is %s" % medtob
rangalc = max(df['Alcohol'])-min(df['Alcohol']) #calculate the range of pounds spent on alcohol in GB
print "The most in pounds any region in GB spends on Alcohol is %s" % rangalc
rangtob = max(df['Tobacco'])-min(df['Tobacco']) #calculate the range of pounds spent on alcohol in GB
print "The most in pounds any region in GB spends on T is %s" % rangtob
varalc = df['Alcohol'].var() #calculate the variance in alcohol sales in GB
print "The variance in alcohol sales across GB is %s" % varalc
vartob = df['Tobacco'].var() #cakcykate the variance in tobacco sales in GB
print "The variance in tobacco sales across GB is %s" % vartob
sdalc =df['Alcohol'].std() #calculate the standard deviation in alcohol sales in GB
print "The standard deviation in alcohol sales across GB is %s" % sdalc
sdtob = df['Tobacco'].std() #calculate the standard deviation in tobacco sales in GB
print "the standard deviation in alcohol sales across GB is %s" % sdtob
