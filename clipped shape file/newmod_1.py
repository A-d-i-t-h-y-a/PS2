# import json
# import geopandas as gpd
# from shapely.geometry import shape, Polygon

# # Load the GeoJSON file with MultiPolygon geometries
# with open('mod_last_final_4.geojson') as f:
#     data = json.load(f)

# # Create empty lists to store the Polygon geometries and properties
# polygons = []
# properties = []

# # Convert MultiPolygon geometries to Polygon geometries
# for feature in data['features']:
#     geometry = feature['geometry']
#     if geometry['type'] == 'MultiPolygon':
#         multipolygon = shape(geometry)
#         if multipolygon.is_valid:
#             for polygon in multipolygon.geoms:
#                 if polygon.is_valid:
#                     polygons.append(polygon)
#                     properties.append(feature['properties'])
#     elif geometry['type'] == 'Polygon':
#         polygon = shape(geometry)
#         if polygon.is_valid:
#             polygons.append(polygon)
#             properties.append(feature['properties'])

# # Create a new GeoDataFrame from the Polygon geometries and properties
# df = gpd.GeoDataFrame(geometry=gpd.GeoSeries(polygons))
# df['properties'] = properties

# # Save the GeoDataFrame to a new GeoJSON file
# df.to_file('output3.geojson', driver='GeoJSON')



import json
import random
from shapely.geometry import shape, Point

# Load the GeoJSON file with MultiPolygon geometries
with open('mod_last_final_4.geojson') as f:
    data = json.load(f)

# Create a new GeoJSON object for Points
points_data = {
    'type': 'FeatureCollection',
    'features': []
}

# Convert MultiPolygon geometries to Point geometries
for feature in data['features']:
    geometry = feature['geometry']
    if geometry['type'] == 'MultiPolygon':
        multipolygon = shape(geometry)
        for polygon in multipolygon.geoms:
            bbox = polygon.bounds  # Get the bounding box of the polygon
            min_x, min_y, max_x, max_y = bbox
            num_points = 10  # Number of points to generate within each polygon
            for _ in range(num_points):
                x = random.uniform(min_x, max_x)
                y = random.uniform(min_y, max_y)
                point = Point(x, y)
                if polygon.contains(point):  # Check if the point is within the polygon
                    point_feature = {
                        'type': 'Feature',
                        'properties': feature['properties'],
                        'geometry': {
                            'type': 'Point',
                            'coordinates': (point.x, point.y)
                        }
                    }
                    points_data['features'].append(point_feature)
    elif geometry['type'] == 'Polygon':
        polygon = shape(geometry)
        bbox = polygon.bounds
        min_x, min_y, max_x, max_y = bbox
        num_points = 10
        for _ in range(num_points):
            x = random.uniform(min_x, max_x)
            y = random.uniform(min_y, max_y)
            point = Point(x, y)
            if polygon.contains(point):
                point_feature = {
                    'type': 'Feature',
                    'properties': feature['properties'],
                    'geometry': {
                        'type': 'Point',
                        'coordinates': (point.x, point.y)
                    }
                }
                points_data['features'].append(point_feature)

# Save the new GeoJSON file with Point geometries
with open('output5.geojson', 'w') as f:
    json.dump(points_data, f)

