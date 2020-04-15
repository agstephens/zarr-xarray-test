import shutil
import os

import xarray as xr
import numpy as np
import pandas as pd


def count_items(dr):
    fc = 0
    dc = 0

    for _, drs, files in os.walk(dr):
        fc += len(files)
        dc += len(drs)

    print(f'Counted: {fc} files and {dc} directories')
 

def main():

    zarr = './directory.zarr'
   
    for scale_factor in range(1, 11, 5):

        print()
        if os.path.isdir(zarr):
            shutil.rmtree(zarr)

        nx = ny = 100 * scale_factor
        nt = 2
        npoints = nx * ny * nt * 2

        ds1 = xr.Dataset({'tasmax': (('lon', 'lat', 'time'), np.random.rand(nx, ny, nt))},
                 coords={'lon': range(nx),
                         'lat': range(ny),
                         'time': pd.date_range('2001-01-01', periods=nt)})

        ds1.to_zarr(zarr)
        ds2 = xr.Dataset({'tasmax': (('lon', 'lat', 'time'), np.random.rand(nx, ny, nt))},
                 coords={'lon': range(nx),
                         'lat': range(ny),
                         'time': pd.date_range('2001-01-03', periods=nt)})
        ds2.to_zarr(zarr, append_dim='time')

        print(f'For point count: {npoints}')
        count_items(zarr)


        print('reload into Xarray...')
        ds = xr.open_zarr(zarr)

        ch = ds.tasmax.chunks
        print(f'Chunks: {ch}')
        print(f'Chunk count (tasmax): {len(ch[0]) * len(ch[1]) * len(ch[2])}')

    return ds


if __name__ == '__main__':

    main()

