
=============
Release Notes
=============


May 21st 2024
==================


New features in API v4:

* 3D tiles generation - Lizard postprocessing can now generate 3D tiles

* Async (bulk) timeseries events import in API - The API now includes functionality for asynchronous import of bulk timeseries events, improving efficiency and performance for large data sets.

* Vulnerable Buildings Analysis - An experimental functionality added to Lizard to allow you to determine vulnerable buildings based on waterdepth maps. 


February 20th 2024
==================

Lizard QGIS plugin updated:

* Download scenario's or use them as a WMS.
  
* Download (non-scenario) rasters directly into your QGIS project.

Everything can be found on the `Lizard Plugin page <b_lizardplugin>`_.


January 12th 2024
=================

Lizard backend updates:

*   Cloud-based import and export tasks (downloads come from Amazon S3 now)

*   Add pixel_size option to raster export in API

*   Set aggregation_type for scenario raster results, so that the Viewer shows statistics for polygon selections

Lizard Viewer:

*   Enable raster export again and use pixel_size option

*   Show web notification when a raster export has finished


October 10th 2023
=================
New viewer released:

*   Documentation for the new viewer: :doc:`b_viewer`


May 2nd 2023
============
New features in API v4:

*   Added spatial information to scenarios (based on raster results)

*   Extended raster '/data' sub-endpoint with option to retrieve data based on a polygon geometry and output format JSON

Bug fixes:

*   Fixed resampling issue for requests on '/zonal' raster sub-endpoint with small polygons compared to raster pixelsize, no longer returning nulls
 

February 28th 2023
==================
New features:

*   Raster alarms on Line and Polygon intersections

*   Vectortiles for assets, per assetset (combination of organisation and asset type)

Other improvements:

*   Adjustments of the notification email for finished 3Di postprocessing

*   API v4 improvements:

    *   Added upper_bounds (in combination with origin specifies spatial bounds in original projection) for rasters and raster sources

    *   Extended API v4 with Favourites and Search endpoints

    *   Add object information (of related asset) to locations listview in API v4


July 26th 2022
==============
This Lizard release contains a number of small but important bug fixes:

*   Lock raster source when deleting data, so that simultaneous imports do not fail

*   Reset metadata of raster source and layer when all data is deleted

*   Validation of alarm thresholds forcing unique input for values and warning levels

*   Improve error handling for raster zonal endpoint in case of too large request



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
