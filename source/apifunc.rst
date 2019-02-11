==============================
API functional documentation
==============================

You can acces the Lizard API via “www.{your_organisation}.lizard.net/api/”.

.. image:: /images/api.JPG

What is an API?
-----------------

API stands for Application Programming Interface. 
The API, looking like the picture above, gives back timeseries, rasters, or other data or information. This is depending on the request you do to the API. This request comes from the URL you type in the browser. You can also access the API via another program, and make automatic requests.


Basic use API
--------------

Below we discuss a basic request to the API. More examples and possibilities will be discussed in the :doc:`apitech`.

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
---------

We have noticed that our users are increasingly making use of the API. To prevent failure of the applications of customers, scripts and Excel connections, we have decided to release new features according to the format below:


* API v2: depricated
* API v3: stable
* API v4: experimental


From now on, the API v2 is deprecated. This means that this API will disappear when the development of API v5 starts, which will be around the end of this year. API v3 will be the stable version of API. We will no longer be updating this version. We are using the experimental version, v4, to develop new features.

We will be organising API masterclasses this year, where any user who wants to increase or maintain his or her knowledge can participate. 


Contact
---------

If you have additional questions about the use of the API, please look in * :doc:`apitech` or contact our servicedesk (servicedesk@nelen-schuurmans.nl)