#coding: utf-8

"""
@Author: Well
@Date: 2014-03-14
"""

# 习题38; 列表的操作

#create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'fl',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states an d some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'fl': 'Jacksonville',
    'NY': 'New York',
    'OR': 'Portland'
}

# add some more cities

# print out some cities
print '-' * 50
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

# print some states
print '-' * 50
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

# do it by using the state then cities dict
print '-' * 50
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

# print every state abbreviation
print '-' * 50
for state, abbrev in states.items():
    print "%s has abbreviated %s" % (state, abbrev)

# print every city in state
print '-' * 50
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)

# now do both at the same time
print '-' * 50
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])

print '-' * 50

# safely get a abbreviation by state that might not be there
# state = 'Texas'
state = 'Oregon'
abbrev = states.get(state, None)

if not abbrev:
    print "Sorry, no %s." % state
else:
    print "the abbreviation of %s is %s." % (state, states[state])

# get a city with a default value
city_1 = cities.get('TX', 'Does not exit')
city_2 = cities.get('OR', 'Does not exit')
print "The city for the state 'TX' is %s" % city_1
print "The city for the state 'OR' is %s" % city_2











