.. _AuthenticationAnchor:

==========
Signing in
==========

Users that already have a Lizard account can click the "Log in"
button on the top right of the screen.

First-time users require an invitation to create a Lizard account. Users with
a "manager" role are able to send invitations to new users.
If you do not know whom to contact, please contact our support office
(servicedesk@nelen-schuurmans.nl).

After clicking "Log in" or after following the invitation link, you will arrive
at the login screen.

.. note::
    Please ensure that "https://auth.lizard.net/" domain is indeed displayed
    in your browser's address bar and that your browser displays the lock
    symbol indicating that the connection is secure.

On the login page you have four different options to sign in:

1. through a company account,
2. trough a social account,
3. with username and password,
4. by creating a new account (Sign up).

First-time users may choose any of these options. If your company is listed as
one of the possible companies to sign in with, that is the preferred choice.

Existing users should use the same method as they used when signing in for 
the first time. If your Lizard username/password existed before Januari 2021,
use method 3.

.. tip::
    Do you want to add your company to the list to centralise the user accounts
    of your organisation? Please contact our support office
    (servicedesk@nelen-schuurmans.nl) for the options.


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



Whitelisting
============

The users of a certain portal may not be interested in a lot of the public/common datasets that are made available by others.
An organisation can determine data of which other organisations is visible in their Lizard API and portal.
This is configured by whitelisting the organisations that are allowed to show their data per portal.

The effect is that for the same user the available data can differ between e.g. [your_organisation].lizard.net and demo.lizard.net (for which all organisations are whitelisted).
The whitelisting mechanism is overruled if a user has specific authorisation for an organisation.

.. tip::
    Do you want to see or change the whitelist settings of a portal? Please contact our support office
    (servicedesk@nelen-schuurmans.nl).

=====
Roles
=====

We have 4 roles and 3 different types of privileges. 

* A **user**, who can only *read* data
* A **supplier**, who can *read* data and change (*'write'*) his or her own data
* An **administator**, who can *read* data and change (*'write'*) all organisation's data. 
* A **manager**, who can *manage* other roles in the organisation. A manager can not read or write data by default. This role should be appointed separately. 


===============	
User management
===============

Users can be managed in the User Management interface.
This interface can be reached via the {yourorganisation}.lizard.net/management/users/ (or `demo.lizard.net/management/users <https://demo.lizard.net/management/users>`_).

.. note::
    You require a “manager” role to access the User Management interface.
    Haven’t got a “manager” role but you would like to add the User Management interface?
    Please contact the application manager within your organisation or our support office (servicedesk@nelen-schuurmans.nl)
	
.. image:: /images/b_usermanagement_03.png

In the example above, you see the current rights for 7 users under the organisation Nelen & Schuurmans. 
	
Manage existing users
=====================

The User Management interface gives you an overview of all users that have roles for your organisation.
If you are Manager for multiple organisations you can switch organisation using the button in the dark green bar. You can change the role of a user by clicking the “three dots" next to the user and choose the roles you want to assign. Then click “Save” to make the changes. 

Adding a new user
=================

You can add a new user by clicking the “NEW ITEM” icon in the upper right corner.

.. image:: /images/c_manage_newitem.png

This will lead you to the screen to add a new user.

.. image:: /images/b_usermanagement_04.png

By default the new user is granted a “User” role. At least one role is required when invite a new user.  
Do not forget to click ‘Save’! When saved, an invitation email will be sent to the new user.
This user can follow the invitation link to (if necessary) create an account and receive the new roles.
The user will appear in the user management overview once they accepted the invite and created the account.

.. note::
    Sometimes this invitation mail will end up in the spam folder. 

.. note::
    The invitated user is required to sign in with the email address that is supplied by the manager. This email address can't be changed later on. 

.. note::
	Deselect all roles will remove the user from the organisation but will not delete the user's account.

.. note::
	You cannot remove your own manager role.	
	
.. tip::
	Click on 'Pending Users', to see who have not completed the acitvation process yet. 	

