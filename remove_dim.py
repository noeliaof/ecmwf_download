import xarray as xr

i_file= '/storage/workspaces/giub_hydro/hydro/data/ERA5/mslp/Daily_era5_MSL_EU_hour_fixc_2021.nc'
o_file= '/storage/workspaces/giub_hydro/hydro/data/ERA5/mslp/Daily_era5_MSL_EU_hour_fixc_2021.copy.nc'
ERA5 = xr.open_mfdataset(i_file,combine='by_coords')
ERA5_combine =ERA5.sel(expver=1).combine_first(ERA5.sel(expver=5))
ERA5_combine.load()
ERA5_combine.to_netcdf(o_file)
