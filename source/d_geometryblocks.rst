.. _GeometryBlocksAnchor:

==========================
Geometry and Series Blocks
==========================
Geometry output
---------------

Geometry outputs are stored in :doc:`labels<c_labels>`. Labels are always linked to your Vectors stored in the Vector Server, for instance flood risk for parcels or buildings.
Labels are grouped in Labeltypes. The graph can be found in the source attribute of the labeltype.

.. image:: /images/d_geoblocks_02.png 

Individual labels (e.g. label linked to one building or parcel) can be found on the `labels endpoint <demo.lizard.net/api/v3/labels>`_.  
Labels can be computed on the fly using the compute endpoint or a-sync using the Lizard Task Server. 


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

Operations
==========

Wolf, work your magic