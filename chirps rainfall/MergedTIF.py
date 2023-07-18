import rasterio
from rasterio.merge import merge
from rasterio.enums import Resampling
import numpy as np

# List the paths of the GeoTIFF files to be merged
file_paths = ["./Avanigadda.tif", "./Atmakur.tif", "./Kavali.tif", "./Gujarat/Khambhaliya.tif"]

#  Read the GeoTIFF files
datasets = []
for file_path in file_paths:
    dataset = rasterio.open(file_path)
    datasets.append(dataset)

# Resample and align the datasets to a common grid
resampled, resampled_transform = merge(datasets, method='first', resampling=Resampling.average)

# Remove the extra dimension from the merged data
resampled = np.squeeze(resampled)

# Update the metadata for the output merged file
meta = datasets[0].meta
meta.update(count=1, transform=resampled_transform)

# Save the merged file
output_file = "./merged_file.tif"
with rasterio.open(output_file, 'w', **meta) as dst:
    dst.write(resampled, 1)

# Close the datasets
for dataset in datasets:
    dataset.close()