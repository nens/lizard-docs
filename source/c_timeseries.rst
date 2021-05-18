==============
Time series
==============


The data management interface for timeseries can be used to upload, edit or remove timeseries, monitoring networks and locations.

.. image:: /images/c_manage_timeseries_menu.png	

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
* Interval (optional): Specify a time range between each time series step.

.. note::
	if you leave the interval at 0, it will mean it is irregular ('nonequidistant') data. This is also necessary if you have timesteps smaller than seconds. 

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
    Locations must be connected to an existing asset to be visualised in the portal. The asset will have a symbol and zoom level depending on the type. Also, the metadata differs per type. For now, only measuringstations can be added via the API. If you have any questions about this, please contact the service desk. 
	
* Asset type (optional): Specify a type of asset.  
* Asset location: after specifying the asset type, you can search by code or name. 


3. RIGHTS
------------

* Accessibility (required, private by default): Choose an access modifier to decide who has access to this object. 


If you are satisfied, click "SAVE"







