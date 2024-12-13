"""Filter Data with boolean index"""

#(data['title'] == 'Watsi | Fund medical treatments for people around the world')
#homepage_index = (data['title'] == 'Watsi | Fund medical treatments for people around the world') # copied from above
#watsi_homepage = data[homepage_index] # selects the "True" rows recorded in the boolean index

"""Partially matching Text"""
#medical_referrer_index = data['referrer'].str.contains('medical')
#medical_referrals = data[medical_referrer_index]
#medical_referrals

#Note str.contains() is case sensitive, we can use .str.contains(case=False)