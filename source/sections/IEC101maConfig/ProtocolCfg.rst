
.. _ref-IEC101maProtocolCfg:

ProtocolCfg group node
----------------------

Protocol-related settings of the IEC60870-5-101 controlling station (Master) communication protocol instance 
are configured using various child element nodes under :ref:`ProtocolCfg<ref-IEC101maProtocolCfg>` group node. 

.. important:: It is essential to keep element nodes in the listed order otherwise it will affect the XML file validation.

Please see sample :ref:`ProtocolCfg<ref-IEC101maProtocolCfg>` group node and the table listing all available child element nodes below.

.. code-block:: none

   <ProtocolCfg> 
      <XMLSettings … />
      <LinkSettings … />
      <CommsSettings … />
      <ASDUSettings … />
      <Timeouts … />
      <TimeSettings … />
      <Broadcast … />
      <Periodic … />
      <BufferSizes … />
   </ProtocolCfg>

.. tip:: All element nodes are optional, default values will be used for attributes of omitted nodes.

.. _ref-IEC101maProtocolCfgAttributes:

.. field-list-table:: IEC 60807-5-101 Master ProtocolCfg child element nodes
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.20}|C{0.25}|S{0.55}|
   :header-rows: 1

   * :attr,10: Attribute
     :val,15:  Values or range
     :desc,75: Description
     
   * :attr:    .. _ref-IEC101maXMLSettings:
       
               :xmlref:`XMLSettings`
     :val:     See table :numref:`ref-IEC101maXMLSettingsAttributes`
     :desc:    XML parse setting specification node. Refer to table :numref:`ref-IEC101maXMLSettingsAttributes` for attribute specification.

   * :attr:    .. _ref-IEC101maLinkSettings:
       
               :xmlref:`LinkSettings`
     :val:     See table :numref:`ref-IEC101maLinkSettingsAttributes`
     :desc:    Communication link layer timeout and control bit configuration node. Refer to table :numref:`ref-IEC101maLinkSettingsAttributes` for attribute specification.

   * :attr:    .. _ref-IEC101maCommsSettings:
       
               :xmlref:`CommsSettings`
     :val:     See table :numref:`ref-IEC101maCommsSettingsAttributes`
     :desc:    Communication status (e.g. online and offline) change behavior and related delay configuration node. Refer to table :numref:`ref-IEC101maCommsSettingsAttributes` for attribute specification.

   * :attr:    .. _ref-IEC101maASDUSettings:
       
               :xmlref:`ASDUSettings`
     :val:     See table :numref:`ref-IEC101maASDUSettingsAttributes`
     :desc:    Various application layer settings configuration node. Refer to table :numref:`ref-IEC101maASDUSettingsAttributes` for attribute specification.

   * :attr:    .. _ref-IEC101maTimeouts:
       
               :xmlref:`Timeouts`
     :val:     See table :numref:`ref-IEC101maTimeoutsAttributes`
     :desc:    Control command expiration timeout configuration node. Refer to table :numref:`ref-IEC101maTimeoutsAttributes` for attribute specification.

   * :attr:    .. _ref-IEC101maTimeSettings:
       
               :xmlref:`TimeSettings`
     :val:     See table :numref:`ref-IEC101maTimeSettingsAttributes`
     :desc:    Unique time settings (e.g. time zone) of particular protocol instance. Refer to table :numref:`ref-IEC101maTimeSettingsAttributes` for attribute specification.

   * :attr:    .. _ref-IEC101maBroadcast:
       
               :xmlref:`Broadcast`
     :val:     See table :numref:`ref-IEC101maBroadcastAttributes`
     :desc:    Broadcast or individual common address of ASDU (CAA) specification node. Refer to table :numref:`ref-IEC101maBroadcastAttributes` for attribute specification.

   * :attr:    .. _ref-IEC101maPeriodic:
       
               :xmlref:`Periodic`
     :val:     See table :numref:`ref-IEC101maPeriodicAttributes`
     :desc:    Periodically generated message configuration node. Refer to table :numref:`ref-IEC101maPeriodicAttributes` for attribute specification.

   * :attr:    .. _ref-IEC101maBufferSizes:
       
               :xmlref:`BufferSizes`
     :val:     See table :numref:`ref-IEC101maBufferSizesAttributes`
     :desc:    Various application layer buffer size configuration node. Refer to table :numref:`ref-IEC101maBufferSizesAttributes` for attribute specification.

.. include-file:: sections/Include/XMLSettings.rstinc "" ":ref:`XMLSettings<ref-IEC101maXMLSettings>`" ".. _ref-IEC101maXMLSettingsAttributes:" "IEC 60807-5-101 Master XMLSettings attributes"
.. include:: IEC101maConfig/LinkSettings.rst
.. include:: IEC101maConfig/CommsSettings.rst
.. include:: IEC101maConfig/ASDUSettings.rst
.. include-file:: sections/Include/IEC10xma_Timeouts.rstinc "" ":ref:`Timeouts<ref-IEC101maTimeouts>`" ".. _ref-IEC101maTimeoutsAttributes:" "IEC 60807-5-101 Master Timeouts attributes"
.. include-file:: sections/Include/TimeSettings.rstinc "" ":ref:`TimeSettings<ref-IEC101maTimeSettings>`" ".. _ref-IEC101maTimeSettingsAttributes:" "IEC 60807-5-101/104 Master TimeSettings attributes" ".. _ref-IEC101maTimeSettingsTimeZone:"
.. include:: IEC101maConfig/Broadcast.rst
.. include-file:: sections/Include/IEC10xmaConfig_Periodic.rstinc "" ":ref:`Periodic<ref-IEC101maPeriodic>`" ".. _ref-IEC101maPeriodicAttributes:" "IEC 60807-5-101 Master Periodic attributes"
.. include-file:: sections/Include/IEC101maConfig_PeriodicAttribute_TimeSync.rstinc ""
.. include-file:: sections/Include/IEC10xmaConfig_BufferSizes.rstinc "" ":ref:`BufferSizes<ref-IEC101maBufferSizes>`" ".. _ref-IEC101maBufferSizesAttributes:" "IEC 60807-5-101 Master BufferSizes attributes"
     
