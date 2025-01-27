.. include:: global.roles

.. _xmlelem-VersionControl: lelabel=VersionControl

Configuration version control
=============================

All XML configuration files must contain version control element node where user can enter a unique number to 
control configuration file version along with file creation date and time. Each configuration file has its own version
number and it is not related to any other XML files. If particular XML file is being modified by web configuration tool, 
the version number is automatically incremented by 1 and modification date and time is recorded.

Version control node must have 3 attributes :ref:`xmlattr-versioncontrolconf`; :ref:`xmlattr-versioncontroldate`; :ref:`xmlattr-versioncontroltime` please see the sample below.

.. code-block:: none

   <VersionControl conf="4" date="2014-01-18" time="10:08:09"/>


VersionControl attributes
-------------------------

.. field-list-table:: VersionControl attributes
   :class: table table-condensed table-bordered longtable
   :name: tabid-VersionControl
   :spec: |C{0.1}|C{0.25}|S{0.65}|
   :header-rows: 1

   * :attr,10,center:	Attribute
     :val,15,center:	Values or range
     :desc,75:		Description

   * :attr:	:xmlattr:`conf`
     :val:	0.01...65535
     :desc:	User assigned version number of the particular XML file. Number will be automatically incremented by 1 when particular XML file is being modified by web configuration tool.

   * :attr:	:xmlattr:`date`
     :val:	date notation YYYY-MM-DD
     :desc:	Date when particular configuration file was created or modified.

   * :attr:	:xmlattr:`time`
     :val:	time notation HH:MM:SS
     :desc:	Time when particular configuration file was created or modified.

.. important:: All attributes are mandatory.
