==============
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










