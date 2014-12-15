
.. _ref-IEC104Csl:

IEC104Csl element node
^^^^^^^^^^^^^^^^^^^^^^

There is an option to clone communication protocol instances which share a common transport interface (same 
:ref:`StationID<ref-IEC104slStationID>` attribute) to create identical communication protocol instances linked to identical transport interface. 
This option might be useful in a situation where number of communication protocol instances (ASDUs) are 
linked to the same transport interface (station) and there is a need to create identical copy of such configuration 
e.g. to be linked to different hardware node. It can be easily achieved using :ref:`IEC104Csl<ref-IEC104Csl>` element node.

Please see sample :ref:`IEC104Csl<ref-IEC104Csl>` element node and the table listing all available attributes below.

.. code-block:: none

   <IEC104Csl   Index="13"
		HWIndex="3"
		CloneFromIndex="12"
		StationID="5"
		FilterID="0"
		CommsFlags="0x80"
		Name="SCADA"/>

.. _ref-IEC104CslAttributes:

.. field-list-table:: Leandc IEC104Csl node
   :class: table table-condensed table-bordered longtable
   :header-rows: 1
   :spec: |C{0.20}|C{0.25}|S{0.55}|

   * :attr,10: Attribute
     :val,15:  Values or range
     :desc,75: Description

   * :attr:    :xmlref:`Index`
     :val:     1...254
     :desc:    Base index of the first cloned communication protocol instance. If there are more protocol instances linked to the same transport interface as the instance which is being cloned, all of those will be cloned and their indexes will be initialized sequentially. :inlinetip:`Indexes don't have to be in a sequential order.`

   * :attr:    :xmlref:`HWIndex`
     :val:     1...254
     :desc:    Hardware Index is used to link cloned communication protocol instance(s) to a hardware node. Use value of the :ref:`TCPSERVER<ref-TCPSERVER>`.\ :ref:`Index<ref-TCPSERVERIndex>` \ attribute as a hardware index in order to link the cloned protocol instance(s). :inlinetip:`Multiple` :ref:`IEC104Csl<ref-IEC104Csl>` :inlinetip:`communication protocol instances can be linked to the same hardware node.`

   * :attr:    :xmlref:`CloneFromIndex`
     :val:     1...254
     :desc:    Source communication protocol instance to be cloned. All protocol instances linked to the same transport interface (station) will be cloned. Use value of the :ref:`IEC104sl<ref-IEC104sl>`.\ :ref:`Index<ref-IEC104slIndex>` \ attribute.

   * :attr:    :xmlref:`StationID`
     :val:     1...254
     :desc:    Station identifier. Multiple ASDUs (communication protocol instances) can share a common transport interface referred as 'station'. Station identifier is unique per hardware node so it is possible to have multiple stations with the same identifier providing these are linked to separate hardware nodes. :inlinetip:`Attribute is optional and doesn't have to be included in configuration, cloned protocol instance will create its own transport interface (unique 'station') if attribute omitted.`

   * :attr:    .. _ref-IEC104CslFilterID:
       
               :xmlref:`FilterID`
     :val:     1...255
     :desc:    Identifier of a predefined filter to restrict the range of TCP client IP addresses allowed to establish connection to the protocol instance(s). Please refer to the table :numref:`ref-ClientFilterCfgIpv4Attributes` for filter settings. :inlinetip:`Attribute is optional and doesn't have to be included in configuration.`

   * :attr:    :xmlref:`CommsFlags`
     :val:     See table :numref:`ref-CommsFlagsAttribute` for description
     :desc:    Initialization settings of the protocol instance(s). :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default system settings will be used if omitted.`

   * :attr:    :xmlref:`Name`
     :val:     Max 100 chars
     :desc:    Freely configurable name, just for reference. :inlinetip:`Name attribute is optional and doesn't have to be included in configuration.`
