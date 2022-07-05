## Pipeline Fire Burn Severity Map

This repository includes code to create a soil burn severity map for the
Pipeline Fire which took place near Flagstaff, AZ, USA in June, 2022. This is
just an exploratory project by me and is _not_ an official US Forest Service (or any other agency's) map. Nevertheless, the results are visually equivalent to the maps produced by the USFS BAER team in June, 2022.

![Map of burn severity](severity_map.png?raw=true "Burn Severity Map")

### The Process

The map was created by using the difference in normalized burn ratio between
pre-and post-file satellite images taken by the Landsat 9 satellite. The
"before" image was taken June 3, 2022, and the after image was taken June 19,
2022.

For more information on the science behind the calculation, see [this](https://un-spider.org/advisory-support/recommended-practices/recommended-practice-burn-severity/in-detail/normalized-burn-ratio).

To create the pdf map, I manually determined the color ramp using the USFS
product (which may be using a standard ramp, it was not
specified). However, a different ramp, such as this one recommended
by the USGS at the above link could also be used. I'll also note that the
official map was ground verified (at least the Coconino NF posted pictures of
personnel on the ground taking soil burn severity readings), so it's possible
the cutoffs were determined empirically based on these readings.

### What's here:
- _burn_severity.pdf_ - A pdf verson of the map
- _dnbr_pipeline.tif_ - A GIS-ready TIFF file with the map data
- _burn_severity.py_ - Code to reproduce the data using the Microsoft Planetary Computer
- _burn_severity_gee.py_ - Code to reproduce the data using Google Earth Engine
