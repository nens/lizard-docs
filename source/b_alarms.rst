==========
Alarms
==========

The Lizard Alarms are a powerful feature designed to provide real-time notifications and alerts based on user-defined criteria. 
This system enables users to monitor various environmental conditions, ensuring timely responses to critical events.


Submenus
==========
An alarm is set-up using multiple submenu's:

* Contacts
* Groups
* Templates
* Notifications 

1. Contacts

In the contacts menu, you can list names and add telephone numbers or email adresses for 
respectively SMS and email alarm notifications.

2. Groups

In the Groups menu, you can set up contacts to be grouped for receiving alerts. Note that only contact groups can be assigned to an alarm. If you want to send messages to a single contact, you need to assign that contact to a group with just one member.

3. Templates

In the templates map the alarm messages are set-up. Here you can configure specific messages using dynamic variables like
names, specific rain variables, timestamps and more. 

4. Notifications

The Notifications tab is where you configure the alerts and bring everything together.  
First you have to choose on what type of data the alert is connected:

* Raster alarms
* Time series alarms

To set up an alarm, choose the raster or time series you are interested in by searching for and selecting the object name. When selecting a raster alarm, you need to define measuring points using longitude-latitude coordinates (note that we specifically use the order longitude-latitude, not latitude-longitude).

The "Limit to relative period" setting determines what selection of the data is used for alerts. If switched off, alarms are triggered whenever new data is added. If switched on, you can configure alerts to only be triggered by near-future events, which is useful for avoiding alerts when adding new historical data.

After selecting the location and data, you can apply multiple boolean expressions to define the conditions for triggering alarms. You can also enter specific threshold values.

For more varying measurements, there is a snooze button that allows you to trigger an alarm only after a threshold has been met or withdrawn a certain number of times.

Finally, you can select the specific contact group (as defined in Groups) and the template message (as defined in Templates) for the alarm.