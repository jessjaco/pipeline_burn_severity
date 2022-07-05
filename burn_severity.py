import geopandas as gpd
import numpy as np
from pystac import Item
from planetary_computer import sign
from rioxarray import open_rasterio
from xarray import DataArray


def nbr(nir: DataArray, swir: DataArray) -> DataArray:
    numerator = np.subtract(nir, swir, dtype="int32")
    denominator = np.add(nir, swir, dtype="int32")
    return np.divide(numerator, denominator)


def load_data(url):
    data = {
        key: open_rasterio(sign(asset.href))
        for key, asset in Item.from_file(url).assets.items()
        if key in ["nir08", "swir22"]
    }
    return data["nir08"], data["swir22"]


before_url = "https://planetarycomputer.microsoft.com/api/stac/v1/collections/landsat-c2-l2/items/LC09_L2SP_037035_20220603_02_T1"
before_nir, before_swir = load_data(before_url)
before_nbr = nbr(before_nir, before_swir)

after_url = "https://planetarycomputer.microsoft.com/api/stac/v1/collections/landsat-c2-l2/items/LC09_L2SP_037035_20220619_02_T1"
after_nir, after_swir = load_data(after_url)
after_nbr = nbr(after_nir, after_swir)

dnbr = before_nbr - after_nbr

fires = gpd.read_file("WFIGS_-_2022_Wildland_Fire_Perimeters_to_Date.zip")
our_fires = fires[fires.poly_Incid.isin(["Pipeline"])].to_crs(26912)
dnbr.rio.clip(our_fires.geometry).rio.to_raster("dnbr_pipeline.tif")
