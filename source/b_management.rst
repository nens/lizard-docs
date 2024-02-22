==========
Management
==========

In the management interface there is a variety of options.

`Usermanagement <d_authentication_user_management>`_ will be discussed later.

Rasters
=============

The data management interface for rasters can be used to upload, edit or remove rasters.
Raster Sources are the data containers, Raster Layers are the configuration of how the data is visualised.

.. image:: /images/c_manage_rasters_01.png
.. image:: /images/c_manage_rasters_02.png
.. image:: /images/c_manage_rasters_03.png

Creating and editing Raster Sources and Layers
----------------------------------------------

The first step in uploading your raster datasets is to create a Raster Source.

The Data Management interface is available at: “www.{your_organisation}.lizard.net/management/”.

After landing on this page, click on ‘Data’ -> ‘Rasters’ -> 'Raster Sources'.
Click on “New Item” |NewItem| to open the form or choose an existing raster to edit.  

.. |NewItem| image:: /images/c_manage_newitem.png

After filling in the form you can choose to directly upload your data by selecting your GeoTIFF's in the 'DATA' section.
In case of a temporal raster source you need to specify which file belongs to which timestep.
This is recognised automatically if the filename is composed according to the specified format.
When you save a new Source you will have the option to go straight to the Raster Layer form to publish your data.

.. image:: /images/c_datatypes_01.png

Interested in the possibilities for your organisation? Please contact us via info@lizard.net.

GeoBlocks management
====================

The GeoBlocks management page provides you a powerful tool to build your GeoBlocks Rasters.
It helps you configure complex GeoBlocks models and enables you to validate your work along the way.

The Visual editor shows your model as a flow diagram, consisting of block objects representing the input Raster Sources and GeoBlocks operations.
The right sidebar shows the available blocks. Click on the blocks for a description and the expected inputs. Drag a block into the canvas to include it in your model.
Connect blocks to use one as input for the other.

When the model is valid it can also be shown in the Text editor. This shows the JSON graph as it would be sent to the API when you save the item.
Here you can also make edits and validate the result.

Example 1 shows a simple model which subtracts one Raster Source from another (difference in surface elevation between two versions of a dataset).

.. image:: /images/c_manage_geoblocks_01.png

Example 2 shows a more complex model with multiple Raster Sources and a series of operations.

.. image:: /images/c_manage_geoblocks_02.png

For more information about the possibilities of GeoBlocks see: :ref:`GeoBlocksAnchor`


WMS Layers
===========

WMS stands for Web Mapping Service.
It is a standard method of sharing georeferenced maps.
The WMS layers management allows the user to configure layers in Lizard even if they are hosted on another platform.
In the management screen you can add new WMS layers or edit existing layers.

.. image:: /images/c_manage_wms_01.png

New WMS Layer
-------------

.. image:: /images/c_manage_newitem.png

After clicking the 'NEW ITEM' icon, you can configure a new WMS layer. 

.. image:: /images/c_manage_wms_02.png

The configuration has some mandatory items while others are optional, an extensive list with descriptions follows:

1. GENERAL
------------

* Name (required): Choose a name that is findable and not too difficult
* Description (optional): Give a description of the information that is displayed by the WMS layer.
* Tags / Datasets (optional): You can connect the layer to an existing dataset. 

2. DATA
------------

* WMS URL (required): Specify which base URL is used to retrieve the image data. It usually ends on '/wms'
* Slug (required): can be seen as layer name used in the external platform
* Download URL (optional): Specify which URL is used to download the data. This will enable the download button in the Lizard Catalogue.
* Legend URL (optional): Specify which URL is used to show the legend of this layer.
* Get Feature URL (optional) : Optional URL to retrieve feature info data.
* Tiled (enabled by default) : Specifies whether the layer is tiled (for better performance)
* Min and max zoom (required): Closest and furthest point of view in this WMS layer. 0 is visible at world scale, 31 is zoomed in at a house. You can check the zoom level in the url in the Viewer (after the coordinates). 
* Spatial bounds (optional): Specify the extent of this layer on the map. This information can also be automatically obtained by clicking "Get from source". 
* Options (JSON): Extra options of this layer, specfied in JSON.

3. RIGHTS
------------

* Accessibility (required, private by default): Choose an access modifier to decide who has access to this object. 
* Shared with (optional): Specify if this object should be accessible by other organisations, and if so, which ones.
* Organisation (required, pre-filled):  The organisation this object belongs to. 
* Supplier (optional): The supplier of this object. If you are not an administrator, this field is always pre-filled with your username.

If you are satisfied, click "SAVE"


Edit WMS Layer
---------------
	
By clicking on the name of a WMS layer, the configuration of the corresponding layer is opened.
In the configuration page you can edit any of the settings previously given to the WMS layer.
To quickly find a WMS layer: use the search bar.
If the layer you are looking for seems unavailable you might have to switch organisations, feel free to contact the servicedesk for any problems (servicedesk@nelen-schuurmans.nl).

.. image:: /images/c_manage_wms_03.png

.. tip::
	Advanced: Is your WMS layer not visible in the Viewer? Check via the network tab (press F12) how Lizard requests the WMS and if that WMS url makes sense. 



Layer collections
====================

.. warning::
    This section will be extended in the near future. 



Time series
==============


The data management interface for timeseries can be used to upload, edit or remove timeseries, monitoring networks and locations.

.. image:: /images/c_manage_timeseries_menu.png	


----------
Locations
----------

.. image:: /images/c_manage_locations_01.png	


Search or sort your locations here.
Check out possible actions by clicking the three dots icon.
Create a new object with the New Item button on the top right corner.


.. image:: /images/c_manage_newitem.png

.. image:: /images/c_manage_locations_02.png	

1. GENERAL
------------

* Location name (required): Choose a name that is findable and not too difficult
* Code (required): Choose a code that represents the object within your organisation.


2. DATA
------------	

.. warning::
    Locations must be connected to an existing asset to be visualised in the Viewer. The asset will have a symbol and zoom level depending on the type. Also, the metadata differs per type. For now, only measuringstations can be added via the API. If you have any questions about this, please contact the service desk. 
	
* Asset type (optional): Specify a type of asset.  
* Asset location: after specifying the asset type, you can search by code or name. 
* Extra metadata (JSON) (optional): Free JSON field to add information to this object.

3. RIGHTS
------------

* Accessibility (required, private by default): Choose an access modifier to decide who has access to this object. 


If you are satisfied, click "SAVE"

------------
Timeseries
------------

.. image:: /images/c_manage_timeseries_01.png	

Search or sort your time series here.
Check out possible actions by clicking the three dots icon next to a time series. You can add timeseries to a monitoring network (MN), edit, or delete hem. 
Create a new object with the New Item button on the top right corner.

.. image:: /images/c_manage_newitem.png

.. image:: /images/c_manage_timeseries_02.png	

1. GENERAL
------------

* Name (required): Choose a name that is findable and not too difficult
* Code (required): Choose a code that represents the object within your organisation.


2. DATA
------------	

* Observation type (required): Choose the way the data is measured, and the units. New observation types can be added via the `api <https://demo.lizard.net/api/v4/observationtypes/>`_ or requested via the servicedesk.
* Location (required): Choose to which location you want to add this timeseries. New locations can be added via the api or via data management --> timeseries --> locations.
* Value type (required): Specify what kind of data you will be supplying. See `Level of measurement <https://en.wikipedia.org/wiki/Level_of_measurement>`_.
* Datasource (optional): Specify a data source if it is available. Otherwise, you can leave it empty or create a new one via the API. 
* Interval (optional): Specify a time range between each time series step.

.. note::
	if you leave the interval at 0, it will mean it is irregular ('nonequidistant') data. This is also necessary if you have timesteps smaller than seconds. 
	
* CSV Files (optional): You can add new data via a csv file or via the API. If you want to supply a csv file, see the instructions below:

.. note::
	The first line of the file should describe the column names, for example:

	| time, value
	| 2020-03-20T01:00:00Z, 3.14 
	| 2020-03-20T01:05:00Z, 2.72
	
	The next lines are the timestemp and value for that timestep. Make sure you do not list the same timestep twice. 
	All uploads in Lizard are expected to be in UTC time. 

	| time: ISO 8601 date and time representation. This is a required field. 
	| value: A number, string, or boolean, depending on the value_type of the corresponding time series. 


* Extra metadata (JSON) (optional): Free JSON field to add information to this object.


3. RIGHTS
------------

* Accessibility (required, private by default): Choose an access modifier to decide who has access to this object. 
* Username of supplier (optional): The supplier of this object. If you are not an administrator, this field is always pre-filled with your username.
* Supplier code (optional): The FTP or Supplier code is used as reference to your own system. 

.. note::
	Timeseries are not linked to an organisation directly. They are linked to organisations via the locations. 

If you are satisfied, click "SAVE"



---------------------
Monitoring networks
---------------------

Monitoring networks are used to group and give insights on time series.
Check out possible actions by clicking the three dots icon next to existing networks.

Create a new object with the New Item button on the top right corner.

.. image:: /images/c_manage_newitem.png

.. image:: /images/c_manage_monitoringnetworks_01.png	

1. GENERAL
------------

* Name (required): Choose a name that is findable and not too difficult
* Description (optional)


2. DATA
------------	

.. warning::
    The button "MANAGE" will only work if there are already timseries connected to the monitoring network. If there are, you can remove the the connection here. New connections can be added via the timeseries management app. 

3. RIGHTS
------------

* Accessibility (required, private by default): Choose an access modifier to decide who has access to this object. 
* Organisation (required, pre-filled):  The organisation this object belongs to. 

If you are satisfied, click "SAVE"



Scenarios
==============

The data management interface for scenarios can be used to manage scenarios.


.. image:: /images/c_manage_scenarios_01.png	


Search for a scenario
------------------------

You can search for a scenario by either typing (part of) the scenario name, the UUID, username of the supplier or model name. 

.. image:: /images/c_manage_scenarios_search.png	

You can also specify that you only want to show your own scenarios by ticking the box in the top right corner.


Used storage and deletion of scenarios
-----------------------------------------

.. image:: /images/c_manage_scenarios_storage.png	

In the left side, you can see the used storage for your organisation. This may have influence on your subscription.

.. image:: /images/c_manage_scenarios_delete1.png	

If you want to remove a complete scenario, you simply check the box of the relevant scenario(s) and choose 'delete'. 
If you choose 'delete raw', it will only remove the raw data and not the timeseries and rasters. You can also remove a specific raster of a scenario by double-clicking on a scenario and clicking on the 'trash' icon next to the layer.

.. image:: /images/c_manage_scenarios_delete2.png	 

.. warning::
	If you delete a scenario, it is really gone! We might be able to retrieve the rasters if you contact support within 14 days.  
	
Add a scenario
--------------------

Scenarios can be automatically exported to Lizard, for example via 3Di. 
You can also add a new scenario with the New Item button on the top right corner.

.. image:: /images/c_manage_newitem.png	
	
Edit a scenario
----------------

Right now you can only edit the accessability of a scenario.
Scenarios are private by default (only visible for logged in users of the same organisation). 
You can choose to make them visible for all logged in users or even public so no login is necessary.

.. image:: /images/c_manage_scenarios_public.png


.. tip::
	Make scenarios public if you want to use them in other GIS applications via a `wms link <https://docs.lizard.net/e_lizardwms.html#di-scenarios>`_. 
	
	
You can add a scenario to an existing project via the threedot icon.

.. image:: /images/c_manage_scenarios_project.png		
	
Group scenarios in a project
-----------------------------

Projects are used to group and give insights on scenarios.

.. image:: /images/c_manage_projects_01.png

Create a new project with the New Item button on the top right corner.

.. image:: /images/c_manage_newitem.png


Labels
============

.. warning::
    This section is to be extended.

.. image:: /images/c_manage_labeltypes.png



Alarms
======

Lizard provides an alarm feature that sends notifications via sms or email when newly processed values of timeseries or temporal rasters exceed a threshold.
It is used to notify people of events that may require action, for instance an upcoming rain event or flood.

The alarm management screens are found at https://demo.lizard.net/management/#/alarms.

.. image:: /images/f_alarms_01.jpg

The configuration has a variety of options to generate relevant notifications with messages that include the specifics of the event. 

Notifications
=============

Behind the Notifications tile you find the overviews of existing raster and timeseries alarms for your organisation and their status (active/inactive).
The 'NEW ITEM' button leads you to the form to register a new alarm.
We go through some of the options that the system provides, to explain them in detail.

Selecting a raster
------------------

Raster alarms are set on temporal rasters. These can be part of a scenario, a single source raster or a Geoblock.
An alarm is set for one point location intersecting this temporal raster.

You can type in the field to search in the names of available rasters. Next, select the type of intersection (Point, Line or Polygon).
Draw the geometry on the map or insert a geometry in the JSON field below the map.

For Line and Polygon intersections a spatial aggregation is needed to derive a timeseries that can be compared to the alarm thresholds.
The options are:

* Sum
* Mean
* Min
* Max
* Median
* Count

Selecting a timeseries
----------------------

Timeseries often do not have a clear name or code by themselves.
That is why we start with looking up the asset it relates to.
Once the asset is selected it should be easy to select the timeseries from the list of related objects.

Relative start and end
----------------------

The user doesn't always want to receive alarms for the whole period of newly processed data.
For instance, for operational flood models which might have records of prior theshold exceedances, you may only be interested in receiving alarms for forecasted threaths.

To only analyse the relevant part of your data you can set relative start and end.
They are set relative to The figure below gives a schematic overview of how this method works.

.. image:: /images/f_alarms_02.jpg

If these fields are left empty the trigger check is done on the complete data frame of newly processed data.

Snoozing option
---------------

It can be considered undesirable for alarms to be triggered during brief spikes.
The snoozing option allows the user to determine the timeperiod a threshold should be exceeded before the alarm is triggered and a notification is sent.
This option is available for both the raising of the alarm and its withdrawal. Default is 1 (trigger at first occurrence). 

Contacts and Groups
===================

The recipients of alarm notifications are configured in the Contacts screen, with their phone number and/or email address.
Each contact can be part of multiple Groups, which in turn can be used in multiple alarms.
So no need to do a whole lot of data duplications of contact info.

Templates
=========

The notification messages are configured with Templates.
There is a difference in setting up Email and SMS Templates:

* Email: Supports both plain text and HTML and are not limited in length
* SMS: Plain text with maximum length of 160 characters (after substitution of variables)

You can use a number of variables to enrich the content of the notifications and make them applicable to different alarms.
The variables contain options for including the name of the receiver and details about the alarm at hand.

The option "No further impact" determines that a message is used specifically to notify when an alarm is fully withdrawn.
This type of message can be set in addition to a standard message to let receivers know that the situation has settled down.
This often requires a different text and therefore a different Template.
