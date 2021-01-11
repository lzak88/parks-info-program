# -*- coding: utf-8 -*-
"""
Intermediate Python Final Project 
Group: The Green Mountain Adventurers
Members: Katherine Diaz, Tess Niewood, Lori Zakalik, Audrey Zhang

""" 

import requests
import json

#%%

# api key 

api_key='&api_key=sbBCdoSqmjwNyakXvNL3LXTFd2cYpe4vfQTMq8qV'

# get info including park description and general weather

def get_info(parkCode):

    url='https://developer.nps.gov/api/v1/parks?parkCode=' + parkCode + api_key
        
    response = requests.get(url)
    
    if response.status_code==200:
        data=json.loads(response.content.decode('utf-8'))
        items=dict(data['data'][0])
        desc=items['description']
        weather=items['weatherInfo'] 
        
        print('\nPark Description: ' , desc)
    
        print('\nGeneral Weather: ', weather) 
    
    else:
        print('bad response code: ', response.status_code)



#%%

# prints list of all available activities at park

def get_activities(parkCode):

    url='https://developer.nps.gov/api/v1/parks?parkCode=' + parkCode + api_key
        
    response = requests.get(url)
    
    if response.status_code==200:
        data=json.loads(response.content.decode('utf-8'))
        items=dict(data['data'][0])
        activities=[]
        for act in items['activities']:
            activities.append(act['name'])
        if len(activities)>0:
            print('\nAll activities:')
            print(', '.join(activities))
        else:
            print('\nNo activiites information')
    else:
        print('bad response code: ', response.status_code)

    return activities 


#%% 

# get current park alerts

def get_alerts(parkCode):

    url='https://developer.nps.gov/api/v1/alerts?parkCode=' + parkCode + api_key
        
    response = requests.get(url)
    
    if response.status_code==200:
        data=json.loads(response.content.decode('utf-8'))
        items=dict(data['data'][0]) 
        
        categories=[]
        titles=[]
        descriptions=[]
        
        for i in items:
            cat=items['category'] 
            title=items['title']
            desc=items['description']
            categories.append(cat)
            titles.append(title)
            descriptions.append(desc)
        
        if len(categories)>0: 
            print('\nAlerts: ')
            print(cat + ': ' + title)
            print('Details: ' + desc)
            
        else: 
            print('\nNo current alerts')
    else:
        print('bad response code: ', response.status_code)
    
#%%

# get recommended activities for the park

def get_activities_rec(parkCode):
    url='https://developer.nps.gov/api/v1/thingstodo?parkCode=' + parkCode + api_key
        
    response = requests.get(url)
    
    if response.status_code==200:
        activities={}

        data=json.loads(response.content.decode('utf-8'))
        if len(data['data'])>0:
            items=dict(data['data'][0]) 
                        
            for i in items:
                activities[items['title']] = items['shortDescription']
        if len(activities)>0:
            print('\nRecommended activities: ')
            for i in activities:
                print(i)
                print('Description: ', activities[i]) 
        else:
            print('\nNo recommended activities')
            
    else:
        print('bad response code: ', response.status_code)
        
#%% 

# get list of all ameneties available at park

def get_ameneties(parkCode):
    url='https://developer.nps.gov/api/v1/amenities/parksplaces?parkCode=' + parkCode + api_key
        
    response = requests.get(url)
    
    if response.status_code==200:
        data=json.loads(response.content.decode('utf-8'))
        items=data['data']
        ameneties=[]
        for i in items:
            ameneties.append(i[0]['name'])
        
        if len(ameneties)>0:
            print('\nAll Ameneties: ')
            print(', '.join(ameneties)) 
        else:
            print('\nNo ameneties information available')  
            
    else:
        print('bad response code: ', response.status_code)
        return 
    
