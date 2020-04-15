import xarray as xr
import xpublish

#ds = xr.tutorial.open_dataset("air_temperature", chunks=dict(lat=5, lon=5))

ds = xr.open_zarr('./directory.zarr', chunks=dict(time=4, lat=600, lon=150))

# customization of the underlying FastAPI application or the server-side cache is possible when the accessor is initialized:

ds.rest.init_app(
    app_kws=dict(
        title="My Dataset",
        description="Dataset Description",
        openapi_url="/dataset.JSON",
    ),
    cache_kws=dict(available_bytes=1e9)
)


# a dataset simply requires calling the serve method on the rest accessor:

print('Browse at: http://192.168.50.70:9000/')
ds.rest.serve()

