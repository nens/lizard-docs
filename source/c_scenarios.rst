==============
3Di scenarios
==============

The data management interface for scenarios can be used to edit or remove scenarios.

.. image:: /images/c_manage_3discenarios.png	


Search for a scenario
------------------------

You can search for a scenario by either typing (part of) the scenario name, the UUID, username of the supplier or model name. 

.. image:: /images/c_manage_3discenarios_search.png	

You can also specify that you only want to show your own scenario's by ticking the box in the top right corner.

Used storage and deletion of scenarios
-----------------------------------------

.. image:: /images/c_manage_3discenarios_storage.png	

In the left side, you can see the used storage for your organisation. This may have influence on your subscription.

.. image:: /images/c_manage_3discenarios_delete1.png	

If you want to remove a complete scenario, you simply check the box of the relevant scenario(s) and choose 'delete'. If you choose 'delete raw', it will only remove the Calculation Core Logging, Raw 3Di Output, Grid Administration and Aggregated 3Di Output. You can also remove a specific raster of a scenario by double-clicking on a scenario and clicking on the 'trash' icon next to the layer.

.. image:: /images/c_manage_3discenarios_delete2.png	 

.. warning::
	If you delete a scenario, it is really gone! We might be able to retrieve the rasters if you contact support within 14 days.  
	
	
Edit a scenario
----------------

Right now you can only edit the accessability of a scenario.
Scenarios are private by default (only visible for logged in users of the same organisation). 
You can choose to make them visible for all logged in users or even public so no login is necessary.

.. image:: /images/c_manage_3discenarios_public.png


.. tip::
	Make scenarios public if you want to use them in other GIS applications via a `wms link <https://docs.lizard.net/e_lizardwms.html#di-scenarios>`_. 
	

	