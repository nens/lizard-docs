==============================
API functional documentation
==============================

You can acces the Lizard API via “www.{your_organisation}.lizard.net/api/”.

.. image:: /images/api.JPG

What is an API?
===============

API stands for Application Programming Interface. 
The API, looking like the picture above, gives back timeseries, rasters, or other data or information. This is depending on the request you do to the API. This request comes from the URL you type in the browser. You can also access the API via another program, and make automatic requests.


Basic use API
=============

Below we discuss a basic request to the API. More examples and possibilities will be discussed further down

The basic url is www.{your_organisation}.lizard.net/api/v3, for example:
 www.demo.lizard.net/api/v3 

If you type this in your browser, for example Google Chrome, you will get a list of parameters. These parameters are so called *endpoints*. If you paste this endpoint after your basic url, you will initiate a query. An example is ``locations``. 
If you click on the url www.demo.lizard.net/api/v3/locations , you will send a query to Lizard to search all locations that you have access to. As a response, you will get indeed the locations back, as well as some metadata. 

.. image:: /images/api2.JPG

Above each page, you will see some additional parameters, with which you can specify your query more. Most endpoints have examples of this.

.. image:: /images/api3.JPG

If we are looking for a specific location, with a name that contains 'gemaal', we can use this query:

www.demo.lizard.net/api/v3/locations/?name__icontains=gemaal

.. tip::
	icontains means that the name does not have to match exactly. 
	

If you are an administrator or supplier of the data, you can also edit or delete the data via the API. 	


Versions
========

We have noticed that our users are increasingly making use of the API. To prevent failure of the applications of customers, scripts and Excel connections, we have decided to release new features according to the format below:


* API v2: depricated
* API v3: stable
* API v4: experimental


From now on, the API v2 is deprecated. This means that this API will disappear when the development of API v5 starts, which will be around the end of this year. API v3 will be the stable version of API. We will no longer be updating this version. We are using the experimental version, v4, to develop new features.

We will be organising API masterclasses this year, where any user who wants to increase or maintain his or her knowledge can participate. 


Contact
=======

If you have additional questions about the use of the API contact our servicedesk (servicedesk@nelen-schuurmans.nl)

=============================
API technical documentation
=============================

This page goes into the technical documentation of our API. 

The Lizard REST API is used to interact with Lizard data and objects. The API enables to collect, export and manage data. With the API, objects and data can be listed, created, (partially) updated and retrieved. Objects and data have different endpoints, to allow specific interactions. 

The endpoints are browseable through the API root view:

- API V3 https://demo.lizard.net/api/v3/

- API V4 https://demo.lizard.net/api/v4/ 


 
Resources are addressable via an URL and can be interacted with via HTTP verbs. The
most commonly used and supported verbs are: 

* GET : retrieve data
* PUT  : change data
* DELETE : delete data
* POST : add data

We also have HEAD and OPTIONS. 

Authentication
==============

When you login via your browser, you get a session-based authentication token that is valid
for 24 hours. All subsequent requests to the API are authenticated with that
token.

Authenticating to the REST API outside of a browser is done by sending
``username`` and ``password`` HTTP header fields with *every* request.


**Example request**:

.. sourcecode:: http

    GET https://demo.lizard.net/api/v3/locations HTTP/1.1
    Host: demo.lizard.net
    username: janedoe
    password: janespw

For all endpoints, users have to be ``admin`` in the organisation that owns the
data to create or update resources.
See :doc:`b_auth` for more information about roles and permissions.

Supported data formats
======================

The data formats supported depend on the endpoint, although
JSON is generally available. See documentation on the individual endpoints
for specifics.

The format of responses can be controlled by specifying an ``Accept`` header
in requests, e.g. Accept: application/json. When posting data, the
format of the payload must be specified via a ``Content-Type`` header, e.g.
Content-Type: text/csv.

When interacting with the API via a browser, the ``format`` query parameter
may also be used for controlling the format of the response, for example:

www.demo.lizard.net/api/v3/timeseries/?format=json

Common variables
================

In this section, query parameters and response fields applicable to all
endpoints are described.

Query parameters
----------------


The API supports the following common query parameters on :http:method:`GET` list requests:

.. http:get:: /<endpoint>/?page=(int:offset)&page_size=(int:size)

   :query page: offset number; default is 0.
   :query page_size: limit number of entries returned; default is 10.


   
Response fields
---------------

All list responses share the following fields.

 *  **count:** number of results for this page
 *  **next:** url to next page, `null` if last page
 *  **previous:** url previous page, `null` if first page
 *  **results:** array with actual results

These fields are not specifically mentioned in the response description of each endpoint.


.. _search_endpoint:

Search
======

This section describes how the search endpoint can be used.

.. _search_base_parameters:


**Example requests**::

	GET https://demo.lizard.net/api/v3/search/?q=water
	GET https://demo.lizard.net/api/v3/search/?type=assetgroup,eventseries
	GET https://demo.lizard.net/api/v3/search/?exclude=ef34gh3
	GET https://demo.lizard.net/api/v3/search/?q=water&in_bbox=4.6,52.1,5.2,52.5&srid=4326
	GET https://demo.lizard.net/api/v3/search/?q=water&point=POINT (5 53)&dist=10000
	
Query parameters
----------------

This API endpoint supports the following parameters on :http:method:`GET` requests:

.. http:get:: /search/?query=input

	:query q: Full-text search filter limited to: bridges, culverts, groundwater stations, levees, levee cross sections, measuring stations, monitoring wells, pressure pipes, pump stations, sluices, waste water treatment plants, and weirs. A search query filter should at least contain two characters.
	:query in_bbx: comma-separated string of a bounding-box, of the form: "xmin,ymin,xmax,ymax".
	:query dist: Distance in meters.
	:query point: Point geometry (either WKT or GeoJSON).
	:query srid: Spatial Reference System Identifier.
	:query type: Comma-seperated list of entity types. Currently the only way to search for layer metadata is by explicitly requesting those entities: type=rasterstore,scenario,assetlayer. It may also be used to limit search results to specific types, i.e. type=levees.
	:query exclude: Comma-seperated list of exclude terms. Results are excluded if the url of the resource contains a term. This is done in the viewset so the serializer still respects the requested page_size.

   
Timeseries
==========

This section describes timeseries-related endpoints.


.. _timeseries_endpoint:




.. _timeseries_base_parameters:


    **Example request:**



        GET  https://demo.lizard.net/api/v3/timeseries/f1f20885-b09b-40fa-a717-1bfd4dffa60e/
		
		
	**Example response:**
	    	
		.. image:: /images/api5.JPG

	

Locations
==========

This section describes location-related endpoints.


.. _locations_endpoint:



    **Example request:**

        GET https://demo.lizard.net/api/v3/locations/6eb648bf-c5a4-4566-ac7a-1311ec69921c/
		
	**Example response:**
	    	
		.. image:: /images/api6.JPG

    
