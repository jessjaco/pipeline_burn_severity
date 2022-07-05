import ee

ee.Initialize()

before_image = ee.Image("LANDSAT/LC09/C02/T1_L2/LC09_037035_20220603")
before_nbr = before_image.normalizedDifference(["SR_B5", "SR_B7"])

after_image = ee.Image("LANDSAT/LC09/C02/T1_L2/LC09_037035_20220619")
after_nbr = after_image.normalizedDifference(["SR_B5", "SR_B7"])

dnbr = before_nbr.subtract(after_nbr)

task = ee.batch.Export.image.toDrive(dnbr)

task.start()
