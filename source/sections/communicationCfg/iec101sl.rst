
.. _ref-IEC101sl:

IEC101sl element node
^^^^^^^^^^^^^^^^^^^^^

General settings of the IEC60870-5-101 controlled station (Slave) communication protocol instance. Please see 
sample :ref:`IEC101sl<ref-IEC101sl>` element node and the table listing all available attributes below.

.. code-block:: none

   <IEC101sl    Index="5"
		HWIndex="1"
		XMLpath="IEC101sl_test.xml"
		LinkAddr="5"
		ASDUAddr="5"
		Source="6"
		CommsFlags="0x80"
		Name="Serial SCADA"/>

.. _ref-IEC101slAttributes:

.. field-list-table:: Leandc IEC101sl node
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
     :desc:    Hardware Index is used to link the communication protocol instance to a hardware node. Use value of the :ref:`UART<ref-UART>`.\ :ref:`Index<ref-UARTIndex>`\; :ref:`TCPSERVER<ref-TCPSERVER>`.\ :ref:`Index<ref-TCPSERVERIndex>`\; :ref:`TCPCLIENT<ref-TCPCLIENT>`.\ :ref:`Index<ref-TCPCLIENTIndex>` \ or :ref:`UDP<ref-UDP>`.\ :ref:`Index<ref-UDPIndex>` \ attribute as a hardware index in order to link the protocol instance. :inlinetip:`Multiple` :ref:`IEC101sl<ref-IEC101sl>` :inlinetip:`communication protocol instances can be linked to the same hardware node.`

   * :attr:    .. _ref-IEC101slXMLpath:
       
               :xmlref:`XMLpath`
     :val:     Max 100 chars
     :desc:    Communication protocol instance XML configuration file name and path. This file contains IO object table as well as additional settings. File path may be omitted if XML file is stored in the same directory as leandc firmware (/home/leandc/app by default) :inlineimportant:`Attribute is case sensitive, observe the case of path and file name when specifying.`

   * :attr:    :xmlref:`LinkAddr`
     :val:     1...254 or 1...65534
     :desc:    Link layer address of the communication protocol instance. Addresses must be equal for the 'Master' and 'Slave' station communicating to each other. Size of the link layer address may be 1 or 2 bytes and it is configured using the :ref:`LinkSettings<ref-IEC101slLinkSettings>`.\ :ref:`LinkAddrSize<ref-IEC101slLinkSettingsLinkAddrSize>` \ attribute. Please note values 255 (if link layer address size is 1 byte) and 65535 (if link layer address size is 2 bytes) are Global addresses and can't be used.

   * :attr:    :xmlref:`ASDUAddr`
     :val:     1...254 or 1...65534
     :desc:    Common address of ASDU (CAA). Size of the common ASDU address may be 1 or 2 bytes and it is configured using the :ref:`ASDUSettings<ref-IEC101slASDUSettings>`.\ :ref:`CAASize<ref-IEC101slASDUSettingsCAASize>` \ attribute. Please note values 255 (if ASDU address size is 1 byte) and 65535 (if ASDU address size is 2 bytes) are Broadcast addresses and can't be used. :inlinetip:`ASDUAddr attribute is optional and doesn't have to be included in configuration, value of the LinkAddr will be used if omitted.`

   * :attr:    .. _ref-IEC101slSource:
   
               :xmlref:`Source`
     :val:     1...254
     :desc:    Source communication protocol instance index. IO objects without individual :ref:`DI<ref-IEC10xslDI>`.\ :ref:`Device<ref-IEC10xslDIDevice>`\; :ref:`AI<ref-IEC10xslAI>`.\ :ref:`Device<ref-IEC10xslAIDevice>`\; :ref:`DO<ref-IEC10xslDO>`.\ :ref:`Device<ref-IEC10xslDODevice>`\; :ref:`AO<ref-IEC10xslAO>`.\ :ref:`Device<ref-IEC10xslAODevice>` \ attributes will be linked to Master protocol instance specified in :xmlref:`Source`. :inlinetip:`Attribute is optional and doesn't have to be included in configuration, IO object` :xmlref:`Device` :inlinetip:`attributes will be used if omitted.`

   * :attr:    :xmlref:`CommsFlags`
     :val:     See table :numref:`ref-CommsFlagsAttribute` for description
     :desc:    Initialization settings of the protocol instance. :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default system settings will be used if omitted.`

   * :attr:    :xmlref:`Name`
     :val:     Max 100 chars
     :desc:    Freely configurable name, just for reference. :inlinetip:`Name attribute is optional and doesn't have to be included in configuration.`
