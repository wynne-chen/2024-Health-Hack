#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 15:15:00 2024

@author: wynne
"""

from pathlib import Path
import streamlit as st
import pandas as pd
import folium as fs
from streamlit_folium import folium_static
from geopy.geocoders import Nominatim
from geopy import distance
import re



st.title('Health Hack 2024')
st.subheader('by Eugenia, Mei Qi, Wynne, Sheila, and Yvonne', divider = 'green')

st.subheader('Donation Box Locations')

# import hospital locations
donations_path = Path(__file__).parent / 'data/locations.csv'
donations = pd.read_csv(donations_path)


# map centred on singapore's central catchment area.
m = fs.Map(location=[1.363605, 103.814168],tiles = 'CartoDB Positron', zoom_start=12, scrollWheelZoom=False)

for lat, lon, name in zip(donations['Latitude'], donations['Longitude'], donations['Name']):
    fs.Marker(location=[f'{lat}',f'{lon}'],popup= f'{name}', icon=fs.Icon(color ='green', icon = 'plus')).add_to(m)

st_map = folium_static(m, width = 1200, height = 800)


# to find closest pins

# Create a geocoder instance
geolocator = Nominatim(user_agent="my_geocoder")

# Input field for address
address = st.text_input("Enter an address in Singapore:")
latitude = 0.0
longitude = 0.0

home_rad = st.slider('Choose max distance for donation boxes (km): ', 1, 15, 2)

if st.button("Submit"):
    address = address.strip().lower()
    
    # for some reason the common short form blk is not recognised
    # you will get an address in arabic
    # it also cannot read postal codes in the SXXXXXX format but (XXXXXX) or XXXXXX is fine
    if 'blk' in address:
        address = address.replace('blk', '').strip()
    elif re.search('([S])?(\d{6})', address):
        address = address.replace('s', '')
    
    
    if address:
        try:
            location = geolocator.geocode(query = address, timeout = 5, addressdetails = True)
            country = location.raw['address']['country']
            
            if country != 'Singapore':
                raise ValueError('Please enter an address in Singapore.')

            if location:
                latitude = location.latitude
                longitude = location.longitude

                st.success(f"The neighbourhood is: {location.raw['address']['suburb']}. Latitude: {latitude}, Longitude: {longitude}")
                
                
                # let's draw a new map centred on the chosen address
                home = [latitude, longitude]


                if home_rad <= 2.5:
                    zoom = 14
                elif  2.5 < home_rad <= 5:
                    zoom = 13
                elif 5 < home_rad <= 10:
                    zoom = 12
                elif 10 < home_rad <= 15:
                    zoom = 11

                home_rad_m = home_rad * 1000

                m2 = fs.Map(location= home,tiles = 'Cartodb Positron', zoom_start= zoom, scrollWheelZoom=False)

                fs.Marker(location=home,popup= 'Selected Address', icon=fs.Icon(color ='red', icon = 'home')).add_to(m2)
                fs.Circle(location=home,fill_color='green', radius= home_rad_m, weight=2, color="green").add_to(m2)

                all_dist = []

                for lat, lon, name in zip(donations['Latitude'], donations['Longitude'], donations['Name']):
                    all_dist.append(distance.geodesic(home, (lat, lon)).km)

                donations['Distance'] = all_dist

                donations_ltd = donations[(donations['Distance'] < home_rad)]

                donations_ltd = donations_ltd.sort_values(by = 'Distance', ascending = True)

                for lat, lon, name in zip(donations_ltd['Latitude'], donations_ltd['Longitude'], donations_ltd['Name']):
                    fs.Marker(location=[f'{lat}',f'{lon}'],popup= f'{name}', icon=fs.Icon(color ='green', icon = 'plus')).add_to(m2)


                st_map = folium_static(m2, width = 1200, height = 800)

                st.dataframe(donations_ltd)
            else:
                st.warning("Address not found.")
        except:
            st.warning("Address not found.")
    else:
        st.warning("Please enter a valid address.")


