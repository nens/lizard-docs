=========
Catalogue
=========

General
========

The Lizard Catalogue offers insight in the data that are available for your organisation.

You can reach the Catalogue via the following url:
https://demo.lizard.net/catalogue/ or {yourorganisation}.lizard.net/catalogue/

.. image:: /images/e_catalog_00.png

For now, the Catalogue covers these three datatypes:  

* **Raster**  Raster layers in Lizard (not included are rasters from 3Di scenarios) 
* **WMS layer**  Wms layers in Lizard
* **Time series**  Time series and monitoring networks

There is an extensive search option to make the data easily accesible.
Every data layer will show available metadata.
From the Catalogue you have the option of opening the data layers via the API or via the Lizard Viewer.

Filter
--------

On the left side of the Catalogue app you can find several ways of filtering the data layers you have access to.
There are three different ways to filter, Organisation, Layer Collection or Observation type.
Per filter there is a list of all possible options.

.. image:: /images/e_catalog_03.png

You can also use the search bar per filter to directly enter what you want to filter on.

.. image:: /images/e_catalog_04.png

Export, Basket and login
-------------------------

In the top right you see the following buttons:

.. image:: /images/e_catalog_07.png

**Export**
Available and running exports will appear here

**Basket**
Using the Basket makes it easy to make different combinations of data layers to show in Lizard.
To the left of the data layers are selection boxes.
Click these boxes to make a selection from one or several data layers.
After making the selection click the 'Add to basket' button in the lower right corner of the data layers overview.
At the top right corner of the Catalogue you will see that the Basket button now shows the number of selected data layers.
Opening the basket gives an overview of all selected layers, and a button to 'Open all data in Lizard'.
This will open a new window for Lizard, with all the selected data layers opened.

**Login**
If you are logged in, you will have access to data that is common, or private and shared with your organisation.
Also, you have to be logged in to be able to export.

Rasters
=========

When you open the Catalogue and choose 'Raster' in the top left, you will see an overview of all the layers you have access to.
It will show a list of 10 items, with the option to click through to other pages.
At the top of the screen there is a search bar.
Using search terms that are in the Name or the Description of the data layer you can more easily find specific data layers that you might be interested in.

The following information is visible in this overview.

* **Type** The type of data. A normal raster, or a temporal raster.
* **Name** Name of the data layer.
* **Organisation** To which organisation the data layer belongs.
* **Description** A short description of the data contained within the data layer.
* **Latest update** When the data layer was last updated.
* **Access modifier** Divided into Public, Common and Private.

.. note::
    Information about the different access modifiers can be found under `organisation modifiers <d_authentication_user_management.html#Organisations>`_.
	
.. note::
    Not included are rasters from 3Di scenarios

Details
--------

Once you have selected a data layer, you will find detailed information about the layer in the panel on the right.
Here it will show a map of the area and a visualisation of the data.
Below the map there is a table with detailed meta information about the data layer.
If you want to visualise the layer in your Viewer or if you want to use it for data science purposes you can either choose to open it in the Viewer or the API. 

.. image:: /images/e_catalog_05.png

Lizard WMS Service for rasters
--------------------------------

When you filtered on “Layer Collection” a Lizard WMS GetCapabilities link appears in the list of meta data of the raster.
You can use this link to visualise the raster in external applications such as QGIS or ESRI applications.

For more infomation, please consult the WMS Services.

Exporting
----------

Select the raster you would like to export.
Click on the Export button in the action menu. 

.. image:: /images/e_catalog_06a.png

The Export Selection window will pop up. 
Follow the steps: 
- Choose a preferred projection of the output GeoTIFF.
- Choose the pixel size (resolution) of the output GeoTIFF.
- Choose a preferred tile size. 

You can export 3 tiles at a time. 
Click on Download selected cells.
A task will be started in the background.
Once your GeoTIFF's are ready you will receive a notification in the Export dropdown menu in the green bar.

.. image:: /images/e_catalog_06b.png


WMS layers
=============

When you open the Catalogue and choose 'WMS layer'  in the top left, you will see an overview of all the wms layers you have access to.
It will show a list of 10 items, with the option to click through to other pages.
At the top of the screen there is a search bar.
Using search terms that are in the Name or the Description of the data layer you can more easily find specific data layers that you might be interested in.

The following information is visible in this overview.


* **Name** Name of the wms layer.
* **Organisation** To which organisation the data layer belongs.
* **Description** A short description of the data contained within the data layer.
* **Access modifier** Divided into Public, Common and Private.

.. note::
    Information about the different access modifiers can be found under `organisation modifiers <d_authentication_user_management.html#Organisations>`_.

Details
--------

Once you have selected a wms layer, you will find detailed information about the layer in the panel on the right.
Here it will show a map of the area and a visualisation of the data.
Below the map there is a table with detailed meta information about the data layer.
If you want to use the layer in your Viewer or if you want to use it for data science purposes you can either choose to open it in the Viewer or the API. 

.. image:: /images/e_catalog_08.png

Action menu
------------

.. image:: /images/e_catalog_09.png

You can download the wms directly, open it in the Viewer or in the API or analyse the wms layer in another application linking to Lizard. 
You can use this link to visualise the raster in external applications such as QGIS or ESRI applications.

For more infomation, please consult the `WMS Services <b_management.html#WMS Services>`_.

Time series and monitoring networks
====================================

When you open the Catalogue and choose 'Time series' in the top left, you will see an overview of all the layers you have access to.
It will show a list of 10 items, with the option to click through to other pages.
At the top of the screen there is a search bar.
Using search terms that are in the Name or the Description of the data layer you can more easily find specific data layers that you might be interested in.

The following information is visible in this overview.

* **Monitoring network** Name of the data layer.
* **Organisation** To which organisation the data layer belongs.
* **Access modifier** Divided into Public, Common and Private.

.. note::
    Information about the different access modifiers can be found under `organisation modifiers <d_authentication_user_management.html#Organisations>`_.
	
In monitoring networks, you can group timeseries. This can be done for example by grouping them by observation type or by source.
	
.. note::
    New monitoring networks can be added via https://demo.lizard.net/api/v4/monitoringnetworks/ or {yourorganisation}.lizard.net/api/v4/monitoringnetworks/ or with the help of a consultant. In the near future, time series can be managed via the management screens. 

Details
--------

Once you have selected a monitoring network, you will find detailed information about the dataset in the panel on the right.
Here it will show a map of the area and a visualisation of the data.
Below the map there is a table with detailed meta information about the data layer.

.. image:: /images/e_catalog_10.png

Action menu
------------

In the action menu, you can export the timeries you are interested in or open it in the Viewer or in the API.
You can filter on the observation type, which time series have data in a certain period and/or on location. 

First choose "Select time series". 

.. image:: /images/e_catalog_11.png

Below you see a screenshot of all locations with time series for monitoring network KNMI weerstations without filtering.

.. image:: /images/e_catalog_12.png

Below you see a screenshot of all locations with time series with observation type 'windsnelheid' and that have data between 14 and 16 March 2021.
Then location Bilt is manually selected (by clicking on a dot or use the search bar) and ready to export or view in the API or in the Viewer. 

.. image:: /images/e_catalog_13.png

Scenarios
==============

When you open the Catalogue and choose 'Scenario' in the top left, you will see an overview of all the scenarios you have access to.
It will show a list of 10 items, with the option to click through to other pages.
At the top of the screen there is a search bar.
Using search terms that are in the Name or the Description of the data layer you can more easily find specific data layers that you might be interested in.

.. image:: /images/e_catalog_14.png



The following information is visible in this overview.

* **Name** Name of the data layer.
* **Model name** Name of the model the scenario is based on. 
* **Organisation** To which organisation the data layer belongs.
* **Last update** When the data layer was last updated.
* **Access modifier** Divided into Public, Common and Private.

.. note::
    Information about the different access modifiers can be found under `organisation modifiers <d_authentication_user_management.html#Organisations>`_.
	

Details
--------

Once you have selected a data layer, you will find detailed information about the layer in the panel on the right.

.. image:: /images/e_catalog_15.png


Action menu
------------

In the action menu, you can open the scenario in the Viewer or in the API.

Results
------------

In the results menu, you can download the results. 

.. image:: /images/e_catalog_16.png