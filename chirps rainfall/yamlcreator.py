import sys
import os
import rasterio
import yaml
import uuid
from datetime import datetime
from osgeo import osr

# Get the input TIF file path from command-line argument
print(str(uuid.uuid4()))
# if len(sys.argv) < 2:
#     print("Please provide the path to the input TIF file.")
#     sys.exit(1)

# tif_path = sys.argv[1]
# print(tif_path[-8:-4], type(tif_path))

# Extract the filename and directory from the TIF path
# with rasterio.open(fname, 'r') as img:
#     spatial_reference = str(str(getattr(img, 'crs_wkt', None) or img.crs.wkt))
# tif_dir = os.path.dirname(tif_path)
# cs_code = "EPSG:4326"
# spatial_ref = osr.SpatialReference()


# spatial_ref.SetFromUserInput(cs_code)
# # print(tif_dir)
current_datetime = datetime.now()

# # Format the date and time
formatted_dt = current_datetime.strftime("%Y-%m-%dT%H:%M:%S.%f") + "Z"
print(formatted_dt)
# tif_filename = os.path.splitext(os.path.basename(tif_path))[0]

# with rasterio.open(tif_path) as dataset:
#     # Get the raster's spatial transform
#     transform = dataset.transform

#     # Get the raster's shape
#     height, width = dataset.shape

#     # Get the corner coordinates
#     ul_x, ul_y = transform * (0, 0)             # Upper Left
#     ur_x, ur_y = transform * (width, 0)         # Upper Right
#     lr_x, lr_y = transform * (width, height)    # Lower Right
#     ll_x, ll_y = transform * (0, height)        # Lower Left
#     d = "-".join(tif_path[-11:-4].split("."))
    # crs = dataset.crs
    # print(crs)
# Generate the output in the specified format
    # '$schema': 'https://schemas.opendatacube.org/datasetb',
# output = {
    # 'id': str(uuid.uuid4()),
    # 'crs': 'epsg:4326',
    # 'product': {
    #     # CHanged from gmw to GMW and remove crs from here
    #     'name': 'rainfall_chirps_monthly'
    # },
    # 'geometry': {
    #     'type': 'Polygon',
    #     'coordinates': [[
    #         [ll_x, ll_y],
    #         [ul_x, ul_y],
    #         [ur_x, ur_y],
    #         [lr_x, lr_y],
    #         [ll_x, ll_y]
    #     ]]
    # },
    # 'grid_spatial': {
    #     'projection': {
    #         'spatial_reference': spatial_ref.ExportToWkt()
    #     }
    # },
    # 'grids': {
    #     'default': {
    #         'shape': [width, height],
    #         'transform': list(transform)
    #     }
    # },
    # 'properties': {
    #     'datetime': f'{d}-15T00:00:00Z',
    #     'dtr:end_datetime': f'{d}-31T23:59:59Z',
    #     'dtr:start_datetime': f'{d}-01T00:00:00Z',
    #     'odc:file_format': 'GeoTIFF',
    #     'odc:processing_datetime': formatted_dt,
    #     'odc:product': 'rainfall_chirps_monthly',
    #     'proj:bbox': [ll_x, ll_y, ur_x, ur_y],
    #     'proj:epsg': 4326,
    #     'proj:geometry': {
    #         'type': 'Polygon',
    #         'coordinates': [[
    #             [ll_x, ll_y],
    #             [ul_x, ul_y],
    #             [ur_x, ur_y],
    #             [lr_x, lr_y],
    #             [ll_x, ll_y]
    #         ]]
    #     },
    #     'proj:shape': [width, height],
    #     'proj:transform': list(transform)
    # },
    # 'measurements': {
    #     'rainfall': {
    #         'path': os.path.abspath(tif_path)
    #     }
    # },
    # 'lineage': {'source_datasets': {}}
#     'id': str(uuid.uuid4()),
#     'creation_dt': formatted_dt,
#     'crs': 'EPSG:4326',
#     'extent': {
#         'from_dt': formatted_dt,
#         'to_dt': formatted_dt,
#         'center_dt': formatted_dt,
#         'coord': "",
#     },
#     'product': {'name': 'rainfall_chirps_monthly'},
#     'grid_spatial': {
#         'projection': {
#             'spatial_reference': spatial_ref.ExportToWkt(),
#         }
#     },
#     'measurements': {
        
#     },
#     'properties': {
#         'datetime': formatted_dt
#     },
#     'lineage': {'source_datasets': {}}
# }


# # Save the output as a YAML file
# yaml_path = os.path.join(tif_dir, f'{tif_filename}.yaml')
# with open(yaml_path, 'w') as yaml_file:
#     yaml.dump(output, yaml_file, default_flow_style=False)

# print(f"Output saved as '{yaml_path}'.")
