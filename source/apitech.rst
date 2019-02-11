
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
See :doc:`users` for more information about roles and permissions.

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


.. _search_base_parameters:


.. autoclass:: lizard_nxt.views.search.SearchViewSet
    :noindex:

    **Example request:**

    .. sourcecode:: http
	
    **Example request:**

        GET https://demo.lizard.net/api/v3/search/ 

   
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

    
