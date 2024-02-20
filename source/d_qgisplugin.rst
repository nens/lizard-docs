==================
Lizard QGIS plugin
==================

The Lizard QGIS plugin enables users to download their scenario results directly from the Lizard API 
to their GIS environment and show them as WMS layers.
On this page you will find how to install, setup and use the plugin.


Installation
============

.. note:: Note: if you are using the `3Di Modeller Interface <https://docs.3di.live/i_what_is_mi.html>`_ the Lizard plugin repository is already added.

* Add the Lizard plugin repository
    1. In the main menu click *Plugins* > *Manage and Install plugins* > *Settings* 
    2. In the section *Plugin repositories*, click *Add*
    3. As details, fill in '3Di' as *Name*, and 'https://plugins.lizard.net/plugins.xml' as *URL*

* Install the Lizard plugin
    1. Click on the tab *All*
    2. In the search bar at the top, search for Lizard
    3. Select Lizard in the panel in the middle
    4. In the bottom-right of the dialog, click *Install plugin*.

Initial setup
=============

The Lizard plugin consists of two components: the plugin and its settings.

Before you are able to start the plugin, you are required to provide an API key within the settings.
If you do not provide an API key first, you will receive a pop-up with the following message:

`There is no Lizard API key defined. Please set it up and try again.`

Which is followed by the settings menu.
There are only two settings to worry about:
* Base URL: this is the Lizard portal you would like to acces. This will typically be *your_organisation*.lizard.net.
* API Key: your personal API key. You can provide one by clicking `Set...`. 
 
If you do not have a Personal API Key yet, follow these steps:

1. Click `Obtain...` You will be redirected to the management page where you can create a new Personal API Key.
2. Create a new Personal API Key by pressing the + NEW ITEM button in the upper right corner.
3. Fill in a name for the new Personal API Key. Click on `Submit` to the right.
4. You now have your own Personal API Key. Copy it.
5. Return to QGIS / the 3Di Modeller Interface.
6. Click Set… and paste your Personal API Key. Then click Save.

.. image:: /images/d_qgisplugin01.png


Lizard browser
==============

The Lizard plugin currently contains a `Simulations results`_ section and a `Rasters`_ section.


Simulations results
-------------------

The simulation results section consists of three compartments: scenario selection, scenario items and feedback.
.. image:: /images/d_qgisplugin02.png

The scenario selection, which can be found at the top of the section. With the search bar a scenario can be found.
Once a scenario has been selected two options are available, below the scenario overview on the right:
* `Show downloadable files`: will display all downloadable files in the middle compartment.
* `Add as WMS`: adds all downloadable layers as WMS into your project.

Within the scenario items compartment all results are shown.
Downloadable results will be black, others are shown as grey.

.. image:: /images/d_qgisplugin02a.png

To download results:
1. Select the results of interest
2. [Optional] Set nodata value and projection that the downloaded rasters should get.
3. Start the download
4. Follow the progress at the top of the QGIS main window.

Temporal layers are currently not available to download can be shown as WMS layers.
To inspect their changes over time: use the `Temporal Controller<https://docs.qgis.org/3.28/en/docs/user_manual/map_views/map_view.html?highlight=temporal%20controller#time-based-control-on-the-map-canvas>` to animate temporal raster results (e.g. water depth).


The last compartment consists of feedback. 
Within this section the actions of the plugin are reported. 
Some examples are:
* Scenario download task added to the queue.
* Scenario download finished.
* WMS layers for scenario added to the project.

If an action fails for any reason this will also be reported in the feedback compartment.

.. image:: /images/d_qgisplugin03.png

Rasters
-------

.. image:: /images/d_qgisplugin04.png

Accessing rasters through the Lizard plugin works like the scenario's, except that scenario's contain multiple rasters.
Temporal rasters can only be used as WMS layers.
Static layers can be downloaded.

To download a raster multiple settings can be provided:

* The output folder: the folder in which the file will be saved.
* The filename: the name of the file.
* Map extent based on:
    * Map canvas: the entire map is exported.
    * Polygons: the polygon provided is used to export the project.
* No-data value: the value which represents no-data available.
* Pixel-size: the size of each individual pixel
* CRS: coordinate system.

.. image:: /images/d_qgisplugin05.png

The last compartment consists of feedback. Within this section the actions of the plugin are reported. Some examples are:
* Scenario download task added to the queue.
* Scenario download finished.
* WMS layers for scenario added to the project.

If an action fails for any reason this will also be reported in the feedback compartment.