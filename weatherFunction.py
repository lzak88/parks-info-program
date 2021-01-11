"""
Intermediate Python Final Project 
Group: The Green Mountain Adventurers
Members: Katherine Diaz, Tess Niewood, Lori Zakalik, Audrey Zhang

""" 

import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

def getWeather(park, lat, long):
    #get weather URL
    weatherURL = '%s%s%s%s' %('https://forecast.weather.gov/MapClick.php?textField1=', lat, '&textField2=', long)
    
    # Create the http request and request the page
    httpString = weatherURL
    #print(httpString)
    page = requests.get(httpString)
    

    while True:
        #check i ccurrent weather conditions available
        try:
                        # Scraping:
            # Parse the page
            soup = BeautifulSoup(page.content, 'html.parser')
            # Find the required tag
            seven_day = soup.find(id="seven-day-forecast")
            # Find the sub-tag
            forecast_items = seven_day.find_all(class_="tombstone-container")
            # Get the forecast items
            tonight = forecast_items[0]
            
            # Find the other data
            period = tonight.find(class_="period-name").get_text()
            short_desc = tonight.find(class_="short-desc").get_text()
            tempCheck = type(tonight.find(class_="temp"))
            temp = tonight.find(class_="temp").get_text()
            #print weather
            print('Today\'s weather in %s is: ' % (park))
            print(short_desc)
            print(temp)
            
            #Scrape Humidity, Wind Speed, Barometer, Dewpoint,
            #Visibility, Wind Chill, and Last update from the current conditions. Display those values with labels.
            
            x = soup.find(id="current_conditions_detail")
            y = x.find_all(class_="text-right")
        
            for i in y[:-1]:
                print(i.get_text() + ': ' + i.find_next("td").get_text())
            break
        #if not print short weather descripiton
        except(AttributeError, IndexError):
            try:
                # Scraping:
                # Parse the page
                soup = BeautifulSoup(page.content, 'html.parser')
                detailed_forecast = soup.find(id="detailed-forecast")
            
                detailed_labels = detailed_forecast.find_all(class_="col-sm-2 forecast-label")
                detailed_text = detailed_forecast.find_all(class_="col-sm-10 forecast-text")
                #create data frame of weather data
                labellist = []
                detailedlist = []
                for i in detailed_labels:
                    labellist.append(i.get_text())
                for i in detailed_text:
                    detailedlist.append(i.get_text())
                detailDict = {'Text':detailedlist}
                detailDF = pd.DataFrame(detailDict, index = labellist)
                #print weekend weather
                print("Today's weather in " + park+ " is: " + detailDF['Text'][0])
                break
            except(AttributeError, IndexError):
                # Scraping:
                # Parse the page
                soup = BeautifulSoup(page.content, 'html.parser')
                detailed_forecast = soup.find(id="detailed-forecast-body")
            
                detailed_labels = detailed_forecast.find_all(class_="col-sm-3 col-lg-2 forecast-label")
                detailed_text = detailed_forecast.find_all(class_="col-sm-9 col-lg-10 forecast-text")
                #create data frame of weather data
                labellist = []
                detailedlist = []
                for i in detailed_labels:
                    labellist.append(i.get_text())
                for i in detailed_text:
                    detailedlist.append(i.get_text())
                detailDict = {'Text':detailedlist}
                detailDF = pd.DataFrame(detailDict, index = labellist)
                #print weekend weather
                print("Today's weather in " + park+ " is: " + detailDF['Text'][0])
                break


def getWeekendWeather(lat, long, park):
    #get latitude and longitude of the park
    #get weather URL
    weatherURL = '%s%s%s%s' %('https://forecast.weather.gov/MapClick.php?textField1=', lat, '&textField2=', long)
    
    # Create the http request and request the page
    httpString = weatherURL
    page = requests.get(httpString)
    while True:
        try:
            # Scraping:
            # Parse the page
            soup = BeautifulSoup(page.content, 'html.parser')
            detailed_forecast = soup.find(id="detailed-forecast")
        
            detailed_labels = detailed_forecast.find_all(class_="col-sm-2 forecast-label")
            detailed_text = detailed_forecast.find_all(class_="col-sm-10 forecast-text")
            #create data frame of weather data
            labellist = []
            detailedlist = []
            for i in detailed_labels:
                labellist.append(i.get_text())
            for i in detailed_text:
                detailedlist.append(i.get_text())
            detailDict = {'Text':detailedlist}
            detailDF = pd.DataFrame(detailDict, index = labellist)
            #print weekend weather
            print("Friday's weather in " + park+ " is: " + detailDF['Text']['Friday'])
            print("Saturday's weather in " + park + " is: " + detailDF['Text']['Saturday'])
            print("Sunday's weather in " + park + " is: " + detailDF['Text']['Sunday'])
            break
        except:
            # Scraping:
                # Parse the page
                soup = BeautifulSoup(page.content, 'html.parser')
                detailed_forecast = soup.find(id="detailed-forecast-body")
            
                detailed_labels = detailed_forecast.find_all(class_="col-sm-3 col-lg-2 forecast-label")
                detailed_text = detailed_forecast.find_all(class_="col-sm-9 col-lg-10 forecast-text")
                #create data frame of weather data
                labellist = []
                detailedlist = []
                for i in detailed_labels:
                    labellist.append(i.get_text())
                for i in detailed_text:
                    detailedlist.append(i.get_text())
                detailDict = {'Text':detailedlist}
                detailDF = pd.DataFrame(detailDict, index = labellist)
                #print weekend weather
                print("Friday's weather in " + park+ " is: " + detailDF['Text']['Friday'])
                print("Saturday's weather in " + park + " is: " + detailDF['Text']['Saturday'])
                print("Sunday's weather in " + park + " is: " + detailDF['Text']['Sunday'])
                break