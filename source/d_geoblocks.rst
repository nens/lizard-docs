=========
GeoBlocks
=========

Digital geo services rely on high resolution big data coming from multiple real-time sources. 
We developed GeoBlocks to make it easier to process and analyse (real-time) that data to create a digital geo service. 

GeoBlocks is a GIS modelling toolbox that allows you to make on-the-fly analysis using raster & vector data stored in Lizard. 
Geoblocks consists of numerous classes which describe geographical operations. An individual class is called a Block and a combination of multiple Blocks is called a Graph.

There are two basetype Blocks, :ref:`RasterBlocksAnchor` and :ref:`GeometryBlocksAnchor`. 

- GeoBlocks derives information on-the-fly, creating a "view" on your data. This is also the reason why it's very efficient in data storage, as intermediate results do not have to be stored!
- All Blocks are modular and can be combined with each other to create extensive models.
- You can apply GeoBlocks on real-time data-flows that expand in space and time (e.g. remote sensing data), immediately processing data as it becomes available!
- You can combine temporal and static datasets. For example, you can combine a static land cover raster with a daily soil moisture raster.
- Unlike conventional GIS raster calculator solutions, you can combine data with different resolutions and varying spatial extent.

Open Source
===========

The computational core of GeoBlocks is published open source under the name `dask-geomodeling <https://dask-geomodeling.readthedocs.io/en/latest/index.html>`_.
Most operations are identical. Only the I/O filetype and configuration differs.
The open source library can be used to build on-the-fly models on your own PC.
Dask-geomodeling has a limitation in the complexity of the models that you can run locally.
This is determined by your memory and processor capabilities. 

If you want to scale up your model or increase complexity you can do publish your model and data to Lizard using the Lizard API.
The GeoBlocks engine uses the powerful Lizard backend allowing you to scale up your models and integrate the model in your geo services using the Lizard API and Lizard WMS capabilities. 

Working with GeoBlocks
======================

GeoBlocks are configured in `JSON <https://en.wikipedia.org/wiki/JSON>`_. Your graph can be edited by POSTing or PATCHing to the Lizard API.
For this we advise using `Postman <https://www.getpostman.com/>`_, but any application with an API component can be used. 
Methods for POSTing geoblocks to Lizard differ between `RasterBlocks <https://demo.lizard.net/doc/rasterblocks.html#>`_ and `Geometry and Series Blocks <https://demo.lizard.net/doc//geometryblocks.html#>`_.
On these pages explanation is provided on how to create a new GeoBlock in Lizard.

Graphs
------
A graph is a combination of multiple single Blocks which work together to create a "view" of one or more datasources in Lizard.
A valid graph always contains one or more source Blocks and one endpoint, which is the final product of your GeoBlock. 
Once you've configured a graph , a visualization of the graph is automatically generated. This visualization can be requested using the API request below: 

https://demo.lizard.net/api/v3/geoblocks/{uuid of graph}/visualize/?format=svg

.. image:: /images/d_geoblocks_03.png 

Examples of a graph
-------------------

Below is an example of a valid Raster graph which calculates the difference between the digitial elevation rasters AHN3 and AHN2.

.. code-block:: json

    {
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
      },
      "name": "difference",
    }

This graph contains two SourceBlocks linking to the individual digital elevation rasters. Furthermore it contains only one operation which calculates the difference between the two inputs.
This difference is also the endpoint as marked by the "name" field. The final "view" on the input data thus contains the difference between AHN3 and AHN2.

Getting familiar with GeoBlocks 
================================

We like helping you get more familiar with GeoBlocks. We've created a Jupyter Notebook to give you a hands-on experience with the basics of GeoBlocks.
You can `download <https://github.com/nens/lizardnotebooks/tree/master/Getting_familiar_with_GeoBlocks>`_ it on our Github page.
Make sure to follow the right `installation procedures <https://dask-geomodeling.readthedocs.io/en/latest/installation.html>`_. 

Any questions? We're happy to help! You can contact our servicedesk on servicedesk@nelen-schuurmans.nl
