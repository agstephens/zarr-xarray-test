import xarray as xr



def main():

    zarr = './directory.zarr'
   
    print('reload into Xarray...')
    ds = xr.open_zarr(zarr)

    ch = ds.tasmax.chunks
    print(f'Chunks: {ch}')
    print(f'Chunk count (tasmax): {len(ch[0]) * len(ch[1]) * len(ch[2])}')
    print(ds.tasmax)

    return ds


if __name__ == '__main__':

    main()

