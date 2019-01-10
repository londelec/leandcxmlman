
.. _docref-TimeZoneSpecification:

Time Zone specification
=======================

It is possible to adjust incoming and outgoing message timestamps in case if |leandcunit| communicates to
the peer station that uses a different time zone. Conventionally timezone and DST information is kept in the
so-called 'Time Zone Database' that consists of a set of TZ format files, these are published and maintained by
the Internet Assigned Numbers Authority (IANA), please refer to their website
(http://www.iana.org/time-zones) for more information. In general there is a TZ file for each country in the world
where information related to DST and other time adjustments is recorded. These files can be found in LEANDC
operating system directory:

\ */usr/share/zoneinfo*

leandc firmware will attempt to locate a TZ file matching the name specified in a :xmlref:`TimeZone` attribute in this
system folder. If a matching file is not found, leandc firmware will use System default time zone which means the
timestamps for the particular communication protocol instance will not be adjusted. Please find the list of most
commonly used time zones below:

.. code-block:: none

   <TimeZone>UTC</TimeZone>
   <TimeZone>Europe/Riga</TimeZone> 
   <TimeZone>Europe/London</TimeZone>
   
If required the System default time zone can be changed as described in |sshmanual| section
'*Change Leandc operating system time zone*'. The System default time zone is used for maintaining internal time of the
|leandcunit|. Internal time is used for time synchronization, time-stamping logfile records, creating logfile
names, etc.
