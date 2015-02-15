.. include:: global.roles

.. _docref-Docreleases:

Document version control
========================

This manual was published with the following leandc firmware release. 

.. field-list-table:: Compatibility with leandc firmware
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.25}|C{0.25}|
   :header-rows: 1

   * :attr,20: Firmware Revision
     :val,80:  Date

   * :attr:    3.07
     :val:     2015-02-15 17:55:25

.. tip:: 

   Use argument -v to check firmware revision and build date:
   *./leandc -v*
   
.. field-list-table:: Document version control
   :class: table table-condensed table-bordered version-control longtable
   :spec: |C{0.15}|C{0.15}|C{0.15}|S{0.55}|
   :header-rows: 1

   * :ver,5:  Version
     :date,5: Date
     :by,5:   By
     :desc,85: Comments

   * :ver:     V1
     :date:    17/08/2012
     :by:      AK
     :desc:    Initial version

   * :ver:     V2
     :date:    03/10/2012
     :by:      AK
     :desc:    New features added, changes in DI and AI Event attribute configuration

   * :ver:     V3
     :date:    13/11/2012
     :by:      AK
     :desc:    Minor changes to DO object address sequence, new DO execution policy added

   * :ver:     V4
     :date:    03/12/2012
     :by:      AK
     :desc:    AI value offset for 4mA transducer input compensation added to Slave protocol instances

   * :ver:     V5
     :date:    01/03/2013
     :by:      AK
     :desc:    Range and Automatic configuration features added; GlobalTimeSync now available; changes to logfile specification
     
   * :ver:     V6
     :date:    13/03/2013
     :by:      AK
     :desc:    HourLimit attribute description added; AI offset, AI zero deadband and 75-125 input transducer offset compensation added
     
   * :ver:     V7
     :date:    12/04/2013
     :by:      AK
     :desc:    Minor formatting corrections; Appendix A – Analogue value processing added
     
   * :ver:     V8
     :date:    14/05/2013
     :by:      AK
     :desc:    Automatic DI and AI object sorting for 'Master' and DO object sorting for 'Slave' communication protocol instances; SummerTime flag configuration added; Communication Status reporting address for Auto-configuration mode added; CommsFlags attribute added; Service DO commands added;
     
   * :ver:     V9
     :date:    21/05/2013
     :by:      AK
     :desc:    SpeedUpStarted configuration option added
     
   * :ver:     V10
     :date:    01/06/2013
     :by:      AK
     :desc:    Timezone configuration option added
     
   * :ver:     V11
     :date:    10/06/2013
     :by:      AK
     :desc:    Offline reporting delay timer added
     
   * :ver:     V12
     :date:    18/11/2013
     :by:      AK
     :desc:    | IEC60870-5-103 Master added;
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
     
   * :ver:     V13
     :date:    18/12/2013
     :by:      AK
     :desc:    | Multiple :xmlref:`IEC101sl` communication protocol instances can share the same serial interface;
               | :xmlref:`OfflineDelay` for :xmlref:`IEC101sl` communication protocol instance added;
               | Setpoint command configuration added;
               | :xmlref:`GlobalDOType` and :xmlref:`GlobalAOType` nodes added for Master communication protocol instances;
               | :xmlref:`IgnoreTimetags` node added for Master communication protocol instances;
               | New bit in DO/AO :xmlref:`qualifier` now enables option to accept only Direct-Execute commands;
               | DO command invert option added, enabled by setting bit[1] in Slave and Master :xmlref:`DO.qualifier`;
               | Master communication protocol instance AI processing sequence flowcharts added;
     
   * :ver:     V14
     :date:    18/01/2014
     :by:      AK
     :desc:    Version control element node added
        
   * :ver:     V15
     :date:    26/02/2014
     :by:      AK
     :desc:    | Order of communication protocol instance definition corrected;
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
     
   * :ver:     V16
     :date:    31/03/2014
     :by:      AK
     :desc:    | Supervision functionality added;
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
               
   * :ver:     V17
     :date:    08/04/2014
     :by:      AK
     :desc:    | Automatic IEC60870-5-101/4 Slave protocol configuration re-enabled;
               | :xmlref:`Source` attribute created for IEC60870-5-101/4 Slave protocols and :xmlref:`Device` attribute in DI/AI/DO/AO object elements is no longer mandatory;
               | :xmlref:`GIStartupDelay` element created for IEC60870-5-101/4 Slave protocols;
               | Bit[4] removed from Slave DI :xmlref:`qualifier` attribute;
               | AI :xmlref:`StartOffset` and :xmlref:`OffsetDeadband` attributes created for IEC60870-5-101/4 Slave AI objects;
               | Bits[5...6] removed from Slave AI :xmlref:`qualifier` attribute;
               | :xmlref:`AIEventStartup` element created for IEC60870-5-101/3/4 Master protocols;
               | AI :xmlref:`StartOffset`; :xmlref:`ZeroDeadband`; :xmlref:`Offset`; :xmlref:`OffsetDeadband` and :xmlref:`NonZeroOffset` attributes created for IEC60870-5-101/3/4 Master AI objects;
               
   * :ver:     V18
     :date:    28/05/2014
     :by:      AK
     :desc:    | Multiple ASDU configuration concept using station identifier :xmlref:`StationID` attribute, which has been added to IEC104sl and IEC104ma element nodes. Existing :xmlref:`LinkAddr` attribute is used as station identifier for :xmlref:`IEC101sl`; :xmlref:`IEC101ma` and :xmlref:`IEC103ma` element nodes.
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
               
   * :ver:     V19
     :date:    26/06/2014
     :by:      AK
     :desc:    | All protocol setting node elements migrated to attributes;
               | New option to mark DI/AI objects with NT bit when outstation goes offline or is disabled using service command. IEC60870-5-101/4 Master protocol attributes :xmlref:`OfflineNTDelay` and :xmlref:`DisabledNT`;
               | Option to send valid AIEVs to SCADA system on leandc startup in order to initialize the state of legacy spontaneous-only AIEVs. Valid AIEVs with 0 value will be sent after a number of seconds specified in :xmlref:`LegacyAIEVinitdelay` attribute on system startup in order to initialize SCADA database and make it ready to receive first legacy AIEV.
               | :xmlref:`StationID` attribute added to :xmlref:`IEC104Csl` node;
               | :xmlref:`TypeID` attribute added to IEC60870-5-101/4 Master DI/AI objects;
               | :xmlref:`SingleCharACK` attribute added for IEC60870-5-101 Slave protocol allowing to respond with single character (0xE5 or 0xA2) ACK or NACK messages
               
   * :ver:     V20
     :date:    09/10/2014
     :by:      AK
     :desc:    :xmlref:`DIEventStartup` attribute added to IEC60870-5-101/3/4 Master protocol configuration;
     
   * :ver:     V21
     :date:    28/11/2014
     :by:      AK
     :desc:    | :xmlref:`Modbusma` communication protocol instance added;
               | Leandc XML configuration manual is HTML-based from now on;
     
   * :ver:     V22
     :date:    15/02/2015
     :by:      AK
     :desc:    | > :xmlref:`Interface` and :xmlref:`Test` attributes added to :xmlref:`UART` node;
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
