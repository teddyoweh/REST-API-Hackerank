#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getTotalGoals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING team
#  2. INTEGER year

# Author: Teddy Oweh
# Email: teddy@teddyoweh.net
import requests
def doac(who,data1):
    return  sum([int(k['team{}goals'.format(who)]) for k in data1['data']])  
    
def getTotalGoals(team, year):
    url1 = 'https://jsonmock.hackerrank.com/api/football_matches?year={}&team1={}'.format(year,team)
    url2 = 'https://jsonmock.hackerrank.com/api/football_matches?year={}&team2={}'.format(year,team)
    data1 = requests.get(url1).json()
    data2 = requests.get(url2).json()
   
    ans1= 0
    ans2= 0
    
    for i in range(data1['total_pages']):
        
        ans1+=doac(1,requests.get('https://jsonmock.hackerrank.com/api/football_matches?year={}&team1={}&page={}'.format(year,team,i+1)).json())
    for k in range(data2['total_pages']):
    
        ans2+=doac(2,requests.get('https://jsonmock.hackerrank.com/api/football_matches?year={}&team2={}&page={}'.format(year,team,k+1)).json())
        
        
            
    return ans1+ans2
 
