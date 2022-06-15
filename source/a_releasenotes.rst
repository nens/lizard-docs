.. raw:: html

    <style> .blue {color:#4a86e8} </style>

.. role:: blue

=============
Release Notes
=============


June 14th 2022
==============

*	API v4 changes:

        *       Enable POST on /scenarios endpoint
	
	*       Enable PATCH and POST on /scenarios/{uuid}/results endpoint
	
*       Create Scenarios and attach raster results in Lizard Management
	
*       Add support for `info_format=application/geo+json` in GetFeatureInfo requests on Lizard WMS service
	
*       Allow nesting templated GeoBlocks in new GeoBlocks Rasters
	
*       Bugfix for timeseries percentiles endpoint: Using start and end parameters no longer results in a 404 error



May 11th 2022
=============

*	API v4 changes:

        *       Introduction of Projects datamodel, to group Scenarios
	
	*       Update of Scenarios metadata model:
	
		*       Added fields `description` and `extra_metadata`
		
		*       Field names changed (`simulation_start`, `simulation_end`, `simulation_identifier` and `model_identifier`)
		
		*       Duplicate field `username` removed (information already available in `supplier` field)
	
*       Scenario Catalogue and Scenario Management updated based on added/changed features in API
	
*       Fix GetCapabilities request for WMS of templated GeoBlocks rasters



March 11th 2022
===============

*	API v4 additions:

        *       Labeltypes endpoint, including Labels and Label Parameters as subendpoint
	
	*       Eventseries endpoint, including Events subendpoint
	
*       Specified error message when exporting more than 1 billion pixels in one raster export



January 18th 2022
===================

*	Improvements in API v4:
	

		
	*	Drop by-organisation subendpoint for most assets and enable pagination on the main endpoint, which means less restrictions in retrieving asset data
		
	*	Make boundary filtering parameters (`boundary__type`, `boundary__name`, `boundary__id`) consistent with other related field filters, i.e. with double underscores (backwards compatible for single underscores)
		
	*	Add filtering on `last_modified`, `created` and `access_modifier` fields in endpoints
		
	*	Add filtering on `start` and `end` fields for timeseries
		
	*	Add filtering on `timeseries__start` and `timeseries__end` for locations
	
	
	
*	Update of PostGIS, improving the performance of spatial filteirng in the API
*	Add `application/json` option for WMS GetLegendGraphic requests, according to Geoserver specifications
*	Limit task that relates locations to assets to only apply to unrelated locations, to improve performance
*	Add button in Geoblocks management to open an item in the Lizard Viewer	
*	Bugfix for number input fields in Lizard Management (on-the-fly validation of decimal number input)	
*	Various other bugfixes in Lizard Management




August 2021 Release
=====================
We’re happy to announce the release of Lizard Homepage.

Important changes
-------------------

*	Lizard Homepage 
*	Datasets will be called Layer collections 
*	Lizard Contracts endpoint
*	Steadier 3Di-result-processing

The story behind  the new homepage 
+++++++++++++++++++++++++++++++++++++++

The past year, many new functionalities have been developed. The Lizard data warehouse and analytics platform has become a solution for many consultants working with environmental data and for setting up digital services. We see that next to the Viewer, the Catalogue, Management and API are increasingly more important for users. The Homepage ensures easy access to functionalities for all users.


.. image:: /images/a_homepage.jpg



Action required?
+++++++++++++++++++

The introduction of the homepage requires no action in itself. What we do recommend to do is to check if you or your colleagues have created quick links to Lizard. This is only needed for links to the Lizard Viewer, for example a link from your intranet or bookmark bar to a map or graph in Lizard.  If your link is broken and results in a 404 error, you can make the following adjustment:



1) Search for links going to {yourorganisation}.lizard.net/

2) Change this link to {yourorganisation}.lizard.net/viewer/.



Example 1: Link to viewer

https://demo.lizard.net/en/map/
will be
https://demo.lizard.net/viewer/en/map/




Example 2: Link to a favourite

https://demo.lizard.net/favourites/55db162c-581a-491f-8579-b52e7e68d2bd
will be
https://demo.lizard.net/viewer/favourites/55db162c-581a-491f-8579-b52e7e68d2bd

.. note::
    NB: Within Lizard all settings and references will be adjusted by us, for example links in dashboards. 
	Links to the API will not change. 
	
.. note::
    The terms Portal and Viewer were both used for {yourorganisation}.lizard.net/. The Portal will remain the base url (which now leads to the Homepage). The Viewer is the new url {yourorganisation}.lizard.net/viewer/





June 2021 Release
=====================
We’re happy to announce the newest release of Lizard Management.

* New time series management interface.
* New user management interface.


.. raw:: html

    <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://www.youtube.com/embed/RG4UvRtyUKo" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
    </div>

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
