
.. _ref-IEC104Rsl:

IEC104Rsl element node
^^^^^^^^^^^^^^^^^^^^^^

There is an option to use multiple redundant connections for communication between leandc and controlling 
(Master) stations ensuring a failure of a single communication channel will not disrupt the exchange of data. 
This option is currently available for leandc IEC60870-5-104 controlled station (Slave) mode and can be 
enabled by creating a redundancy group. Redundancy group is a number of leandc communication protocol
instances which are working together allowing several controlling stations (Masters) to receive the same data 
over single/multiple communication channels. Only one controlling station (Master) within a redundancy group is 
in a 'Started state' which means it is exchanging the application data with leandc. Other controlling stations 
(Masters) are in a 'Stopped state', they only monitor availability of the communication channel and do not 
exchange the application data.

In order to explain how to configure a redundancy group in leandc there are two terms 'Main' (:ref:`IEC104sl<ref-IEC104sl>` node) 
and 'Redundant' (:ref:`IEC104Rsl<ref-IEC104Rsl>` node) communication protocol instance used throughout this manual. There is no 
functional difference between 'Main' and 'Redundant' communication protocol instance as far as communication 
standard is concerned, these are only used to reference different types of nodes in leandc configuration.

IEC60870-5-104 controlled station (Slave) redundancy group in leandc is enabled as follows: any :ref:`IEC104sl<ref-IEC104sl>` 
node can be chosen as 'Main' communication protocol instance and redundancy is automatically enabled if one 
or more :ref:`IEC104Rsl<ref-IEC104Rsl>` nodes are linked to the 'Main' communication protocol instance. It is possible to link up to 15 
'Redundant' communication protocol instances to the same 'Main' communication protocol instance, thus 
creating a redundancy group of 16. This allows for up to 16 controlling (Master) stations to connect to leandc.

No IO object XML configuration is required for 'Redundant' communication protocol instance, because it is 
always linked to 'Main' communication protocol instance, which has an IO object table and the application data 
will be shared by all instances within a redundancy group. Please see sample :ref:`IEC104Rsl<ref-IEC104Rsl>` element node and the 
table listing all available attributes below.

.. code-block:: none

   <IEC104Rsl   Index="13" 
		HWIndex="3" 
		RedundantToIndex="12" 
		FilterID="0" 
		CommsFlags="0x80" 
		Name="SCADA" />

.. _ref-IEC104RslAttributes:

.. field-list-table:: Leandc IEC104Rsl node
   :class: table table-condensed table-bordered longtable
   :header-rows: 1
   :spec: |C{0.20}|C{0.25}|S{0.55}|

   * :attr,10: Attribute
     :val,15:  Values or range
     :desc,75: Description

   * :attr:    :xmlref:`Index`
     :val:     1...254
     :desc:    Index is a unique identifier of the communication protocol instance. It is used to reference protocol instance from other configuration files e.g. logfile configuration XML file. :inlinetip:`Indexes don't have to be in a sequential order.`

   * :attr:    :xmlref:`HWIndex`
     :val:     1...254
     :desc:    Hardware Index is used to link the communication protocol instance to a hardware node. Use value of the :ref:`TCPSERVER<ref-TCPSERVER>`.\ :ref:`Index<ref-TCPSERVERIndex>` \ attribute as a hardware index in order to link the protocol instance. :inlinetip:`Multiple` :ref:`IEC104Rsl<ref-IEC104Rsl>` :inlinetip:`communication protocol instances can be linked to the same hardware node.`

   * :attr:    :xmlref:`RedundantToIndex`
     :val:     1...254
     :desc:    Link current 'Redundant' communication protocol instance to 'Main' communication protocol instance. Use value of the :ref:`IEC104sl<ref-IEC104sl>`.\ :ref:`Index<ref-IEC104slIndex>` \ attribute.

   * :attr:    .. _ref-IEC104RslFilterID:
       
               :xmlref:`FilterID`
     :val:     1...255
     :desc:    Identifier of a predefined filter to restrict the range of TCP client IP addresses allowed to connect to the protocol instance. Please refer to the table :numref:`docref-ClientFilterCfgIPv4Attab` for filter settings. :inlinetip:`Attribute is optional and doesn't have to be included in configuration.`

   * :attr:    :xmlref:`CommsFlags`
     :val:     See table :numref:`ref-CommsFlagsAttribute` for description
     :desc:    Initialization settings of the protocol instance. :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default system settings will be used if omitted.`

   * :attr:    :xmlref:`Name`
     :val:     Max 100 chars
     :desc:    Freely configurable name, just for reference. :inlinetip:`Name attribute is optional and doesn't have to be included in configuration.`

Example configuration below, redundancy group of 4 instances is created allowing up to 4 controlling (Master) 
stations to connect to leandc.

.. code-block:: none

   <CommunicationCfg> 
            <IEC104sl Index="12" HWIndex="3" XMLpath="IEC104ma_test.xml" Name="SCADA1"/>
            <IEC104Rsl Index="13" HWIndex="3" RedundantToIndex="12" Name="SCADA2"/>
            <IEC104Rsl Index="14" HWIndex="3" RedundantToIndex="12" Name="SCADA3"/>
            <IEC104Rsl Index="15" HWIndex="3" RedundantToIndex="12" Name="SCADA4"/>
   </CommunicationCfg>
   
