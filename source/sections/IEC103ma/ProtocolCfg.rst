
.. _ref-IEC103maProtocolCfg:

ProtocolCfg group node
----------------------

Protocol-related settings of the IEC60870-5-103 controlling station (Master) communication protocol instance 
are configured using various child element nodes under :ref:`ProtocolCfg<ref-IEC103maProtocolCfg>` group node. 

.. important:: It is essential to keep element nodes in the listed order otherwise it will affect the XML file validation.

Please see sample :ref:`ProtocolCfg<ref-IEC103maProtocolCfg>` group node and the table listing all available child element nodes below.

.. code-block:: none

   <ProtocolCfg> 
      <CommsSettings … />
      <ASDUSettings … />
      <Timeouts … />
      <TimeSettings … />
      <Broadcast … />
      <Periodic … />
   </ProtocolCfg>

.. tip:: All element nodes are optional, default values will be used for attributes of omitted nodes.

.. _ref-IEC103maProtocolCfgAttributes:

.. field-list-table:: IEC 60807-5-103 Master ProtocolCfg child element nodes
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.20}|C{0.25}|S{0.55}|
   :header-rows: 1

   * :attr,10: Attribute
     :val,15:  Values or range
     :desc,75: Description

   * :attr:    .. _ref-IEC103maCommsSettings:
       
               :xmlref:`CommsSettings`
     :val:     See table :numref:`ref-IEC103maCommsSettingsAttributes`
     :desc:    Communication status (e.g. online and offline) change behavior and related delay configuration node. Refer to table :numref:`ref-IEC103maCommsSettingsAttributes` for attribute specification.

   * :attr:    .. _ref-IEC103maASDUSettings:
       
               :xmlref:`ASDUSettings`
     :val:     See table :numref:`ref-IEC103maASDUSettingsAttributes`
     :desc:    Various application layer settings configuration node. Refer to table :numref:`ref-IEC103maASDUSettingsAttributes` for attribute specification.

   * :attr:    .. _ref-IEC103maTimeouts:
       
               :xmlref:`Timeouts`
     :val:     See table :numref:`ref-IEC103maTimeoutsAttributes`
     :desc:    Control command expiration timeout configuration node. Refer to table :numref:`ref-IEC103maTimeoutsAttributes` for attribute specification.

   * :attr:    .. _ref-IEC103maTimeSettings:
       
               :xmlref:`TimeSettings`
     :val:     See table :numref:`ref-IEC103maTimeSettingsAttributes`
     :desc:    Unique time settings (e.g. time zone) of particular protocol instance. Refer to table :numref:`ref-IEC103maTimeSettingsAttributes` for attribute specification.

   * :attr:    .. _ref-IEC103maBroadcast:
       
               :xmlref:`Broadcast`
     :val:     See table :numref:`ref-IEC103maBroadcastAttributes`
     :desc:    Broadcast or individual common address of ASDU (CAA) specification node. Refer to table :numref:`ref-IEC103maBroadcastAttributes` for attribute specification.

   * :attr:    .. _ref-IEC103maPeriodic:
       
               :xmlref:`Periodic`
     :val:     See table :numref:`ref-IEC103maPeriodicAttributes`
     :desc:    Periodic command generation interval specification node. Refer to table :numref:`ref-IEC103maPeriodicAttributes` for attribute specification.

.. include:: IEC103ma/CommsSettings.rst
.. include:: IEC103ma/ASDUSettings.rst
.. include:: IEC103ma/Timeouts.rst
.. include-file:: sections/Include/TimeSettings.rstinc "" ":ref:`TimeSettings<ref-IEC103maTimeSettings>`" ".. _ref-IEC103maTimeSettingsAttributes:" "IEC 60807-5-103 Master TimeSettings attributes" ".. _ref-IEC103maTimeSettingsTimeZone:"
.. include:: IEC103ma/Broadcast.rst
.. include:: IEC103ma/Periodic.rst
     
