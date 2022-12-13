=============================
API technical documentation
=============================

This page goes into the technical documentation of our API. 

The Lizard REST API is used to interact with Lizard data and objects.
The API enables to collect, export and manage data.
With the API, objects and data can be listed, created, (partially) updated and retrieved.
Objects and data have different endpoints, to allow specific interactions. 

The endpoints are browseable through the API root view:

- API V3 https://demo.lizard.net/api/v3/ (deprecated)

- API V4 https://demo.lizard.net/api/v4/ (stable)
 
Resources are addressable via an URL and can be interacted with via HTTP verbs. The
most commonly used and supported verbs are: 

* GET : retrieve data
* PATCH/PUT  : change data
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

   url = "demo.lizard.net/api/v4/locations"
   my_secret_key = "abcdefg.01234567890"  # Example
   
   response = requests.get(url, auth=("__key__", my_secret_key))


Postman
~~~~~~~

In Postman you can set up HTTP Basic Authentication as shown in the image below.
Be sure to choose "Basic Auth" as Type, and not "API Key".

.. image:: /images/c_apitechnical_03.png


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
	This form of authentication has been deprecated on *June 1st, 2021*. Ensure
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

https://demo.lizard.net/api/v4/timeseries/?format=json

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

Timeseries
==========

This section describes timeseries-related endpoints.

.. _timeseries_endpoint:

.. _timeseries_base_parameters:

    **Example request:**

        GET  https://demo.lizard.net/api/v4/timeseries/1bcba36e-781d-4339-9632-00d5398c3b15/
		
	**Example response:**
	    	
		.. image:: /images/c_apitechnical_01.jpg

Locations
==========

This section describes location-related endpoints.

.. _locations_endpoint:

    **Example request:**

        GET https://demo.lizard.net/api/v4/locations/faa84a55-cb8d-460c-a8b8-18d2b59da28c/
		
	**Example response:**
	    	
		.. image:: /images/c_apitechnical_02.jpg