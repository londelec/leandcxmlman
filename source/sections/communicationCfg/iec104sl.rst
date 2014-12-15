
.. _ref-IEC104sl:

IEC104sl element node
^^^^^^^^^^^^^^^^^^^^^

General settings of the IEC60870-5-104 controlled station (Slave) communication protocol instance. Please see
sample :ref:`IEC104sl<ref-IEC104sl>` element node and the table listing all available attributes below.

.. code-block:: none

   <IEC104sl    Index="12"
		HWIndex="4"
		XMLpath="IEC104sl_test.xml"
		ASDUAddr="5"
		StationID="2"
		FilterID="0"
		Source="6"
		CommsFlags="0x80"
		Name="SCADA"/>

.. _ref-IEC104slAttributes:

.. field-list-table:: Leandc IEC104sl node
   :class: table table-condensed table-bordered longtable
   :header-rows: 1
   :spec: |C{0.20}|C{0.25}|S{0.55}|

   * :attr,10: Attribute
     :val,15:  Values or range
     :desc,75: Description

   * :attr:    .. _ref-IEC104slIndex:
       
               :xmlref:`Index`
     :val:     1...254
     :desc:    Index is a unique identifier of the communication protocol instance. It is used to reference protocol instance from other configuration files e.g. logfile configuration XML file. :inlinetip:`Indexes don't have to be in a sequential order.`

   * :attr:    :xmlref:`HWIndex`
     :val:     1...254
     :desc:    Hardware Index is used to link the communication protocol instance to a hardware node. Use value of the :ref:`TCPSERVER<ref-TCPSERVER>`.\ :ref:`Index<ref-TCPSERVERIndex>` \ attribute as a hardware index in order to link the protocol instance. :inlinetip:`Multiple` :ref:`IEC104sl<ref-IEC104sl>` :inlinetip:`communication protocol instances can be linked to the same hardware node.`

   * :attr:    .. _ref-IEC104slXMLpath:
       
               :xmlref:`XMLpath`
     :val:     Max 100 chars
     :desc:    Communication protocol instance XML configuration file name and path. This file contains IO object table as well as additional settings. File path may be omitted if XML file is stored in the same directory as leandc firmware (/home/leandc/app by default) :inlineimportant:`Attribute is case sensitive, observe the case of path and file name when specifying.`

   * :attr:    :xmlref:`ASDUAddr`
     :val:     1...65534
     :desc:    Common address of ASDU (CAA). Please note value 65535 is Broadcast address and can't be used.

   * :attr:    .. _ref-IEC104slStationID:
       
               :xmlref:`StationID`
     :val:     1...254
     :desc:    Station identifier. Multiple ASDUs (communication protocol instances) can share a common transport interface referred as 'station'. Station identifier is unique per hardware node so it is possible to have multiple stations with the same identifier providing these are linked to separate hardware nodes. :inlinetip:`Attribute is optional and doesn't have to be included in configuration, each protocol instance will create its own transport interface (unique 'station') if attribute omitted.`

   * :attr:    .. _ref-IEC104slFilterID:
       
               :xmlref:`FilterID`
     :val:     1...255
     :desc:    Identifier of a predefined filter to restrict the range of TCP client IP addresses allowed to establish connection to the protocol instance. Please refer to the table :numref:`ref-ClientFilterCfgIpv4Attributes` for filter settings. :inlinetip:`FilterID attribute is optional and doesn't have to be included in configuration.`

   * :attr:    .. _ref-IEC104slSource:
   
               :xmlref:`Source`
     :val:     1...254
     :desc:    Source communication protocol instance index. IO objects without individual :ref:`DI<ref-IEC10xslDI>`.\ :ref:`Device<ref-IEC10xslDIDevice>`\; :ref:`AI<ref-IEC10xslAI>`.\ :ref:`Device<ref-IEC10xslAIDevice>`\; :ref:`DO<ref-IEC10xslDO>`.\ :ref:`Device<ref-IEC10xslDODevice>`\; :ref:`AO<ref-IEC10xslAO>`.\ :ref:`Device<ref-IEC10xslAODevice>` \ attributes specified will be linked to this protocol instance. :inlinetip:`Attribute is optional and doesn't have to be included in configuration, IO object :xmlref:`Device` attributes will be used if omitted.`

   * :attr:    :xmlref:`CommsFlags`
     :val:     See table :numref:`ref-CommsFlagsAttribute` for description
     :desc:    Initialization settings of the protocol instance. :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default system settings will be used if omitted.`

   * :attr:    :xmlref:`Name`
     :val:     Max 100 chars
     :desc:    Freely configurable name, just for reference. :inlinetip:`Name attribute is optional and doesn't have to be included in configuration.` 
