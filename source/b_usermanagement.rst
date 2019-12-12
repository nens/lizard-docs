.. _OrganisationsAnchor:

=============
Organisations
=============

All data in Lizard is linked to an organisation.
Organisations are the backbone of our authorisation model.
There are three types of authorisation options that can be applied to your data: 

* **Public**: everyone can see your data 
* **Common**: everyone with login credentials to Lizard can see your data 
* **Private**: everyone with login credentials to Lizard AND user rights to your organisation can see your data

.. image:: /images/b_usermanagement_01.png

=====
Roles
=====

We have 4 roles and 3 different types of privileges. 

1. A **user**, who can only *read* data
2. A **supplier**, who can *read* data and change (*'write'*) his or her own data
3. An **administator**, who can *read* data and change (*'write'*) all organisation's data. 
4. A **manager**, who can *manage* other roles in the organisation. A manager can not read or write data by default. This role should be appointed separately. 

.. image:: /images/b_usermanagement_02.png

===============	
User Management
===============

Users can be managed in the User Management interface.
This interface can be reached via the {yourorganisation}.lizard.net/management/users/ (or `demo.lizard.net/management/users<https://demo.lizard.net/management/users>`).

.. image:: /images/b_usermanagement_03.png

.. note::
    You require a “manager” role to access the User Management interface.
    Haven’t got a “manager” role but you would like to add the User Management interface?
    Please contact the application manager within your organisation or our support office (servicedesk@nelen-schuurmans.nl)
	
Manage Existing users
=====================

The User Management interface gives you an overview of all users that have roles for your organisation.
If you are Manager for multiple organisations you can switch organisation using the button in the dark green bar. You can change the role of a user by clicking the ““ button and choose the roles you want to assign. Then click “Save” to make the changes. 

Adding a new user
=================

.. image:: /images/b_usermanagement_04.png

You can add a new user by clicking the “NEW USER” in the upper right corner.
This will lead you to the screen to add a new user.
By default the new user is granted a “User” role. 

Don’t forget to click ‘Save’! When saved, an activation email will be send to the new user (sometimes this activation mail will end up in the spam folder). 


.. tip::
	Forgot which Roles exist and what they grant a user? Click the “Need Help” button to find this overview:  
.. image:: /images/b_usermanagement_05.png

.. tip::
    In order to keep your users organised, we advise you to choose the username based on the users’ email address.
    Use everything before the @email.com, or the format {firstname.lastname}.