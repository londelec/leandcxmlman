
.. _ref-IEC103ma:

IEC103ma element node
^^^^^^^^^^^^^^^^^^^^^

General settings of the IEC60870-5-103 controlling station (Master) communication protocol instance. Please 
see sample :ref:`IEC103ma<ref-IEC103ma>` element node and the table listing all available attributes below.

.. code-block:: none

   <IEC103ma    Index="20"
		HWIndex="3"
		XMLpath="Feeder_F1.xml"
		LinkAddr="5"
		ASDUAddr="5"
		CommsFlags="0x80"
		Name="Feeder_IED1" />

.. _ref-IEC103maAttributes:

.. field-list-table:: Leandc IEC103ma node
   :class: table table-condensed table-bordered longtable
   :header-rows: 1
   :spec: |C{0.20}|C{0.25}|S{0.55}|

   * :attr,10: Attribute
     :val,15:  Values or range
     :desc,75: Description

   * :attr:    :xmlref:`Index`
     :val:     1...254
     :desc:    Index is a unique identifier of the communication protocol instance. It is used to reference protocol instance from other configuration files e.g. IO object tables (please see :ref:`DI<ref-IEC10xslDI>`.\ :ref:`Device<ref-IEC10xslDIDevice>`\; :ref:`AI<ref-IEC10xslAI>`.\ :ref:`Device<ref-IEC10xslAIDevice>`\; :ref:`DO<ref-IEC10xslDO>`.\ :ref:`Device<ref-IEC10xslDODevice>`\; :ref:`AO<ref-IEC10xslAO>`.\ :ref:`Device<ref-IEC10xslAODevice>` \ attributes of the Slave protocol instance) :inlinetip:`Indexes don't have to be in a sequential order.`

   * :attr:    :xmlref:`HWIndex`
     :val:     1...254
     :desc:    Hardware Index is used to link the communication protocol instance to a hardware node. Use value of the :ref:`UART<ref-UART>`.\ :ref:`Index<ref-UARTIndex>`\; :ref:`TCPSERVER<ref-TCPSERVER>`.\ :ref:`Index<ref-TCPSERVERIndex>`\; :ref:`TCPCLIENT<ref-TCPCLIENT>`.\ :ref:`Index<ref-TCPCLIENTIndex>` \ or :ref:`UDP<ref-UDP>`.\ :ref:`Index<ref-UDPIndex>` \ attribute as a hardware index in order to link the protocol instance. :inlinetip:`Multiple` :ref:`IEC103ma<ref-IEC103ma>` :inlinetip:`communication protocol instances can be linked to the same hardware node.`

   * :attr:    .. _ref-IEC103maXMLpath:
       
               :xmlref:`XMLpath`
     :val:     Max 100 chars
     :desc:    Communication protocol instance XML configuration file name and path. This file contains IO object table as well as additional settings. File path may be omitted if XML file is stored in the same directory as leandc firmware (/home/leandc/app by default) :inlineimportant:`Attribute is case sensitive, observe the case of path and file name when specifying.`

   * :attr:    :xmlref:`LinkAddr`
     :val:     1...254
     :desc:    Link layer address of the communication protocol instance. Addresses must be equal for the 'Master' and 'Slave' station communicating to each other. Size of the link layer address may be 1 or 2 bytes and it is configured using the :ref:`LinkSettings<ref-IEC101maLinkSettings>`.\ :ref:`LinkAddrSize<ref-IEC101maLinkSettingsLinkAddrSize>` \ attribute. Please note values 255 is Global addresses and can't be used.

   * :attr:    :xmlref:`ASDUAddr`
     :val:     1...254
     :desc:    Common address of ASDU (CAA). There is only one ASDU available in IEC 60870-5-103 Master station and addresses must be equal for the 'Master' and 'Slave' station communicating to each other. Please note value 255 is Broadcast address and can't be used. :inlinetip:`ASDUAddr attribute is optional and doesn't have to be included in configuration, LinkAddr value will be used if omitted.`

   * :attr:    :xmlref:`CommsFlags`
     :val:     See table :numref:`ref-CommsFlagsAttribute` for description
     :desc:    Initialization settings of the protocol instance. :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default system settings will be used if omitted.`

   * :attr:    :xmlref:`Name`
     :val:     Max 100 chars
     :desc:    Freely configurable name, just for reference. :inlinetip:`Name attribute is optional and doesn't have to be included in configuration.`
