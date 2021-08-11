=============
Rasters
=============

The data management interface for rasters can be used to upload, edit or remove rasters.

.. warning::
    This section will be updated in the coming days.

.. image:: /images/c_manage_rasters_01.png
.. image:: /images/c_manage_rasters_02.png
.. image:: /images/c_manage_rasters_03.png

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
#. Choose the preferred authorisation type (read more).
#. Give the dataset a name.
#. Describe your dataset. Make sure to name the source and describe the analysis that resulted in this dataset. Users can read this description in the Lizard Catalog.
#. Choose how your data should be aggregated. This functionality is only needed when you want to use the Region Analysis mode in Lizard Viewer or Lizard API. 
#. Choose the observation type of this dataset. 
#. Choose a preferred color map. Choose “Rescalable” if you want to be able to rescale the color map in Lizard Viewer.
#. Fill in the supplier name. We use your username by default.
#. You can fill in a supplier code for your own administration.
#. If you’re supplying a temporal dataset. Choose “Raster Series”. Next, fill in the interval of the dataset. 
#. Click submit. You have now created the Raster Store. You’re all set up to  supply your geotiff’s using the upload button. 

.. image:: /images/c_datatypes_01.png

The Data Management interface is available at: “{your_organisation}.lizard.net/management/”.

.. note::
	This functionality is available only to users with an admin, manager or supplier role.

After this screen, please click on ‘Data Management’, then ‘Rasters’ and, depending on if you want to manage a new or pre-existing raster, continue.

.. image:: /images/c_datatypes_02.jpg
.. image:: /images/c_datatypes_03.jpg
.. image:: /images/c_datatypes_04.jpg

Interested in the possibilities for your organisation? Please contact Joeri Verheijden via info@lizard.net.

.. _vector_data_types:

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