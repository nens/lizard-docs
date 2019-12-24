==========================
Data Management & Exchange
==========================

We support multiple types of data uploads.
Data can be uploaded manually, via the data management interface, or you can set up real-time data connections using the API.
We can also provide support on either manual or automatic data uploads. 

.. note::
    Please note that Lizard assumes the data to be in UTC

Rasters
=======

Requirements 
--------------

Your raster data has to be in the format of a single band, georeferenced TIFF (geotiff), with the following requirements: 

* **Geotiff should have valid projection** including transformation (EPSG code). All projections supported by proj4 are supported.
* **Geotiff should have a NODATA value**.
* **Geotiff should be single band**. RGB or multi-band is not supported. 
* **Temporal raster datasets** with multiple timesteps **should be supplied with a single geotiff per timestamp**

Creating and editing a Raster Store
-------------------------------------

The first step in uploading your raster datasets is to create a Raster Store.
This can easily be done using our Data Management app.
Following this step-by-step tutorial to upload a raster dataset:

.. image:: /images/c_dataexchange_01.jpg

The Data Management interface is available at: “www.{your_organisation}.lizard.net/management/”.

After landing on this page, please click on ‘Data Management’, then ‘Rasters’.
Click on “New Raster” |NewRaster| to open the form for new Rasters.
Or choose an existing raster to edit.  

.. |NewRaster| image:: /images/c_dataexchange_02.png

#. Choose the organisation you’re supplying data for. 
#. Choose the organisations you want to share this dataset with. 
#. Choose the preferred authorization type (read more).
#. Give the dataset a name.
#. Describe your dataset. Make sure to name the source and describe the analysis that resulted in this dataset. Users can read this description in the Lizard Catalog.
#. Choose how your data should be aggregated. This functionality is only needed when you want to use the Region Analysis mode in Lizard Portal or Lizard API. 
#. Choose the observation type of this dataset. 
#. Choose a preferred color map. Choose “Rescalable” if you want to be able to rescale the color map in Lizard Portal.
#. Fill in the supplier name. We use your username by default.
#. You can fill in a supplier code for your own administration.
#. If you’re supplying a temporal dataset. Choose “Raster Series”. Next, fill in the interval of the dataset. 
#. Click submit. You have now created the Raster Store. You’re all set up to  supply your geotiff’s using the upload button. 

Upload 
------

You can supply your GeoTIFF’s in multiple ways: 

* Use the Data Management App 
* Use the Lizard API 
* Use the Lizard FTP

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

.. warning::
   Text required!

Using the Lizard FTP
++++++++++++++++++++ 

.. warning::
   Text required!

Time Series
===========

Requirements
------------

Time series should always be linked to one of the vector data models listed :ref:`here <vector_data_types>`.

Time series can be imported manually, by uploading a csv file to https://demo.lizard.net/import/.

Time series can be uploaded through a 4 column csv.
Select both the organisation you want to upload and the asset type the time series belongs to (e.g. groundwater station).
The csv should not contain a header.

.. csv-table:: Example with headers
    :header: timestamp, unit id / name, value, asset id
    
    2015-01-01T00:00:00Z, GWmMSL, 248.0, your_own_code_1
    2015-01-01T01:00:00Z, GWmBGS, 248.0, your_own_code_1
    2015-01-01T00:00:00Z, GWmMSL, 252.3, your_own_code_2
    2015-01-02T05:00:00Z, GWmMSL, 234.2, your_own_code_3

The columns should contain:

* **timestamp:** a timestamp in iso8601 format.
* **unit id / name:** This is both the name of the observation type name and this will become the timeseries name.
* **value:** value as either a float or integer number.
* **asset id:** either an asset uuid or an organisation-code (an identifier for an asset, unique for your organisation). In case the assets have been added with a code under category [columns].

Since a csv should not contain a header, your csv should look like this:

.. csv-table:: Example without headers

    2015-01-01T00:00:00Z, GWmMSL, 248.0, your_own_code_1
    2015-01-01T01:00:00Z, GWmBGS, 248.0, your_own_code_1
    2015-01-01T00:00:00Z, GWmMSL, 252.3, your_own_code_2
    2015-01-02T05:00:00Z, GWmMSL, 234.2, your_own_code_3

Authentication
--------------

SFTP users are authenticated with a username / password.

Supported data formats
----------------------

Via SFTP the following formats are supported:

    * CSV
    * PiXML

Every supplier has its own directory on the SFTP.
It can be accessed by logging in with the Lizard credentials.

As soon as a new file is uploaded to the SFTP server, it will be automatically recognised and processed by Lizard.
After processing the file is moved to a backup for a limited period of time.

When a file is rejected, the supplied file is moved to the directory ‘rejected’ and a message is sent to the suppliers Inbox.
In the Inbox a supplier can see the status of his supplied files.

CSV
+++++

Use CSV for supplying timeseries data with numerical or textual values according to the following format:

.. code-block:: none

    <timestamp>,<timeseries_supplier_code or uuid>,<value>[\n]
    <timestamp>,<timeseries_supplier_code or uuid>,<value>[\n]
    <timestamp>,<timeseries_supplier_code or uuid>,<value>[\n]      
    …

Where:

    * **timestamp:** time in UTC in ISO 8601 format. For example 2012-10-26T09:22:35Z. Supplying timestamps in different timezone is only allowed when the UTC offset is added to the timestamp according to ISO 8601. For example: 2012-10-26T07:22:35+02.
    * **timeseries_supplier_code or UUID:** supplier_code attribute of timeseries as registered by administrator/supplier or the UUID of the timeseries object.
    * **value:** numerical or textual value.
    * **[\\n]:** newline character.

CSV requirements:

    * CSV file size may not exceed 100 MB. For one timeseries with a measuring frequency of 1 second that would be around 1 month of data.
    * Every supplied file should contain new measurements. It is not allowed to add measurements to a previously supplied file.
    * Use the empirical CSV format where the field separator is a comma (,) and the decimal separator a period (.).

PiXML
+++++++++

Pi-XML is a file exchange format used by Delft-FEWS. A description can be found `here <https://publicwiki.deltares.nl/display/FEWSDOC/Delft-Fews+Published+Interface+timeseries+Format+%28PI%29+Import>`_.

Images
++++++++++++

The following formats are supported for image timeseries:

    * PNG
    * JPEG

Image filenames should have the following format:

.. code-block:: none

    <timeseries_supplier_code>_<timestamp>.png
    <timeseries_supplier_code>_<timestamp>.jpg

Where:

    * **timestamp:** time in UTC in ISO 8601 format. Colons (:) should be excluded as they are not allowed in filenames. An example timestamp is: 2012-10-26T092235Z. Supplying timestamps in different timezone is only allowed when the UTC offset is added to the timestamp according to ISO 8601. For example: 2012-10-26T072235+02.
    * **timeseries_supplier_code:** supplier_code attribute of timeseries as registered by administrator/supplier.

Video and multimedia
++++++++++++++++++++++

The following multimedia file extensions are supported for multimedia timeseries:

    * PDF
    * AVI
    * WMV

Multimedia filenames should have the following format:

.. code-block:: none

    <timeseries_supplier_code>_<timestamp>.pdf
    <timeseries_supplier_code>_<timestamp>.avi
    <timeseries_supplier_code>_<timestamp>.wmv

Where:

* **timestamp:** time in UTC in ISO 8601 format or as a unix timestamp in ms since epoch. Colons (:) should be excluded as they are not allowed in filenames. An example timestamp is: 2012-10-26T092235Z. Supplying timestamps in different timezone is only allowed when the UTC offset is added to the timestamp according to ISO 8601. For example: 2012-10-26T072235+02.
* **timeseries_supplier_code:** supplier_code attribute of timeseries as registered by administrator/supplier.

LMW data
+++++++++++

Every 10 minutes a file is downloaded from LMW.

Error handling
++++++++++++++++++

When a file is in the **wrong format**, **authorisation fails** and / or **value type is not valid**:

    * File is moved to ‘rejected’ directory of supplier
    * An error is logged
    * A message is sent to the Inbox of the supplier

SUF-HYD
+++++++++

SUF-HYD files can be imported manually, by uploading a file to https://demo.lizard.net/import/

We currently do not support GWSW-Hyd yet.

The description of SUF-HYD files can be found here: https://www.riool.net/documents/20182/557556/suf-hyd-gegevens%20stelsel-1996-2003.pdf/512c2708-0594-4227-998e-f9c51bec6a50 

API
------------

Timeseries data can be supplied with a POST request to the timeseries data endpoint in the API (`<baseurl>`/api/v3/timeseries/{uuid}/data/).
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

Vectors
=======

We support vector synchronisation.
This type of data feed has to be configured per customer.
Changes in location names, coördinates and new locations can be seen in Lizard as soon as the following day. 

Upload vectors as a shapefile
-----------------------------

Assets can be uploaded to Lizard with shapefiles via the import form at <base-url>/import.
These shapefiles contain information about assets or assets together with their nested assets (e.g. GroundwaterStations and their Filters).

A shapefile can be uploaded as a zipped archive.
The zipfile should contain at least a .dbf, .shp, .sh xand .ini file.
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

Data downloads
==============

.. warning::
   Text required!

Rasters
-------

.. warning::
   Text required!

Timeseries
-----------

.. warning::
   Text required!