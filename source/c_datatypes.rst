=======
Rasters
=======

Introduction
============

Rasters are data that represent continuous information across an area. Examples include digital elevation models, flood depths, radar precipitation measurements, satellite imagery and land cover classifications. Rasters are stored in a rasterstore. 

.. _why_rasterstores:

Why Rasterstores
================

The rasterstore is a library designed for quick data retrieval. Rasters provide a simple structure for data analyis.

Main functionalities:

* Retrieve values for a specific location or area
* Analyse data for a particular period or moment in time
* Map visualization in the lizard portal
* Exporting to a geotiff file
* Connecting with external applications via WMS
* Base block for on-the-fly map calculations and conversions
* API interactions: list, create, (partial) update, retrieve and delete

Raster data
===========

A rasters is a grid of cells organized into rows and columns. Each cell contains a value that represents real-world phenomena, such as water depth. The values can be continuous (e.g. 28.5 degrees) or integer numbers. Integer numbers can represent classes (e.g. 1: Water, 2: Land).

Rasterstore data can be static or temporal. Examples of static data are a digital elevation model and a land cover map. Temporal rasterstores consist of multiple timesteps. The data can be stored in time using an origin (e.g. 2019-01-01) and an interval (e.g. every day). Examples are weather predictions and timeseries of 3Di model results.

Raster metadata
===============

Characteristics of rasters are stored in the attributes of a rasterstore. The attributes are used to indicate the function, purpose and meaning of data. The main attributes are listed below.

* Organisation
* Name
* Description
* Aggregation type
* Observation type
* Colormap
* Supplier name
* Supplier code
* Temporal behaviour

Raster management
=================

The data management interface for rasters can be used to upload, edit or remove rasters.
 

.. image:: /images/c_datatypes_01.jpg

The Data Management interface is available at: “{your_organisation}.lizard.net/management/”.

.. note::
	This functionality is available only to users with an admin, manager or supplier role.

After this screen, please click on ‘Data Management’, then ‘Rasters’ and, depending on if you want to manage a new or pre-existing raster, continue.

.. image:: /images/c_datatypes_02.jpg
.. image:: /images/c_datatypes_03.jpg
.. image:: /images/c_datatypes_04.jpg

Interested in the possibilities for your organisation? Please contact Joeri Verheijden via info@lizard.net.