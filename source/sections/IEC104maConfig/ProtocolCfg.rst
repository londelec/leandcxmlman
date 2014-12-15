
.. _ref-IEC104maProtocolCfg:

ProtocolCfg group node
----------------------

Protocol-related settings of the IEC60870-5-104 controlling station (Master) communication protocol instance 
are configured using various child element nodes under :ref:`ProtocolCfg<ref-IEC104maProtocolCfg>` group node. 

.. important:: It is essential to keep element nodes in the listed order otherwise it will affect the XML file validation.

Please see sample :ref:`ProtocolCfg<ref-IEC104maProtocolCfg>` group node and the table listing all available child element nodes below.

.. code-block:: none

   <ProtocolCfg> 
      <XMLSettings … />
      <TransportSettings … />
      <CommsSettings … />
      <ASDUSettings … />
      <Timeouts … />
      <TimeSettings … />
      <Broadcast … />
      <Periodic … />
      <BufferSizes … />
   </ProtocolCfg>

.. tip:: All element nodes are optional, default values will be used for attributes of omitted nodes.

.. _ref-IEC104maProtocolCfgAttributes:

.. field-list-table:: IEC 60807-5-104 Master ProtocolCfg element nodes
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.20}|C{0.25}|S{0.55}|
   :header-rows: 1

   * :attr,10: Attribute
     :val,15:  Values or range
     :desc,75: Description
     
   * :attr:    .. _ref-IEC104maXMLSettings:
       
               :xmlref:`XMLSettings`
     :val:     See table :numref:`ref-IEC104maXMLSettingsAttributes`
     :desc:    XML parse setting specification node. Refer to table :numref:`ref-IEC104maXMLSettingsAttributes` for attribute specification.

   * :attr:    .. _ref-IEC104maTransportSettings:
       
               :xmlref:`TransportSettings`
     :val:     See table :numref:`ref-IEC104maTransportSettingsAttributes`
     :desc:    Communication transport interface timeout and message window size configuration node. Refer to table :numref:`ref-IEC104maTransportSettingsAttributes` for attribute specification.

   * :attr:    .. _ref-IEC104maCommsSettings:
       
               :xmlref:`CommsSettings`
     :val:     See table :numref:`ref-IEC104maCommsSettingsAttributes`
     :desc:    Communication status (e.g. online and offline) change behavior and related delay configuration node. Refer to table :numref:`ref-IEC104maCommsSettingsAttributes` for attribute specification.

   * :attr:    .. _ref-IEC104maASDUSettings:
       
               :xmlref:`ASDUSettings`
     :val:     See table :numref:`ref-IEC104maASDUSettingsAttributes`
     :desc:    Various application layer settings configuration node. Refer to table :numref:`ref-IEC104maASDUSettingsAttributes` for attribute specification.

   * :attr:    .. _ref-IEC104maTimeouts:
       
               :xmlref:`Timeouts`
     :val:     See table :numref:`ref-IEC104maTimeoutsAttributes`
     :desc:    Control command expiration timeout configuration node. Refer to table :numref:`ref-IEC104maTimeoutsAttributes` for attribute specification.

   * :attr:    .. _ref-IEC104maTimeSettings:
       
               :xmlref:`TimeSettings`
     :val:     See table :numref:`ref-IEC104maTimeSettingsAttributes`
     :desc:    Unique time settings (e.g. time zone) of particular protocol instance. Refer to table :numref:`ref-IEC104maTimeSettingsAttributes` for attribute specification.

   * :attr:    .. _ref-IEC104maBroadcast:
       
               :xmlref:`Broadcast`
     :val:     See table :numref:`ref-IEC104maBroadcastAttributes`
     :desc:    Broadcast or individual common address of ASDU (CAA) specification node. Refer to table :numref:`ref-IEC104maBroadcastAttributes` for attribute specification.

   * :attr:    .. _ref-IEC104maPeriodic:
       
               :xmlref:`Periodic`
     :val:     See table :numref:`ref-IEC104maPeriodicAttributes`
     :desc:    Periodically generated message configuration node. Refer to table :numref:`ref-IEC104maPeriodicAttributes` for attribute specification.

   * :attr:    .. _ref-IEC104maBufferSizes:
       
               :xmlref:`BufferSizes`
     :val:     See table :numref:`ref-IEC104maBufferSizesAttributes`
     :desc:    Various application layer buffer size configuration node. Refer to table :numref:`ref-IEC104maBufferSizesAttributes` for attribute specification.

.. include-file:: sections/Include/XMLSettings.rstinc "" ":ref:`XMLSettings<ref-IEC104maXMLSettings>`" ".. _ref-IEC104maXMLSettingsAttributes:" "IEC 60807-5-104 Master XMLSettings attributes"
.. include:: IEC104maConfig/TransportSettings.rst
.. include:: IEC104maConfig/CommsSettings.rst
.. include:: IEC104maConfig/ASDUSettings.rst
.. include-file:: sections/Include/IEC10xma_Timeouts.rstinc "" ":ref:`Timeouts<ref-IEC104maTimeouts>`" ".. _ref-IEC104maTimeoutsAttributes:" "IEC 60807-5-104 Master Timeouts attributes"
.. include-file:: sections/Include/TimeSettings.rstinc "" ":ref:`TimeSettings<ref-IEC104maTimeSettings>`" ".. _ref-IEC104maTimeSettingsAttributes:" "IEC 60807-5-101/104 Master TimeSettings attributes" ".. _ref-IEC104maTimeSettingsTimeZone:"
.. include:: IEC104maConfig/Broadcast.rst
.. include-file:: sections/Include/IEC10xmaConfig_Periodic.rstinc "" ":ref:`Periodic<ref-IEC104maPeriodic>`" ".. _ref-IEC104maPeriodicAttributes:" "IEC 60807-5-104 Master Periodic attributes"
.. include-file:: sections/Include/IEC10xmaConfig_BufferSizes.rstinc "" ":ref:`BufferSizes<ref-IEC104maBufferSizes>`" ".. _ref-IEC104maBufferSizesAttributes:" "IEC 60807-5-104 Master BufferSizes attributes"
