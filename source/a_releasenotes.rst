.. raw:: html

    <style> .blue {color:#4a86e8} </style>

.. role:: blue

====================
Latest Release Notes
====================

We’re happy to announce the newest release of Lizard Portal, Lizard Backend and Lizard Catalogue.
If you have questions about this release or if you’re interested in features please contact us via info@lizard.net  

Frontend
========

Lizard Client
-------------

* Reorganisation of the omnibox

    * Multiple legends below each other
    * Name of the raster and organisation added to diagrams and legends

.. image:: /images/a_releasenotes_01.jpg

Catalogue
---------

The Lizard Catalogue offers insight in the data layers that are available for your organisation.
There is an extensive search option to make the layers easily accesible.
Every data layer will show available metadata.
From the Catalogue you have the option of opening the data layers via the API or via the Lizard portal.

The Catalogue can be reached via this url: https://demo.lizard.net/catalogue/

.. image:: /images/a_releasenotes_02.jpg

Backend
=======

API
---

* added api/v4/wmslayers/
* added api/v4/scenarios/
* added api/v4/datasets/
* added api/v4/organisations/<uuid>/usage/
* added ordering to api/v4/rasters/
* removed CSV renderer on all timeseries endpoints
* improved performance of api/v3/labels/
* added a dedicated cache to api/v4/labels/counts/
* Rerouted 3Di result processing through the Lizard API (/api/v4/scenarios/process_result)

Geoblocks
---------

* added "TemporalAggregate" and "Cumulative" geoblocks that compute temporal statistics on rasters on-the-fly

Maintenance/updates
-------------------

* Updated django to 1.11.24
* Added a dedicated queue for 3Di operational scenarios

Previous Release notes
======================

:doc:`Release notes Lizard release 25-06-2019<a_release_25062019>`