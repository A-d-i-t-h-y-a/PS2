import sys
import os
import rasterio
import yaml
import uuid
from osgeo import osr


def get_grid_spatial_projection(fname):
    with rasterio.open(fname, 'r') as img:
        left, bottom, right, top = img.bounds
        print("fnamejsshfdsfbh wbi", fname)
        spatial_reference = str(
            str(getattr(img, 'crs_wkt', None) or img.crs.wkt))
        geo_ref_points = {
            'ul': {'x': left, 'y': top},
            'ur': {'x': right, 'y': top},
            'll': {'x': left, 'y': bottom},
            'lr': {'x': right, 'y': bottom},
        }
        return geo_ref_points, spatial_reference

def get_coords(geo_ref_points, spatial_ref):
    spatial_ref = osr.SpatialReference(spatial_ref)
    t = osr.CoordinateTransformation(spatial_ref, spatial_ref.CloneGeogCS())

    def transform(p):
        lat, lon, z = t.TransformPoint(p['x'], p['y'])
        return [lon,lat]

    # return {key: transform(p) for key, p in geo_ref_points.items()}
    return [transform(p) for key, p in geo_ref_points.items()]

# Get the input TIF file path from command-line argument
if len(sys.argv) < 2:
    print("Please provide the path to the input TIF file.")
    sys.exit(1)

tif_path = sys.argv[1]
# print(tif_path, type(tif_path))
# print(os.path.abspath(tif_path))

# Extract the filename and directory from the TIF path
tif_dir = os.path.dirname(tif_path)
# print(tif_dir)
# tif_filename = os.path.splitext(os.path.basename(tif_path))[0]

with rasterio.open(tif_path) as dataset:
    # Get the raster's spatial transform
    transform = dataset.transform

    # Get the raster's shape
    height, width = dataset.shape

    # Get the corner coordinates
    ul_x, ul_y = transform * (0, 0)             # Upper Left
    ur_x, ur_y = transform * (width, 0)         # Upper Right
    lr_x, lr_y = transform * (width, height)    # Lower Right
    ll_x, ll_y = transform * (0, height)        # Lower Left
    geo_ref_points, spatial_ref = get_grid_spatial_projection(
        os.path.abspath(tif_path))
    # crs = dataset.crs
    # print(crs)
# Generate the output in the specified format
    # '$schema': 'https://schemas.opendatacube.org/dataset',
output = {
    'id': str(uuid.uuid4()),
    'crs': 'EPSG:4326',
    'product': {
        'name': 'gmw_latest'  # CHanged from gmw to GMW and remove crs from here
    },
    'geometry': {
        'type': 'Polygon',
        'coordinates': [[
            [ll_x, ll_y],
            [ul_x, ul_y],
            [ur_x, ur_y],
            [lr_x, lr_y],
            [ll_x, ll_y]
        ]]
    },
    'grid_spatial': {
        'projection': {
            'geo_ref_points': geo_ref_points,

            'spatial_reference': spatial_ref,
        }
    },
    'creation_dt': f'{tif_path[-8:-4]}-12-31T00:00:00Z',
    'measurements': {
        'mangrove': {
            'path': os.path.abspath(tif_path)
        }
    },
    'properties': {
        'datetime': f'{tif_path[-8:-4]}-12-31T00:00:00Z',
        'odc': {
            'processing_datetime': f'{tif_path[-8:-4]}-12-31T00:00:00Z'
        }
    },
    'lineage': {'source_datasets': {}}
}

# Save the output as a YAML file
yaml_path = os.path.join(tif_dir, f'gmw_dataset{tif_path[-8:-4]}.yaml')
with open(yaml_path, 'w') as yaml_file:
    yaml.dump(output, yaml_file, default_flow_style=False)

print(f"Output saved as '{yaml_path}'.")
