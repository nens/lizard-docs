============
WMS Services
============

Lizard provides a Web Map Service (WMS) that you can use to visualize rasters and 3Di scenario’s stored in Lizard Raster Server as tiled images.
The Lizard WMS Service follows the `OGC WMS guidelines <https://www.ogc.org/standards/wms>`_.

Rasters
=======

To visualize and request the GetCapabilities of a specific raster you can use the following URL: 

{yourportal}.lizard.net/wms/raster_{UUID of raster}/?request=GetCapabilities

for example: 

https://demo.lizard.net/wms/raster_550e8400-e29b-41d4-a716-446655440000/?request=GetCapabilities

You can easily find the UUID of the raster in the Lizard Catalogue.
The Lizard Catalogue also provides the Lizard WMS GetCapabilities link for each raster.
With the GetCapabilities query parameter you retrieve the metadata of the service, including supported operations, parameters and a list of available layers. 

3Di Scenario’s
==============

To visualize and request the GetCapabilities of a 3Di scenario (list of rasters) you can use the following URL: 

{yourportal}.lizard.net/wms/scenario_{UUID of scenario}/?request=GetCapabilities

For example:

https://demo.lizard.net/scenario_550e8445-e29b-41d4-a716-446655440000/?request=GetCapabilities

You can look up the UUID of the scenario using the Scenarios endpoint in the Lizard API: 

https://demo.lizard.net/api/v3/scenarios

All available filters are listed on the endpoints’ page.
E.g. you can look up a scenario and it’s uuid by filtering on your own username with {yourportal}.lizard.net/api/v3/scenarios/?username __contains={your username}

With the GetCapabilities query parameter you retrieve the metadata of the service, including supported operations, parameters and a list of available layers. 
 
Datasets
========

To visualize and request the GetCapabilities of datasets (list of rasters) you can use the following URL: 

{yourportal}.lizard.net/wms/{slug of dataset}?request=GetCapabilities

For example:

https://demo.lizard.net/basiskaarten/?request=GetCapabilities

You can search for datasets in the Lizard Catalogue by using the Datasets filter in the left panel.
You will find the Lizard WMS GetCapabilities URL of the dataset in the metadata panel of a specific layer.  
 
Authorisation
=============

The Lizard WMS Service follows the authorisation system mentioned under :ref:`Authorisation<OrganisationsAnchor>`.
If layers are private you need privileges in the organisation that owns the dataset.
Use a Personal API Key to authenticate with the Lizard WMS Service, as described in :ref:`API Authentication<_APIAuthenticationAnchor>`.
