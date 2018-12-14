.. include:: global.roles

.. _docref-Docreleases:

Document version control
========================

This manual was published with the following leandc firmware release. 

.. field-list-table:: Compatibility with leandc firmware
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.25}|C{0.25}|
   :header-rows: 1

   * :attr,20: Firmware version
     :val,20:  Date
     :osv,60:  Required Operating System version

   * :attr:    4.10
     :val:     2018-12-12 13:14:10
     :osv:     V3.0 or V4.0

.. tip::

   Use argument -v to check firmware revision and build date:
   **leandc -v**


.. field-list-table:: Previous Firmware releases
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.15}|C{0.15}|C{0.15}|S{0.55}|
   :header-rows: 1

   * :fw,10:	Firmware version
     :fdate,10:	Firmware date
     :doc,10:	Manual version(s)
     :osv,10:	Operating System version

   * :fw:       4.09
     :fdate:    2018-03-05 15:55:30
     :doc:      V33
     :osv:      V3.0

   * :fw:       4.08
     :fdate:    2018-02-26 16:06:36
     :doc:      V32
     :osv:      V3.0

   * :fw:       4.07
     :fdate:    2017-08-14 17:02:51
     :doc:      V31
     :osv:      V3.0

   * :fw:       4.06
     :fdate:    2017-07-31 14:37:41
     :doc:      V31
     :osv:      V3.0

   * :fw:       4.05
     :fdate:    2017-03-16 06:32:27
     :doc:      V31
     :osv:      V3.0

   * :fw:       4.04
     :fdate:    2017-02-02 17:08:45
     :doc:      V30
     :osv:      V3.0

   * :fw:       4.03
     :fdate:    2016-07-25 17:04:55
     :doc:      V29
     :osv:      V3.0

   * :fw:       4.02
     :fdate:    2016-07-14 19:27:51
     :doc:      V29
     :osv:      V3.0

   * :fw:       4.01
     :fdate:    2016-05-18 12:57:20
     :doc:      V28
     :osv:      V3.0

   * :fw:       4.00
     :fdate:    2016-05-08 11:22:30
     :doc:      V27
     :osv:      V3.0

   * :fw:	3.14
     :fdate:	2015-09-04 10:05:40
     :doc:	V26
     :osv:	V2.0

   * :fw:	3.13
     :fdate:	2015-08-24 21:04:07
     :doc:	V25
     :osv:	V2.0

   * :fw:	3.12
     :fdate:	2015-08-11 12:36:44
     :doc:	V25
     :osv:	V2.0

   * :fw:	3.11
     :fdate:	2015-07-08 14:07:37
     :doc:	V24
     :osv:	V2.0

   * :fw:	3.10
     :fdate:	2015-06-29 15:52:23
     :doc:	V24
     :osv:	V2.0

   * :fw:	3.09
     :fdate:	2015-03-25 10:57:25
     :doc:	V23
     :osv:	V2.0

   * :fw:	3.08
     :fdate:	2015-03-24 21:06:41
     :doc:	V23
     :osv:	V2.0

   * :fw:	3.07
     :fdate:	2015-02-15 17:55:25
     :doc:	V22
     :osv:	V2.0

   * :fw:	3.06
     :fdate:	2014-12-01 08:47:07
     :doc:	V21
     :osv:	V2.0

   * :fw:	3.05
     :fdate:	2014-11-28 11:39:37
     :doc:	V21
     :osv:	V2.0

   * :fw:	3.04
     :fdate:	2014-10-08 15:43:46
     :doc:	V20
     :osv:	V2.0

   * :fw:	3.02
     :fdate:	2014-06-26 14:48:34
     :doc:	V19
     :osv:	V2.0

   * :fw:	3.01
     :fdate:	2014-05-28 12:20:12
     :doc:	V18
     :osv:	V2.0

   * :fw:	3.00
     :fdate:	2014-05-26 21:19:06
     :doc:	V18
     :osv:	V2.0

   * :fw:	2.07
     :fdate:	2014-04-08 20:59:57
     :doc:	V17
     :osv:	V2.0

   * :fw:	2.06
     :fdate:	2014-03-31 14:58:09
     :doc:	V16
     :osv:	V2.0

   * :fw:	2.05
     :fdate:	2014-02-26 20:20:30
     :doc:	V15
     :osv:	V2.0

   * :fw:	2.04
     :fdate:	2013-12-18 08:55:06
     :doc:	V13, V14
     :osv:	V2.0

   * :fw:	2.01
     :fdate:	2013-10-16 17:21:27
     :doc:	V12
     :osv:	V2.0


.. field-list-table:: Document version control
   :class: table table-condensed table-bordered version-control longtable
   :spec: |C{0.15}|C{0.15}|C{0.15}|S{0.55}|
   :header-rows: 1

   * :ver,5:	Version
     :date,5:	Date
     :by,5:	By
     :desc,85:	Comments

   * :ver:	V34
     :date:	14/12/2018
     :by:	AK
     :desc:	| > :xmlref:`orCat` and :xmlref:`orIdent` attributes added to :ref:`<ref-IEC61850clAppSettings>` node. Values are used for sending control commands to IED;
		| > Bit[2] added to :ref:`<ref-IEC61850clAppSettings>`.\ :ref:`<ref-IEC61850clAppFlags>` attribute, use millisecond accuracy of timetags received from IED;
		| > Bit[4] added to :ref:`<ref-IEC61850clAppSettings>`.\ :ref:`<ref-IEC61850clAppFlags>` attribute, Ignore Resv attribute value of the Unbufferred report control block received from IED;
		| > Bit[8] added to :ref:`<ref-IEC61850clAppSettings>`.\ :ref:`<ref-IEC61850clAppFlags>` attribute, enable all report control block found in the SCL file;
		| > :ref:`<ref-IEC61850clPresentationSettings>`.\ :ref:`<ref-IEC61850clPresentationFlags>` attribute created;
		| > Bit[0] of the :ref:`<ref-IEC61850clTransportSettings>`.\ :ref:`Flags<ref-IEC61850clTransportFlagsBits>` attribute controls destination reference checks and Bit[1] - Calling/Called Transport Selector checks;
		| > Bit[0] of the :ref:`<ref-IEC61850clSessionSettings>`.\ :ref:`Flags<ref-IEC61850clSessionFlagsBits>` attribute controls Calling/Called Session Selector checks and Bit[1] - keeping transport connection open after finishig session;
		| > Bit[6] added to IEC61850 client :ref:`DI<ref-IEC61850clDI>`.\ :ref:`Qualifier<ref-IEC61850clDIqualifierBits>` and :ref:`AI<ref-IEC61850clAI>`.\ :ref:`Qualifier<ref-IEC61850clAIqualifierBits>` attributes, non-persistent dynamic dataset support;
		| > Bit[6] added to IEC61850 client :ref:`DO<ref-IEC61850clDO>`.\ :ref:`Qualifier<ref-IEC61850clDOqualifierBits>` and :ref:`AO<ref-IEC61850clAO>`.\ :ref:`Qualifier<ref-IEC61850clAOqualifierBits>` attributes, control Test bit support;
		| > Bit[1] Synchrocheck and Bit[2] Interlock added to IEC61850 client :ref:`AO<ref-IEC61850clAO>`.\ :ref:`Qualifier<ref-IEC61850clAOqualifierBits>` attribute
		| Decode AI as 32bit Integer and 16bit Binary Coded Decimal (BCD) options added to Modbus Master :ref:`AI<ref-ModbusmaAI>`.\ :ref:`<ref-ModbusmaAIType>` attribute;
		| Encode date and time as 16bit Binary Coded Decimal (BCD) little endian option added to Modbus Master :ref:`<ref-ModbusmaTimeSettings>` types;
		| > Bit[6] added to :ref:`<ref-CommsCfgPCAPLOG>`.\ :ref:`<ref-CommsCfgPCAPLOGLogFlags>` attribute, SSH (TCP port 22) traffic capture enable flag;
		| > System log levels can be enabled Bits[0..2] of the :ref:`<ref-SYSLOGFILE>`.\ :ref:`<ref-SYSLOGFILELogFlags>` attribute.

   * :ver:	V33
     :date:	21/03/2018
     :by:	AK
     :desc:	| > :ref:`AI<ref-IEC103maAI>`.\ :ref:`<ref-IEC103maAIDIAndIndex>` and :ref:`AI<ref-IEC103maAI>`.\ :ref:`<ref-IEC103maAILogicValue>` attributes added to IEC60870-5-103 Master

   * :ver:	V32
     :date:	20/03/2018
     :by:	AK
     :desc:	| Modbus Master protocol messages can be defined in XML, nodes :ref:`InitMessages<ref-InitMessages>`, :ref:`PollMessages<ref-PollMessages>`, :ref:`CtrlMessages<ref-CtrlMessages>`, :ref:`<ref-ModbusmaTimeSettings>`, :ref:`<ref-ModbusmaPeriodic>` created;
		| > :ref:`<ref-IEC61850clAssociationSettings>`.\ :ref:`<ref-IEC61850clAssociationFlags>` attribute created for IEC61850 Client;
		| > Bit[2] added to :ref:`<ref-IEC61850clScsmSettings>`.\ :ref:`<ref-IEC61850clScsmFlags>` attribute, enables to read Basic Types of all objects when station goes online;
		| > :ref:`<ref-IEC61850cl>`.\ :ref:`<ref-IEC61850clIEDname>` attribute created, used if SCL file contains more than one IED;
		| > :xmlref:`DO`, :xmlref:`DIEVsize` and  :xmlref:`AIEVsize` attributes removed from IEC60870-5-101/104 Slave :ref:`<ref-IEC101slBufferSizes>` node;
		| > :xmlref:`BufferSizes` node removed from IEC60870-5-101/104 Master :ref:`ProtocolCfg<ref-IEC101maProtocolCfg>` group.

   * :ver:	V31
     :date:	16/03/2017
     :by:	AK
     :desc:	| > :xmlref:`IgnoreTimetags` attribute can have value 2 which enables to substitute timestamp of received events if a received timetag is in future compared to the local time.
		| > :xmlref:`MaxTxDelay` and :xmlref:`MaxStations` attributes added to :ref:`<ref-UART>` node. Dynamic transmit delay feature introduced allowing to automatically adjust transmit delay depending on a number of outstations being communicated to via the serial port.

   * :ver:	V30
     :date:	02/02/2017
     :by:	AK
     :desc:	| > :ref:`<ref-UARTCOM>` attribute in :ref:`<ref-UART>` node can have value 0;
		| > Default value of the :xmlref:`ControlLockTimer` attribute changed to 20 seconds;
		| > :xmlref:`LEIODC-X32-4000`; :xmlref:`LEIODC-X10-4000`; :xmlref:`LEIODC-X32-0400`; :xmlref:`LEIODC-X10-0400`; :xmlref:`LEIODC-X32-2200`; :xmlref:`LEIODC-X10-2200` types added to Modbus Master :xmlref:`Hardcoded` node;

   * :ver:	V29
     :date:	14/07/2016
     :by:	AK
     :desc:	| > :xmlref:`TxAllVarLength` :inlineimportant:`attribute of IEC60870-5-101 Master and Slave protocols converted to Link layer` :ref:`<ref-IEC101slLinkSettingsFlags>`
		| > :xmlref:`SingleCharACK` :inlineimportant:`and` :xmlref:`FCBMaskLinkReq` :inlineimportant:`attributes of IEC60870-5-101 Slave protocol converted to Link layer` :ref:`<ref-IEC101slLinkSettingsFlags>`
		| > :ref:`<ref-IEC103maLinkSettingsFlags>` attribute added to IEC60870-5-103 Master :ref:`<ref-IEC103maLinkSettings>` node;

   * :ver:	V28
     :date:	18/05/2016
     :by:	AK
     :desc:	| > :ref:`<ref-UARTCOM>` attribute added to :ref:`<ref-UART>` node;

   * :ver:	V27
     :date:	08/05/2016
     :by:	AK
     :desc:	| :inlineimportant:`Bit[5] of the IEC60870-5-101/104 Slave protocol` :ref:`DO<ref-IEC10xslDO>`.\ :ref:`qualifier<ref-IEC10xslDOqualifierBits>` :inlineimportant:`and` :ref:`AO<ref-IEC10xslAO>`.\ :ref:`qualifier<ref-IEC10xslAOqualifierBits>` :inlineimportant:`is inverted. From now on Direct and Select-before-Execute commands will be accepted by default, i.e. if the DO/AO qualifier is not specified or 0x00. Use value 0x20 to accept only Direct commands.`
		| > :xmlref:`IEC61850cl` (Client) communication protocol instance added;
		| > :xmlref:`DOProc` and :xmlref:`AOProc` attributes added to IEC60870-5-101/104 Slave :ref:`<ref-IEC101slASDUSettings>` node;
		| > :ref:`<ref-IEC101maASDUSettingsTimetagFBrange>` attribute added to IEC60870-5-101 Master :ref:`<ref-IEC101maASDUSettings>` node;
		| > :ref:`<ref-IEC101maASDUSettingsFlags>` attribute added to IEC60870-5-101/104 Master :ref:`<ref-IEC101maASDUSettings>` node;
		| > :ref:`<ref-IEC10xmaDIInterDelay>` and :ref:`<ref-IEC10xmaDIIndetDelay>` attributes added to IEC60870-5-101/103/104 Master :ref:`DI<ref-IEC10xmaDI>` node;
		| > Bit[5] added to the IEC60870-5-101/103/104 Master protocol :ref:`DI<ref-IEC10xmaDI>`.\ :ref:`qualifier<ref-IEC10xmaDIqualifierBits>`, it enables to select First or Last time tag for DPI reporting if Intermediate state is masked;
		| > :ref:`<ref-UARTWatchdog>` attribute added to :ref:`<ref-UART>` node;
		| > New :ref:`<ref-LogSettings>` node created with attributes :ref:`<ref-SettingsCleanOlder>` and :ref:`<ref-SettingsMinFreespace>`;
		| > New :ref:`<ref-CommsCfgPCAPLOG>` node created which enables to capture traffic through Ethernet interfaces in a pcap format;
		| Default value columns added to attribute tables;
		| Recorded logfile samples and description of keywords/identifiers added;

   * :ver:	V26
     :date:	04/09/2015
     :by:	AK
     :desc:	| > :xmlref:`ClassIgnore` attribute added to IEC60870-5-101 Slave :xmlref:`LinkSettings` node which can be used to ignore class of the received messages

   * :ver:	V25
     :date:	11/08/2015
     :by:	AK
     :desc:	| > :xmlref:`TimeSync` attribute added to IEC60870-5-104 Master :xmlref:`Periodic` node which can be used to enable periodic Time Synchronization commands;
		| > :xmlref:`TimeSync` attribute added to IEC60870-5-104 Master :xmlref:`Broadcast` node to enable broadcast Common Address of ASDU (CAA) for outgoing Time Synchronization commands;
		| > :xmlref:`TimeSync` attribute added to IEC60870-5-104 Slave :xmlref:`ASDUSettings` node to enable internal clock synchronization when command is received;
		| > :xmlref:`LEIODC-X32-3100`, :xmlref:`LEIODC-X10-3100` and :xmlref:`THT2` types added to Modbus Master :xmlref:`Hardcoded` node

   * :ver:	V24
     :date:	29/06/2015
     :by:	AK
     :desc:	| > :xmlref:`DIEventStartup` and :xmlref:`AIEventStartup` attributes added to IEC60870-5-101/4 Slave :xmlref:`ASDUSettings` node;
		| > :xmlref:`OffIndex` attribute added to IEC60870-5-101/4 Slave :xmlref:`DI` node for single to double point indication conversion;
		| > :xmlref:`DIInterDelay` and :xmlref:`DIIndetDelay` attributes added to IEC60870-5-101/4 Slave :xmlref:`ASDUSettings` node and corresponding attributes :xmlref:`InterDelay` and :xmlref:`IndetDelay` added to DI node;
		| > Bit[5] added to IEC60870-5-101/4 Slave DI qualifier attribute which enables to select time tag when single status information is converted to double;
		| > :xmlref:`ChatterFilter` attribute added to Modbus Master DI node;
		| > :xmlref:`PulseDuration` attribute added to Modbus Master DO node;
		| > :xmlref:`LEIODC-C32-3100` type added to Modbus Master :xmlref:`Hardcoded` node;

   * :ver:	V23
     :date:	24/03/2015
     :by:	AK
     :desc:	| > :xmlref:`IgnoreWhileLinkcnt` attribute added to IEC60870-5-101 Master :xmlref:`LinkSettings` node;

   * :ver:	V22
     :date:	15/02/2015
     :by:	AK
     :desc:	| > :xmlref:`Interface` and :xmlref:`Test` attributes added to :xmlref:`UART` node;
		| > :xmlref:`TimeZone` attribute added to all logfile configuration nodes;
		| > :xmlref:`DOType` and :xmlref:`AOType` attributes added to IEC60870-5-101/4 Slave protocols. These can be used to create common filters for incoming command ASDU types;
		| > :xmlref:`ForwardGI` attribute added to all :xmlref:`ASDUSettings` nodes. GI commands will be forwarded to downstream outstations if received from upstream station by default. This feature can be disabled with :xmlref:`ForwardGI` attribute;
		| > :xmlref:`ServiceSettings` node and attributes added to all protocol configurations;
		| > :xmlref:`DIEvent` and :xmlref:`AIEvent` attributes renamed to :xmlref:`DIEVsize` and :xmlref:`AIEVsize` respectively;
		| > :xmlref:`DIEVmult` and :xmlref:`AIEVmult` attributes added to IEC60870-5-101/4 Slave protocol :xmlref:`BufferSizes` nodes;
		| > :xmlref:`DisabledNT` attribute removed, service settings can be used from now on to enable the functionality;
		| > :xmlref:`PostOfflineDelay` attribute added to all Master protocol configurations. Together with :xmlref:`ServiceSettings` node and attributes this extends configuration flexibility of DI/AI object quality marking when stations goes OFFLINE;
		| > :xmlref:`Reset` attribute added to IEC60870-5-101/4 Master protocol :xmlref:`Broadcast` node. This enables to send Reset Process commands to dowstream stations using Broadcast Common address of ASDU;
		| > :xmlref:`Miscellaneous` node added to IEC60870-5-101 Master protocol. Attributes :xmlref:`TimeSyncIOA` and :xmlref:`DayOfWeek` enable to customize Information Object Address (IOA) and supress Day Of Week use in outgoing Time Synchronziation commands respectively;

   * :ver:	V21
     :date:	28/11/2014
     :by:	AK
     :desc:	| :xmlref:`Modbusma` communication protocol instance added;
		| Leandc XML configuration manual is HTML-based from now on;

   * :ver:	V20
     :date:	09/10/2014
     :by:	AK
     :desc:	:xmlref:`DIEventStartup` attribute added to IEC60870-5-101/3/4 Master protocol configuration;

   * :ver:	V19
     :date:	26/06/2014
     :by:	AK
     :desc:	| All protocol setting node elements migrated to attributes;
		| New option to mark DI/AI objects with NT bit when outstation goes offline or is disabled using service command. IEC60870-5-101/4 Master protocol attributes :xmlref:`OfflineNTDelay` and :xmlref:`DisabledNT`;
		| Option to send valid AIEVs to SCADA system on leandc startup in order to initialize the state of legacy spontaneous-only AIEVs. Valid AIEVs with 0 value will be sent after a number of seconds specified in :xmlref:`LegacyAIEVinitdelay` attribute on system startup in order to initialize SCADA database and make it ready to receive first legacy AIEV.
		| :xmlref:`StationID` attribute added to :xmlref:`IEC104Csl` node;
		| :xmlref:`TypeID` attribute added to IEC60870-5-101/4 Master DI/AI objects;
		| :xmlref:`SingleCharACK` attribute added for IEC60870-5-101 Slave protocol allowing to respond with single character (0xE5 or 0xA2) ACK or NACK messages;

   * :ver:	V18
     :date:	28/05/2014
     :by:	AK
     :desc:	| Multiple ASDU configuration concept using station identifier :xmlref:`StationID` attribute, which has been added to IEC104sl and IEC104ma element nodes. Existing :xmlref:`LinkAddr` attribute is used as station identifier for :xmlref:`IEC101sl`; :xmlref:`IEC101ma` and :xmlref:`IEC103ma` element nodes.
		| All :xmlref:`ASDUAddr` attributes removed from individual DI/AI/DO/AO nodes;
		| New concept of protocol setting node element migration to attributes begins with this firmware release;  First protocol element nodes to contain setting attributes are:  :xmlref:`XMLSettings`; :xmlref:`CommsSettings`; :xmlref:`ASDUFlags`; :xmlref:`Broadcast` and :xmlref:`Periodic`;
		| Information address sequence check across object types introduced. It is essential to use new attribute :xmlref:`IOAOverlap` if the same information addresses are being reused for DI/AI/DO/AO objects. :xmlref:`IOAOverlap` is attribute of the newly created :xmlref:`XMLSettings` element node;
		| IEC60870-5-101/4 Slave protocol configuration :xmlref:`StartupGIDelay` element migrated to become an attribute of the newly created :xmlref:`CommsSettings` element node;
		| :xmlref:`TranspTypes` attribute created for IEC60870-5-101/4 Slave protocol configuration;
		| IEC60870-5-101/4 Master protocol configuration :xmlref:`OnlineGIDelay` element migrated to become an attribute of the newly created :xmlref:`CommsSettings` element node;
		| New option to send General Interrogation using broadcast Common address of ASDU can be configured using GI attribute in IEC60870-5-101/4 :xmlref:`Broadcast` element node;
		| IEC60870-5-101/4 Master protocol configuration :xmlref:`GlobalTimeSync` element migrated to become an attribute :xmlref:`TimeSync` of the newly created :xmlref:`Broadcast` element node;
		| IEC60870-5-101/4 Master protocol configuration periodic :xmlref:`GIInterval`; :xmlref:`Group1Interval`... :xmlref:`Group16Interval`; :xmlref:`TimeSyncInterval` elements migrated to become attributes :xmlref:`GI`; :xmlref:`Group1`... :xmlref:`Group16`; :xmlref:`TimeSync` respectively of the newly created :xmlref:`Periodic` element node;
		| Default values of :xmlref:`DIEventBuffSize` and :xmlref:`AIEventBuffSize` elements are automatically initialized to twice the amount of configured objects, instead of fixed value 1024 as used to before;

   * :ver:	V17
     :date:	08/04/2014
     :by:	AK
     :desc:	| Automatic IEC60870-5-101/4 Slave protocol configuration re-enabled;
		| :xmlref:`Source` attribute created for IEC60870-5-101/4 Slave protocols and :xmlref:`Device` attribute in DI/AI/DO/AO object elements is no longer mandatory;
		| :xmlref:`GIStartupDelay` element created for IEC60870-5-101/4 Slave protocols;
		| Bit[4] removed from Slave DI :xmlref:`qualifier` attribute;
		| AI :xmlref:`StartOffset` and :xmlref:`OffsetDeadband` attributes created for IEC60870-5-101/4 Slave AI objects;
		| Bits[5...6] removed from Slave AI :xmlref:`qualifier` attribute;
		| :xmlref:`AIEventStartup` element created for IEC60870-5-101/3/4 Master protocols;
		| AI :xmlref:`StartOffset`; :xmlref:`ZeroDeadband`; :xmlref:`Offset`; :xmlref:`OffsetDeadband` and :xmlref:`NonZeroOffset` attributes created for IEC60870-5-101/3/4 Master AI objects;

   * :ver:	V16
     :date:	31/03/2014
     :by:	AK
     :desc:	| Supervision functionality added;
		| UART :xmlref:`Timeout`; :xmlref:`TxDelay` and :xmlref:`CtrlRdTimeout` ranges changed;
		| UART :xmlref:`DataBits`; :xmlref:`StopBits` and :xmlref:`TxDelay` attributes are no longer mandatory;
		| Socket node name changed from :xmlref:`IPv4` to :xmlref:`TCPSERVER` and :xmlref:`TCPCLIENT` and related :xmlref:`Mode` and :xmlref:`Type` attributes removed;
		| New :xmlref:`UDP` socket node created;
		| Socket :xmlref:`IPport` attribute name changed to :xmlref:`Port`;
		| New socket attributes :xmlref:`ConnectTimeout`; :xmlref:`Timeout`; :xmlref:`TxDelay` and :xmlref:`IdleTimeout` created;
		| IEC60870-5-101 master and slave protocol instances can now be linked to :xmlref:`TCPSERVER`; :xmlref:`TCPCLIENT` and :xmlref:`UDP` socket nodes;
		| Multiple IEC60870-5-104 master protocol instances can now be linked to the same :xmlref:`TCPCLIENT` socket node;
		| Bit[3] added to :xmlref:`CommsFlags` attribute to select either accept or reject new incoming connection to TCP server if linked protocol instance is already connected;
		| :xmlref:`TxAllVarLength` node added for IEC60870-5-101 master and slave protocols;
		| IEC60870-5-104 master :xmlref:`OfflineDelay` node can have value 0 now and default value changed to 6sec;
		| Description of the logger :xmlref:`LogFlags` attribute Bit[4] updated to include IEC60870-5-101 link layer status information recording

   * :ver:	V15
     :date:	26/02/2014
     :by:	AK
     :desc:	| Order of communication protocol instance definition corrected;
		| UART :xmlref:`TxDelay` sample value table added;
		| UART :xmlref:`CtrlRdTimer` and :xmlref:`CtrlRdDebounce` attributes created;
		| :xmlref:`ACDAlways` and :xmlref:`FCBMaskLinkReq` attributes created for IEC60870-5-101 Slave protocol;
		| :xmlref:`CommsFlags` attribute added for Slave protocol instances;
		| :xmlref:`OfflineDelay` default value of the IEC60870-5-101 Master protocol corrected, must be 0 and :xmlref:`OfflineDelay` element for IEC60870-5-104 Slave protocol created;
		| :xmlref:`DegradedRetries`; :xmlref:`DegradedTimeout` and :xmlref:`LinkOnlineDelay` nodes added to IEC60870-5-101 and IEC60870-5-103 Master protocols;
		| :xmlref:`GlobalGI`; :xmlref:`AIDeadband` and :xmlref:`AIPercent` nodes added to Master protocol instances;
		| :inlineimportant:`Master protocol instance nodes` :xmlref:`GlobalQOC`; :xmlref:`GlobalDOType` :inlineimportant:`and` :xmlref:`GlobalAOType` :inlineimportant:`nodes are renamed to` :xmlref:`DOQOC`; :xmlref:`DOType` :inlineimportant:`and` :xmlref:`AOType` :inlineimportant:`respectively;`
		| :inlineimportant:`Bit[5] removed  from Master protocol instance DO qualifier, use` :xmlref:`DOType` :inlineimportant:`element or individual DO object` :xmlref:`TypeID` :inlineimportant:`attributes for outgoing command ASDU Type selection;`
		| Ignore individual Time tag bit created for Master protocol DI/AI :xmlref:`qualifier`  attributes;
		| :xmlref:`Name` attributes added to all nodes;
		| New Service DI (-5) created allowing to monitor status of the UART Ring Indicator RI pin(9);
		| New Service DO (-5) created allowing to send Reset command to downstream outstation;

   * :ver:	V14
     :date:	18/01/2014
     :by:	AK
     :desc:	Version control element node added

   * :ver:	V13
     :date:	18/12/2013
     :by:	AK
     :desc:	| Multiple :xmlref:`IEC101sl` communication protocol instances can share the same serial interface;
		| :xmlref:`OfflineDelay` for :xmlref:`IEC101sl` communication protocol instance added;
		| Setpoint command configuration added;
		| :xmlref:`GlobalDOType` and :xmlref:`GlobalAOType` nodes added for Master communication protocol instances;
		| :xmlref:`IgnoreTimetags` node added for Master communication protocol instances;
		| New bit in DO/AO :xmlref:`qualifier` now enables option to accept only Direct-Execute commands;
		| DO command invert option added, enabled by setting bit[1] in Slave and Master :xmlref:`DO.qualifier`;
		| Master communication protocol instance AI processing sequence flowcharts added;

   * :ver:	V12
     :date:	18/11/2013
     :by:	AK
     :desc:	| IEC60870-5-103 Master added;
		| Unique names for communication protocol instance nodes under CommunicationCfg node;
		| Link layer and common address of ASDU (CAA) now configured using attributes in communication protocol instance nodes;
		| :xmlref:`CommsFlags` attribute created for Master communication protocol instances;
		| :xmlref:`DIEventType` and :xmlref:`AIEventType` nodes created for Slave communication protocol instances;
		| :xmlref:`SpeedUpStarted` node removed;
		| Time-tagged command support added for IEC60870-5-104 Slave and new :xmlref:`CommandLatency` node created;
		| DI/AI/DO :xmlref:`qualifier` attributes are optional from now on;
		| DI/AI/DO :xmlref:`TypeID` attributes created;
		| :xmlref:`OffIndex` attribute added to Slave communication protocol instance DO object nodes allowing to link 'On' and 'Off' commands to separate DO objects;
		| Auto-configuration temporary disabled;
		| :xmlref:`GlobalQOC` node added for Master communication protocol instances;
		| Event logfile configuration moved to lelogger.xml file;
		| :xmlref:`HWLOG` and :xmlref:`HWEVENTLOG` nodes created allowing to enable event logging for all communication protocol instances sharing the same hardware interface;
		| Static and Event DI/AI information recording to event logfiles added;
		| Slave communication protocol instance AI processing sequence flowcharts added;

   * :ver:	V11
     :date:	10/06/2013
     :by:	AK
     :desc:	Offline reporting delay timer added

   * :ver:	V10
     :date:	01/06/2013
     :by:	AK
     :desc:	Timezone configuration option added

   * :ver:	V9
     :date:	21/05/2013
     :by:	AK
     :desc:	SpeedUpStarted configuration option added

   * :ver:	V8
     :date:	14/05/2013
     :by:	AK
     :desc:	Automatic DI and AI object sorting for 'Master' and DO object sorting for 'Slave' communication protocol instances; SummerTime flag configuration added; Communication Status reporting address for Auto-configuration mode added; CommsFlags attribute added; Service DO commands added;

   * :ver:	V7
     :date:	12/04/2013
     :by:	AK
     :desc:	Minor formatting corrections; Appendix A – Analogue value processing added

   * :ver:	V6
     :date:	13/03/2013
     :by:	AK
     :desc:	HourLimit attribute description added; AI offset, AI zero deadband and 75-125 input transducer offset compensation added

   * :ver:	V5
     :date:	01/03/2013
     :by:	AK
     :desc:	Range and Automatic configuration features added; GlobalTimeSync now available; changes to logfile specification

   * :ver:	V4
     :date:	03/12/2012
     :by:	AK
     :desc:	AI value offset for 4mA transducer input compensation added to Slave protocol instances

   * :ver:	V3
     :date:	13/11/2012
     :by:	AK
     :desc:	Minor changes to DO object address sequence, new DO execution policy added

   * :ver:	V2
     :date:	03/10/2012
     :by:	AK
     :desc:	New features added, changes in DI and AI Event attribute configuration

   * :ver:	V1
     :date:	17/08/2012
     :by:	AK
     :desc:	Initial version

