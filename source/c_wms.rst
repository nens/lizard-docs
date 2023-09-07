===========
WMS Layers
===========

WMS stands for Web Mapping Service.
It is a standard method of sharing georeferenced maps.
The WMS layers management allows the user to configure layers in Lizard even if they are hosted on another platform.
In the management screen you can add new WMS layers or edit existing layers.

.. image:: /images/c_manage_wms_01.png

New WMS Layer
==============


.. image:: /images/c_manage_newitem.png

After clicking the 'new item' icon, you can configure a new WMS layer. 

.. image:: /images/c_manage_wms_02.png

The following fields can or must be filled in:

1. GENERAL
------------

* Name (required): Choose a name that is findable and not too difficult
* Description (optional)
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
===============
	
By clicking on the name of a WMS layer, the configuration of the corresponding layer is opened.
In the configuration page you can edit any of the settings previously given to the WMS layer.
To quickly find a WMS layer: use the search bar.
If the layer you are looking for seems unavailable you might have to switch organisations, feel free to contact the servicedesk for any problems (servicedesk@nelen-schuurmans.nl).

.. image:: /images/c_manage_wms_03.png

You can for example edit the description or share your WMS layer with other organisations. 

.. tip::
	Advanced: Is your WMS layer not visible in the Viewer? Check via the network tab (press F12) how Lizard requests the WMS and if that WMS url makes sense. You can always ask the service desk to help as well. 
