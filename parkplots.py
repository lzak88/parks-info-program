#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Intermediate Python Final Project 
Group: The Green Mountain Adventurers
Members: Katherine Diaz, Tess Niewood, Lori Zakalik, Audrey Zhang

""" 

import pandas as pd
import matplotlib.pyplot as plt


import geopandas as gpd
from shapely.geometry import Point, Polygon
    
parkVisitors = pd.read_csv('parkVisitors.csv')

parkLocations = pd.read_csv('parks.csv')

#import US map

US_map = gpd.read_file('cb_2018_us_state_5m.shp')

# Since only using National Park data, need to remove all the unnecessary
# parks from parkVisitors

parkVisitors2 = parkVisitors[parkVisitors['Park Name'].str.contains('NP')]
parkVisitors2 = parkVisitors2[~parkVisitors2['Park Name'].str.contains('PRES')]

parkVisitors2['Park Name'] = parkVisitors2['Park Name'].str.replace('NP', 'National Park')

parkData = pd.merge(parkLocations, parkVisitors2, on = ['Park Name'], how = 'outer')

parkData = parkData[0:56]

parkData = parkData.fillna("No data available")

# Need to transpose file to scatter plots

parkData_transposed = parkData
del parkData_transposed['Park Name']
del parkData_transposed['State']
del parkData_transposed['Acres']
del parkData_transposed['Latitude'] 
del parkData_transposed['Longitude']
parkData_transposed = parkData_transposed.T
parkData_transposed = parkData_transposed.rename(columns = parkData_transposed.iloc[0])
parkData_transposed = parkData_transposed.iloc[1:10]
parkData_transposed.reset_index(inplace =True)
parkData_transposed = parkData_transposed.rename(columns = {'index':'Year'})

## function that creates scatterplot graphs for visitor data

def parkVisitorsByYear(parkCode):
    if parkData_transposed.loc[0, str(parkCode)] == "No data available":
        print("No visitor data available for this park")
    else:
        plt.title('Visitor Data for ' + parkCode)
        plt.xlabel('Year')
        plt.ylabel('Total Visitors Per Year')
        plt.scatter(parkData_transposed['Year'], parkData_transposed[parkCode])
        plt.xticks(rotation=45)
        plt.show()

# plot lat and long on US map of all parks

parkVisitorData = parkLocations.merge(parkVisitors2, "outer")

parkVisitorData = parkVisitorData[0:56]

parkVisitorData = parkVisitorData.fillna("No data available")
    
def parkLocationOnMap(parkCode):
    parkCodeData = parkVisitorData[parkVisitorData['Park Code'] == parkCode]
    crs = 4326
    geometry = [Point(xy) for xy in zip(parkCodeData["Longitude"], parkCodeData["Latitude"])]
    geo_locations = gpd.GeoDataFrame(parkCodeData, crs = crs, geometry = geometry)
    fig, ax = plt.subplots(figsize=(15,15))
    US_map.boundary.plot(ax=ax, alpha=0.4, color='grey')
    geo_locations.plot(ax=ax,alpha=0.5,markersize=10)
    name = geo_locations["Park Name"]
    state = geo_locations["State"]
    acres = geo_locations["Acres"]
    plt.xlim(-170,-50)
    plt.ylim(15,75)
    geo_locations['coords'] = geo_locations['geometry'].apply(lambda x: x.representative_point().coords[:])
    geo_locations['coords'] = [coords[0] for coords in geo_locations['coords']]
    for index, row in geo_locations.iterrows():
        plt.annotate(s=row['Park Code'], xy=row['coords'])
    if parkCodeData["Average"].any() == "No data available":
        plt.title('Location of National Park: %s \n State: %s         Number of Acres: %s \n No visitor data information available' % (name.iloc[0], state.iloc[0], acres.iloc[0]), fontsize=15,fontweight='bold')
        plt.show()
    else:
        averageVisitor = geo_locations["Average"]
        name = geo_locations["Park Name"]
        plt.title('Location of National Park: %s \n State: %s         Number of Acres: %s \n Average Number of Visitors Per Year: %s' % (name.iloc[0], state.iloc[0], acres.iloc[0], averageVisitor.iloc[0]), fontsize=15,fontweight='bold')
        plt.show()
    
