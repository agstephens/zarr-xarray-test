import xarray as xr
import zarr

from fsspec.implementations.http import HTTPFileSystem
fs = HTTPFileSystem()

http_map = fs.get_mapper('http://0.0.0.0:9000')

# s a zarr group
zg = zarr.open_consolidated(http_map, mode='r')

# as another xarray dataset
ds = xr.open_zarr(http_map, consolidated=True)

print(ds)
