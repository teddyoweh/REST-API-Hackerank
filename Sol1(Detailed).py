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
#
# Author: Teddy Oweh
# Email: teddy@teddyoweh.net
import requests
def doac(who,data):
    box =[]
    for k in data['data']:
        num = int(k['team{}goals'.format(who)])
        box.append(num)
    ans = sum(box) # Adding al the numbers in the array
    return ans
    
def getTotalGoals(team, year):
    url1 = 'https://jsonmock.hackerrank.com/api/football_matches?year={}&team1={}'.format(year,team) # First URL for when the team parsed is team1
    url2 = 'https://jsonmock.hackerrank.com/api/football_matches?year={}&team2={}'.format(year,team) # First URL for when the team parsed is team2
    
    response1 = requests.get(url1) # API Call to the API Endpoint for the First URL
    response2 = requests.get(url2) # API Call to the API Endpoint for the Second URL
    
    # Decoding the API Response to JSON Format to be parsed as a dictionary then to allow easy Mutation.
    data1=response1.json() 
    data2=response2.json()
 
    # Initial values for the sum of for goals on each page for the 2 URLS
    ans1= 0
    ans2= 0
    
    for i in range(data1['total_pages']):  # Making a loop to repeat based of the number of pages. 
        n_url1 = 'https://jsonmock.hackerrank.com/api/football_matches?year={}&team1={}&page={}'.format(year,team,i+1)
        n_response1 = requests.get(n_url1)
        n_data1 =  n_response1.json()
        n_1 = 1 # Indicating that this is for URL 1
        
        
        ans1+= doac(n_1,n_data1) # Adding the sum of goals on each page // Function (doac()) Calculates the sum of goals on each page.
        
    for k in range(data2['total_pages']):  # Making a loop to repeat based of the number of pages. 
        n_url2 = 'https://jsonmock.hackerrank.com/api/football_matches?year={}&team2={}&page={}'.format(year,team,k+1)
        n_response2 = requests.get(n_url2)
        n_data2 =  n_response2.json()
        n_2 = 2 # Indicating that this is for URL 2
        
        
        ans2+= doac(n_2,n_data2) # Adding the sum of goals on each page // Function (doac()) Calculates the sum of goals on each page.
        
    
        
            
    return ans1+ans2 # Returning the sum of goals on each page for both URLS

