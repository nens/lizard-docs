=========
Catalogue
=========

.. warning::
    This section will be extended in the coming days.

The Lizard Catalogue offers insight in the data layers that are available for your organisation.
There is an extensive search option to make the layers easily accesible.
Every data layer will show available metadata.
From the Catalogue you have the option of opening the data layers via the API or via the Lizard portal.

The Catalogue can be reached via the following url.

https://demo.lizard.net/catalogue/

Data Layers
===========

When you open the Catalogue you will see an overview of all the layers you have access to.
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
    Information about the different Access modifiers can be found under :ref:`OrganisationsAnchor`.

Filters
=======

On the left side of the Catalogue app you can find several ways of filtering the data layers you have access to.
There are three different ways to filter, Organisation, Dataset or Observation type.
Per filter there is a list of all possible options.

.. image:: /images/e_catalog_03.png

You can also use the search bar per filter to directly enter what you want to filter on.

.. image:: /images/e_catalog_04.png

Details
=======

Once you have selected a data layer, you will find detailed information about the dataset in the panel on the right.
Here it will show a map of the area and a visualisation of the data.
Below the map there is a table with detailed meta information about the data layer.
If you want to use the dataset in your Portal or if you want to use it for data science purposes you can either choose to open it in the Portal or the API. 

.. image:: /images/e_catalog_05.png

Exporting
=========

Select the raster you would like to export.
Click on the Export button in the panel on the right. 

.. image:: /images/e_catalog_02.png

The Export Selection window will pop up. 
Follow the steps: 
- Choose a preferred projection of the output GeoTIFF.
- Choose the pixel size (resolution) of the output GeoTIFF.
- Choose a preferred tile size. 

You can export 3 tiles at a time. 
Click on Download selected cells.
A task will be started in the background.
Once your GeoTIFF's are ready you will receive a notification in the Export dropdown menu in the green bar.

.. image:: /images/e_catalog_06.png

Lizard WMS Service for rasters
==============================
When you filtered on "Dataset" a Lizard WMS GetCapabilities link appears in the list of meta data of the raster.
You can use this link to visualize the raster in external applications such as QGIS or ESRI applications.

.. image:: /images/e_catalog_01.png

For more infomation, please consult the :doc:`WMS Services<e_lizardwms>`.


Basket
======

Using the Basket it is easy to make different combinations of data layers to show in Lizard.
To the left of the data layers are selection boxes.
Click these boxes to make a selection from one or several data layers.
After making the selection click the 'Add to basket' button in the lower right corner of the data layers overview.
At the top right corner of the Catalogue you will see that the Basket button now shows the number of selected data layers.
Opening the basket gives an overview of all selected layers, and a button to 'Open all data in Lizard'.
This will open a new window for Lizard, with all the selected data layers opened.

.. image:: /images/e_catalog_07.png
