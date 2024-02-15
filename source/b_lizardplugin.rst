==============================
QGIS Plugin
==============================

The Lizard QGIS plugin enables users to download their scenario results directly from the Lizard API 
to their GIS environment and show WMS of raster results.
Here we describe how to install and use the plugin.


Installation
============

* Add the Lizard plugin repository
    * Note: if you are using the `3Di Modeller Interface <https://docs.3di.live/i_what_is_mi.html>`_, you can skip this step.
    * In the main menu click *Plugins* > *Manage and Install plugins* > *Settings* 
    * In the section *Plugin repositories*, click *Add*
    * As details, fill in '3Di' as *Name*, and 'https://plugins.lizard.net/plugins.xml' as *URL*

* Install the Lizard plugin
    * Click on the tab *All*
    * In the search bar at the top, search for Lizard
    * Select Lizard in the panel in the middle
    * In the bottom-right of the dialog, click *Install plugin*.

Initial setup
=============

When starting the plugin for the first time you are prompted to provide some settings that are required.
In the following screen you need to provide:

* The base URL of the Lizard portal you want to use. This will typically be *your_organisation*.lizard.net.

* A Personal API Key. If you already have an API Key, you can fill it in by clicking "Set...". If you do not have a Personal API Key yet, follow these steps.

    * Click "Obtain..." You will be redirected to the management page where you can create a new Personal API Key.

    * Create a new Personal API Key by pressing the + NEW ITEM button in the upper right corner.

    * Fill in a name for the new Personal API Key. Click on ‘Submit’ to the right.

    * You now have your own Personal API Key. Copy it.

    * Return to QGIS / the 3Di Modeller Interface.

    * Click Set… and paste your Personal API Key. Then click Save.

.. image:: /images/d_qgisplugin01.png


Scenario archive browser
========================

The Lizard plugin currently contains the Scenario archive browser (to be extended with more functionality).

* Select a scenario from the list, which can be filtered by scenario name.

After selecting a scenario, you have two options:

* Retrieve downloadable results (raw results and non-temporal rasters)

    * Select the results of interest

    * [Optional] Set nodata value and projection that the downloaded rasters should get.

    * Start the download

    * Follow the progress at the top of the QGIS main window.

* Add raster results to your project as WMS layers

    * Use the `Temporal Controller<https://docs.qgis.org/3.28/en/docs/user_manual/map_views/map_view.html?highlight=temporal%20controller#time-based-control-on-the-map-canvas>` to animate temporal raster  results (e.g. water depth)

.. note:
   
    Downloading temporal rasters is not supported at the moment. To visualize them in QGIS or the 3Di Modeller Interface, add them as WMS and use the `Temporal Controller<https://docs.qgis.org/3.28/en/docs/user_manual/map_views/map_view.html?highlight=temporal%20controller#time-based-control-on-the-map-canvas>` to navigate through its time steps.

.. image:: /images/d_qgisplugin02.png

