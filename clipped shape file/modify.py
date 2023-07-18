import geojson
from shapely.geometry import shape, mapping, Polygon, MultiPolygon

# Load the existing GeoJSON file
with open('final2.geojson') as f:
    existing_data = geojson.load(f)

# Define the area of interest (bounding box coordinates)

min_lon = 80.89302062988283
min_lat = 15.7605361485013
max_lon = 81.03515625000001
max_lat = 15.89794240102209

# Create a bounding box polygon for the area of interest
bbox_polygon = Polygon([
    (min_lon, min_lat),
    (max_lon, min_lat),
    (max_lon, max_lat),
    (min_lon, max_lat),
    (min_lon, min_lat)
])

# Create a new GeoJSON object for modified data
modified_data = {
    "type": "FeatureCollection",
    "features": []
}

# Iterate through the bounding box grid and check if each grid cell intersects with the existing data
for lon in range(int(min_lon), int(max_lon)):
    for lat in range(int(min_lat), int(max_lat)):
        cell_polygon = Polygon([
            (lon, lat),
            (lon + 1, lat),
            (lon + 1, lat + 1),
            (lon, lat + 1),
            (lon, lat)
        ])
        
        cell_intersect = False
        
        for feature in existing_data['features']:
            geometry = shape(feature['geometry'])
            if geometry.intersects(cell_polygon):
                cell_intersect = True
                break
        
        if not cell_intersect:
            # Create a new feature with pixel value 0 for non-mangrove cells
            feature = {
                "type": "Feature",
                "properties": {
                    "PXLVAL": 0
                },
                "geometry": mapping(cell_polygon)
            }
            modified_data['features'].append(feature)

# Add the existing features with pixel value 1 to the modified data
for feature in existing_data['features']:
    modified_data['features'].append(feature)

# Save the modified GeoJSON
with open('mod_final5.geojson', 'w') as f:
    geojson.dump(modified_data, f)











# import geojson

# # Load the existing GeoJSON file
# with open('./final2.geojson') as f:
#     existing_data = geojson.load(f)


# modified_data = {
#     "type": "FeatureCollection",
#     "features": []
# }

# # Get the bounding box of the existing data
# # Latitude = (15.7605361485013, 15.89794240102209)
# # Longitude = (80.89302062988283, 81.03515625000001)
# min_lon = 80.89302062988283
# min_lat = 15.7605361485013
# max_lon = 81.03515625000001
# max_lat = 15.89794240102209

# # Iterate through all pixels in the bounding box and create features
# for lon in range(int(min_lon), int(max_lon) + 1):
#     for lat in range(int(min_lat), int(max_lat) + 1):
#         # Check if the pixel exists in the existing data
#         pixel_exists = False
#         for feature in existing_data['features']:
#             geometry = feature['geometry']
#             if geometry['type'] == 'MultiPolygon':
#                 coordinates = geometry['coordinates']
#                 for polygon_coords in coordinates:
#                     if geojson.Point((lon, lat)).within(geojson.MultiPolygon(polygon_coords)):
#                         pixel_exists = True
#                         break
#             elif geometry['type'] == 'Polygon':
#                 coordinates = geometry['coordinates']
#                 if geojson.Point((lon, lat)).within(geojson.Polygon(coordinates)):
#                     pixel_exists = True
#                     break

#         # Create a new feature with pixel value 0 for non-existing pixels
#         if not pixel_exists:
#             feature = {
#                 "type": "Feature",
#                 "properties": {
#                     "PXLVAL": 0
#                 },
#                 "geometry": {
#                     "type": "MultiPolygon",
#                     "coordinates": [[[(lon, lat), (lon + 1, lat), (lon + 1, lat + 1), (lon, lat + 1), (lon, lat)]]]
#                 }
#             }
#             modified_data['features'].append(feature)

# # Add the existing features with pixel value 1 to the modified data
# for feature in existing_data['features']:
#     modified_data['features'].append(feature)

# # Save the modified GeoJSON
# with open('mod_final2.geojson', 'w') as f:
#     geojson.dump(modified_data, f)

# Initialize the minimum and maximum longitude and latitude values
# min_lon = float('inf')
# min_lat = float('inf')
# max_lon = float('-inf')
# max_lat = float('-inf')

# # Find the minimum and maximum values of longitude and latitude
# for feature in existing_data['features']:
#     lon, lat = feature['geometry']['coordinates']
#     min_lon = min(min_lon, lon)
#     min_lat = min(min_lat, lat)
#     max_lon = max(max_lon, lon)
#     max_lat = max(max_lat, lat)

# min_lon = float('inf')
# min_lat = float('inf')
# max_lon = float('-inf')
# max_lat = float('-inf')

# # Find the minimum and maximum values of longitude and latitude
# for feature in existing_data['features']:
#     geometry = feature['geometry']
#     if geometry['type'] == 'MultiPolygon':
#         for polygon in geometry['coordinates']:
#             for coord in polygon[0]:  # Assuming single outer ring
#                 lon, lat = coord[0], coord[1]
#                 min_lon = min(min_lon, lon)
#                 min_lat = min(min_lat, lat)
#                 max_lon = max(max_lon, lon)
#                 max_lat = max(max_lat, lat)

# # print(existing_data)

# grid_spacing = 0.01  # Adjust the grid spacing as needed
# grid_points = []
# for lon in range(int(min_lon), int(max_lon) + 1):
#     for lat in range(int(min_lat), int(max_lat) + 1):
#         point = geojson.Point((lon, lat))
#         grid_points.append(geojson.Feature(geometry=point, properties={"pixel_value": 0}))

# # Add the new features to the existing GeoJSON features
# existing_data['features'].extend(grid_points)
# # print(existing_data)

# # print(min_lat, min_lon, max_lat, max_lon)

# with open('modified_file.geojson', 'w') as f:
#     geojson.dump(existing_data, f)


# Find the maximum "PXLVAL" value in the existing features
# grid_spacing = 0.01  # Adjust the grid spacing as needed
# grid_points = []
# for feature in existing_data['features']:
#     geometry = feature['geometry']
#     if geometry['type'] == 'MultiPolygon':
#         for polygon in geometry['coordinates']:
#             for coord in polygon[0]:  # Assuming single outer ring
#                 lon, lat = coord[0], coord[1]
#                 point = geojson.Point((lon, lat))
#                 properties = {"PXLVAL": 0}  # Set the pixel value to 0
#                 grid_points.append(geojson.Feature(geometry=point, properties=properties))

# # Add the new features to the existing GeoJSON features
# existing_data['features'].extend(grid_points)

# # Save the modified GeoJSON
# with open('mod_final.geojson', 'w') as f:
#     geojson.dump(existing_data, f)