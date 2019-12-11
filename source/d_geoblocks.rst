=========
Geoblocks
=========

Introduction
============

Geo-information services often rely on high resolution data from multiple sources.
Geoblocks provide the tool to process these geo-data on-the-fly. 
The technology enables big geo-data solutions for operational data flows.
Geoblock operations can be computed on a regular basis or executed upon request.

One geoblock can modify the information in raster or geometry data, e.g. multiply two rasters or buffer a geometry.
Multiple geoblocks can be stacked together into a model, like stacking lego blocks into a tower.

Geoblocks information services are transparent and reproducible.
A geoblocks graph is the model configuration that defines how data should be combined to create information.
The model configuration can be accessed and altered via API and a graph view visualization is automatically generated (example in figure x).

https://demo.lizard.net/api/v4/geoblocks/e12fcc5c-7313-827b-1d5c-26bd294792c4/visualize/?format=svg

Figure x: Geoblocks visualization example of a water depth raster masked below 2.5 cm.

.. warning::
    Missing Figure!
    Linked geoblock is no longer available

Flexibility
===========

- Geoblocks are modular. This means that the blocks are self-contained units, that can be combined or interchanged with others to create different shapes or designs. Hence, multiple geoblocks configurations can be combined into a new configuration or information service.
- Data can expand, which automatically results into updates in the information service.
- Spatial data expansion provides result maps at larger extent
- Temporal data expansion can make the information service more actual, e.g. the information service uses the latest time step from daily data updates.
- By adjusting a few lines in the configuration, one can replace a deprecated dataset with a more recent version (e.g. replace AHN2 with AHN3)
- Unlike conventional GIS raster calculator solutions (e.g. QGIS, gdal_calc), you can combine data at different resolutions with varying spatial extent.
- Temporal operations, e.g. combine a static land cover raster with a daily soil moisture raster.

Configuration using Lizard API
==============================

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

Raster:

* read raster data (e.g. read :ref:`raster store <why_rasterstores>`)
* Combine raster data (e.g. mosaic raster A and raster B)
* Temporal edits (e.g. raster A gets temporal behaviour of raster B)
* Spatial edits (e.g. gaussian smoothing)
* Value edits (e.g. reclassification)

Geometry:

* Read geometry data
* Geometry operations (e.g. buffer)
* Combine raster and geometry data (e.g. sum of raster values aggregated by region)
* Attribute table operations (e.g. classify continuous values into groups)

Edits on raster values and geometry attributes:

* Math blocks (e.g. A*B)
* Comparison blocks (e.g A>B)
* Logical blocks (e.g. A==B)
