.. include:: global.roles

.. _ref-LogfileConfig:

Logfiles
========

Leandc features a raw communication traffic and decoded application level information recording
to logfiles for supervision and maintenance purposes. Fixed name XML configuration file **lelogger.xml** 
contains settings to enable logfiles. This file must be kept in the same directory as **leandc.xml** 
file. Its path and name can't be changed.

**lelogger.xml** configuration file consists of a root object node :xmlref:`SystemConfig` which has 3 optional child group 
object nodes :ref:`VersionControl<ref-VersionControl>`; :ref:`CommsCfg<ref-CommsCfg>`; :ref:`EventCfg<ref-EventCfg>`, please see the sample below. 

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
   | **lelogger.xml** configuration file is optional and leandc is able to run normally without it.
   | Node names are case sensitive.

.. _ref-CommsCfg:
.. _ref-CommsCfgLOGGER:
.. _ref-CommsCfgHWLOG:

LOGGER and HWLOG nodes
----------------------

:ref:`LOGGER<ref-CommsCfgLOGGER>` and :ref:`HWLOG<ref-CommsCfgHWLOG>` nodes contain settings for raw communication traffic logging and these nodes are children of :ref:`CommsCfg<ref-CommsCfg>` group node.
Following functionality is available:

* Record all raw traffic over a serial/Ethernet interface - :ref:`HWLOG<ref-CommsCfgHWLOG>` node;
* Filter and record traffic related to a specific communication protocol instance - :ref:`LOGGER<ref-CommsCfgLOGGER>` node;

Configuration may contain both nodes at the same time in any combination.
However only 1 logfile per protocol instance and 1 logfile per hardware interface is allowed. 

Please see sample :ref:`CommsCfg<ref-CommsCfg>` group node and :ref:`LOGGER<ref-CommsCfgLOGGER>` and :ref:`HWLOG<ref-CommsCfgHWLOG>` child element nodes below.
The sample below shows 2 logfiles for recording filtered traffic related to particular communication protocol instance and 1 logfile for recording all traffic over a serial interface.

.. code-block:: none

   <CommsCfg> 
      <LOGGER Index="5" LogFlags="0x06" Logfile="Log/serial101" Mode="0x00" HourLimit="4"/>
      <LOGGER Index="6" LogFlags="0xFF" Logfile="Log/tcpserv104"/>
      <HWLOG HWIndex="1" LogFlags="0x06" Logfile="Log/COM1" Mode="0x00" HourLimit="0"/>
   </CommsCfg>

Please see all available attributes of the :ref:`LOGGER<ref-CommsCfgLOGGER>` and :ref:`HWLOG<ref-CommsCfgHWLOG>` nodes below:

.. code-block:: none

   <LOGGER Index="5" LogFlags="0xFF" Logfile="Log/serial101" Mode="0" HourLimit="4" TimeZone="Europe/Riga" Name="IED logfile" />
   <HWLOG HWIndex="1" LogFlags="0x06" Logfile="Log/COM1" Mode="0" HourLimit="4" TimeZone="UTC" Name="COM port logfile" />

.. tip:: Attributes can be arranged in any order, it will not affect the XML file validation.

LOGGER and HWLOG attributes
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _docref-LOGGERAttab:

.. include-file:: sections/Include/table_attrs.rstinc "" "LOGGER and HWLOG attributes"

   * :attr:     :xmlref:`Index`
     :val:      1...254
     :def:      n/a
     :desc:     Attribute is used to enable logging for a specific communication protocol instance.
		Use value of the :ref:`<ref-IEC101maIndex>` attribute of any communication protocol instance to enable logging.
		:inlineimportant:`Attribute is mandatory for` :ref:`LOGGER<ref-CommsCfgLOGGER>` :inlineimportant:`node and must not be used for` :ref:`HWLOG<ref-CommsCfgHWLOG>` :inlineimportant:`node.`
		:inlinetip:`Indexes don't have to be in a sequential order.`

   * :attr:     :xmlref:`HWIndex`
     :val:      1...254
     :def:      n/a
     :desc:     Attribute is used to enable logging for a hardware node.
		Use value of the :ref:`<ref-UART>`.\ :ref:`<ref-UARTIndex>` \; :ref:`<ref-TCPSERVER>`.\ :ref:`<ref-TCPSERVERIndex>` \; :ref:`<ref-TCPCLIENT>`.\ :ref:`<ref-TCPCLIENTIndex>` \ or :ref:`<ref-UDP>`.\ :ref:`<ref-UDPIndex>` \ attribute to enable logging.
		:inlineimportant:`Attribute is mandatory for` :ref:`HWLOG<ref-CommsCfgHWLOG>` :inlineimportant:`node and must not be used for` :ref:`LOGGER<ref-CommsCfgLOGGER>` :inlineimportant:`node.`
		:inlinetip:`Indexes don't have to be in a sequential order.`

   * :attr:     .. _ref-CommsCfgLOGGERLogFlags:

		:xmlref:`LogFlags`
     :val:      0...255 or 0x00...0xFF
     :def:	0x00
     :desc:     Select type of the messages to be logged.
		See table :numref:`docref-CommsCfgLogFlagsBits` for description.
		Logfile will not be created if the value is 0.

   * :attr:     .. _ref-CommsCfgLOGGERLogfile:

                :xmlref:`Logfile`
     :val:      Max 200 chars
     :def:      n/a
     :desc:     Name of a logfile excluding extension (e.g. '.log').
		It is possible to specify relative or absolute path as part of the file name.
		Logfile will be created in the default home folder (e.g. '/home/leandc/app') if path is not specified.
		Date when the file was created and extension '.log' will be appended to the file name automatically.	
		Logfile will not be created if this attribute is left blank.
		(sample value 'Log/abc', where 'Log' is the name of the folder and 'abc' is the name of the file)
		:inlineimportant:`Attribute is case sensitive, observe the case of the path and name of the file when specifying.`

   * :attr:     .. _ref-CommsCfgLOGGERMode:

		:xmlref:`Mode`

		\*
     :val:      0...255 or 0x00...0xFF
     :def:	0x00
     :desc:     Logfile initialization settings. See table :numref:`docref-LoggerModeBits` for description.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, default settings will be used if omitted.`

   * :attr:     .. _ref-CommsCfgLOGGERHourLimit:

                :xmlref:`HourLimit`

		\*
     :val:      0...12
     :def:	4 hours
     :desc:     Option to create a new file after selected number of hours in order to limit the size of a file.
		(default 4 hours – total of 6 files will be created daily at 00:00, 04:00, 08:00, 12:00, 16:00, 20:00)
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, default settings will be used if omitted.`

   * :attr:     :xmlref:`TimeZone`
     :val:      Max 200 chars
     :def:	n/a
     :desc:     Adjust time-tags of the recorded information based on the specified time zone.
		:inlineimportant:`Attribute must not be used if not required, there is no default value. Time-tags will not be adjusted if attribute omitted.`
		:inlinetip:`Please see` :ref:`docref-TimeZoneSpecification` :inlinetip:`for additional information.`

.. include-file:: sections/Include/hidden_LogDebugFlags.rstinc "internal" ":numref:`docref-LOGGERDebugFlagsAttab`"

.. include-file:: sections/Include/Name.rstinc ""

.. tip:: \* List of files created with various :ref:`<ref-CommsCfgLOGGERMode>` \ and :ref:`<ref-CommsCfgLOGGERHourLimit>` \ attribute settings can be found in section :ref:`docref-LogfileSampleList`.


LOGGER.LogFlags
^^^^^^^^^^^^^^^
.. _docref-CommsCfgLogFlagsBits:

.. include-file:: sections/Include/table_flags.rstinc "" "Communication logfile flags" ":ref:`<ref-CommsCfgLOGGERLogFlags>`" "Logger flags"
		Logfile will not be created, if the value is 0.

   * :attr:     Bit 0
     :val:      xxxx.xxx0
     :desc:     Link layer (of the IEC60870-5-101 communication protocol) or Transport layer (of the IEC60870-5-104 communication protocol) message recording **disabled**

   * :(attr):
     :val:      xxxx.xxx1
     :desc:     Link layer (of the IEC60870-5-101 communication protocol) or Transport layer (of the IEC60870-5-104 communication protocol) message recording **enabled**

   * :attr:     Bit 1
     :val:      xxxx.xx0x
     :desc:     Incoming message logging **disabled**

   * :(attr):
     :val:      xxxx.xx1x
     :desc:     Incoming message logging **enabled**

   * :attr:     Bit 2
     :val:      xxxx.x0xx
     :desc:     Outgoing message logging **disabled**

   * :(attr):
     :val:      xxxx.x1xx
     :desc:     Outgoing message logging **enabled**

   * :attr:     Bit 4
     :val:      xxx0.xxxx
     :desc:     Socket connection status and [Started]; [Stopped] state information of the IEC60870-5-104 protocol instance or link layer state information of the IEC60870-5-101 protocol instance logging **disabled**

   * :(attr):
     :val:      xxx1.xxxx
     :desc:     Socket connection status and [Started]; [Stopped] state information of the IEC60870-5-104 protocol instance or link layer state information of the IEC60870-5-101 protocol instance logging **enabled**

   * :attr:     Bit 7
     :val:      0xxx.xxxx
     :desc:     Only applicable to IEC60870-5-101 protocol instances, **don't** log the transmitted message echo (if it exists)

   * :(attr):
     :val:      1xxx.xxxx
     :desc:     Only applicable to IEC60870-5-101 protocol instances, **log** the transmitted message echo (if it exists)

   * :attr:     Bits 3;5;6
     :val:      Any
     :desc:     Bits reserved for future use


.. _ref-CommsCfgPCAPLOG:

PCAPLOG
-------

:ref:`<ref-CommsCfgPCAPLOG>` node enables to capture traffic through a specific or any Ethernet interfaces in a pcap format.
:ref:`<ref-CommsCfgPCAPLOG>` node is a child of :ref:`CommsCfg<ref-CommsCfg>` group node.

Please see sample :ref:`CommsCfg<ref-CommsCfg>` group and :ref:`<ref-CommsCfgPCAPLOG>` child element node below.

.. code-block:: none

   <CommsCfg>
      <PCAPLOG HWIndex="1" LogFlags="0x07" Logfile="Log/trace" Mode="0x00" HourLimit="0"/>
   </CommsCfg>

.. important:: Group node :ref:`CommsCfg<ref-CommsCfg>` may contain only one :ref:`<ref-CommsCfgPCAPLOG>` node. :ref:`<ref-CommsCfgPCAPLOG>` must be the last in the group after all :ref:`LOGGER<ref-CommsCfgLOGGER>` and :ref:`HWLOG<ref-CommsCfgHWLOG>` nodes, if there are any.

Please see all available attributes of the :ref:`<ref-CommsCfgPCAPLOG>` node below:

.. code-block:: none

   <PCAPLOG HWIndex="1" LogFlags="0x07" Logfile="Log/trace" Mode="0" HourLimit="4" Name="pcap trace" />

.. tip:: Attributes can be arranged in any order, it will not affect the XML file validation.

PCAPLOG attributes
^^^^^^^^^^^^^^^^^^

.. _docref-PCAPLOGAttab:

.. include-file:: sections/Include/table_attrs.rstinc "" "PCAPLOG attributes"

   * :attr:     :xmlref:`HWIndex`
     :val:      1...254
     :def:      n/a
     :desc:     Capture traffic through Ethernet interface used by this Hardware node.
		Use value of the :ref:`<ref-TCPSERVER>`.\ :ref:`<ref-TCPSERVERIndex>` \; :ref:`<ref-TCPCLIENT>`.\ :ref:`<ref-TCPCLIENTIndex>` \ or :ref:`<ref-UDP>`.\ :ref:`<ref-UDPIndex>` \ attribute to enable capture.
		:inlineimportant:`Only one` :ref:`<ref-CommsCfgPCAPLOG>` :inlineimportant:`node can be defined.`
		:inlinetip:`Use` :ref:`<ref-CommsCfgPCAPLOGLogFlags>` :inlinetip:`attribute to enable capture on all Ethernet interfaces, if required.`

   * :attr:     .. _ref-CommsCfgPCAPLOGLogFlags:

		:xmlref:`LogFlags`
     :val:      0...255 or 0x00...0xFF
     :def:	0x00
     :desc:     Capture filter specifications.
		See table :numref:`docref-CommsCfgPCAPLogFlagsBits` for description.
		Capture is disabled if value is 0.

   * :attr:     .. _ref-CommsCfgPCAPLOGLogfile:

                :xmlref:`Logfile`
     :val:      Max 200 chars
     :def:      n/a
     :desc:     Name of a logfile excluding extension (e.g. '.pcap').
		It is possible to specify relative or absolute path as part of the file name.
		Logfile will be created in the default home folder (e.g. '/home/leandc/app') if path is not specified.
		Date when the file was created and extension '.pcap' will be appended to the file name automatically.	
		Logfile will not be created if this attribute is left blank.
		(sample value 'Log/abc', where 'Log' is the name of the folder and 'abc' is the name of the file)
		:inlineimportant:`Attribute is case sensitive, observe the case of the path and name of the file when specifying.`

   * :attr:     .. _ref-CommsCfgPCAPLOGMode:

		:xmlref:`Mode`

		\*
     :val:      0...255 or 0x00...0xFF
     :def:	0x00
     :desc:     Logfile initialization settings. See table :numref:`docref-LoggerModeBits` for description.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, default settings will be used if omitted.`

   * :attr:     .. _ref-CommsCfgPCAPLOGHourLimit:

                :xmlref:`HourLimit`

		\*
     :val:      0...12
     :def:	4 hours
     :desc:     Option to create a new file after selected number of hours in order to limit the size of a file.
		(default 4 hours – total of 6 files will be created daily at 00:00, 04:00, 08:00, 12:00, 16:00, 20:00)
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, default settings will be used if omitted.`

.. include-file:: sections/Include/Name.rstinc ""

.. tip:: \* List of files created with various :ref:`<ref-CommsCfgPCAPLOGMode>` \ and :ref:`<ref-CommsCfgPCAPLOGHourLimit>` \ attribute settings can be found in section :ref:`docref-LogfileSampleList`.


PCAPLOG.LogFlags
^^^^^^^^^^^^^^^^
.. _docref-CommsCfgPCAPLogFlagsBits:

.. include-file:: sections/Include/table_flags.rstinc "" "Capture filter flags" ":ref:`<ref-CommsCfgPCAPLOGLogFlags>`" "Filter flags"
		Capture is disabled if the value is 0.

   * :attr:     Bits 0,1
     :val:      xxxx.xx00
     :desc:     Reserved - don't use.

   * :(attr):
     :val:      xxxx.xx01
     :desc:     Capture traffic through **all** available Ethernet interfaces. Traffic will not be filtered by IP address.

   * :(attr):
     :val:      xxxx.xx10
     :desc:     Capture traffic trough a **single** Ethernet interface, the one used for communication.

   * :(attr):
     :val:      xxxx.xx11
     :desc:     Filter captured traffic by **IP address**. Only messages with matching Source or Destination IP address will be captured.
		Address from :ref:`<ref-TCPSERVER>`.\ :ref:`<ref-TCPSERVERIPaddr>` \; :ref:`<ref-TCPCLIENT>`.\ :ref:`<ref-TCPCLIENTIPaddr>` \ or :ref:`<ref-UDP>`.\ :ref:`<ref-UDPRemoteIPaddr>` \ attribute is used as a filter.

   * :attr:     Bit 2
     :val:      xxxx.x0xx
     :desc:     Capture filter by port number is **disabled**

   * :(attr):
     :val:      xxxx.x1xx
     :desc:     Capture filter by port number is  **enabled**. Only messages with matching Source or Destination Port number will be captured.
		Port number from :ref:`<ref-TCPSERVER>`.\ :ref:`<ref-TCPSERVERPort>` \; :ref:`<ref-TCPCLIENT>`.\ :ref:`<ref-TCPCLIENTPort>` \ or :ref:`<ref-UDP>`.\ :ref:`<ref-UDPRemotePort>` \ attribute is used as a filter.

   * :attr:     Bits 3...7
     :val:      Any
     :desc:     Bits reserved for future use


.. _ref-EventCfg:
.. _ref-EventCfgEVENTLOG:
.. _ref-EventCfgHWEVENTLOG:

EVENTLOG and HWEVENTLOG nodes
-----------------------------

:ref:`EVENTLOG<ref-EventCfgEVENTLOG>` and :ref:`HWEVENTLOG<ref-EventCfgHWEVENTLOG>` nodes contain settings for decoded application level information (DI/AI/DO/AO object types, addresses, values, etc) logging and these nodes are children of :ref:`EventCfg<ref-EventCfg>` group node.
Following functionality is available:

* Record all decoded information over a serial/Ethernet interface - :ref:`HWEVENTLOG<ref-EventCfgHWEVENTLOG>` node;
* Filter and record decoded information related to a specific communication protocol instance - :ref:`EVENTLOG<ref-EventCfgEVENTLOG>` node;

Configuration may contain both nodes at the same time in any combination.
However only 1 logfile per protocol instance and 1 logfile per hardware interface is allowed. 

Please see sample :ref:`EventCfg<ref-EventCfg>` group node and :ref:`EVENTLOG<ref-EventCfgEVENTLOG>` and :ref:`HWEVENTLOG<ref-EventCfgHWEVENTLOG>` child element nodes below.
The sample below shows 2 logfiles for recording decoded information of a particular communication protocol instance and 1 logfile for recording decoded information over a serial interface.

.. code-block:: none

   <EventCfg> 
      <EVENTLOG Index="5" LogFlags="0x3F" Logfile="Events/serial101" HourLimit="0" Mode="0"/> 
      <EVENTLOG Index="6" LogFlags="0x0C" Logfile="Events/tcpserv104"/> 
      <HWEVENTLOG HWIndex="1" LogFlags="0x40" Logfile="Events/COM1_events" HourLimit="0"/> 
   </EventCfg>

Please see all available attributes of the :ref:`EVENTLOG<ref-EventCfgEVENTLOG>` and :ref:`HWEVENTLOG<ref-EventCfgHWEVENTLOG>` nodes below:

.. code-block:: none

   <EVENTLOG Index="5" LogFlags="0xFF" Logfile="Events/101slave" Mode="0" HourLimit="4" TimeZone="Europe/Riga" Name="IED Events" />
   <HWEVENTLOG HWIndex="1" LogFlags="0x06" Logfile="Events/COM1" Mode="0" HourLimit="4" TimeZone="UTC" Name="All IED Events" />

.. tip:: Attributes can be arranged in any order, it will not affect the XML file validation.

EVENTLOG and HWEVENTLOG attributes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _docref-EventCfgEVENTLOGAttab:

.. include-file:: sections/Include/table_attrs.rstinc "" "EVENTLOG and HWEVENTLOG attributes"

   * :attr:     :xmlref:`Index`
     :val:      1...254
     :def:      n/a
     :desc:     Attribute is used to enable logging for a specific communication protocol instance.
		Use value of the :ref:`<ref-IEC101maIndex>` attribute of any communication protocol instance to enable logging.
		:inlineimportant:`Attribute is mandatory for` :ref:`EVENTLOG<ref-EventCfgEVENTLOG>` :inlineimportant:`node and must not be used for` :ref:`HWEVENTLOG<ref-EventCfgHWEVENTLOG>` :inlineimportant:`node.`
		:inlinetip:`Indexes don't have to be in a sequential order.`

   * :attr:     :xmlref:`HWIndex`
     :val:      1...254
     :def:      n/a
     :desc:     Attribute is used to enable logging for a hardware node.
		Use value of the :ref:`<ref-UART>`.\ :ref:`<ref-UARTIndex>` \; :ref:`<ref-TCPSERVER>`.\ :ref:`<ref-TCPSERVERIndex>` \; :ref:`<ref-TCPCLIENT>`.\ :ref:`<ref-TCPCLIENTIndex>` \ or :ref:`<ref-UDP>`.\ :ref:`<ref-UDPIndex>` \ attribute to enable logging.
		:inlineimportant:`Attribute is mandatory for` :ref:`HWEVENTLOG<ref-EventCfgHWEVENTLOG>` :inlineimportant:`node and must not be used for` :ref:`EVENTLOG<ref-EventCfgEVENTLOG>` :inlineimportant:`node.`
		:inlinetip:`Indexes don't have to be in a sequential order.`

   * :attr:     .. _ref-CommsCfgEVENTLOGLogFlags:

		:xmlref:`LogFlags`
     :val:      0...255 or 0x00...0xFF
     :def:	0x00
     :desc:     Select type of the decoded information to be logged.
		See table :numref:`docref-EventCfgLogFlagsBits` for description.
		Logfile will not be created if value is 0.

   * :attr:     .. _ref-EventCfgEVENTLOGLogfile:

                :xmlref:`Logfile`
     :val:      Max 200 chars
     :def:      n/a
     :desc:     Name of a logfile excluding extension (e.g. '.event').
		It is possible to specify relative or absolute path as part of the file name.
		Logfile will be created in the default home folder (e.g. '/home/leandc/app') if path is not specified.
		Date when the file was created and extension '.event' will be appended to the file name automatically.
		Logfile will not be created if this attribute is left blank.	
		(sample value 'Events/abc', where 'Events' is the name of the folder and 'abc' is the name of the file)
		:inlineimportant:`Attribute is case sensitive, observe the case of the path and name of the file when specifying.`

   * :attr:     .. _ref-EventCfgEVENTLOGMode:

		:xmlref:`Mode`

		\*
     :val:      0...255 or 0x00...0xFF
     :def:      0x01
     :desc:     Logfile initialization settings.
		See table :numref:`docref-LoggerModeBits` for description.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, default settings will be used if omitted.`

   * :attr:     .. _ref-EventCfgEVENTLOGHourLimit:

		:xmlref:`HourLimit`

		\*
     :val:      0...12
     :def:	6 hours
     :desc:     Option to create a new file after selected number of hours in order to limit the size of the file.
		(default 6 hours – total of 4 files will be created daily at 00:00, 06:00, 12:00, 18:00)
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, default settings will be used if omitted.`

   * :attr:     :xmlref:`TimeZone`
     :val:      Max 200 chars
     :def:      n/a
     :desc:     Adjust time-tags of the recorded information based on the specified time zone.
		:inlineimportant:`Attribute must not be used if not required, there is no default value. Time-tags will not be adjusted if attribute omitted.`
		:inlinetip:`Please see` :ref:`docref-TimeZoneSpecification` :inlinetip:`for additional information.`

.. include-file:: sections/Include/hidden_LogDebugFlags.rstinc "internal" ":numref:`docref-LOGGERDebugFlagsAttab`"

.. include-file:: sections/Include/Name.rstinc ""

.. tip:: \* List of files created with various :ref:`<ref-EventCfgEVENTLOGMode>` \ and :ref:`<ref-EventCfgEVENTLOGHourLimit>` \ attribute settings can be found in section :ref:`docref-LogfileSampleList`.


EVENTLOG.LogFlags
^^^^^^^^^^^^^^^^^

.. _docref-EventCfgLogFlagsBits:

.. include-file:: sections/Include/table_flags.rstinc "" "Event logfile flags" ":ref:`<ref-CommsCfgEVENTLOGLogFlags>`" "Logger flags"
		Logfile will not be created, if the value is 0.

   * :attr:     Bit 0
     :val:      xxxx.xxx0
     :desc:     Received/sent spontaneous (event) DI information **will not be** logged

   * :(attr):
     :val:      xxxx.xxx1
     :desc:     Received/sent spontaneous (event) DI information **will be** logged

   * :attr:     Bit 1
     :val:      xxxx.xx0x
     :desc:     Received/sent spontaneous (event) AI information **will not be** logged

   * :(attr):
     :val:      xxxx.xx1x
     :desc:     Received/sent spontaneous (event) AI information **will be** logged

   * :attr:     Bit 2
     :val:      xxxx.x0xx
     :desc:     Received/sent control/setpoint command information **will not be** logged

   * :(attr):
     :val:      xxxx.x1xx
     :desc:     Received/sent control/setpoint command information **will be** logged

   * :attr:     Bit 3
     :val:      xxxx.0xxx
     :desc:     Processed command information and error messages **will not be** logged

   * :(attr):
     :val:      xxxx.1xxx
     :desc:     Processed command information and error messages **will be** logged

   * :attr:     Bit 4
     :val:      xxx0.xxxx
     :desc:     Received/sent static (General Interrogation) DI information **will not be** logged

   * :(attr):
     :val:      xxx1.xxxx
     :desc:     Received/sent static (General Interrogation) DI information **will be** logged

   * :attr:     Bit 5
     :val:      xx0x.xxxx
     :desc:     Received/sent static (General Interrogation) AI information **will not be** logged

   * :(attr):
     :val:      xx1x.xxxx
     :desc:     Received/sent static (General Interrogation) AI information **will be** logged

   * :attr:     Bit 6
     :val:      x0xx.xxxx
     :desc:     Received/sent cyclic AI information **will not be** recorded to event logfile

   * :(attr):
     :val:      x1xx.xxxx
     :desc:     Received/sent cyclic AI information **will be** logged

   * :attr:     Bit 7
     :val:      Any
     :desc:     Bits reserved for future use


LOGGER.Mode and EVENTLOG.Mode
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _docref-LoggerModeBits:

.. include-file:: sections/Include/table_flags.rstinc "" "Logfile initialization Mode" ":xmlref:`Mode`" "Logfile initialization Mode"

   * :attr:     Bit 0
     :val:      xxxx.xxx0
     :desc:     New logfile **will be** created every time leandc is being started/restarted.
		This means total number of files created each day will reflect how many times leandc was started/restarted.

   * :(attr):
     :val:      xxxx.xxx1
     :desc:     New file **will not be** created if there is a logfile which was created the same date upon leandc start/restart.
		New messages will be appended at the end of the existing file.
		This means there will be only one file created each day, regardless of how many times leandc was started/restarted.

   * :attr:     Bits 1...7
     :val:      Any
     :desc:     Bits reserved for future use


.. _docref-LogfileSampleList:

Logfile samples
---------------

This section provides information on how communication and event logfiles are created based on default settings as well as contents of each file.

New communication logfile is created every 4 hours based on the default value of the :ref:`LOGGER<ref-CommsCfgLOGGER>`.\ :ref:`<ref-CommsCfgLOGGERHourLimit>` \ attribute.
In addition to that new file will be created every time leandc is started/restarted based on the default value "0x00" of the :ref:`LOGGER<ref-CommsCfgLOGGER>`.\ :ref:`<ref-CommsCfgLOGGERMode>` \ attribute.
Example below shows 2 lists of files created if leandc runs continuously and if being restarted.

.. tip::

   File creation date and hour (yyyy-mm-dd_hh) is automatiaclly added to the name of the file specified in :ref:`LOGGER<ref-CommsCfgLOGGER>`.\ :ref:`<ref-CommsCfgLOGGERLogfile>` \ attribute.
   This is a sample list of files created, if leandc is running continuously without being restarted.
      
   * 'logfile_2013-04-12_00.log'
   * 'logfile_2013-04-12_04.log'
   * 'logfile_2013-04-12_08.log'
   * 'logfile_2013-04-12_12.log'
      
   Time-tag (hhmmss) is added to the name of the file which is created after leandc restart.
   Time-tag will be added to the name of the new file only if there is an existing file which was created at the same hour range (4 hours).
   This is a sample list of files created, if leandc was restarted at 14:04:13 and 14:07:32 and then swtiched off at 17:00:00 and started at 21:10:10.
   
   * 'logfile_2013-04-12_12.log'
   * 'logfile_2013-04-12_140413.log'	← new file created after leandc restart at 14:04:13, time-tag is added because file created within a 4 hour range (at 12:00:00) exists
   * 'logfile_2013-04-12_140732.log'	← new file created after leandc restart at 14:04:13, time-tag is added because file created within a 4 hour range (at 12:00:00) exists
   * 'logfile_2013-04-12_16.log'
   * 'logfile_2013-04-12_20.log'	← new file created when leandc started at 21:10:10, no time-tag because there are no files created within a 4 hour range (from 20:00:00 to 23:59:59)

Default settings of the event files are slightly different. 
New event logfile is created every 6 hours based on the default value of the :ref:`EVENTLOG<ref-EventCfgEVENTLOG>`.\ :ref:`<ref-EventCfgEVENTLOGHourLimit>` \ attribute.
However new file will not be created upon leandc restart based on the default value "0x01" of the :ref:`EVENTLOG<ref-EventCfgEVENTLOG>`.\ :ref:`<ref-EventCfgEVENTLOGMode>` \ attribute. 
If an existing file created within the same hour range (6 hours) is found after leandc reastart, new entires will appended to that file.
Example below shows the list of files created if leandc runs continuously and if being restarted.

.. tip::

   File creation date and hour (yyyy-mm-dd_hh) is automatiaclly added to the name of the file specified in :ref:`EVENTLOG<ref-EventCfgEVENTLOG>`.\ :ref:`<ref-EventCfgEVENTLOGLogfile>` \ attribute.
   This is a sample list of files created, if leandc was restarted at 14:04:13.

   * 'eventfile_2013-04-12_00.event'
   * 'eventfile_2013-04-12_06.event'
   * 'eventfile_2013-04-12_12.event'	← leandc restart at 14:04:13, no new file is created because file within a 6 hour range exists. New entries are appended to this file.
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
Each entry (row) in the file represents sucessfully decoded protocol message and is prefixed with a time-tag, log entry type and direction identifier.
Timetag represents the internal time when the message was received/sent.
Log entry type may contain values listed in the table below:

.. field-list-table:: Logfile entry types
   :class: table table-condensed table-bordered table-left
   :spec: |C{0.1}|S{0.8}|
   :header-rows: 1

   * :attr,15: Entry Type
     :desc,70: Description

   * :attr:     COMM
     :desc:     Successfully decoded protocol message

   * :attr:     INFO
     :desc:     Additional status information e.g. ONLINE, OFFLINE, etc

   * :attr:     ERR
     :desc:     Failed protocol messages and timeouts

| Direction identifier shows incoming/outgoing direction of a message as follows:
| <-  Outgoing message (sent by leandc)
| ->  Incoming message (received by leandc)
| Directions are the same for Slave/Master communication protocol instances.

Contents of a typical event logfile is shown below:

.. code-block:: none

       Time        	Info	Type	ASDUadr	InfAddr	Value	QualHex	TimeTag                	Description
   12:00:09.470 SU	SPNTAI	36	400	2101	63.88	0x00	2015-07-31 09:00:09.470	 
   12:00:12.943 SU	SPNTAI	36	400	39	8.45	0x00	2015-07-31 09:00:12.942	 
   12:00:12.943 SU	SPNTAI	34	400	57	24	0x00	2015-07-31 09:00:12.942	 
   12:00:12.943 SU	SPNTDI	31	400	1002	OFF	0x01	2015-07-31 09:00:14.873	
   12:02:59.720		>CMD	45	400	6001	5	0x05				Direct execute command received, validated and forwarded to Master protocol
   12:02:59.846		<CMD	45	400	6001	5	0x05				Execute Confirmation sent successfully
   12:02:01.347		<CMD	45	400	6001	5	0x05				Termination sent successfully

Decoded information is arranged in a tab separated colums.
The layout of the file is aimed to present a decoded information readable without additional tools,
yet tab separated columns make importing event file into a spreadsheet an easy task. 
List of colums of the event logfile is shown in the table below:

.. field-list-table:: Event logfile columns
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.1}|S{0.8}|
   :header-rows: 1

   * :attr,15: Column
     :desc,85: Description

   * :attr:     Time
     :desc:     Internal time when the event was received. Summer Time [SU] flag may be added to the time stamp.

   * :attr:     Info
     :desc:     Type of the event. See table :numref:`docref-EventLogInfoTypes` for description.

   * :attr:     Type
     :desc:     ASDU typeID of the message.

   * :attr:     ASDUadr
     :desc:     Common Address of ASDU [CAA].

   * :attr:     InfAddr
     :desc:     Information object address [IOA].

   * :attr:     Value
     :desc:     Value of the event. Decoded Floating point and Integer analog values can be easily distinguished by presence of a decimal point.
		Decimal point is only used for Floating point values, Integers doesn't have it.
		Status information has 4 or 2 states (i.e. ON, OFF, INTER, INDET) which are shown depending on single or double message type.
		In case of control command decimal value of command qualifier including additional information (e.g. [Short pulse]) is shown in this column. 

   * :attr:     QualHex
     :desc:     Hexadecimal value of the object qualifier.

   * :attr:     TimeTag
     :desc:     Time-tag of the event as received/sent to peer station. This column is populated only if event message has a time-tag. Summer Time [SU] flag may be added to the time tag.

   * :attr:     Description
     :desc:     Additional information on the command execution progress.


.. _docref-EventLogInfoTypes:

.. field-list-table:: Event logfile Info types
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.1}|S{0.8}|
   :header-rows: 1

   * :attr,15: Info
     :desc,85: Description

   * :attr:     >CMD
     :desc:     Received control or setpoint command in the contex of Slave protocol instance. Received confirmation or termination in the contex of Master protocol instance.

   * :attr:     <CMD
     :desc:     Sent control or setpoint command in the contex of Master protocol instance. Sent confirmation or termination in the contex of Slave protocol instance.

   * :attr:     >CMDN
     :desc:     Received negative confirmation or termination, only applies to Master protocol instances.

   * :attr:     <CMDN
     :desc:     Sent negative confirmation or termination, only applies to Slave protocol instances.

   * :attr:     >CMDERR
     :desc:     Received control or setpoint command validation failed, command is immediately rejected, only applies to Slave protocol instances.

   * :attr:     CMD
     :desc:     Additional information on command execution progress.

   * :attr:     CMDERR
     :desc:     Internal error occurred while command being processed. Please contact vendor if this type of error appears.

   * :attr:     SPNTDI
     :desc:     Spontaneous status information (DI Event).

   * :attr:     DI
     :desc:     Static status information (e.g. as a response to General Interrogation).

   * :attr:     SPNTAI
     :desc:     Spontaneous analog information (AI Event).

   * :attr:     AI
     :desc:     Static analog information (e.g. as a response to General Interrogation).

   * :attr:     AICYC
     :desc:     Cyclic/periodic analog information.

   * :attr:     AIBSCN
     :desc:     Background scan analog information.

   * :attr:     ERR
     :desc:     Internal error. Please contact vendor if this type of error appears.

