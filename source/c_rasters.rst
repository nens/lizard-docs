=============
Rasters
=============

The data management interface for rasters can be used to upload, edit or remove rasters.
Raster Sources are the data containers, Raster Layers are the configuration of how the data is visualised.

.. image:: /images/c_manage_rasters_01.png
.. image:: /images/c_manage_rasters_02.png
.. image:: /images/c_manage_rasters_03.png

Creating and editing Raster Sources and Layers
----------------------------------------------

The first step in uploading your raster datasets is to create a Raster Source.

The Data Management interface is available at: “www.{your_organisation}.lizard.net/management/”.

After landing on this page, click on ‘Data’ -> ‘Rasters’ -> 'Raster Sources'.
Click on “New Item” |NewItem| to open the form or choose an existing raster to edit.  

.. |NewItem| image:: /images/c_dataexchange_02.png

After filling in the form you can choose to directly upload your data by selecting your GeoTIFF's in the 'DATA' section.
In case of a temporal raster source you need to specify which file belongs to which timestep.
This is recognised automatically if the filename is composed according to the specified format.
When you save a new Source you will have the option to go straight to the Raster Layer form to publish your data.

.. image:: /images/c_datatypes_01.png

Interested in the possibilities for your organisation? Please contact us via info@lizard.net.

.. _vector_data_types:

GeoBlocks management
--------------------

The GeoBlocks management page provides you a powerful tool to build your GeoBlocks Rasters.
It helps you configure complex GeoBlocks models and enables you to validate your work along the way.

The Visual editor shows your model as a flow diagram, consisting of block objects representing the input Raster Sources and GeoBlocks operations.
The right sidebar shows the available blocks. Click on the blocks for a description and the expected inputs. Drag a block into the canvas to include it in your model.
Connect blocks to use one as input for the other.

When the model is valid it can also be shown in the Text editor. This shows the JSON graph as it would be sent to the API when you save the item.
Here you can also make edits and validate the result.

Example 1 shows a simple model which subtracts one Raster Source from another (difference in surface elevation between two versions of a dataset).

.. image:: /images/c_manage_geoblocks_01.png

Example 2 shows a more complex model with multiple Raster Sources and a series of operations.

.. image:: /images/c_manage_geoblocks_02.png

For more information about the possibilities of GeoBlocks see: :ref:`GeoBlocksAnchor`
