.. _GeometryBlocksAnchor:

==========================
Geometry and Series Blocks
==========================
GeometryBlocks are the GeoBlocks which assimilate and operate rasterdata into vector data. They can sample rasters and perform geometric operations like intersections and geometric differences.
The output from a Geometry GeoBlock is a label value. This means that the operation should always end with a classification of one of the feature columns into a label value. 
The result of the GeometryBlock can be requested through the API. Such request returns the label for a geometric feature along with a defined list of intermediate results.

Creating a new GeometryBlock
----------------------------
To create a new GeometryBlock you have to POST the graph directly to the labeltypes api endpoint: https://demo.lizard.net/api/v3/labeltypes/. Unlike for RasterBlocks it is not possible to define a GeometryBlock without the API.
Once the graph has been posted it is possible to PATCH changes and alter the structure of the graph. If you want to patch changes to the graph this can be done by providing a valid JSON object for its source element, and perform a patch on https://demo.lizard.net/api/v3/labeltypes/{uuid of the new labeltype}/.

Currently it is not possible to visualize the resultant labels in the Lizard portals. Individual labels can be computed with a GET request on the labeltype endpoint. For example with:
https://demo.lizard.net/api/v3/labeltypes/{label type uuid}/compute/?geom_intersects=POINT(4.46648 51.92938). It is also possible to pre-compute larger amounts of labels. By doing so it becomes possible to quickly request multiple
labels or label statistics. 

To pre-compute labels for a specific region you have to send a POST request on the labeltype endpoint, for example:
https://demo.lizard.net/api/v3/labeltypes/{label type uuid}/compute/?boundary_id=95246&start=2018-10-01T01:00:00Z&tile_size=500&tile_projection=EPSG:28992&mode=centroid.

In the pre-compute you have to provide some sort of geographic bounding area. This can be through a predefined boundary in Lizard (like in the example) or a geometric bounding box.
The start parameter applies a temporal filter to the features included.
Features which are valid at the start date are computed, features which were built after or removed before the start-date are not computed. 

Label endpoint
--------------
Labels which have been pre-computed are stored in the labels endpoint of the API: https://demo.lizard.net/api/v3/labels/. By using this endpoint it is possible to request both individual labels and label statistics. Through a GET request it is possible to determine statistics of the entire labeltype or specific regions: https://demo.lizard.net/api/v3/labels/counts/?label_type__uuid={label type uuid}. 


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

Geometry outputs are stored in :doc:`labels<c_labels>`. Labels are always linked to your Vectors stored in the Vector Server, for instance flood risk for parcels or buildings.
Labels are grouped in Labeltypes. The graph can be found in the source attribute of the labeltype.

.. image:: /images/d_geoblocks_02.png 

Individual labels (e.g. label linked to one building or parcel) can be found on the `labels endpoint <demo.lizard.net/api/v3/labels>`_.  
Labels can be computed on the fly using the compute endpoint or a-sync using the Lizard Task Server. 

Operations
----------

Wolf
