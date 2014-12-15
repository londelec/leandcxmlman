.. include:: global.roles

.. _ref-LogfileConfig:

Logfile configuration file **lelogger.xml**
===========================================

Leandc features an option to record raw communication protocol traffic or decoded application level information 
to logfiles for supervision and maintenance purposes. XML configuration file with a fixed file name **lelogger.xml** 
contains all settings related to logfiles. The configuration file must be stored in the same directory as leandc 
firmware and its path can't be changed. 

**lelogger.xml** configuration file consists of a root object node :xmlref:`SystemConfig` which has 3 optional child group 
object nodes :ref:`VersionControl<ref-VersionControl>`; :ref:`CommsCfg<ref-CommsCfg>`; :ref:`EventCfg<ref-EventCfg>`, please see the sample below. 

.. code-block:: none

   <SystemConfig xmlns="http://www.londelec.com/xmlschemas/leandc/lelogger" … version="1.00"> 
         <VersionControl conf="4" date="2014-01-18" time="10:08:09"/>
         <CommsCfg> 
            <LOGGER Index="6" LogFlags="0x7F" Logfile="Log/ma2"/>
            … 
         </CommsCfg>
         <EventCfg>
            <EVENTLOG Index="104" LogFlags="0x3F" HourLimit="0" Logfile="Events/SL104_1"/>
            … 
         </EventCfg> 
   </SystemConfig>

.. tip:: 
   | **lelogger.xml** configuration file is optional and system is able to run normally without it.
   | Node names are not case sensitive.

.. _ref-CommsCfg:
.. _ref-CommsCfgLOGGER:
.. _ref-CommsCfgHWLOG:

CommsCfg group and LOGGER; HWLOG nodes   
--------------------------------------   

Group node :ref:`CommsCfg<ref-CommsCfg>` and child element nodes :ref:`LOGGER<ref-CommsCfgLOGGER>`; :ref:`HWLOG<ref-CommsCfgHWLOG>` are used to configure raw communication 
protocol traffic recording to logfiles. There are to options: 

* Record all raw traffic on a serial/Ethernet interface;
* Record the traffic only related to a particular communication protocol instance.

:ref:`LOGGER<ref-CommsCfgLOGGER>` node is used to record traffic only related to a specific communication protocol instance. :ref:`HWLOG<ref-CommsCfgHWLOG>` 
node on the other hand is used to record all traffic on a serial/Ethernet interface. These two methods become 
very useful and provide flexible filtering options in case more than 1 communication protocol instance share the 
same hardware interface (e.g. IEC 60870-5-101 controlling station (Master) instances communicating to 
multiple outstations).


Please see sample :ref:`CommsCfg<ref-CommsCfg>` group node and :ref:`LOGGER<ref-CommsCfgLOGGER>`; :ref:`HWLOG<ref-CommsCfgHWLOG>` child element nodes below. The sample 
contains configuration of 2 individual communication protocol instance logfiles and 1 serial interface logfile.

.. code-block:: none

   <CommsCfg> 
      <LOGGER Index="5" LogFlags="0x00" Mode="0x00" HourLimit="4" Logfile="Log/101slave"/>
      <LOGGER Index="6" LogFlags="255" Logfile="Log/104logserv"/>
      <HWLOG HWIndex="1" LogFlags="0x06" Mode="0x00" HourLimit="0" Logfile="Log/COM1"/>
   </CommsCfg>

Please see sample :ref:`LOGGER<ref-CommsCfgLOGGER>` and :ref:`HWLOG<ref-CommsCfgHWLOG>` element node below listing all available attributes.

.. code-block:: none

   <LOGGER  Index="5"
            LogFlags="0xFF"
            Mode="0"
            HourLimit="4"
            Logfile="Log/101slave"
            Name="IED logfile" />

   <HWLOG   HWIndex="1"
            LogFlags="0x06"
            Mode="0"
            HourLimit="4"
            Logfile="Log/COM1"
            Name="Port logfile" />

.. tip:: Attributes of the :ref:`LOGGER<ref-CommsCfgLOGGER>` and :ref:`HWLOG<ref-CommsCfgHWLOG>` element nodes can be arranged in any order, it will not affect the XML file validation.

LOGGER and HWLOG attributes
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _ref-LOGGERAttributes:

.. field-list-table:: LOGGER and HWLOG attributes
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.20}|C{0.25}|S{0.55}|
   :header-rows: 1

   * :attr,10: Attribute
     :val,15:  Values or range
     :desc,75: Description

   * :attr:    :xmlref:`Index`
     :val:     1...254
     :desc:    Index attribute is used to enable logging for a particular communication protocol instance. Use value of the :ref:`Index<ref-IEC101maIndex>` attribute of any communication protocol instance in order to enable logging. :inlineimportant:`Attribute is mandatory for` :ref:`LOGGER<ref-CommsCfgLOGGER>` :inlineimportant:`node, it is not required for` :ref:`HWLOG<ref-CommsCfgHWLOG>` :inlineimportant:`node.` :inlinetip:`Indexes don't have to be in a sequential order.`

   * :attr:    :xmlref:`HWIndex`
     :val:     1...254
     :desc:    Index attribute is used to enable logging for a hardware node. Use value of the :ref:`UART<ref-UART>`.\ :ref:`Index<ref-UARTIndex>` \; :ref:`TCPSERVER<ref-TCPSERVER>`.\ :ref:`Index<ref-TCPSERVERIndex>` \; :ref:`TCPCLIENT<ref-TCPCLIENT>`.\ :ref:`Index<ref-TCPCLIENTIndex>` \ or :ref:`UDP<ref-UDP>`.\ :ref:`Index<ref-UDPIndex>` \ attribute in order to enable logging. :inlineimportant:`Attribute is mandatory for` :ref:`HWLOG<ref-CommsCfgHWLOG>` :inlineimportant:`node, it is not required for` :ref:`LOGGER<ref-CommsCfgLOGGER>` :inlineimportant:`node.` :inlinetip:`Indexes don't have to be in a sequential order.`

   * :attr:    :xmlref:`LogFlags`
     :val:     See table :numref:`ref-CommsCfgLogFlagsBits` for description
     :desc:    Log flags specify type of information to be recorded to the logfile. Logfile will not be created, if value is 0.

   * :attr:    .. _ref-CommsCfgLOGGERLogfile:
               
               :xmlref:`Logfile`
     :val:     Max 200 chars
     :desc:    Logfile name without an extension, but including absolute or relative path. Logfile will be created in the same folder as leandc firmware if path is not specified. The date and extension 'log' will be added to the file name automatically. Logfile will not be created if attribute is left blank. (default entry 'Log/aaa', where 'aaa' is name of the file) :inlineimportant:`Attribute is case sensitive, observe the case of path and file name when specifying.`

   * :attr:    .. _ref-CommsCfgLOGGERMode:
               
               :xmlref:`Mode`\*
     :val:     See table :numref:`ref-LoggerModeBits` for description
     :desc:    New logfile initialization settings. (default value 0) :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default settings will be used if omitted.`

   * :attr:    .. _ref-CommsCfgLOGGERHourLimit:
   
               :xmlref:`HourLimit`\*
     :val:     0...12
     :desc:    New file will be created after selected number of hours in order to limit the size. (default 4 hours) :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default settings will be used if omitted.`

   * :attr:    :xmlref:`Name`
     :val:     Max 100 chars
     :desc:    Freely configurable name, just for reference. :inlinetip:`Name attribute is optional and doesn't have to be included in configuration.`

.. tip::
   \* Please refer to the (:ref:`ref<ref-LogfileSampleList>`) for sample list of files created with various :ref:`LOGGER<ref-CommsCfgLOGGER>`.\ :ref:`HourLimit<ref-CommsCfgLOGGERHourLimit>` \ and :ref:`LOGGER<ref-CommsCfgLOGGER>`.\ :ref:`Mode<ref-CommsCfgLOGGERMode>` \ attribute settings.

LOGGER.LogFlags
^^^^^^^^^^^^^^^
.. _ref-CommsCfgLogFlagsBits:

.. field-list-table:: LOGGER LogFlags
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.20}|C{0.25}|S{0.55}|
   :header-rows: 1

   * :attr,10: Bits
     :val,15:  Values
     :desc,75: Description

   * :attr:    :xmlref:`LogFlags` [xxxx.xxxx]
     :val:     0...0xFF
     :desc:    LogFlags is 8 bit encoded variable. Logfile will not be created, if value is 0

   * :attr:    Bit 0
     :val:     xxxx.xxx0
     :desc:    Link layer (of the IEC60870-5-101 communication protocol) or Transport layer (of the IEC60870-5-104 communication protocol) message recording **disabled**

   * :(attr):
     :val:     xxxx.xxx1
     :desc:    Link layer (of the IEC60870-5-101 communication protocol) or Transport layer (of the IEC60870-5-104 communication protocol) message recording **enabled**

   * :attr:    Bit 1
     :val:     xxxx.xx0x
     :desc:    Incoming message recording **disabled**

   * :(attr):
     :val:     xxxx.xx1x
     :desc:    Incoming message recording **enabled**

   * :attr:    Bit 2
     :val:     xxxx.x0xx
     :desc:    Outgoing message recording **disabled**

   * :(attr):
     :val:     xxxx.x1xx
     :desc:    Outgoing message recording **enabled**

   * :attr:    Bit 4
     :val:     xxx0.xxxx
     :desc:    Socket connection status and [Started]; [Stopped] state information for IEC60870-5-104 protocol instances or link layer state information for IEC60870-5-101 protocol instances recording **disabled**

   * :(attr):
     :val:     xxx1.xxxx
     :desc:    Socket connection status and [Started]; [Stopped] state information for IEC60870-5-104 protocol instances or link layer state information for IEC60870-5-101 protocol instances recording **enabled**

   * :attr:    Bit 7
     :val:     0xxx.xxxx
     :desc:    Only applicable to IEC60870-5-101 protocol instances; transmitted message echo (if it exists) **will not be** recorded to a logfile

   * :(attr):
     :val:     1xxx.xxxx
     :desc:    Only applicable to IEC60870-5-101 protocol instances; transmitted message echo (if it exists) **will be** recorded to a logfile

   * :attr:    Bits 3;5;6
     :val:     Any
     :desc:    Bits reserved for future use

.. _ref-EventCfg:
.. _ref-EventCfgEVENTLOG:
.. _ref-EventCfgHWEVENTLOG:

EventCfg group and EVENTLOG; HWEVENTLOG node
--------------------------------------------

Group node :ref:`EventCfg<ref-EventCfg>` and child element nodes :ref:`EVENTLOG<ref-EventCfgEVENTLOG>`; :ref:`HWEVENTLOG<ref-EventCfgHWEVENTLOG>` are used to configure decoded 
application level information (DI/AI/DO object types, addresses, values, etc) recording to logfiles. There are to 
options: 

* Record all decoded information on a serial/Ethernet interface;
* Record the decoded information only related to a particular communication protocol instance.

:ref:`EventCfg<ref-EventCfg>` node is used to record decoded information only related to a specific communication protocol 
instance. :ref:`HWEVENTLOG<ref-EventCfgHWEVENTLOG>` node on the other hand is used to record all decoded information on a serial/Ethernet 
interface. These two methods become very useful and provide flexible filtering options in case more than 1 
communication protocol instance share the same hardware interface (e.g. IEC 60870-5-101 controlling station 
(Master) instances communicating to multiple outstations).

Please see sample :ref:`EventCfg<ref-EventCfg>` group node and :ref:`EVENTLOG<ref-EventCfgEVENTLOG>`; :ref:`HWEVENTLOG<ref-EventCfgHWEVENTLOG>` child element nodes below. The 
sample contains configuration of 2 individual communication protocol instance logfiles and 1 serial interface 
logfile.

.. code-block:: none

   <EventCfg> 
      <EVENTLOG Index="5" LogFlags="0x3F" HourLimit="0" Mode="0" Logfile="Events/101slave"/> 
      <EVENTLOG Index="6" LogFlags="0x0C" Logfile="Events/101slave_test2"/> 
      <HWEVENTLOG HWIndex="1" LogFlags="0x40" HourLimit="0" Logfile="Events/COM1_events"/> 
   </EventCfg>

Please see sample :ref:`EVENTLOG<ref-EventCfgEVENTLOG>` and :ref:`HWEVENTLOG<ref-EventCfgHWEVENTLOG>` element node below listing all available attributes.

.. code-block:: none

   <EVENTLOG   Index="5"
               LogFlags="0xFF"
               Mode="0"
               HourLimit="4"
               Logfile="Events/101slave"
               Name="IED Events" />
   
   
   <HWEVENTLOG HWIndex="1"
               LogFlags="0x06"
               Mode="0"
               HourLimit="4"
               Logfile="Events/COM1"
               Name="All IED Events" />

.. tip:: Attributes of the :ref:`EVENTLOG<ref-EventCfgEVENTLOG>` and :ref:`HWEVENTLOG<ref-EventCfgHWEVENTLOG>` element nodes can be arranged in any order, it will not affect the XML file validation.

EVENTLOG and HWEVENTLOG attributes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _ref-EventCfgEVENTLOGAttributes:

.. field-list-table:: EVENTLOG and HWEVENTLOG attributes
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.20}|C{0.25}|S{0.55}|
   :header-rows: 1

   * :attr,10: Attribute
     :val,15:  Values or range
     :desc,75: Description

   * :attr:    :xmlref:`Index`
     :val:     1...254
     :desc:    Index attribute is used to enable logging for a particular communication protocol instance. Use value of the :ref:`Index<ref-IEC101maIndex>` attribute of any communication protocol instance in order to enable logging. :inlineimportant:`Attribute is mandatory for` :ref:`EVENTLOG<ref-EventCfgEVENTLOG>` :inlineimportant:`node, it is not required for` :ref:`HWEVENTLOG<ref-EventCfgHWEVENTLOG>` :inlineimportant:`node.` :inlinetip:`Indexes don't have to be in a sequential order.`

   * :attr:    :xmlref:`HWIndex`
     :val:     1...254
     :desc:    Index attribute is used to enable logging for a hardware node. Use value of the :ref:`UART<ref-UART>`.\ :ref:`Index<ref-UARTIndex>` \; :ref:`TCPSERVER<ref-TCPSERVER>`.\ :ref:`Index<ref-TCPSERVERIndex>` \; :ref:`TCPCLIENT<ref-TCPCLIENT>`.\ :ref:`Index<ref-TCPCLIENTIndex>` \ or :ref:`UDP<ref-UDP>`.\ :ref:`Index<ref-UDPIndex>` \ attribute in order to enable logging. :inlineimportant:`Attribute is mandatory for` :ref:`EVENTLOG<ref-EventCfgEVENTLOG>` :inlineimportant:`node, it is not required for` :ref:`HWEVENTLOG<ref-EventCfgHWEVENTLOG>` :inlineimportant:`node.` :inlinetip:`Indexes don't have to be in a sequential order.`

   * :attr:    :xmlref:`LogFlags`
     :val:     See table :numref:`ref-EventCfgLogFlagsBits` for description
     :desc:    Log flags specify type of information to be recorded to the logfile. Logfile will not be created, if value is 0.

   * :attr:    .. _ref-EventCfgEVENTLOGLogfile:
               
               :xmlref:`Logfile`
     :val:     Max 200 chars
     :desc:    Event logfile name without an extension, but including absolute or relative path. Logfile will be created in the same folder as leandc firmware if path is not specified. The date and extension 'event' will be added to the file name automatically. Logfile will not be created if attribute is left blank. (default entry 'Events/aaa', where 'aaa' is name of the file) :inlineimportant:`Attribute is case sensitive, observe the case of path and file name when specifying.`

   * :attr:    .. _ref-EventCfgEVENTLOGMode:
               
               :xmlref:`Mode`\*
     :val:     See table :numref:`ref-LoggerModeBits` for description
     :desc:    New logfile initialization settings. (default value 1) :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default settings will be used if omitted.`

   * :attr:    .. _ref-EventCfgEVENTLOGHourLimit:
   
               :xmlref:`HourLimit`\*
     :val:     0...12
     :desc:    New file will be created after selected number of hours in order to limit the size. (default 6 hours) :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default settings will be used if omitted.`

   * :attr:    :xmlref:`Name`
     :val:     Max 100 chars
     :desc:    Freely configurable name, just for reference. :inlinetip:`Name attribute is optional and doesn't have to be included in configuration.`

.. tip::
   \* Please refer to the (:ref:`ref<ref-LogfileSampleList>`) for sample list of files created with various :ref:`EVENTLOG<ref-EventCfgEVENTLOG>`.\ :ref:`HourLimit<ref-EventCfgEVENTLOGHourLimit>` \ and :ref:`EVENTLOG<ref-EventCfgEVENTLOG>`.\ :ref:`Mode<ref-EventCfgEVENTLOGMode>` \ attribute settings.

 
EVENTLOG.LogFlags
^^^^^^^^^^^^^^^^^

.. _ref-EventCfgLogFlagsBits:

.. field-list-table:: EVENTLOG LogFlags
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.20}|C{0.25}|S{0.55}|
   :header-rows: 1

   * :attr,10: Bits
     :val,15:  Values
     :desc,75: Description

   * :attr:    :xmlref:`LogFlags` [xxxx.xxxx]
     :val:     0...0xFF
     :desc:    LogFlags is 8 bit encoded variable. Logfile will not be created, if value is 0

   * :attr:    Bit 0
     :val:     xxxx.xxx0
     :desc:    Received/sent spontaneous (event) DI information **will not be** recorded to event logfile

   * :(attr):
     :val:     xxxx.xxx1
     :desc:    Received/sent spontaneous (event) DI information **will be** recorded to event logfile

   * :attr:    Bit 1
     :val:     xxxx.xx0x
     :desc:    Received/sent spontaneous (event) AI information **will not be** recorded to event logfile

   * :(attr):
     :val:     xxxx.xx1x
     :desc:    Received/sent spontaneous (event) AI information **will be** recorded to event logfile

   * :attr:    Bit 2
     :val:     xxxx.x0xx
     :desc:    Received/sent control/setpoint command information **will not be** recorded to event logfile

   * :(attr):
     :val:     xxxx.x1xx
     :desc:    Received/sent control/setpoint command information **will be** recorded to event logfile

   * :attr:    Bit 3
     :val:     xxxx.0xxx
     :desc:    Processed command information and related error messages **will not be** recorded to event logfile

   * :(attr):
     :val:     xxxx.1xxx
     :desc:    Processed command information and related error messages **will be** recorded to event logfile

   * :attr:    Bit 4
     :val:     xxx0.xxxx
     :desc:    Received/sent static (General Interrogation) DI information **will not be** recorded to event logfile

   * :(attr):
     :val:     xxx1.xxxx
     :desc:    Received/sent static (General Interrogation) DI information **will be** recorded to event logfile

   * :attr:    Bit 5
     :val:     xx0x.xxxx
     :desc:    Received/sent static (General Interrogation) AI information **will not be** recorded to event logfile

   * :(attr):
     :val:     xx1x.xxxx
     :desc:    Received/sent static (General Interrogation) AI information **will be** recorded to event logfile

   * :attr:    Bit 6
     :val:     x0xx.xxxx
     :desc:    Received/sent cyclic AI information **will not be** recorded to event logfile

   * :(attr):
     :val:     x1xx.xxxx
     :desc:    Received/sent cyclic AI information **will be** recorded to event logfile

   * :attr:    Bit 7
     :val:     Any
     :desc:    Bits reserved for future use

LOGGER.Mode and EVENTLOG.Mode
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _ref-LoggerModeBits:

.. field-list-table:: Mode attribute
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.20}|C{0.25}|S{0.55}|
   :header-rows: 1

   * :attr,10: Bits
     :val,15:  Values
     :desc,75: Description

   * :attr:    :xmlref:`Mode` [xxxx.xxxx]
     :val:     0...0xFF
     :desc:    Mode is 8 bit encoded variable

   * :attr:    Bit 0
     :val:     xxxx.xxx0
     :desc:    New logfile **will be** created each time leandc firmware is being started/restarted

   * :(attr):
     :val:     xxxx.xxx1
     :desc:    New logfile **will not be** created, providing a logfile with the same date string already exists upon leandc firmware start/restart. In this case new entries will be appended to the end of the existing logfile.

   * :attr:    Bits 1...6
     :val:     Any
     :desc:    Bits reserved for future use

Please note new communication traffic logfile will be created every time leandc firmware is started/restarted, if 
:ref:`LOGGER<ref-CommsCfgLOGGER>`.\ :ref:`Mode<ref-CommsCfgLOGGERMode>` \ attribute is 0 (default value). :ref:`LOGGER<ref-CommsCfgLOGGER>`.\ :ref:`HourLimit<ref-CommsCfgLOGGERHourLimit>` \ attribute controls the interval of creating new 
logfile if leandc firmware is running without being restarted. By default new logfile is created every 4 hours 
(:ref:`LOGGER<ref-CommsCfgLOGGER>`.\ :ref:`HourLimit<ref-CommsCfgLOGGERHourLimit>` \ default value).

.. _ref-LogfileSampleList:

.. tip::

   File creation date and hour (format yyyy-mm-dd_hh) is added to the name of the file specified in :ref:`LOGGER<ref-CommsCfgLOGGER>`.\ :ref:`Logfile<ref-CommsCfgLOGGERLogfile>` \. Please see sample list of files created, if leandc firmware is running without being restarted.
      
   * 'logfile_2013-04-12_00.log'
   * 'logfile_2013-04-12_04.log'
   * 'logfile_2013-04-12_08.log'
   * 'logfile_2013-04-12_12.log'
      
   Time tag (format hhmmss) is also added to the name of the file specified in :ref:`LOGGER<ref-CommsCfgLOGGER>`.\ :ref:`Logfile<ref-CommsCfgLOGGERLogfile>` \, if leandc firmware restarts. Please see sample list of files created, if leandc firmware is being restarted at 14:04:13 and 14:07:32.
   
   * 'logfile_2013-04-12_12.log'
   * 'logfile_2013-04-12_140413.log'
   * 'logfile_2013-04-12_140732.log'
   * 'logfile_2013-04-12_16.log'

Default settings for application level information event files are slightly different. New event file will not be 
created upon leandc firmware restart, if :ref:`EVENTLOG<ref-EventCfgEVENTLOG>`.\ :ref:`Mode<ref-EventCfgEVENTLOGMode>` \ attribute is 1 (default value). New entires are 
appended to an existing file after firmware restart. :ref:`EVENTLOG<ref-EventCfgEVENTLOG>`.\ :ref:`HourLimit<ref-EventCfgEVENTLOGHourLimit>` \ attribute controls the interval of 
creating new event file if leandc firmware is running without being restarted. By default new event file is created 
every 6 hours (:ref:`EVENTLOG<ref-EventCfgEVENTLOG>`.\ :ref:`HourLimit<ref-EventCfgEVENTLOGHourLimit>` \ default value).

.. tip::

   File creation date and hour (format yyyy-mm-dd_hh) is added to the name of the file specified in :ref:`EVENTLOG<ref-EventCfgEVENTLOG>`.\ :ref:`Logfile<ref-EventCfgEVENTLOGLogfile>` \. Please see sample list of files created, regardless if leandc firmware is being restarted or not.

   * '104events_2013-04-12_00.event'
   * '104events_2013-04-12_06.event'
   * '104events_2013-04-12_12.event'
   * '104events_2013-04-12_18.event'      


