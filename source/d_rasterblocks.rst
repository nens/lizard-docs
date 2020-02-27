.. _RasterBlocksAnchor:

============
RasterBlocks
============

RasterBlocks are the GeoBlocks that work with rasterdata. RasterBlocks operate on `Lizard Rasterdata <https://docs.lizard.net/c_datatypes.html#rasters>`_.

Creating a new RasterBlock
==========================

The first step of creating a new raster GeoBlock is making a new Lizard raster instance which will contain your graph.
This can be done on the `Lizard management page <https://demo.lizard.net/management/#/>`_ or by performing a POST on the API endpoint https://demo.lizard.net/api/v4/rasters/ 

The second step is PATCHing the ``source`` element of your new raster. This element will contain the graph of your GeoBlock.
To PATCH your raster provide a valid JSON object for its source element, and perform a patch on https://demo.lizard.net/api/v4/rasters/{uuid of the new raster}/

An example of a valid PATCH object is provided below. 

.. code-block:: json

    {
      "source": {
        "name": "difference",
        "graph": {
            "AHN3": [
              "lizard_nxt.blocks.LizardRasterSource",
              "a60ad336-c95b-4fb6-b852-96fc352ee808"
            ],
            "AHN2": [
              "lizard_nxt.blocks.LizardRasterSource",
              "65912f43-0b70-425a-b471-1883378578eb"
            ],
            "difference": [
              "geoblocks.raster.elemwise.Subtract",
              "AHN3",
              "AHN2"
            ]
        }
      }
    }

PATCHing a raster can be done multiple times, until you are happy with the final output. 

Raster output
-------------

After you PATCH your raster, the changes immediately take effect. 
To view your GeoBlocks results you can access the raster via the `Catalogue <https://demo.lizard.net/catalogue>`_, `Raster API endpoint <https://demo.lizard.net/api/v4/rasters/>`_ or the Lizard WMS service.

If you want to find the visualisation of your graph in the Lizard API it's easiest to use the Catalogue.

- Search for your raster in the catalogue.
- Open the raster in the API using the Open in API button. 
- Follow the link mentioned in the source_url attribute. 

.. image:: /images/d_geoblocks_01.png

Operations
==========

Wolf, work your magic

