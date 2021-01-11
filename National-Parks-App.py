# The Green Mountain Adventurers National Parks App
# Katherine Diaz, Tess Niewood, Lori Zakalik, Audrey Zhang

"""
Intermediate Python Final Project 
Group: The Green Mountain Adventurers
Members: Katherine Diaz, Tess Niewood, Lori Zakalik, Audrey Zhang

""" 

import pandas as pd
import nps_api as nps
import weatherFunction as wf
import parkplots as pp

def main():
    #read in national parks data
    parks_data = pd.read_csv('parks.csv')        
    print('NATIONAL PARKS KEY')
    
    #create a key-value dictionary that user can reference to input park code of choice
    parks_dict = dict(zip(parks_data['Park Code'], parks_data['Park Name']))
    for key, value in parks_dict.items():
        print('%s: %s' % (key, value))   
    
    #user selects park code to use in all menu functions
    parkCode = input('Enter the code for your National Park: ')
    parkCode = parkCode.upper()
    
    #get latitude and longitude for selected park to use in weather function
    for i in range(len(parks_data)):
        if parks_data.iloc[i]['Park Code'] == parkCode:
            lat = parks_data.iloc[i]['Latitude']
            long = parks_data.iloc[i]['Longitude']
    
    #program retrieves park that corresponds with chosen code        
    while parkCode != 'park app':
        #checks to make sure park code is valid.
        if parkCode in parks_dict.keys():
            park = parks_dict[parkCode]
            
            #program confirms with user that they inputted correct park code
            confirm_in = input('You selected '+park+'. Is this correct? Y/N: ')
            confirm = confirm_in.upper() #all codes are uppercase. This function allows user input to be any case
            
            #user can choose Y if park is correct, or N to enter a new park code
            while confirm != -5:
                if confirm == 'Y':
                    break
                elif confirm == 'N':
                    print('Please select another park code.')
                    
                #user can re-enter new park code
                parkCode = input('Enter the code for your National Park: ')
                parkCode = parkCode.upper()
                if parkCode in parks_dict.keys():
                    park = parks_dict[parkCode]
                    confirm_in = input('You selected '+park+'. Is this correct? Y/N: ')
                    confirm = confirm_in.upper()
                #if park code is invalid, returns error
                else:
                    print('ERROR: Please enter a valid park code.')
            break
        #if park code is invalid, returns error
        else:
            print('ERROR: Please enter a valid park code.')
        parkCode = input('Enter the code for your National Park: ')
        parkCode = parkCode.upper()   
    print()
    
    #Menu of info options for selected park
    print('Menu Options for '+park+':')
    a = '1. Park Descriptions'
    b = '2. All Park Activities'
    c = '3. Recommended Park Activities'
    d = '4. Park Alerts'
    e = '5. Park Amenities'
    f = '6. Today\'s Park Weather'
    g = '7. Park Weekend Weather Forecast'
    h = '8. Historical Park Visitation Data'
    i = '9. Park Location on Map'
    j = '0. Quit Program'
    #print menu
    print('%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s' % (a, b, c, d, e, f, g, h, i, j))
    #user inputs menu option of choice. Menu loops until user enters 0 to quit program
    option = int(input('Enter numeric menu choice 1-9 or enter 0 to quit: '))
    print()
    def menu(option):
        while option != 'menu choice':
            if option == 1:
                nps.get_info(parkCode)
                print('\n')
            elif option == 2:
                nps.get_activities(parkCode)
                print('\n')
            elif option == 3:
                nps.get_activities_rec(parkCode)
                print('\n')
            elif option == 4:
                nps.get_alerts(parkCode)
                print('\n')
            elif option == 5:
                nps.get_ameneties(parkCode)
                print('\n')
            elif option == 6:
                wf.getWeather(park, lat, long)
                print('\n')
            elif option == 7:
                wf.getWeekendWeather(lat, long, park)
                print('\n')
            elif option == 8:
                pp.parkVisitorsByYear(parkCode)
                print('\n')
            elif option == 9:
                pp.parkLocationOnMap(parkCode)
                print('\n')
            elif option == 0:
                print('You have quit the menu.')
                break
            #if user enters invalid menu option, returns an error and prompts user to re-enter
            else:
                print('ERROR: Please enter a valid menu option.')
            print()
            print('Menu Options for '+park+':')
            print('%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s' % (a, b, c, d, e, f, g, h, i, j))
            option = int(input('Enter numeric menu choice 1-9 or enter 0 to quit: '))
            print()
    menu(option)
            
if __name__ == '__main__':
    main()

