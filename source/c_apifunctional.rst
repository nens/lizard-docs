==============================
API functional documentation
==============================

You can acces the Lizard API via “{your_organisation}.lizard.net/api/v3/”.

.. image:: /images/c_apifunctional_01.jpg

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

.. image:: /images/c_apifunctional_02.jpg

Above each page, you will see some additional parameters, with which you can specify your query more. Most endpoints have examples of this.

.. image:: /images/c_apifunctional_03.jpg

If we are looking for a specific location, with a name that contains 'gemaal', we can use this query:

www.demo.lizard.net/api/v3/locations/?name__icontains=gemaal

.. tip::
	icontains means that the name does not have to match exactly. 

If you are an administrator or supplier of the data, you can also edit or delete the data via the API. 	

Versions
========

We support three versions of our API:

* API v2: depricated
* API v3: stable
* API v4: experimental

The API V2 is deprecated and we advise not to use this API for developing purposes.
API V2 will disappear in the near future.
API V3 is the stable version of API and can be used for developing purposes.
API V4 can be used in cooperation with our dev-team.
API V4 is used to de

Digitale Delta API
------------------

De Nederlandse watersector staat voor de opgave om in een snel veranderende omgeving haar informatievoorziening te transformeren en klaar te maken voor de toekomst.
De Digitale Delta is het open platform voor het aanbieden en vinden van relevante data voor het waterbeheer in Nederland.
Lizard spreekt Digitale Delta en is een van de dataleveranciers binnen de Digitale Delta.
De Digitale Delta API Root is te vinden op https://demo.lizard.net/dd/api/v1 

De documentatie van de Digitale Delta API is te vinden op:  
https://github.com/DigitaleDeltaOrg/dd-api-spec/blob/master/README.md


Contact
=======

If you have additional questions about the use of the API contact our servicedesk (servicedesk@nelen-schuurmans.nl)