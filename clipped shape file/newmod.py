import geojson

# Load the existing GeoJSON file
with open('last_final_2.geojson') as f:
    existing_data = geojson.load(f)

# Define the area of interest (bounding box coordinates)
# Latitude = (15.828260040178774, 15.84411406692531)
# Longitude = (80.94417572021486, 80.97198486328126)
# Latitude = (15.832223663515174, 15.843536077393118)
# Longitude = (80.95018386840822, 80.9685516357422)

min_lon = 80.95018386840822
min_lat = 15.832223663515174
max_lon = 80.9685516357422
max_lat = 15.843536077393118

# Create a new GeoJSON object for modified data
modified_data = {
    "type": "FeatureCollection",
    "features": []
}

# Create a polygon representing the area of interest
bbox_polygon = geojson.Polygon([[
    (min_lon, min_lat),
    (max_lon, min_lat),
    (max_lon, max_lat),
    (min_lon, max_lat),
    (min_lon, min_lat)
]])

# Add the area of interest as a feature with pixel value 0
feature = {
    "type": "Feature",
    "properties": {
        "PXLVAL": 0
    },
    "geometry": bbox_polygon
}
modified_data['features'].append(feature)

# Add the existing features to the modified data
modified_data['features'].extend(existing_data['features'])

# Save the modified GeoJSON
with open('mod_last_final_4.geojson', 'w') as f:
    geojson.dump(modified_data, f)
