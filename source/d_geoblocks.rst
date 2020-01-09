=========
Geoblocks
=========

Digital geo services rely on high resolution big data coming from multiple real-time sources. 
We developed GeoBlocks to make it more easy to process and analyse (real-time) that data to create a digital geo service. 

GeoBlocks is a GIS modelling toolbox that allows you to make on-the-fly analysis using raster & vector data. 
There are two basetype Blocks: `RasterBlocks <https://dask-geomodeling.readthedocs.io/en/latest/raster.html>`_ and `Geometry and Series Blocks <https://dask-geomodeling.readthedocs.io/en/latest/geometry.html#>`_. 
A combination of blocks is called a "graph".

- GeoBlocks derives information on-the-fly and creating a "view" on your data. This is also the reason why it's very efficient in data storage. For example, you can clip, substract and mask without having to store intermediate results! 
- All Blocks are modular and can be combined with others to create extensive models, called graphs. 
- You can apply GeoBlocks on real-time data-flows that expand in space and time (e.g. remote sensing data) allowing you to create real-time GIS analysis.
- You can combine temporal and static datasets. For example, you can combine a static land cover raster with a daily soil moisture raster).
- It's easy to apply your model on different input datastes (e.g. replace Elevation dataset 1 with a newer Elevation dataset 2), for example to detect changes.
- Unlike conventional GIS raster calculator solutions, you can combine data with different resolutions and varying spatial extent.

Open Source
===========

The computational core of GeoBlocks is published open source under the name `dask-geomodeling <https://dask-geomodeling.readthedocs.io/en/latest/index.html>`_.
Most operations are identical. Only the I/O filetype and configuration differs.
The open source library can be used to build on-the-fly models on your own PC.
There's a limitation in the complexity of the models that you can run locally.
This is determined by your memory and processor capabilities. 

If you want to scale up your model or increase complexity you can do publish your model and data to Lizard using the Lizard API.
With the GeoBlocks engine you can scale up your models and integrate the model in your geo services using the Lizard API and Lizard WMS capabilities. 


Getting familiair with GeoBlocks 
================================

We like helping you get more familiair with GeoBlocks. We've created a Jupyter Notebook to give you a hands-on experience with the basics of GeoBlocks.
You can `download <https://github.com/nens/lizardnotebooks/tree/master/Getting_familiar_with_GeoBlocks>`_ it on our Github page.
Make sure to follow the right `installation procedures <https://dask-geomodeling.readthedocs.io/en/latest/installation.html>`_. 

Any questions? We're happy to help! You can contact our servicedesk on servicedesk@nelen-schuurmans.nl

How to create a GeoBlocks model/graph and view the result
=========================================================

GeoBlocks are interpreted in `JSON <https://en.wikipedia.org/wiki/JSON>`_. Your graph can be edited by POSTing or PATCHing to the Lizard API.
`Postman <https://www.getpostman.com/>`_ can come in handy to manage your graph. 
API filtering is supported and documented in the API raster endpoint: `<https://demo.lizard.net/api/v3/rasters/>`_

Raster output
-------------

If your GeoBlock output is a raster. Your GeoBlocks results can be requested via the `Catalogue <demo.lizard.net/catalogue>`_ `Raster API endpoint <demo.lizard.net/api/v3/rasters/>`_ and can be request via the Lizard WMS service.
If you want to find your graph in the Lizard API it's easiest to use the Catalogue.

- Search for your raster in the catalogue.
- Open the raster in the API using the Open in API button. 
- Follow the link mentioned in the source_url attribute. 

.. image:: /images/d_geoblocks_01.png

Geometry output
---------------

Geometry outputs are stored in :doc:`labels<c_labels>`. Labels are always linked to your Vectors stored in the Vector Server, for instance flood risk for parcels or buildings.
Labels are grouped in Labeltypes. The graph can be found in the source attribute of the labeltype.

.. image:: /images/d_geoblocks_02.png 

Individual labels (e.g. label linked to one building or parcel) can be found on the `labels endpoint <demo.lizard.net/api/v3/labels>`_.  
Labels can be computed on the fly using the compute endpoint or a-sync using the Lizard Task Server. 

Graphs
------
Once you've configured a graph , a visualization of the graph is automatically generated. This visualization can be requested using the API request below: 

https://demo.lizard.net/api/v3/geoblocks/{uuid of graph}/visualize/?format=svg

.. image:: /images/d_geoblocks_03.png 

Examples of a graph
-------------------

Raster example: difference between digital elevation rasters AHN3 and AHN2 

.. code-block:: json

    {
      "name": "endpoint",
      "graph": {
        "AHN3": [
          "geoblocks.raster.sources.RasterStoreSource",
          "file:///path/to/some/store"
        ],
        "AHN2": [
          "geoblocks.raster.sources.RasterStoreSource",
          "file:///path/to/another/store"
        ],
        "endpoint": [
          "geoblocks.raster.elemwise.Subtract",
          "AHN3",
          "AHN2"
        ]
      }
    }

Geometry example: classify build year of buildings.

.. code-block:: json

    {
        "source": {
            "graph": {
                "buildings": [
                    "geoblocks.geometry.sources.GeoDjangoSource",
                    "hydra_core",
                    "building",
                    {
                        "id": "object_id",
                        "build_year": "building_build_year"
                    },
                    "geometry",
                    "start",
                    "end"
                ],
                "buildyear": [
                    "geoblocks.geometry.base.GetSeriesBlock",
                    "buildings",
                    "building_build_year"
                ],
                "label": [
                    "geoblocks.geometry.field_operations.Classify",
                    "buildyear",
                    [
                        1900,
                        1940,
                        1970,
                        1990
                    ],
                    [
                        "A",
                        "B",
                        "C",
                        "D",
                        "E"
                    ]
                ],
                "result": [
                    "geoblocks.geometry.base.SetSeriesBlock",
                    "buildings",
                    "label_value",
                    "label"
                ]
            },
            "name": "result"
        }
    }