=============================
API technical documentation
=============================

This page goes into the technical documentation of our API. 

The Lizard REST API is used to interact with Lizard data and objects.
The API enables to collect, export and manage data.
With the API, objects and data can be listed, created, (partially) updated and retrieved.
Objects and data have different endpoints, to allow specific interactions. 

The endpoints are browseable through the API root view:

- API V3 https://demo.lizard.net/api/v3/ (stable)

- API V4 https://demo.lizard.net/api/v4/ (experimental)
 
Resources are addressable via an URL and can be interacted with via HTTP verbs. The
most commonly used and supported verbs are: 

* GET : retrieve data
* PUT  : change data
* DELETE : delete data
* POST : add data

We also have HEAD and OPTIONS. 

.. _APIAuthenticationAnchor:

Authentication
==============

When you login via your browser, your browser receives a session cookie.
All subsequent requests to the API are authenticated with that session cookie.

Authenticating to the REST API outside of a browser is done by attaching a
Personal API Key to *every* request. You can attach a Personal API Key to 
a request by using HTTP Basic Authentication with password = {your api key}.
The username needs to be fixed to ``__key__`` (with double underscores on both
sides of the word "key").

Almost all applications or script languages support HTTP Basic Authentication.
See below for some examples.

Generate a Personal API key at https://demo.lizard.net/management/.
It is considered best practise to generate one Personal API Key per application
or script, so that you can selectively revoke keys in case they are compromised.

Examples
--------

Python requests
~~~~~~~~~~~~~~~

With Python, we recommend using the ``requests`` package. Supply your API Key
in the ``auth`` parameter, as follows:

.. code-block:: python
   import requests

   url = "demo.lizard.net/api/v3/locations"
   my_secret_key = "abcdefg.01234567890"  # Example
   
   response = requests.get(url, auth=("__key__", my_secret_key))


Postman
~~~~~~~

In Postman you can set up HTTP Basic Authentication as shown in the image below.
Be sure to choose "Basic Auth" as Type, and not "API Key".

.. image:: /images/c_apitechnical_03.jpg


Applications: OAuth2
--------------------

Applications (such as dashboards) that use the Lizard API should authenticate
using OAuth2. For this, you will need a registration. Contact our servicedesk to
request one.


Legacy: username / password
---------------------------

Lizard supports authenticating by attaching ``username`` and ``password`` to
every request, either directly in Username and Password headers, or using 
HTTP Basic Authentication. This legacy authentication does generate a session.

.. warning::
	This form of authentication will be deprecated on *June 1st, 2021*. Ensure
	that your applications and scripts use new API Keys after that date.

In the period until June 1st, 2021, correct username / password combinations
will be migrated automatically to a Personal API Key, in such a way that
you may keep using the same username / password combination. Password changes
will however not be reflected anymore in the migrated API Key.


Authorisation
=============

For all endpoints, users have to be ``admin`` in the organisation that owns the
data to create or update resources.
See :doc:`b_usermanagement` for more information about roles and permissions.

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
	    	
		.. image:: /images/c_apitechnical_01.jpg

Locations
==========

This section describes location-related endpoints.

.. _locations_endpoint:

    **Example request:**

        GET https://demo.lizard.net/api/v3/locations/6eb648bf-c5a4-4566-ac7a-1311ec69921c/
		
	**Example response:**
	    	
		.. image:: /images/c_apitechnical_02.jpg