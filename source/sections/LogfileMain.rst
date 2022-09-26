.. include:: global.roles

.. _xmlgroup-Logfiles: lelabel=SystemConfig

Logfiles
========

Leandc features a raw communication traffic and decoded application level information recording
to logfiles for supervision and maintenance purposes. Fixed name XML configuration file |leloggerxml|
contains settings to enable logfiles. This file must be kept in the same directory as |leandcxml|
file. Its path and name can't be changed.

|leloggerxml| configuration file consists of a root object node :ref:`xmlgroup-Logfiles` which has 3 optional child group
object nodes :ref:`xmlelem-VersionControl`; :ref:`xmlgroup-CommsCfg`; :ref:`xmlgroup-EventCfg`, please see the sample below.

.. code-block:: none

   <SystemConfig xmlns="http://www.londelec.com/xmlschemas/leandc/lelogger" … version="1.00">
         <VersionControl conf="4" date="2014-01-18" time="10:08:09"/>
         <CommsCfg>
            <LOGGER Index="6" LogFlags="0x7F" Logfile="Log/ma2"/>
            …
            <HWLOG HWIndex="1" LogFlags="0x06" Logfile="Log/COM1" Mode="0x00" HourLimit="0"/>
            …
            <PCAPLOG HWIndex="1" LogFlags="0x07" Logfile="Log/trace" Mode="0x00" HourLimit="0"/>
         </CommsCfg>
         <EventCfg>
            <EVENTLOG Index="104" LogFlags="0x3F" HourLimit="0" Logfile="Events/SL104_1"/>
            …
         </EventCfg>
   </SystemConfig>

.. tip::
   | |leloggerxml| configuration file is optional and leandc is able to run normally without it.
   | Node names are case sensitive.

.. _xmlgroup-CommsCfg: lelabel=CommsCfg
.. _xmlelem-CommsHWlog: lelabel=HWLOG
.. _xmlelem-CommsLogger: lelabel=LOGGER

LOGGER and HWLOG nodes
----------------------

:ref:`xmlelem-CommsLogger` and :ref:`xmlelem-CommsHWlog` nodes contain settings for raw communication traffic logging and these nodes are children of :ref:`xmlgroup-CommsCfg` group node.
Following functionality is available:

* Record all raw traffic over a serial/Ethernet interface - :ref:`xmlelem-CommsHWlog` node;
* Filter and record traffic related to a specific communication protocol instance - :ref:`xmlelem-CommsLogger` node;

Configuration may contain both nodes at the same time in any combination.
However only 1 logfile per protocol instance and 1 logfile per hardware interface is allowed.

Please see sample :ref:`xmlgroup-CommsCfg` group node and :ref:`xmlelem-CommsLogger` and :ref:`xmlelem-CommsHWlog` child element nodes below.
The sample below shows 2 logfiles for recording filtered traffic related to particular communication protocol instance and 1 logfile for recording all traffic over a serial interface.

.. code-block:: none

   <CommsCfg>
      <LOGGER Index="5" LogFlags="0x06" Logfile="Log/serial101" Mode="0x00" HourLimit="4"/>
      <LOGGER Index="6" LogFlags="0xFF" Logfile="Log/tcpserv104"/>
      <HWLOG HWIndex="1" LogFlags="0x06" Logfile="Log/COM1" Mode="0x00" HourLimit="0"/>
   </CommsCfg>

Please see all available attributes of the :ref:`xmlelem-CommsLogger` and :ref:`xmlelem-CommsHWlog` nodes below:

.. code-block:: none

   <LOGGER Index="5" LogFlags="0xFF" Logfile="Log/serial101" Mode="0" HourLimit="4" TimeZone="Europe/Riga" Name="IED logfile" />
   <HWLOG HWIndex="1" LogFlags="0x06" Logfile="Log/COM1" Mode="0" HourLimit="4" TimeZone="UTC" Name="COM port logfile" />

.. tip:: Attributes can be arranged in any order, it will not affect the XML file validation.

LOGGER and HWLOG attributes
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include-file:: sections/Include/table_attrs.rstinc "" "tabid-CommsLogger" "LOGGER and HWLOG attributes" ":spec: |C{0.12}|C{0.12}|C{0.1}|S{0.66}|"

   * :attr:	:xmlattr:`Index`
     :val:	|gpindexrange|
     :def:	n/a
     :desc:	Attribute is used to enable logging for a specific communication protocol instance.
		Use value of the :ref:`xmlattr-gp101maIndex` attribute of any communication protocol instance to enable logging.
		:inlineimportant:`Attribute is mandatory for` :ref:`xmlelem-CommsLogger` :inlineimportant:`node and must not be used for` :ref:`xmlelem-CommsHWlog` :inlineimportant:`node.`
		:inlinetip:`Indexes don't have to be in a sequential order.`

   * :attr:	:xmlattr:`HWIndex`
     :val:	|hwindexrange|
     :def:	n/a
     :desc:	Attribute is used to enable logging for a hardware node.
		Use value of the :ref:`xmlelem-uart`.\ :ref:`xmlattr-UARTIndex` \; :ref:`xmlelem-tcpserver`.\ :ref:`xmlattr-TCPSERVERIndex` \; :ref:`xmlelem-tcpclient`.\ :ref:`xmlattr-TCPCLIENTIndex` \ or :ref:`xmlelem-udp`.\ :ref:`xmlattr-UDPIndex` \ attribute to enable logging.
		:inlineimportant:`Attribute is mandatory for` :ref:`xmlelem-CommsHWlog` :inlineimportant:`node and must not be used for` :ref:`xmlelem-CommsLogger` :inlineimportant:`node.`
		:inlinetip:`Indexes don't have to be in a sequential order.`

   * :attr:	:xmlattr:`LogFlags`
     :val:	|flags8range|
     :def:	0x00
     :desc:	Select type of the messages to be logged.
		See :numref:`tabid-CommsLoggerLogFlags` for description.
		Logfile will not be created if the value is 0.

.. include-file:: sections/Include/log_Logfile.rstinc "" ".log" "(sample value 'Log/abc', where 'Log' is the name of the folder and 'abc' is the name of the file)"

.. include-file:: sections/Include/log_ModeHourLimit.rstinc "" "0x00" "4" "(default 4 hours – total of 6 files will be created daily at 00:00, 04:00, 08:00, 12:00, 16:00, 20:00)"

.. include-file:: sections/Include/log_TimeZone.rstinc ""

.. include-file:: sections/Include/hidden_LogDebugFlags.rstinc "internal" ":numref:`tabid-syslogfileDebugFlags`"

.. include-file:: sections/Include/Name.rstinc ""

.. tip:: \* List of files created with various :ref:`xmlattr-CommsLoggerMode` \ and :ref:`xmlattr-CommsLoggerHourLimit` \ attribute settings can be found in section :ref:`docref-LogfileSampleList`.


LOGGER.LogFlags
^^^^^^^^^^^^^^^

.. include-file:: sections/Include/table_flags8.rstinc "" "tabid-CommsLoggerLogFlags" "Communication logfile flags" ":ref:`xmlattr-CommsLoggerLogFlags`" "Communication logger flags"
		Logfile will not be created, if the value is 0.
		Some bits are not used for all communication protocols.
		For those bits applicable protocols are listed.

   * :attr:	Bit 0
     :val:	xxxx.xxx0
     :desc:	| IEC60870-5-101/3 Link layer message recording **disabled**
		| IEC60870-5-104 Transport layer message recording **disabled**

   * :(attr):
     :val:	xxxx.xxx1
     :desc:	| IEC60870-5-101/3 Link layer message recording **enabled**
		| IEC60870-5-104 Transport layer message recording **enabled**

   * :attr:	Bit 1
     :val:	xxxx.xx0x
     :desc:	Incoming message logging **disabled**.
		Applies to IEC60870-5-101/3/4; Modbus and Spabus protocols.

   * :(attr):
     :val:	xxxx.xx1x
     :desc:	Incoming message logging **enabled**.
		Applies to IEC60870-5-101/3/4; Modbus and Spabus protocols.

   * :attr:	Bit 2
     :val:	xxxx.x0xx
     :desc:	Outgoing message logging **disabled**.
		Applies to IEC60870-5-101/3/4; Modbus and Spabus protocols.

   * :(attr):
     :val:	xxxx.x1xx
     :desc:	Outgoing message logging **enabled**.
		Applies to IEC60870-5-101/3/4; Modbus and Spabus protocols.

   * :attr:	Bit 4
     :val:	xxx0.xxxx
     :desc:	Error message recording **disabled**.

   * :(attr):
     :val:	xxx1.xxxx
     :desc:	Error message recording **enabled**.
		These are communication errors arrising from corrupted messages and timeouts.
		Also includes incorrect or unexpected received data.

   * :attr:	Bit 5
     :val:	xx0x.xxxx
     :desc:	| Warning message recording **disabled**.

   * :(attr):
     :val:	xx1x.xxxx
     :desc:	| Warning message recording **enabled**.

   * :attr:	Bit 6
     :val:	x0xx.xxxx
     :desc:	| Informative message recording **disabled**.

   * :(attr):
     :val:	x1xx.xxxx
     :desc:	| Informative message recording **enabled**.
		  These messages include station communication states (ONLINE, OFFLINE, etc.) and bit applies to all protocols. 
		| IEC60870-5-104 [:lemonobgtext:`Started`]; [:lemonobgtext:`Stopped`] messages.
		| IEC61850 underlying layer information messages can be enabled for each particular layer.

   * :attr:	Bit 7
     :val:	0xxx.xxxx
     :desc:	| IEC60870-5-101/3 **don't log** the transmitted message echo (if it exists).
		| IEC61850 Debug message recording **disabled**.

   * :(attr):
     :val:	1xxx.xxxx
     :desc:	| IEC60870-5-101/3 **log** the transmitted message echo (if it exists).
		| IEC61850 Debug message recording **enabled**.

   * :attr:	Bits 3
     :val:	Any
     :desc:	Bits reserved for future use


.. _xmlelem-pcaplog:

PCAPLOG
-------

:ref:`xmlelem-pcaplog` node enables to capture traffic through a specific or any Ethernet interfaces in a pcap format.
:ref:`xmlelem-pcaplog` node is a child of :ref:`xmlgroup-CommsCfg` group node.

Please see sample :ref:`xmlgroup-CommsCfg` group and :ref:`xmlelem-pcaplog` child element node below.

.. code-block:: none

   <CommsCfg>
      <PCAPLOG HWIndex="1" LogFlags="0x07" Logfile="Log/trace" Mode="0x00" HourLimit="0"/>
   </CommsCfg>

.. important:: Group node :ref:`xmlgroup-CommsCfg` may contain only one :ref:`xmlelem-pcaplog` node. :ref:`xmlelem-pcaplog` must be the last in the group after all :ref:`xmlelem-CommsLogger` and :ref:`xmlelem-CommsHWlog` nodes, if there are any.

Please see all available attributes of the :ref:`xmlelem-pcaplog` node below:

.. code-block:: none

   <PCAPLOG HWIndex="1" LogFlags="0x07" Logfile="Log/trace" Mode="0" HourLimit="4" Filter="vlan 0" Name="pcap trace" />

.. tip:: Attributes can be arranged in any order, it will not affect the XML file validation.

PCAPLOG attributes
^^^^^^^^^^^^^^^^^^

.. include-file:: sections/Include/table_attrs.rstinc "" "tabid-pcaplog" "PCAPLOG attributes" ":spec: |C{0.12}|C{0.12}|C{0.1}|S{0.66}|"

   * :attr:	:xmlattr:`HWIndex`
     :val:	|hwindexrange|
     :def:	n/a
     :desc:	Capture traffic through Ethernet interface used by this Hardware node.
		Use value of the :ref:`xmlelem-tcpserver`.\ :ref:`xmlattr-TCPSERVERIndex` \; :ref:`xmlelem-tcpclient`.\ :ref:`xmlattr-TCPCLIENTIndex` \ or :ref:`xmlelem-udp`.\ :ref:`xmlattr-UDPIndex` \ attribute to enable capture.
		:inlineimportant:`Only one` :ref:`xmlelem-pcaplog` :inlineimportant:`node can be defined.`
		:inlinetip:`Use` :ref:`xmlattr-pcaplogLogFlags` :inlinetip:`attribute to enable capture on all Ethernet interfaces, if required.`

   * :attr:	:xmlattr:`LogFlags`
     :val:	|flags8range|
     :def:	0x00
     :desc:	Capture filter specifications.
		See :numref:`tabid-pcaplogLogFlags` for description.
		Capture is disabled if value is 0.

.. include-file:: sections/Include/log_Logfile.rstinc "" ".pcap" "(sample value 'Log/abc', where 'Log' is the name of the folder and 'abc' is the name of the file)"

.. include-file:: sections/Include/log_ModeHourLimit.rstinc "" "0x00" "4" "(default 4 hours – total of 6 files will be created daily at 00:00, 04:00, 08:00, 12:00, 16:00, 20:00)"

   * :attr:	:xmlattr:`Filter`
     :val:	1...200 chars
     :def:	n/a
     :desc:	Custom capture filter e.g. "vlan 0".
		See pcap-filter(7) manual for more information.

.. include-file:: sections/Include/Name.rstinc ""

.. tip:: \* List of files created with various :ref:`xmlattr-pcaplogMode` \ and :ref:`xmlattr-pcaplogHourLimit` \ attribute settings can be found in section :ref:`docref-LogfileSampleList`.


PCAPLOG.LogFlags
^^^^^^^^^^^^^^^^

.. include-file:: sections/Include/table_flags8.rstinc "" "tabid-pcaplogLogFlags" "Capture filter flags" ":ref:`xmlattr-pcaplogLogFlags`" "PCAP logger flags"
		Capture is disabled if the value is 0.

   * :attr:	Bits 0,1
     :val:	xxxx.xx00
     :desc:	Reserved - don't use.

   * :(attr):
     :val:	xxxx.xx01
     :desc:	Capture traffic through **all** available Ethernet interfaces. Traffic will not be filtered by IP address.

   * :(attr):
     :val:	xxxx.xx10
     :desc:	Capture traffic trough a **single** Ethernet interface, the one used for communication.

   * :(attr):
     :val:	xxxx.xx11
     :desc:	Filter captured traffic by **IP address**. Only messages with matching Source or Destination IP address will be captured.
		Address from :ref:`xmlelem-tcpserver`.\ :ref:`xmlattr-TCPSERVERServerIPaddr` \; :ref:`xmlelem-tcpclient`.\ :ref:`xmlattr-TCPCLIENTServerIPaddr` \ or :ref:`xmlelem-udp`.\ :ref:`xmlattr-UDPRemoteIPaddr` \ attribute is used as a filter.

   * :attr:	Bit 2
     :val:	xxxx.x0xx
     :desc:	Capture filter by port number is **disabled**

   * :(attr):
     :val:	xxxx.x1xx
     :desc:	Capture filter by port number is  **enabled**. Only messages with matching Source or Destination Port number will be captured.
		Port number from :ref:`xmlelem-tcpserver`.\ :ref:`xmlattr-TCPSERVERPort` \; :ref:`xmlelem-tcpclient`.\ :ref:`xmlattr-TCPCLIENTPort` \ or :ref:`xmlelem-udp`.\ :ref:`xmlattr-UDPRemotePort` \ attribute is used as a filter.

   * :attr:	:bitdef:`6`
     :val:	x0xx.xxxx
     :desc:	SSH (TCP/UDP port 22) traffic capture **disabled**

   * :(attr):
     :val:	x1xx.xxxx
     :desc:	SSH (TCP/UDP port 22) traffic capture **enabled**

   * :attr:	Bits 3...5;7
     :val:	Any
     :desc:	Bits reserved for future use


.. _xmlgroup-EventCfg: lelabel=EventCfg
.. _xmlelem-HWeventLog: lelabel=HWEVENTLOG
.. _xmlelem-EventLog: lelabel=EVENTLOG

EVENTLOG and HWEVENTLOG nodes
-----------------------------

:ref:`xmlelem-EventLog` and :ref:`xmlelem-HWeventLog` nodes contain settings for decoded application level information (DI/AI/DO/AO object types, addresses, values, etc) logging and these nodes are children of :ref:`xmlgroup-EventCfg` group node.
Following functionality is available:

* Record all decoded information over a serial/Ethernet interface - :ref:`xmlelem-HWeventLog` node;
* Filter and record decoded information related to a specific communication protocol instance - :ref:`xmlelem-EventLog` node;

Configuration may contain both nodes at the same time in any combination.
However only 1 logfile per protocol instance and 1 logfile per hardware interface is allowed.

Please see sample :ref:`xmlgroup-EventCfg` group node and :ref:`xmlelem-EventLog` and :ref:`xmlelem-HWeventLog` child element nodes below.
The sample below shows 2 logfiles for recording decoded information of a particular communication protocol instance and 1 logfile for recording decoded information over a serial interface.

.. code-block:: none

   <EventCfg>
      <EVENTLOG Index="5" LogFlags="0x3F" Logfile="Events/serial101" HourLimit="0" Mode="0"/>
      <EVENTLOG Index="6" LogFlags="0x0C" Logfile="Events/tcpserv104"/>
      <HWEVENTLOG HWIndex="1" LogFlags="0x40" Logfile="Events/COM1_events" HourLimit="0"/>
   </EventCfg>

Please see all available attributes of the :ref:`xmlelem-EventLog` and :ref:`xmlelem-HWeventLog` nodes below:

.. code-block:: none

   <EVENTLOG Index="5" LogFlags="0xFF" Logfile="Events/101slave" Mode="0" HourLimit="4" TimeZone="Europe/Riga" Name="IED Events" />
   <HWEVENTLOG HWIndex="1" LogFlags="0x06" Logfile="Events/COM1" Mode="0" HourLimit="4" TimeZone="UTC" Name="All IED Events" />

.. tip:: Attributes can be arranged in any order, it will not affect the XML file validation.

EVENTLOG and HWEVENTLOG attributes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include-file:: sections/Include/table_attrs.rstinc "" "tabid-EventLog" "EVENTLOG and HWEVENTLOG attributes" ":spec: |C{0.12}|C{0.12}|C{0.1}|S{0.66}|"

   * :attr:	:xmlattr:`Index`
     :val:	|gpindexrange|
     :def:	n/a
     :desc:	Attribute is used to enable logging for a specific communication protocol instance.
		Use value of the :ref:`xmlattr-gp101maIndex` attribute of any communication protocol instance to enable logging.
		:inlineimportant:`Attribute is mandatory for` :ref:`xmlelem-EventLog` :inlineimportant:`node and must not be used for` :ref:`xmlelem-HWeventLog` :inlineimportant:`node.`
		:inlinetip:`Indexes don't have to be in a sequential order.`

   * :attr:	:xmlattr:`HWIndex`
     :val:	|hwindexrange|
     :def:	n/a
     :desc:	Attribute is used to enable logging for a hardware node.
		Use value of the :ref:`xmlelem-uart`.\ :ref:`xmlattr-UARTIndex` \; :ref:`xmlelem-tcpserver`.\ :ref:`xmlattr-TCPSERVERIndex` \; :ref:`xmlelem-tcpclient`.\ :ref:`xmlattr-TCPCLIENTIndex` \ or :ref:`xmlelem-udp`.\ :ref:`xmlattr-UDPIndex` \ attribute to enable logging.
		:inlineimportant:`Attribute is mandatory for` :ref:`xmlelem-HWeventLog` :inlineimportant:`node and must not be used for` :ref:`xmlelem-EventLog` :inlineimportant:`node.`
		:inlinetip:`Indexes don't have to be in a sequential order.`

   * :attr:	:xmlattr:`LogFlags`
     :val:	|flags8range|
     :def:	0x00
     :desc:	Select type of the decoded information to be logged.
		See :numref:`tabid-EventLogLogFlags` for description.
		Logfile will not be created if value is 0.

.. include-file:: sections/Include/log_Logfile.rstinc "" ".event" "(sample value 'Events/abc', where 'Events' is the name of the folder and 'abc' is the name of the file)"

.. include-file:: sections/Include/log_ModeHourLimit.rstinc "" "0x01" "6" "(default 6 hours – total of 4 files will be created daily at 00:00, 06:00, 12:00, 18:00)"

.. include-file:: sections/Include/log_TimeZone.rstinc ""

.. include-file:: sections/Include/hidden_LogDebugFlags.rstinc "internal" ":numref:`tabid-syslogfileDebugFlags`"

.. include-file:: sections/Include/Name.rstinc ""

.. tip:: \* List of files created with various :ref:`xmlattr-EventLogMode` \ and :ref:`xmlattr-EventLogHourLimit` \ attribute settings can be found in section :ref:`docref-LogfileSampleList`.


EVENTLOG.LogFlags
^^^^^^^^^^^^^^^^^

.. include-file:: sections/Include/table_flags8.rstinc "" "tabid-EventLogLogFlags" "Event logfile flags" ":ref:`xmlattr-EventLogLogFlags`" "Event logger flags"
		Logfile will not be created, if the value is 0.

   * :attr:	Bit 0
     :val:	xxxx.xxx0
     :desc:	Received/sent spontaneous (event) DI information **will not be** logged

   * :(attr):
     :val:	xxxx.xxx1
     :desc:	Received/sent spontaneous (event) DI information **will be** logged

   * :attr:	Bit 1
     :val:	xxxx.xx0x
     :desc:	Received/sent spontaneous (event) AI information **will not be** logged

   * :(attr):
     :val:	xxxx.xx1x
     :desc:	Received/sent spontaneous (event) AI information **will be** logged

   * :attr:	Bit 2
     :val:	xxxx.x0xx
     :desc:	Received/sent control/setpoint command information **will not be** logged

   * :(attr):
     :val:	xxxx.x1xx
     :desc:	Received/sent control/setpoint command information **will be** logged

   * :attr:	Bit 3
     :val:	xxxx.0xxx
     :desc:	Processed command information and error messages **will not be** logged

   * :(attr):
     :val:	xxxx.1xxx
     :desc:	Processed command information and error messages **will be** logged

   * :attr:	Bit 4
     :val:	xxx0.xxxx
     :desc:	Received/sent static (General Interrogation) DI information **will not be** logged

   * :(attr):
     :val:	xxx1.xxxx
     :desc:	Received/sent static (General Interrogation) DI information **will be** logged

   * :attr:	Bit 5
     :val:	xx0x.xxxx
     :desc:	Received/sent static (General Interrogation) AI information **will not be** logged

   * :(attr):
     :val:	xx1x.xxxx
     :desc:	Received/sent static (General Interrogation) AI information **will be** logged

   * :attr:	Bit 6
     :val:	x0xx.xxxx
     :desc:	Received/sent cyclic AI information **will not be** recorded to event logfile

   * :(attr):
     :val:	x1xx.xxxx
     :desc:	Received/sent cyclic AI information **will be** logged

   * :attr:	Bit 7
     :val:	Any
     :desc:	Bits reserved for future use


LOGGER.Mode and EVENTLOG.Mode
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include-file:: sections/Include/table_flags8.rstinc "" "tabid-LoggerMode" "Logfile initialization Mode" ":ref:`xmlattr-CommsLoggerMode`" "Logfile initialization Mode"

   * :attr:	Bit 0
     :val:	xxxx.xxx0
     :desc:	New logfile **will be** created every time leandc is being started/restarted.
		This means total number of files created each day will reflect how many times leandc was started/restarted.

   * :(attr):
     :val:	xxxx.xxx1
     :desc:	New file **will not be** created if there is a logfile which was created the same date upon leandc start/restart.
		New messages will be appended at the end of the existing file.
		This means there will be only one file created each day, regardless of how many times leandc was started/restarted.

   * :attr:	Bits 1...7
     :val:	Any
     :desc:	Bits reserved for future use


.. _docref-LogfileSampleList:

Logfile samples
---------------

This section provides information on how communication and event logfiles are created based on default settings as well as contents of each file.

New communication logfile is created every 4 hours based on the default value of the :ref:`xmlelem-CommsLogger`.\ :ref:`xmlattr-CommsLoggerHourLimit` \ attribute.
In addition to that new file will be created every time leandc is started/restarted based on the default value "0x00" of the :ref:`xmlelem-CommsLogger`.\ :ref:`xmlattr-CommsLoggerMode` \ attribute.
Example below shows 2 lists of files created if leandc runs continuously and if being restarted.

.. tip::

   File creation date and hour (yyyy-mm-dd_hh) is automatically added to the name of the file specified in :ref:`xmlelem-CommsLogger`.\ :ref:`xmlattr-CommsLoggerLogfile` \ attribute.
   This is a sample list of files created, if leandc is running continuously without being restarted.

   * 'logfile_2013-04-12_00.log'
   * 'logfile_2013-04-12_04.log'
   * 'logfile_2013-04-12_08.log'
   * 'logfile_2013-04-12_12.log'

   Time-tag (hhmmss) is added to the name of the file which is created after leandc restart.
   Time-tag will be added to the name of the new file only if there is an existing file which was created at the same hour range (4 hours).
   This is a sample list of files created, if leandc was restarted at 14:04:13 and 14:07:32 and then switched off at 17:00:00 and started at 21:10:10.

   * 'logfile_2013-04-12_12.log'
   * 'logfile_2013-04-12_140413.log'	<- new file created after leandc restart at 14:04:13, time-tag is added because file created within a 4 hour range (at 12:00:00) exists
   * 'logfile_2013-04-12_140732.log'	<- new file created after leandc restart at 14:04:13, time-tag is added because file created within a 4 hour range (at 12:00:00) exists
   * 'logfile_2013-04-12_16.log'
   * 'logfile_2013-04-12_20.log'	<- new file created when leandc started at 21:10:10, no time-tag because there are no files created within a 4 hour range (from 20:00:00 to 23:59:59)

Default settings of the event files are slightly different.
New event logfile is created every 6 hours based on the default value of the :ref:`xmlelem-EventLog`.\ :ref:`xmlattr-EventLogHourLimit` \ attribute.
However new file will not be created upon leandc restart based on the default value "0x01" of the :ref:`xmlelem-EventLog`.\ :ref:`xmlattr-EventLogMode` \ attribute.
If an existing file created within the same hour range (6 hours) is found after leandc restart, new entires will appended to that file.
Example below shows the list of files created if leandc runs continuously and if being restarted.

.. tip::

   File creation date and hour (yyyy-mm-dd_hh) is automatically added to the name of the file specified in :ref:`xmlelem-EventLog`.\ :ref:`xmlattr-EventLogLogfile` \ attribute.
   This is a sample list of files created, if leandc was restarted at 14:04:13.

   * 'eventfile_2013-04-12_00.event'
   * 'eventfile_2013-04-12_06.event'
   * 'eventfile_2013-04-12_12.event'	<- leandc restart at 14:04:13, no new file is created because file within a 6 hour range exists. New entries are appended to this file.
   * 'eventfile_2013-04-12_18.event'


Contents of a typical communication logfile is shown below:

.. code-block:: none

   17:14:34.170	INFO	ONLINE
   17:14:34.205	COMM ->	10 40 01 41 16
   17:14:34.205	COMM <-	10 00 01 01 16
   17:14:34.413	COMM ->	68 0F 0F 68 73 01 67 01 06 01 00 00 42 86 0E 11 CB 05 0D A7 16
   17:14:34.414	COMM <-	10 20 01 21 16
   17:14:34.625	COMM ->	68 09 09 68 53 01 64 01 06 01 00 00 14 D4 16

Raw traffic that is captured over a communication interface is recorded to a file along with some is additional information.
Each entry (row) in the file represents successfully decoded protocol message and is prefixed with a time-tag, log entry type and direction identifier.
Timetag represents the internal time when the message was received/sent.
Log entry type may contain values listed in the table below:

.. field-list-table:: Logfile entry types
   :class: table table-condensed table-bordered table-left
   :name: tabid-LogfileEntries
   :spec: |C{0.1}|S{0.8}|
   :header-rows: 1

   * :attr,15: Entry Type
     :desc,70: Description

   * :attr:	COMM
     :desc:	Successfully decoded protocol message

   * :attr:	INFO
     :desc:	Additional status information e.g. ONLINE, OFFLINE, etc

   * :attr:	ERR
     :desc:	Failed protocol messages and timeouts

| Direction identifier shows incoming/outgoing direction of a message as follows:
| <-  Outgoing message (sent by leandc)
| ->  Incoming message (received by leandc)
| Directions are the same for Slave/Master communication protocol instances.

Contents of a typical event logfile is shown below:

.. code-block:: none

       Time        	Info	Type	CAA	InfAddr	Value	QualHex	Quality	TimeTag                	Description
   12:00:09.470 SU	SPNTAI	36	400	2101	63.88	0x00	GOOD	2015-07-31 09:00:09.470
   12:00:12.943 SU	SPNTAI	36	400	39	8.45	0x00	GOOD	2015-07-31 09:00:12.942
   12:00:12.943 SU	SPNTAI	34	400	57	24	0x81	IV OV	2015-07-31 09:00:12.942
   12:00:12.943 SU	SPNTDI	31	400	1002	OFF	0x41	NT	2015-07-31 09:00:14.873
   12:02:59.720		>CMD	45	400	6001	5	0x05	SHORT				Direct execute command received, validated and forwarded to Master protocol
   12:02:59.846		<CMD	45	400	6001	5	0x05	SHORT				Execute Confirmation sent successfully
   12:02:01.347		<CMD	45	400	6001	5	0x05	SHORT				Termination sent successfully

Decoded information is arranged in a tab separated columns.
The layout of the file is aimed to present a decoded information readable without additional tools,
yet tab separated columns make importing event file into a spreadsheet an easy task.
List of columns of the event logfile is shown in the table below:

.. field-list-table:: Event logfile columns
   :class: table table-condensed table-bordered longtable
   :name: tabid-EventLogColumns
   :spec: |C{0.12}|S{0.88}|
   :header-rows: 1

   * :attr,15: Column
     :desc,85: Description

   * :attr:	Time
     :desc:	Internal time when the event was received. Summer Time [:lemonobgtext:`SU`] flag may be added to the time stamp.

   * :attr:	Info
     :desc:	Type of the event. See :numref:`tabid-EventLogInfoTypes` for description.

   * :attr:	Type
     :desc:	ASDU typeID of the message.

   * :attr:	CAA
     :desc:	Common Address of ASDU [:lemonobgtext:`CAA`].

   * :attr:	InfAddr
     :desc:	Information object address [:lemonobgtext:`IOA`].

   * :attr:	Value
     :desc:	Value of the event. Decoded Floating point and Integer analog values can be easily distinguished by presence of a decimal point.
		Decimal point is only used for Floating point values, Integers doesn't have it.
		Status information has 4 or 2 states (i.e. ON, OFF, INTER, INDET) which are shown depending on single or double message type.
		In case of control command decimal value of command qualifier including additional information (e.g. [:lemonobgtext:`Short Pulse`]) is shown in this column.

   * :attr:	QualHex
     :desc:	Hexadecimal value of the object qualifier.

   * :attr:	Quality
     :desc:	| Quality flags of the DI/AI objects and [:lemonobgtext:`Qualifier Of Command`] values. This column can have the follwing values:
		| GOOD - No quality flags are set
		| IV - [:lemonobgtext:`INVALID`]
		| NT - [:lemonobgtext:`NOT TOPICAL`]
		| SB - [:lemonobgtext:`SUBSTITUTED`]
		| BL - [:lemonobgtext:`BLOCKED`]
		| OV - [:lemonobgtext:`OVERFLOW`] (AI only)
		| NODEF - [:lemonobgtext:`No additional definition`] (DO only)
		| SHORT - [:lemonobgtext:`Short Pulse Duration`] (DO only)
		| LONG - [:lemonobgtext:`Long Pulse Duration`] (DO only)
		| PERS - [:lemonobgtext:`Persistent Output`] (DO only)

   * :attr:	TimeTag
     :desc:	Time-tag of the event as received/sent to peer station. This column is populated only if event message has a time-tag. Summer Time [SU] flag may be added to the time tag.

   * :attr:	Description
     :desc:	Additional information on the command execution progress.


.. field-list-table:: Event logfile Info types
   :class: table table-condensed table-bordered longtable
   :name: tabid-EventLogInfoTypes
   :spec: |C{0.14}|S{0.86}|
   :header-rows: 1

   * :attr,15: Info
     :desc,85: Description

   * :attr:	>CMD
     :desc:	Received control or setpoint command in the context of Slave protocol instance. Received confirmation or termination in the context of Master protocol instance.

   * :attr:	<CMD
     :desc:	Sent control or setpoint command in the context of Master protocol instance. Sent confirmation or termination in the context of Slave protocol instance.

   * :attr:	>CMDN
     :desc:	Received negative confirmation or termination, only applies to Master protocol instances.

   * :attr:	<CMDN
     :desc:	Sent negative confirmation or termination, only applies to Slave protocol instances.

   * :attr:	>CMDERR
     :desc:	Received control or setpoint command validation failed, command is immediately rejected, only applies to Slave protocol instances.

   * :attr:	CMD
     :desc:	Additional information on command execution progress.

   * :attr:	CMDERR
     :desc:	Internal error occurred while command being processed. Please contact vendor if this type of error appears.

   * :attr:	SPNTDI
     :desc:	Spontaneous status information (DI Event).

   * :attr:	DI
     :desc:	Static status information (e.g. as a response to General Interrogation).

   * :attr:	SPNTAI
     :desc:	Spontaneous analog information (AI Event).

   * :attr:	AI
     :desc:	Static analog information (e.g. as a response to General Interrogation).

   * :attr:	AICYC
     :desc:	Cyclic/periodic analog information.

   * :attr:	AIBSCN
     :desc:	Background scan analog information.

   * :attr:	ERR
     :desc:	Internal error. Please contact vendor if this type of error appears.

