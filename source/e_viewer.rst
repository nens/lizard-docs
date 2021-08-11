======
Viewer
======

The Viewer of Lizard is the graphical user interface (GUI), in which measuring locations, parameters, timeseries, rasters and other layers are visible in maps and graphs.

Basic elements	
==============

After logging in:

.. image:: /images/e_portal_01.jpg

1. Log in or out and manage your account
2. Make and access favourites
3. Switch to graph view
4. Open export screen
5. Links to partner platforms and applications
6. Zoom in and out on map
7. Search for addresses, dates, names or codes/tags
8. Open and close data menu
9. Selection tools to query data on the map

Data menu and layers	
--------------------

The topmost entry in the data menu toggles between the following base layers:

- Neutral
- Topography
- Satellite 

Click a data layer to activate it.
   
.. note::
	Data layers need to be active to retrieve information from them in the map.
	
.. tip::
   You can rescale the colour scale of the elevation layer (DEM) >> Double click the layer in the menu.
   

Adjust the opacity by clicking the green bar below the activated data layer.

.. image:: /images/e_portal_02.jpg

Upon activating a raster layer a crosshair appears. By clicking it the application zooms to the full data extent, both in space and time.

Add more data
--------------------

Want to see more or other data layers? Just add data that is available to your organisation.

Hit the button in the bottom of the data menu: Add data. Clicking the cross (x) in the layer bar removes it from the menu instantaneously.

Below is the 'Add data interface'. Use the search bar (1) to navigate through the data layers that you or your organisation are authorized to see.

.. image:: /images/e_portal_03.jpg
   :height: 400px
   :width: 400 px
   :align: center

Close the Add data interface (2) and go back to the data menu.
	
One of the available data layer types is *3Di scenarios*. A scenario is a combination of layers and products that belong to a 3Di model run.
Click a scenario layer to expand it and activate data layers or download products. 

Navigation in time	
==================

Search for the period you are interested in through the search bar or use the buttons next to the timeline.
You can adjust the period by panning, zooming or dragging the timeline, or by specifying the start and end date. 

Temporal rasters
----------------

Raster layers with a time component (temporal raster layers, e.g. Rain radar) can be animated.
Start or pause the animation using the button on the left-hand side of the timeline.
	
.. image:: /images/e_portal_04.jpg
   :align: center
   
When the rain layer is active, the bars in the timeline show the distribution of rainfall in time for the area on your screen.

The length of the selected period of time determines the aggregation level of the rainfall data. This can be 5 minutes, hourly or daily.

Timeseries
----------

Once a time series has been selected, by clicking on a timeseries location or after you searched it in the search bar, you see something like the following:

.. image:: /images/e_portal_05.jpg
   :align: center
   
The graph appears in in a new screen in the top left, which we call the *omnibox*.  You also inspect the graph closer in the "Graph" mode (click it in the menu). 
	
.. tip::
   In the omnibox click the button 'ZOOM TO EXTENT' to zoom to the full extent of the series.
   There are also three buttons for standard periods. This means no more searching for a historical or short-term time series. Just click the buttons! 

Navigation in space	
===================

Zoom in and out on the map by using the buttons next to the search bar.
Use the search bar to navigate to specific locations like countries, cities or addresses.

Symbols
-------

.. image:: /images/e_portal_12.png 
    :align: center

All asset types have a unique symbol as you can see above.
From the symbol, or by clicking on an asset, you can see if you are for example dealing with a groundwaterstation or a pumpstation.
You can also see both black and red symbols.
A red symbol means that there is a timeseries linked to it.
A black symbol means that there is no timeseries linked to it.
If an asset is red, but you cannot see the timeseries, it means that you either do not have the rights to see the timeseries,
or that you have to go further back in time (tip: click on “zoom to extent”).
Lastly, for groundwaterstations, you can see a line drawn through the station.

.. image:: /images/e_portal_13.png 
    :align: center

This means that the groundwaterstation is inactive. 

.. tip::
	Looking for a specific region? Drag a frame with your mouse while holding SHIFT. This feature enables you to navigate to the selected area.

Selection tools
----------------
   
There are 4 selection tools:

.. image:: /images/e_portals_selection01.jpg
   :align: right 
   
1. Point
2. Multipoint
3. Line
4. Region
   
**Point selection** 
Point selectionretrieves asset information, time series and map values from the active data layers. Results are displayed on the left.

**Multipoint selection** 

.. image:: /images/e_portals_selection02.jpg
   :align: right
   
Use the multipoint tool to select multiple objects and/or locations.
When multiple assets are selected, time series are not displayed in the omnibox. 
Go to the graph view to see them.

.. tip::
	Add a set of locations to a favourite to always have them available instantaneously.

**Line selection** 	

.. image:: /images/e_portals_selection03.jpg
   :align: right 
   
Use the line selection tool to retrieve data along a profile, e.g. elevation from a DEM.

* 1st click: Start point
* 2nd click: End point
* 3rd click: Reset

.. image:: /images/e_portal_11.jpg
   :height: 400px
   :width: 300 px
   :align: center
   
Hovering along the profile on the map shows a corresponding indicator in the graph.

**Region selection** 

The region selection tool aggregates data of the selected region. 

.. image:: /images/e_portals_selection04.jpg
   :align: right 

.. image:: /images/e_portal_06.jpg
   :align: center
   
Region analysis can be performed on raster of data type nominal (quantititive) or ordinal (classes). Click the *star* behind the layer name and the analysis is applied on-the-fly on the active region type for the zoom level. The regions are coloured based on the most abundant class.

.. tip::
    Hover over the classes in the diagram to see more information.

.. tip::
	Select a class in the legend and the regions are coloured based on the relative abundancy of that class. 
	This answers questions like: what is the general rice growth stage within my district or which municipality is most urbanized?

Graph view and data interpretation
==================================

There are multiple ways to interpret your data. For example, you can:

* Activate multiple layers in order to get a more integral scope on situations or to see interaction between locations.
* Export the data and analyse in another program (see next paragraph) 
 
Graph view
----------

Switch between map view and graph view with the Graph/Map button.

.. image:: /images/e_portal_07.jpg

By scrolling or dragging within the graph the domain of the Y-axis can be changed. By scrolling or dragging the datetimebar, the X-axis can be changed. 

.. note::
	If multiple locations with time series are selected initially there are no time series displayed. Click time series in the menu to show/hide them.

.. tip::
	Adjust the colour of a line by choosing from the scale that opens by clicking the coloured bar.

.. tip::
	Drag multiple time series items into one graph to combine them. 

.. tip::
	Water level time series can be recalculated relative to the surface level. This is done by clicking the button 'relative'. This enables analysis of drainage depth or freeboard.  The option also applies to the export of these time series.

Next to the relative button you can zoom to the standard periods and full extent of the active timeseries.

Apps
------

In order to examine your data in further detail open one of our partner platforms through the Apps screen.

.. note::
	Apps are not available by default in every Lizard Viewer. Do you want to see or change the App settings of a Viewer? Please contact our support office (servicedesk@nelen-schuurmans.nl).
	
	

Share
=====

Lizard enables sharing asset, time series and raster data between organisations to provide (water) managers with a better overview of systems and processes.

Favourites
----------------

You can save a Lizard state with data of one or more assets, maps or time series as a favourite and share it with others.

.. image:: /images/e_portal_08.jpg
   :height: 400px
   :width: 300 px
   :align: center
   
Open the Favourites dropdown and enter a name/short description. You can save a specific period or one that is relative to ‘now’. In that case, the favourite is always up to date.

Click a favourite to load the Lizard state that was saved in it. A link to the favourite can be retrieved by clicking the blue symbol next to the delete button.