import rasterio
from rasterio.features import geometry_mask
from shapely.geometry import shape, box
import json

# Load the GeoJSON file
geojson_file = "./india.geojson"


# Define the latitude and longitude ranges

lat_range = (21.822747643151935, 22.59575464855534)
lon_range = (68.88427734375001, 69.90600585937501)

# Read the GeoJSON data
with open(geojson_file) as f:
    data = json.load(f)

# Extract the coordinates of the first feature (assuming it is a Polygon or MultiPolygon)
coordinates = data['features'][385]['geometry']['coordinates']
area_name = data['features'][385]['properties']['NAME_3']

# Create a Shapely geometry from the coordinates
geometry = shape({"type": "MultiPolygon", "coordinates": coordinates})

# Create a bounding box geometry based on the latitude and longitude ranges
bbox = box(lon_range[0], lat_range[0], lon_range[1], lat_range[1])

# Intersect the GeoJSON geometry with the bounding box geometry
intersection = bbox.intersection(geometry)

# Set up the metadata for the output GeoTIFF file
meta = {
    'driver': 'GTiff',
    'count': 1,
    'dtype': 'float32',
    'nodata': 0.0,
    'width': 512,  # Define the width of the output image
    'height': 512,  # Define the height of the output image
    'transform': rasterio.transform.from_bounds(*intersection.bounds, 512, 512),
    'crs': 'EPSG:4326'  # Specify the CRS (WGS84)
}

# Create a new raster image
image = rasterio.features.geometry_mask([intersection], out_shape=(meta['height'], meta['width']),
                                        transform=meta['transform'], invert=True)
image = image.astype(meta['dtype']) * 0.2

# color_map = {0.2: (255, 0, 0)}  # Assigned value of 0.2 is mapped to red color (255, 0, 0)
color_interpretation = {0.2: (255, 0, 0)}

# Save the image as a GeoTIFF file
output_file = f"./Gujarat/{area_name}.tif"
with rasterio.open(output_file, 'w', **meta) as dst:
    dst.write(image, 1)
    dst.write_colormap(1, color_interpretation)




