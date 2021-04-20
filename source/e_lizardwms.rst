============
WMS Services
============

Lizard provides a Web Map Service (WMS) that you can use to visualise rasters and 3Di scenarios stored in Lizard Raster Server as tiled images.
The Lizard WMS Service follows the `OGC WMS guidelines <https://www.ogc.org/standards/wms>`_.

Rasters
=======

To visualise and request the GetCapabilities of a specific raster you can use the following URL: 

``https://{yourportal}.lizard.net/wms/raster_{UUID of raster}/?request=GetCapabilities``

for example: 
https://demo.lizard.net/wms/raster_eae92c48-cd68-4820-9d82-f86f763b4186/?request=GetCapabilities

You can easily find the UUID of the raster in the `Lizard Catalogue <https://demo.lizard.net/catalogue>`_ or `API <https://demo.lizard.net/api/v4/rasters/>`_.
The Lizard Catalogue also provides the Lizard WMS GetCapabilities link for each raster.
With the GetCapabilities query parameter you retrieve the metadata of the service, including supported operations, parameters and a list of available layers. 

3Di Scenarios
==============

To visualise and request the GetCapabilities of a 3Di scenario (list of rasters) you can use the following URL: 

``https://{yourportal}.lizard.net/wms/scenario_{UUID of scenario}/?request=getcapabilities``

For example:
https://demo.lizard.net/wms/scenario_c30ef7f2-c871-4d70-a087-8f078f9ebafd/?request=GetCapabilities

You can look up the UUID of the scenario using the `Scenarios endpoint in the Lizard API <https://demo.lizard.net/api/v4/scenarios>`_.
All available filters are listed on the endpoints’ page. E.g. you can look up a scenario and it’s uuid by filtering on your own username.
With the GetCapabilities query parameter you retrieve the metadata of the service, including supported operations, parameters and a list of available layers. 
 
Datasets
========

To visualise and request the GetCapabilities of datasets (list of rasters) you can use the following URL: 

``https://{yourportal}.lizard.net/wms/{slug of dataset}?request=GetCapabilities``

For example:
https://demo.lizard.net/wms/basiskaarten/?request=GetCapabilities

You can search for datasets in the Lizard Catalogue by using the Datasets filter in the left panel.
You will find the Lizard WMS GetCapabilities URL of the dataset in the metadata panel of a specific layer.  
 
Authorisation
=============

The Lizard WMS Service follows the authorisation system mentioned under :ref:`Authorisation<OrganisationsAnchor>`.
If layers are private you need privileges in the organisation that owns the dataset.


Use a Personal API Key to authenticate with the Lizard WMS Service, as described in :ref:`API Authentication<APIAuthenticationAnchor>`.

In QGIS the authentication is filled in as follows: 

- username = __key__ 
- password = Personal API Key



