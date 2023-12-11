==================
Lizard QGIS plugin
==================

The Lizard QGIS plugin enables users to download their scenario results directly from the Lizard API 
to their GIS environment and show WMS of raster results.
Here we describe how to install and use the plugin.


Installation
============

* Add the Lizard plugin repository
    * In the main menu click *Plugins* > *Manage and Install plugins* > *Settings* 
    * In the section *Plugin repositories*, click *Add*
    * As details, fill in '3Di' as *Name*, and 'https://plugins.3di.live/plugins.xml' as *URL*

* Install the Lizard plugin: in the tab *All*, install the Lizard plugin. Restart QGIS when prompted.

* Enable macros
    * Make sure that *Enable macros* is set to *Always* in Settings > Options > General > Project files. 


Initial setup
=============

When starting the plugin for the first time you are prompted to provide some settings that are required.
In the following screen you need to provide the base URL of the Lizard portal you want to use. Also, you 
need to set or obtain a personal API key, for authentication with the API.

.. image:: /images/d_qgisplugin01.png


Scenario archive browser
========================

The Lizard plugin currently contains the Scenario archive browser (to be extended with more functionality).

* Select a scenario from the list, which can be filtered by scenario name.
* Two options:
    * Retrieve downloadable results (raw results and non-temporal rasters)
        * Select the results of interest
        * [Optional] Set nodata value and projection for raster exports
        * Start the download
    * Open raster results as WMS layers
        * Use the time controls to animate temporal raster results (e.g. water depth)

.. image:: /images/d_qgisplugin02.png

