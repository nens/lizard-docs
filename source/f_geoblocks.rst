.. _GeoBlocksAnchor:

=========
GeoBlocks
=========

Digital geo services rely on high resolution big data coming from multiple real-time sources. 
We developed GeoBlocks to make it easier to process and analyse (real-time) that data to create a digital geo service. 

GeoBlocks is a GIS modelling toolbox that allows you to make on-the-fly analyses using raster & vector data stored in Lizard. 
Geoblocks consists of numerous classes which describe geographical operations. An individual class is called a Block and a combination of multiple Blocks is called a Graph.

Lizard uses GeoBlocks technology to derive two different types of data: Rasters and Labels. On top of the basic set of block operations (:ref:`RasterBlocksAnchor`) there is an additional set specifically for label computation (:ref:`GeometryBlocksAnchor`).
Geoblock rasters can be visualized through the WMS, analyzed through the API or exported to GeoTIFF.
Geoblock labeltypes are used for computing labels on-the-fly or in a batch so that they are stored and available via the API.

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
This is determined by your memory and processor capacity. 

If you want to scale up your model or increase complexity you can publish your model and data to Lizard using the Lizard API.
The GeoBlocks engine uses the powerful Lizard backend allowing you to scale up your models and integrate the model in your geo services using the Lizard API and Lizard WMS capabilities. 

Working with GeoBlocks
======================

GeoBlocks are configured in `JSON <https://en.wikipedia.org/wiki/JSON>`_. Your graph can be edited by POSTing or PATCHing to the Lizard API.
For this we advise using `Postman <https://www.getpostman.com/>`_, but any application with an API component can be used. 
Methods for POSTing geoblocks to Lizard are similar for rasters and labeltypes.
The difference is that the a raster requires a RasterBlock as Graph endpoint and the labeltypes a GeometryBlock.
On these pages explanation is provided on how to create or update a GeoBlock in Lizard.

Graphs
------
A graph is a combination of multiple Blocks that work together to create a "view" of one or more datasources in Lizard.
A valid graph always contains one or more source Blocks and one endpoint, which is the final product of your GeoBlock. 
Once you've configured a graph, a visualisation of the graph is automatically generated. This visualisation can be requested using the API request below: 

``https://demo.lizard.net/api/v4/rasters/{uuid of raster}/visualize/?format=svg``

.. image:: /images/d_geoblocks_03.png 

Example of a graph
------------------

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

API specification
=================

.. _RasterBlocksAnchor:

RasterBlocks
============

RasterBlocks are the GeoBlocks that work with rasterdata. RasterBlocks operate on `Lizard Rasterdata <d_datatypes.html#rasters>`_.

Creating a new RasterBlock
--------------------------

The first step of creating a new raster GeoBlock is making a new Lizard raster instance that will contain your graph.
This can be done on the `Lizard management page <https://demo.lizard.net/management/#/>`_ or by performing a POST on the API endpoint https://demo.lizard.net/api/v4/rasters/ 

The second step is PATCHing the ``source`` element of your new raster. This element will contain the graph of your GeoBlock.
To PATCH your raster provide a valid JSON object for its source element, and perform a patch on ``https://demo.lizard.net/api/v4/rasters/{uuid of the new raster}/``

In the example we provided earlier we used the 'SUBTRACT' geoblock operation to determine the difference between the AHN3 and the AHN2.
As a new version of the AHN is now available, we want to compare the AHN4 and AHN3, instead of the AHN3 and AHN2.
If we want to update our model, a PATCH request can be send.
A PATCH can be considered as an update.
Multiple PATCH requests can be send to apply multiple updates. 

.. code-block:: json

    {
      "source": {
        "name": "difference",
        "graph": {
            "AHN4": [
              "lizard_nxt.blocks.LizardRasterSource",
              "f83b5020-b296-489e-8f1f-a166ff086422"
            ],
            "AHN3": [
              "lizard_nxt.blocks.LizardRasterSource",
              "a60ad336-c95b-4fb6-b852-96fc352ee808"
            ],
            "difference": [
              "geoblocks.raster.elemwise.Subtract",
              "AHN4",
              "AHN3"
            ]
        }
      }
    }



Raster output
-------------

After you PATCH your raster, the changes immediately take effect. 
To view your GeoBlocks results you can access the raster via the `Catalogue <https://demo.lizard.net/catalogue>`_, `Raster API endpoint <https://demo.lizard.net/api/v4/rasters/>`_ or the Lizard WMS service.

.. tip::
	Use the generate uuid to find your raster quickly with the following link: https://demo.lizard.net/catalog/?data=Raster&uuid={uuid}. By keeping a tab with your resulting raster open, you are able to refresh the page quickly after each PATCH request. This will allow you to see the effects of your patch immediately.	

If you want to show the result of your raster Geoblock it is easiest to use the Catalogue.

- Search for your raster in the catalogue.
- Open the raster in the API using the Open in API button. 
- Follow the link mentioned in the source_url attribute. 

.. image:: /images/d_geoblocks_01.png

Operations
----------

Raster data sources
+++++++++++++++++++++

.. autoclass:: lizard_nxt.blocks.LizardRasterSource
   :members:
   :exclude-members: get_sources_and_requests, process

.. note:: If a UUID of a raster (instead of a rastersource) is given, it will
  automatically be replaced by the Geoblock graph of that raster.


RasterBlocks that combine rasters
+++++++++++++++++++++++++++++++++++++++

.. automodule:: dask_geomodeling.raster.combine
   :members:
   :exclude-members: get_sources_and_requests, process, get_stores

.. autoclass:: lizard_nxt.blocks.LizardRasterGroup
   :members:
   :exclude-members: get_sources_and_requests, process

.. autoclass:: lizard_nxt.blocks.LizardRasterId
   :members:
   :exclude-members: get_sources_and_requests, process


Elementwise RasterBlocks
+++++++++++++++++++++++++++++++++++++++++

.. automodule:: dask_geomodeling.raster.elemwise
   :members:
   :exclude-members: get_sources_and_requests, process

Spatial RasterBlocks
+++++++++++++++++++++++++++++++++++++++

.. automodule:: dask_geomodeling.raster.spatial
   :members:
   :exclude-members: get_sources_and_requests, process, projection, geometry, geo_transform

Temporal RasterBlocks
+++++++++++++++++++++++++++++++++++++++

.. automodule:: dask_geomodeling.raster.temporal
   :members:
   :exclude-members: TemporalSum, get_sources_and_requests, process

Miscelleneous RasterBlocks
+++++++++++++++++++++++++++++++++++++++

.. automodule:: dask_geomodeling.raster.misc
   :members:
   :exclude-members: get_sources_and_requests, process, extent, geometry

.. _GeometryBlocksAnchor:

Geometry and Series Blocks
==========================

GeometryBlocks are the GeoBlocks that modify geometries or integrate rasterdata into geometries.
They can sample rasters and perform geometric operations like intersections and geometric differences.
The output from a Geometry GeoBlock is a label value.
This means that the operation should always end with a classification of one of the feature properties into a ``"label_value"`` column. 
Also, the generated label should be related to a Lizard object through the ``"object_id"`` column. The object_type (e.g. ``"building"``) is configured when creating the labeltype.
The result of the GeometryBlock can be requested through the API.
Such request returns the label for a geometric feature along with a predefined list of intermediate results.

Creating a new GeometryBlock
----------------------------

To create a new GeometryBlock you have to POST the graph directly to the labeltypes api endpoint: https://demo.lizard.net/api/v4/labeltypes/.
Unlike for RasterBlocks it is not possible to define a GeometryBlock without the API.
Once the graph has been posted it is possible to PATCH changes and alter the structure of the graph.
If you want to patch changes to the graph this can be done by providing a valid JSON object for its source element,
and perform a patch on ``https://demo.lizard.net/api/v4/labeltypes/{uuid of the new labeltype}/``.

Currently it is not possible to visualize the resulting labels in the Lizard Viewer.
Individual labels can be computed with a GET request on the labeltype endpoint. For example with:
``https://demo.lizard.net/api/v4/labeltypes/{label type uuid}/compute/?geom_intersects=POINT(4.46648 51.92938)``.
It is also possible to pre-compute larger amounts of labels, which will either be exported to a downloadable file, or become available via https://demo.lizard.net/api/v4/labeltypes/{label type uuid}/labels/.
By doing so it becomes possible to quickly request multiple labels or label statistics.

To pre-compute labels for a specific region you have to send a POST request on the labeltype endpoint, for example:
``https://demo.lizard.net/api/v4/labeltypes/{label type uuid}/compute/?boundary_id=95246&start=2018-10-01T01:00:00Z&tile_size=500&tile_projection=EPSG:28992&mode=centroid``.
For details about file exports, consult the documentation at ``https://demo.lizard.net/api/v4/labeltypes/{label type uuid}/compute/``.

Labels that have been pre-computed are stored in the labels endpoint of the API: https://demo.lizard.net/api/v4/labeltypes/{label type uuid}/labels/.
By using this endpoint it is possible to request both individual labels and label statistics. Through a GET request it is possible to determine statistics of the entire labeltype or specific regions: https://demo.lizard.net/api/v4/labeltypes/{label type uuid}/labels/counts/. 

Examples of a graph
-------------------

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

Geometry output
---------------

Geometry outputs are stored in :doc:`labels<c_labels>`.
Labels are always linked to your Vectors stored in the Vector Server, for instance flood risk for parcels or buildings.
Labels are grouped in Labeltypes. The graph can be found via the labeltypes endpoint:

``https://demo.lizard.net/api/v4/labeltypes/{label type uuid}/visualize/?format=svg``

.. image:: /images/d_geoblocks_02.png 

Individual labels (e.g. label linked to one building or parcel) can be found on the labels endpoint.  
Labels can be computed on the fly using the compute endpoint or a-sync using the Lizard Task Server. 

Operations
----------

Source GeometryBlocks
+++++++++++++++++++++++++

The following Geoblocks are current geometry source of geometry-type geoblocks.
The geometry data comes from internal Lizard tables.


.. autoclass:: django_geoblocks.blocks.sources.GeoDjangoSource
   :members:
   :exclude-members: get_sources_and_requests, process

.. note:: ``app_label`` should be "hydra_core" and ``model_name``
  should be one of "building", "administrativeboundary", "parcel", "pumpeddrainagearea", "fixeddrainagelevelarea", "leveezone", "pumpstation", "groundwaterstation", "measuringstation", "polder"

.. autoclass:: django_geoblocks.blocks.sources.AddDjangoFields
   :members:
   :exclude-members: get_sources_and_requests, process

.. note:: ``app_label`` should be "lizard_nxt" and ``model_name``
  should be one of "labelparameter", "labeltype", "rasterlayer"


Aggregate GeometryBlocks
++++++++++++++++++++++++++

.. automodule:: dask_geomodeling.geometry.aggregate
   :members:
   :exclude-members: get_sources_and_requests, process


GeometryBlocks for set operations
+++++++++++++++++++++++++++++++++++++++++++++++

.. automodule:: dask_geomodeling.geometry.set_operations
   :members:
   :exclude-members: get_sources_and_requests, process


Constructive for constructive operations
+++++++++++++++++++++++++++++++++++++++++++

.. automodule:: dask_geomodeling.geometry.constructive
   :members:
   :exclude-members: get_sources_and_requests, process


GeometryBlocks that operate on non-geometry fields
++++++++++++++++++++++++++++++++++++++++++++++++++

.. automodule:: dask_geomodeling.geometry.field_operations
   :members:
   :exclude-members: get_sources_and_requests, process

.. automodule:: dask_geomodeling.geometry.text
   :members:
   :exclude-members: get_sources_and_requests, process


Miscelleneous GeometryBlocks
+++++++++++++++++++++++++++++++++++++++++++++++

.. automodule:: dask_geomodeling.geometry.geom_operations
   :members:
   :exclude-members: get_sources_and_requests, process


.. automodule:: dask_geomodeling.geometry.merge
   :members:
   :exclude-members: get_sources_and_requests, process
