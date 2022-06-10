================
Data uploads
================

We support multiple types of data uploads.
Data can be uploaded manually, via the data management interface, or you can set up real-time data connections using the API.
We can also provide support on either manual or automatic data uploads. 

.. note::
    Please note that Lizard assumes the data to be in UTC
	
	
Rasters
===========

Requirements 
--------------

Your raster data has to be in the format of a single band, georeferenced TIFF (geotiff), with the following requirements: 

* **Geotiff should have valid projection** including transformation (EPSG code). All projections supported by proj4 are supported.
* **Geotiff should have a NODATA value**.
* **Geotiff should be single band**. RGB or multi-band is not supported. 
* **Temporal raster datasets** with multiple timesteps **should be supplied with a single geotiff per timestamp**


Upload 
------

You can supply your GeoTIFF’s in multiple ways: 

* Use the Data Management App 
* Use the Lizard API 
* Use the Lizard FTP (will become absolete) 

Use of the Data Management App is fairly straightforward and is build upon our API.
If you want to upload larger raster datasets, please make use of our API. 


Using the Data Management App
++++++++++++++++++++++++++++++

Once you have successfully created a raster store you will see the pop up below.

.. image:: /images/c_dataexchange_03.png

Choose upload data to browse your GeoTIFF’s.
When you want to add data to an existing raster store, click on the upload icon |uploadicon| in the list of existing Raster Stores. 

.. |uploadicon| image:: /images/c_dataexchange_04.png

You can supply multiple rasters, Lizard will blend them together! Click “Save all Files” to start uploading your data.
Your GeoTIFF’s will be uploaded in a task. You can follow the status of the task by clicking “show asynchronous task”.

.. image:: /images/c_dataexchange_05.png

Using the Lizard API
++++++++++++++++++++

Below you find an example of how to upload a temporal geotiff in Python:

.. code-block:: python

	import os
	import shutil
	import requests
	import json
	import time
	from datetime import datetime, timedelta

	srcdir = r""
	tgtdir = r"" #Files are transfered here after being uploaded
	base_url = 'https://demo.lizard.net/api/v4/rastersources/{}/data/' #Fill in rastersource__uuid
	api_key = '' #Fill in personal API key of supplier account

	headers= {
		"username": "__key__",
		"password": "{}".format(api_key)
		}

	file_id = 10000001 #Random counter

	for filename in os.listdir(srcdir):
		print(filename)
		f = open(os.path.join(srcdir, filename), 'rb')
		files = {'file': f}
		payload = {'file_id': file_id,
				   'timestamp': '{}'.format(
					   datetime.strptime(filename.split('.')[0],
										 '%Y%m%dT%H%MZ'
										 ).strftime('%Y-%m-%dT%H:%M:00Z')
					   )
				   }
		#The upload request could be put in a try/except like the result check, to prevent disruptions
		res = requests.post(url=base_url,
							files=files,
							data=payload,
							headers=headers
							)
		f.close()
		#Check task result to know when to upload the next
		task_url= res.json()['url']
		processed = False
		while not processed:
			time.sleep(4) #Can be adjusted based on average processing time per file
			try:
				task_res= requests.get(url=task_url,
									   headers=headers
									   )
				if task_res.json()['status'] == 'SUCCESS':
					processed = True
			except:
				print('Error occurred')
		shutil.move(os.path.join(srcdir, filename),
					os.path.join(tgtdir, filename)
					)
		file_id+= 1


Time Series
=============

Requirements
------------

Time series should always be linked to one of the vector data models listed :ref:`here <vector_data_types>`.

Time series can be imported manually, by uploading a csv file in the timeseries management screen (see https://docs.lizard.net/c_timeseries.html) or via the API. 

Upload 
------


Using the Data Management App
++++++++++++++++++++++++++++++

The first line of the file should describe the column names, for example:


.. csv-table:: Example wcsv
    :header: timestamp, value
    
	2020-03-20T01:00:00Z, 3.14
	2020-03-20T01:05:00Z, 2.72

The columns should contain:

* **timestamp:** a timestamp in iso8601 format.
* **value:** value as either a float or integer number.


.. note::
    The upload will fail if there are duplicate timestamp



Using the Lizard API
++++++++++++++++++++

Timeseries data can be supplied with a POST request to the timeseries data endpoint in the API (`<baseurl>`/api/v4/timeseries/{uuid}/data/).
Interaction with the API can be done from e.g. Postman or Python.
User credentials should be included in the header and the data in the payload of the request. 

Value based timeseries
+++++++++++++++++++++++++++

This type of timeseries consists of integers, floats, float arrays or text. The body of the request is a JSON object with timestamps and values:

.. code-block:: json 

    {
    	"data": [{
    			"datetime": "2019-07-01T01:30:00Z",
    			"value": 40.7
    		},
    		{
    			"datetime": "2019-07-01T02:00:00Z",
    			"value": 39.1
    		}
    	]
    }

File based timeseries
++++++++++++++++++++++

This type consists of images, movies or files. A single files is posted on a certain datetime, which is included in the header of the request.

An example of an upload of an image using requests in Python:

.. code-block:: none  

    import requests
    import datetime as dt

    now = dt.datetime.utcnow()
    uuid = ‘385c08c5-a0cf-4097-a98f-b6f053ef32c6’
    url = 'https://demo.lizard.net/api/v3/timeseries/{}/data/'.format(uuid)
    data = open('./x.png', 'rb').read()
    res = requests.post(url=url,
                        data=data,
                        headers={
                        'Content-Type': 'image/png',
                        'datetime': now.strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
                        'username': 'jane.doe',
                        'password': 'janespassword'
                        })

Assets
=======

We support asset synchronisation.
This type of data feed has to be configured per customer.
Changes in location names, coördinates and new locations can be seen in Lizard as soon as the following day. 

Upload vectors as a shapefile
-----------------------------

Assets can be uploaded to Lizard with shapefiles via the import form at <base-url>/import.
These shapefiles contain information about assets or assets together with their nested assets (e.g. GroundwaterStations and their Filters).

A shapefile can be uploaded as a zipped archive.
The zipfile should contain at least a .dbf, .shp, .sh and a .ini file.
In case of nested assets, these should be found in the same shapefile record (row) as their assets.
The following section provides an example of an .ini file for groundwater stations.

Assets without nested assets
++++++++++++++++++++++++++++++++++++

An .ini file is used to map shapefile attributes to Lizard database tables, organisations and attributes. An .ini file consists of three sections:

    * **[general]:** indicates asset name to upload to and optionally organisation uuid.
    * **[columns]:** maps lizard columns to shapefile columns
    * **[default]:** optionally provide default values for columns

This example .ini creates a new asset from each record of the shapefile, with:

    * A **code** taken from the ID_1 column of the shapefile;
    * A **name** taken from the NAME column of the shapefile;
    * A **surface_level** taken from the HEIGHT column of the shapefile;
    * A **frequency** that defaults to daily;
    * A **scale** that defaults to 1, which means this asset can be seen at world scale, when the asset-layer in Lizard-nxt is configured accordingly.

Assets with nested assets
++++++++++++++++++++++++++++++++++++

In case of nested assets another section should be added to the .ini file:

    * **[nested]:** maps lizard columns to shapefile columns, it is possible to add multiple nested assets for one asset.

A groundwater station with filters (its nested assets) would look like this:

.. code-block:: none

    [general]
    asset_name = GroundwaterStation
    nested_asset = Filter

    [columns]
    code = ID_1
    name = NAME
    surface_level = HEIGHT

    [defaults]
    frequency = daily
    scale = 1

    [nested]
    first = 2_code
    fields = [code, filter_bottom_level, filter_top_level, aquifer_confiment, litology]

The **[nested]** categories describe:

    * **first:** indicates the first column in the shapefile that maps lizard columns to shapefile columns. This column and all columns to its right configure nested assets. The number of these columns should be a multiple  (the number of maximum nested assets per asset) of the fields.
    * **fields:** lizard-nxt fields. Each column in the shapefile (including the ‘first’) is mapped to these fields in order, without considering the shape column names.

This example .ini creates (a) new nested asset(s) from each record of the shapefile, with:

* A **link** to an asset that conforms to the asset as described in the `Assets without nested assets`_.
* A **code** taken from the 2_code column of the shapefile. And a new nested asset with a filter_bottom_level for each 5th column from that column onwards;
* A **filter_bottom_level** taken from the column directly next to the 2_code column of the shapefile. And a new nested asset with a filter_bottom_level for each 5th column from that column onwards;
* A **filter_top_level** taken from the column 2 columns next to the 2_code column of the shapefile. And a new nested asset with a filter_top_level for each 5th column from that column onwards;
* A **aquifer_confiment** taken from the column 3 columns next to the 2_code column of the shapefile. And a new nested asset with a aquifer_confiment for each 5th column from that column onwards;
* A **litology** taken from the column 4 columns next to the 2_code column of the shapefile and each. And a new nested asset with a litology for each 5th column from that column onwards

You can copy paste this code in your own .ini file and zip it together with the shapefile.



