======
Alarms
======

Lizard provides an alarm feature that sends notifications via sms or email when newly processed values of timeseries or temporal rasters exceed a threshold.
It is used to notify people of events that may require action, for instance an upcoming rain event or flood.

The alarm management screens are found at https://demo.lizard.net/management/#/alarms.

.. image:: /images/f_alarms_01.jpg

The configuration has a variety of options to generate relevant notifications with messages that include the specifics of the event. 

Notifications
=============

Behind the Notifications tile you find the overviews of existing raster and timeseries alarms for your organisation and their status (active/inactive).
The 'NEW ITEM' button leads you to the form to register a new alarm.
We go through some of the options that the system provides, to explain them in detail.

Selecting a raster
------------------

Raster alarms are set on temporal rasters. These can be part of a scenario, a single source raster or a Geoblock.
An alarm is set for one point location intersecting this temporal raster.

You can type in the field to search in the names of available rasters. Next, select the type of intersection (Point, Line or Polygon).
Draw the geometry on the map or insert a geometry in the JSON field below the map.

For Line and Polygon intersections a spatial aggregation is needed to derive a timeseries that can be compared to the alarm thresholds.
The options are:

* Sum
* Mean
* Min
* Max
* Median
* Count

Selecting a timeseries
----------------------

Timeseries often do not have a clear name or code by themselves.
That is why we start with looking up the asset it relates to.
Once the asset is selected it should be easy to select the timeseries from the list of related objects.

Relative start and end
----------------------

The user doesn't always want to receive alarms for the whole period of newly processed data.
For instance, for operational flood models which might have records of prior theshold exceedances, you may only be interested in receiving alarms for forecasted threaths.

To only analyse the relevant part of your data you can set relative start and end.
They are set relative to The figure below gives a schematic overview of how this method works.

.. image:: /images/f_alarms_02.jpg

If these fields are left empty the trigger check is done on the complete data frame of newly processed data.

Snoozing option
---------------

It can be considered undesirable for alarms to be triggered during brief spikes.
The snoozing option allows the user to determine the timeperiod a threshold should be exceeded before the alarm is triggered and a notification is sent.
This option is available for both the raising of the alarm and its withdrawal. Default is 1 (trigger at first occurrence). 

Contacts and Groups
===================

The recipients of alarm notifications are configured in the Contacts screen, with their phone number and/or email address.
Each contact can be part of multiple Groups, which in turn can be used in multiple alarms.
So no need to do a whole lot of data duplications of contact info.

Templates
=========

The notification messages are configured with Templates.
There is a difference in setting up Email and SMS Templates:

* Email: Supports both plain text and HTML and are not limited in length
* SMS: Plain text with maximum length of 160 characters (after substitution of variables)

You can use a number of variables to enrich the content of the notifications and make them applicable to different alarms.
The variables contain options for including the name of the receiver and details about the alarm at hand.

The option "No further impact" determines that a message is used specifically to notify when an alarm is fully withdrawn.
This type of message can be set in addition to a standard message to let receivers know that the situation has settled down.
This often requires a different text and therefore a different Template.
