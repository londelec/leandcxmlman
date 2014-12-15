
.. _ref-IEC104slProtocolCfg:

ProtocolCfg group node
----------------------

Protocol-related settings of the IEC60870-5-104 controlled station (Slave) communication protocol instance are 
configured using various child element nodes under :ref:`ProtocolCfg<ref-IEC104slProtocolCfg>` group node. 

.. important:: It is essential to keep element nodes in the listed order otherwise it will affect the XML file validation.

Please see sample :ref:`ProtocolCfg<ref-IEC104slProtocolCfg>` group node and the table listing all available child element nodes below.

.. code-block:: none

   <ProtocolCfg>
      <XMLSettings … />
      <TransportSettings … />
      <CommsSettings … />
      <ASDUSettings … />
      <Timeouts … />
      <TimeSettings … />
      <Periodic … />
      <BufferSizes … />
      <Miscellaneous … />
   </ProtocolCfg>

.. tip:: All element nodes are optional, default values will be used for attributes of omitted nodes.

.. _ref-IEC104slProtocolCfgAttributes:

.. field-list-table:: IEC 60807-5-104 Slave ProtocolCfg child element nodes
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.20}|C{0.25}|S{0.55}|
   :header-rows: 1

   * :attr,10: Attribute
     :val,15:  Values or range
     :desc,75: Description
     
   * :attr:    .. _ref-IEC104slXMLSettings:
       
               :xmlref:`XMLSettings`
     :val:     See table :numref:`ref-IEC104slXMLSettingsAttributes`
     :desc:    XML parse setting specification node. Refer to table :numref:`ref-IEC104slXMLSettingsAttributes` for attribute specification.

   * :attr:    .. _ref-IEC104slTransportSettings:
       
               :xmlref:`TransportSettings`
     :val:     See table :numref:`ref-IEC104slTransportSettingsAttributes`
     :desc:    Communication transport interface timeout and message window size configuration node. Refer to table :numref:`ref-IEC104slTransportSettingsAttributes` for attribute specification.

   * :attr:    .. _ref-IEC104slCommsSettings:
       
               :xmlref:`CommsSettings`
     :val:     See table :numref:`ref-IEC104slCommsSettingsAttributes`
     :desc:    Communication status (e.g. online and offline) change behavior and related delay configuration node. Refer to table :numref:`ref-IEC104slCommsSettingsAttributes` for attribute specification.

   * :attr:    .. _ref-IEC104slASDUSettings:
       
               :xmlref:`ASDUSettings`
     :val:     See table :numref:`ref-IEC104slASDUSettingsAttributes`
     :desc:    Various application layer settings configuration node. Refer to table :numref:`ref-IEC104slASDUSettingsAttributes` for attribute specification.

   * :attr:    .. _ref-IEC104slTimeouts:
       
               :xmlref:`Timeouts`
     :val:     See table :numref:`ref-IEC104slTimeoutsAttributes`
     :desc:    Control command expiration timeout configuration node. Refer to table :numref:`ref-IEC104slTimeoutsAttributes` for attribute specification.

   * :attr:    .. _ref-IEC104slTimeSettings:
       
               :xmlref:`TimeSettings`
     :val:     See table :numref:`ref-IEC104slTimeSettingsAttributes`
     :desc:    Unique time settings (e.g. time zone) of particular protocol instance. Refer to table :numref:`ref-IEC104slTimeSettingsAttributes` for attribute specification.

   * :attr:    .. _ref-IEC104slPeriodic:
       
               :xmlref:`Periodic`
     :val:     See table :numref:`ref-IEC104slPeriodicAttributes`
     :desc:    Periodically generated message configuration node. Refer to table :numref:`ref-IEC104slPeriodicAttributes` for attribute specification.

   * :attr:    .. _ref-IEC104slBufferSizes:
       
               :xmlref:`BufferSizes`
     :val:     See table :numref:`ref-IEC104slBufferSizesAttributes`
     :desc:    Various application layer buffer size configuration node. Refer to table :numref:`ref-IEC104slBufferSizesAttributes` for attribute specification.

   * :attr:    .. _ref-IEC104slMiscellaneous:
       
               :xmlref:`Miscellaneous`
     :val:     See table :numref:`ref-IEC104slMiscellaneousAttributes`
     :desc:    Miscellaneous and project-specific setting configuration node. Refer to table :numref:`ref-IEC104slMiscellaneousAttributes` for attribute specification.

.. include-file:: sections/Include/XMLSettings.rstinc "" ":ref:`XMLSettings<ref-IEC104slXMLSettings>`" ".. _ref-IEC104slXMLSettingsAttributes:" "IEC 60807-5-104 Slave XMLSettings attributes"
.. include:: IEC104slConfig/TransportSettings.rst
.. include:: IEC104slConfig/CommsSettings.rst
.. include:: IEC104slConfig/ASDUSettings.rst
.. include-file:: sections/Include/IEC10xslConfig_Timeouts.rstinc "" ":ref:`Timeouts<ref-IEC104slTimeouts>`" ".. _ref-IEC104slTimeoutsAttributes:" "IEC 60807-5-104 Slave Timeouts attributes"
.. include-file:: sections/Include/TimeSettings.rstinc "" ":ref:`TimeSettings<ref-IEC104slTimeSettings>`" ".. _ref-IEC104slTimeSettingsAttributes:" "IEC 60807-5-101/104 Slave TimeSettings attributes" ".. _ref-IEC104slTimeSettingsTimeZone:"
.. include-file:: sections/Include/IEC10xslConfig_Periodic.rstinc "" ":ref:`Periodic<ref-IEC104slPeriodic>`" ".. _ref-IEC104slPeriodicAttributes:" "IEC 60807-5-104 Slave Periodic attributes"
.. include-file:: sections/Include/IEC10xslConfig_BufferSizes.rstinc "" ":ref:`BufferSizes<ref-IEC104slBufferSizes>`" ".. _ref-IEC104slBufferSizesAttributes:" "IEC 60807-5-104 Slave BufferSizes attributes"
.. include:: IEC104slConfig/Miscellaneous.rst
