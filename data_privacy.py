from cmath import nan
from operator import ge
import os
from pickle import LONG_BINGET
# from turtle import left
import pandas as pd

GOOGLE_API_KEY = "AIzaSyAFxvs4OijavyR0Oi0vMEcR_OdKuYu72zg"
Base_address = "https://maps.googleapis.com/maps/api/geocode/json?"
# geolocator = GoogleV3(api_key=GOOGLE_API_KEY)

os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY
# headerList = ["id",	"description","firstname",	"gender",	"lastname",	"location",	"profilephotolink"
# ]
# df = pd.read_csv('foursquareusers.csv',on_bad_lines='skip')#usecols = headerList
# print(df.shape)

df =  pd.read_table('foursquareusers',delimiter = ';')
df2 = df[df.location.notna()]
geo_loc = pd.read_csv("fs_latlong.csv",delimiter=";",names=["location","latitude","longitude"])
twitter_users = pd.read_csv("twitterusers.csv",delimiter=",")
latlong = {}
twitter_loc = pd.read_csv("Twitter_latlongitude.csv",delimiter=";")
df_twitter_merged = pd.read_csv("merge_twitter.csv")
df_fs_merged = pd.read_csv("fs_merged_file.csv")
# df.location = df.location.str.strip()
# print(df.location.unique())
# geo_loc.location = geo_loc.location.str.strip()
# df.location = df.location.astype(str)
# geo_loc.location = geo_loc.location.astype(str)
# df.location = df.location.str.encode("utf-8")
# geo_loc.location=geo_loc.location.str.encode("utf-8")


# twitter_users.location = twitter_users.location.str.strip()
# twitter_loc.location = twitter_loc.location.str.strip()
# twitter_users.location = twitter_users.location.astype(str)
# twitter_loc.location = twitter_loc.location.astype(str)

# df_twitter = pd.merge(twitter_users,twitter_loc,left_on="location",right_on="location",how="left")
# df_twitter.to_csv("merge_twitter.csv")

# df_fs = pd.merge(df,geo_loc,left_on="location",right_on="location",how="left")
# df_fs.to_csv("merged_file.csv")


# print(df.info())
# print(geo_loc.info())

# for i,r in geo_loc.iterrows():
#     # print(geo_loc["location"],geo_loc["latitude"],geo_loc["longitude"]),
#     latlong[str(geo_loc["location"])] = [geo_loc["latitude"],geo_loc["longitude"]] 
# print(latlong)

# for i,r in df.iterrows():
#     if df[i]['location'] == None:
#         df['latitude'],df['longitude'] = ",",","
#     else:
#         df['latitude'],df['longitude'] = latlong[df["location"]].split(";")
        
# print(twitter_users.shape,twitter_users.location.unique().shape)
# # print(df.shape,geo_loc.shape)
# exit()
# # print((df2.location.unique()))
# df3 = df2.location.unique()
# from geopy.geocoders import Nominatim
# # geolocator = Nominatim()
# import geocoder
# geolocator = Nominatim(user_agent="sample app")
# for i in df2.location.unique():
#     # print (i)
#     if i == nan:
#         continue
#     # data = geolocator.geocode("1 Apple Park Way, Cupertino, CA")
#     # try:
#     data = geolocator.geocode(i,timeout=None)
#     # data = geolocator.google(i)
#     if data == None:
#         print(i,",",",")
#         continue
#     # df2['latitude'] = data.latitude
#     # df2['longitude'] = data.longitude
#     print(i,";",data.latitude,";",data.longitude)
#     # df2["loc"] = df2["location"].apply(geolocator.geocode(i,timeout=None))
#     # data.raw.get("lat"), data.raw.get("lon")
#     # print(data.point.latitude, data.point.longitude)
# # print(df2.location.value_counts())
# # print(fs)
# # df2["loc"] = df2["location"].apply(geolocator.geocode)
# # df2["point"]= df2["loc"].apply(lambda loc: tuple(loc.point) if loc else None)
# # df2[['lat', 'lon']] = pd.DataFrame(df['data'].to_list(), index=df.index)
# twitter_users_1 = twitter_users[twitter_users.location.notna()]

# for i in twitter_users_1.location.unique():
#     # print (i)
#     if i == nan:
#         continue
#     # data = geolocator.geocode("1 Apple Park Way, Cupertino, CA")
#     # try:
#     data = geolocator.geocode(i,timeout=None)
#     # data = geolocator.google(i)
#     if data == None:
#         print(i,",",",")
#         continue
#     # df2['latitude'] = data.latitude
#     # df2['longitude'] = data.longitude
#     print(i,";",data.latitude,";",data.longitude)
import geopy.distance
import numpy as np
for index,row in df_twitter_merged.iterrows():
    for index_1,row_1 in df_fs_merged.iterrows():
        if (pd.isna(row['latitude']) or pd.isna(row['longitude']) or pd.isna(row_1['latitude']) or pd.isna(row['longitude'])):
            
            continue
        coords_1 = (row['latitude'], row['longitude'])
        coords_2 = (row_1["latitude"], row_1['longitude'])
        # print("compute",type(row['latitude']),row['longitude'],row_1["latitude"],row_1['longitude'])
        print("distance",geopy.distance.geodesic(coords_1, coords_2).km)