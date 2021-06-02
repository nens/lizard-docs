.. raw:: html

    <style> .blue {color:#4a86e8} </style>

.. role:: blue

=============
Release Notes
=============


June 2021 Release
=====================
We’re happy to announce the newest release of Lizard Management.
If you have questions about this release or if you’re interested in features please contact us via info@lizard.net


February 2021 Release
=====================
We’re happy to announce the newest release of Lizard Management and Lizard Catalogue.
If you have questions about this release or if you’re interested in features please contact us via info@lizard.net



November 2019 Release
=====================

We’re happy to announce the newest release of Lizard Portal, Lizard Backend and Lizard Catalogue.
If you have questions about this release or if you’re interested in features please contact us via info@lizard.net

Frontend
--------

Lizard Client
+++++++++++++

* Reorganisation of the omnibox

    * Multiple legends below each other
    * Name of the raster and organisation added to diagrams and legends

.. image:: /images/a_releasenotes_01.jpg

Catalogue
+++++++++

The Lizard Catalogue offers insight in the data layers that are available for your organisation.
There is an extensive search option to make the layers easily accesible.
Every data layer will show available metadata.
From the Catalogue you have the option of opening the data layers via the API or via the Lizard portal.

The Catalogue can be reached via this url: https://demo.lizard.net/catalogue/

.. image:: /images/a_releasenotes_02.jpg

Backend
-------

API
+++

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
+++++++++

* added "TemporalAggregate" and "Cumulative" geoblocks that compute temporal statistics on rasters on-the-fly

Maintenance/updates
+++++++++++++++++++

* Updated django to 1.11.24
* Added a dedicated queue for 3Di operational scenarios

June 2019 Release
=================

We’re happy to announce the newest release of Lizard Portal, Lizard Backend and Lizard Catalogue. If you have questions about this release or if you’re interested in features please contact us via info@lizard.net  

.. raw:: html

    <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://www.youtube.com/embed/NhK2OaYfc8E" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
    </div>


Lizard Client
-------------

Lizard Management Interface
+++++++++++++++++++++++++++

    * Multiple legends below each other
    * Name of the raster and organisation added to diagrams and legends

We’ve developed a user friendly user management interface. With this interface managers can add users to their organisation and give them the right authorisation to data and applications. 

.. image:: /images/a_release_25062019_09.png

.. image:: /images/a_release_25062019_10.png

.. image:: /images/a_release_25062019_11.png

.. image:: /images/catalogue.jpg

.. image:: /images/a_release_25062019_12.png

.. image:: /images/a_release_25062019_13.png

* added api/v4/wmslayers/
* added api/v4/scenarios/
* added api/v4/datasets/
* added api/v4/organisations/<uuid>/usage/
* added ordering to api/v4/rasters/
* removed CSV renderer on all timeseries endpoints
* improved performance of api/v3/labels/
* added a dedicated cache to api/v4/labels/counts/
* Rerouted 3Di result processing through the Lizard API (/api/v4/scenarios/process_result)

Maintenance/updates
+++++++++++++++++++

* A bug that hampered users to upload temporal rasters or configuring a raster store (bug reference: PROJ-1114)