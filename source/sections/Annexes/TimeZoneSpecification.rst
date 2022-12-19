
.. _docref-TimeZoneSpecification:

Time Zone specification
=======================

It is possible to adjust incoming and outgoing message timestamps in case |leandcapp| communicates to a station that uses a different time zone.
Conventionally timezone and Daylight Saving Time (DST) information is kept in the so-called 'Time Zone Database' that consists of a set of TZ format files.
These files are published and maintained by the Internet Assigned Numbers Authority (IANA), please refer to their website (http://www.iana.org/time-zones) for more information.
In general there is a TZ file for each country in the world where information related to DST and other time adjustments is recorded.
These files can be found in the |linuxos| directory:

\ */usr/share/zoneinfo*

|leandcapp| will attempt to locate a TZ file matching the name specified in a :ref:`xmlattr-IEC101maTimeSettingsTimeZone` attribute in this system directory.
If a matching file is not found, |leandcapp| will use System default time zone which means timestamps of a particular communication protocol instance will not be adjusted.
Please find the list of most commonly used time zones below:

.. code-block:: none

   <TimeZone>UTC</TimeZone>
   <TimeZone>Europe/London</TimeZone>
   <TimeZone>Europe/Riga</TimeZone>
   
System default time zone can be changed as described in |sshmanual| section '*Change Leandc operating system time zone*'.
The System default time zone is used for maintaining internal time of the |opsystem|.
Internal time is used for time synchronization, time-stamping logfile records, creating logfile names, etc.
