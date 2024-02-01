==============
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

	