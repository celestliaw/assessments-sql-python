# Pandas
""".iloc is integer index-based. If you .iloc[1], it will return to you the row at the 1st index regardless of the index’s name. 
.loc however is label-based, meaning that .iloc[1] will only return the row at the first index if "1" is the index’s label. In the case of this dataframe 
.iloc[1] and .loc[1] will return the same row."""
#first three rows of the title column 
"""data['title'][:3]"""

#Selects the first 20 most-frequently occurrin
"""data['title'].value_counts()[:20]"""

#
"""data['title'].value_counts()[:20].plot(kind='barh')"""
