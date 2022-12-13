==============================
API functional documentation
==============================

You can access the Lizard API via “{your_organisation}.lizard.net/api/v4/”.

.. image:: /images/c_apifunctional_01.jpg

What is an API?
===============

API stands for Application Programming Interface. 
The API, looking like the picture above, gives back timeseries, rasters, or other data or information.
This is depending on the request you do to the API.
This request comes from the URL you type in the browser.
You can also access the API via another program, and make automatic requests.

Basic use API
=============

Below we discuss a basic request to the API.
More examples and possibilities will be discussed further down

The basic url is www.{your_organisation}.lizard.net/api/v4, for example:
 www.demo.lizard.net/api/v4 

If you type this in your browser, for example Google Chrome, you will get a list of parameters.
These parameters are so called *endpoints*.
If you paste this endpoint after your basic url, you will initiate a query.
An example is ``locations``. 
If you click on the url www.demo.lizard.net/api/v4/locations , you will send a query to Lizard to search all locations that you have access to.
As a response, you will get indeed the locations back, as well as some metadata. 

.. image:: /images/c_apifunctional_02.jpg

Above each page, you will see some additional parameters, with which you can specify your query more.
Most endpoints have examples of this.

.. image:: /images/c_apifunctional_03.jpg

If we are looking for a specific location, with a name that starts with 'Inlaat', we can use this query:

https://demo.lizard.net/api/v4/locations/?name__startswith=Inlaat

If you are an administrator or supplier of the data, you can also edit or delete the data via the API. 	

Versions
========

We support two versions of our API:

* API v3: deprecated (sunset date: 15 May 2023)
* API v4: stable


API V3 will be taken offline by 15 May 2023. Any use in scripts or applications should be reimplemented in API V4.
API V4 is the stable version. We can make changes to this version, but they should always be backwards compatible and therefore not break any existing use.

Digitale Delta API
------------------

De Nederlandse watersector staat voor de opgave om in een snel veranderende omgeving haar informatievoorziening te transformeren en klaar te maken voor de toekomst.
De Digitale Delta is het open platform voor het aanbieden en vinden van relevante data voor het waterbeheer in Nederland.
Lizard spreekt Digitale Delta en is een van de dataleveranciers binnen de Digitale Delta.
De Digitale Delta API Root is te vinden op https://demo.lizard.net/dd/api/v2

De documentatie van de Digitale Delta API is te vinden op:  
https://github.com/DigitaleDeltaOrg/dd-api-spec/blob/master/README.md

Contact
=======

If you have additional questions about the use of the API contact our servicedesk (servicedesk@nelen-schuurmans.nl)