=========
Geoblocks
=========

Digital geo services often rely on high resolution big data coming from multiple real-time sources. 
We developed GeoBlocks to make it more easy to process and analyse (real-time) big geo data as part of your digital geo service. 
GeoBlocks is published open source under the name `dask-geomodeling <https://dask-geomodeling.readthedocs.io/en/latest/index.html>`_.
Dask-geomodeling can be used to build on-the-fly models on your own PC.  
The size of the models that you can make is then determined by your memory and processor capabilities and are therefore limited.
If you want to scale up your model you can do publish your model to the GeoBlocks engine using the Lizard API. 
With the GeoBlocks engine you can scale up your models to easily calculate with data sets of >100GB and integrate the analysis into your digital geo service. 

The operations available are called Blocks.
The two basetype Blocks are `RasterBlocks <https://dask-geomodeling.readthedocs.io/en/latest/raster.html>`_ and `Geometry and Series Blocks <https://dask-geomodeling.readthedocs.io/en/latest/geometry.html#>`_. 
A collection of blocks is called a graph or model and describes the relationship between the data and the operations that you use to derive information.

* GeoBlocks derives information on-the-fly, making it very efficient in data storage. E.g. you can clip, substract and mask without storing intermediate datasets and present the result on-the-fly on the map. 
* GeoBlocks allows you to analyse these geo data on-the-fly, making your analysis very efficient and traceable. 
* Blocks are modular and can be combined or interchanged with others to create extensive models. 
* You can apply GeoBlocks on operational data-flows that expand in space and time (e.g. remote sensing data). Information is automatically updated based on the newest data avaiable. 
* You can easily combine temporal datasets with static datasets. (e.g. combine a static land cover raster with a daily soil moisture raster).
* It's easy to apply your model on different input datastes (e.g. replace Elevation dataset 1 with a newer Elevation dataset 2)
* Unlike conventional GIS raster calculator solutions (e.g. QGIS, gdal_calc), you can combine data at different resolutions with varying spatial extent.

Getting familiair with GeoBlocks 
================================

.. warning::
    Download link for Jupyter notebook needs to be added!

We'd like to help you get more familiair with GeoBlocks.
You can `download <LINK TO GITHUB PAGE FOR JUPYTER NOTEBOOK>`_ this Jupyter Notebook and follow the tutorials to get a hands-on experience.
Make sure to follow the right `installation procedures <https://dask-geomodeling.readthedocs.io/en/latest/installation.html>`_.     

How to build GeoBlocks models using the Lizard API
==================================================

The geoblocks graph can be created and edited via the Lizard API, using POST and PATCH methods.
Geoblocks can be applied to Lizard rasters and assets. 
API filtering is supported and documented in the API raster endpoint: `<https://demo.lizard.net/api/v4/rasters/>`_
Geoblock endpoints can use raster and geometry inputs.
For rasters, the geoblock graph is stored in the "source" attribute field of `rasters <https://demo.lizard.net/api/v4/rasters/>`_. 
Assets on the other hand, can be assigned with `labels <https://demo.lizard.net/api/v3/labels/>`_, using `labeltypes <https://demo.lizard.net/api/v3/labeltypes/>`_,
e.g.flood risk for buildings).
Labels can be retrieved with the latest data, or computed on a regular basis.
The final block in a geoblocks configuration is used to derive the data in the form that is specified in the geoblocks graph.
Multiple data inputs can be configured into one graph. 
A geoblocks configuration has similar behaviour as a view on a database.

Once configured, a visualization of the graph is automatically generated. This visualization can be requested using the API request below: 

https://demo.lizard.net/api/v4/geoblocks/{uuid of graph}/visualize/?format=svg

Figure x: Geoblocks visualization example of a water depth raster masked below 2.5 cm.

.. warning::
    Missing Figure!
    Insert Geoblocks visualization example!

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

Geoblock operations 
===================

**Raster:**

* read raster data (e.g. read :ref:`raster store <why_rasterstores>`)
* Combine raster data (e.g. mosaic raster A and raster B)
* Temporal edits (e.g. raster A gets temporal behaviour of raster B)
* Spatial edits (e.g. gaussian smoothing)
* Value edits (e.g. reclassification)

**Geometry:**

* Read geometry data
* Geometry operations (e.g. buffer)
* Combine raster and geometry data (e.g. sum of raster values aggregated by region)
* Attribute table operations (e.g. classify continuous values into groups)

**Edits on raster values and geometry attributes:**

* Math blocks (e.g. A*B)
* Comparison blocks (e.g A>B)
* Logical blocks (e.g. A==B)