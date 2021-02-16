======
Alarms
======

Lizard provides an alarm option via sms or email on both rasters and timeseries.
The alarms can be configured in https://demo.lizard.net/management/#/alarms.

.. image:: /images/d_alarms_01.png

If a value in timeseries or intersection of a temporal raster is exceeding a threshold value, an alarm will be triggered and contact groups will receive a notification. 

The Management System is used to define who receives which notifications, including the configuration of which persons will receive each alarm,
with what text, and whether that is by SMS, email or both.  

Notifications
=============

In the Notifications tile, you see the configured raster and timeseries alarms and new alarms can be configured.

New raster alarms
-----------------

A raster alarm can be set, by giving input to the following values:

* The name of the alarm
* The raster layer for which the alarm applies (e.g. rainfall or water level)
* The X-Y coordinates to which the alarm applies (by pinpointing a location on the map)
* The threshold level (in the unit of the data, e.g. mMSL)
* The recipients

An alarm can check only in one direction, either series going above or below certain thresholds. One or more thresholds can be defined per alarm.
The alarm receives the status of the highest or lowest threshold that is crossed within the period that is analysed.

New timeseries alarms
----------------------

A timeseries alarm can be set, by giving input to the following values:

* The name of the alarm
* The timeseries for which the alarm applies (e.g. rainfall or water level)
* The thresholds (i.e. trigger levels (in m, AHD) for water levels or rainfall depth  in mm for rainfall)
* The recipients

An alarm can check only in one direction, either series going above or below certain thresholds.
One or more thresholds can be defined per alarm.
The alarm receives the status of the highest or lowest threshold that is crossed within the period that is analysed. 

Groups and contacts
===================

The recipients can be added to a Group or new Groups can be created.
By making use of groups, it is not necessary to type in all email addresses and phone numbers for each new alarm.
New users can be added in the user management interface (https://demo.lizard.net/management/users/) 

Templates
=========

In the Templates tile, the message that is send by email or sms can be configured.
There are a couple of variables that can be included in the text to send dynamic messages with the latest status of the alarm.