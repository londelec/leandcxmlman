
.. _ref-IEC101slProtocolCfg:

ProtocolCfg group node
----------------------

Protocol settings of the IEC60870-5-101 controlled station (Slave) communication protocol instance are 
configured using various child element nodes under :ref:`ProtocolCfg<ref-IEC101slProtocolCfg>` group node.

.. important:: It is essential to keep element nodes in the listed order otherwise it will affect the XML file validation.

Please see sample :ref:`ProtocolCfg<ref-IEC101slProtocolCfg>` group node and the table listing all available child element nodes below.

.. code-block:: none

   <ProtocolCfg>
      <XMLSettings … />
      <LinkSettings … />
      <CommsSettings … />
      <ASDUSettings … />
      <Timeouts … />
      <TimeSettings … />
      <Periodic … />
      <BufferSizes … />
   </ProtocolCfg>

.. tip:: All element nodes are optional, default values will be used for attributes of omitted nodes.

.. _ref-IEC101slProtocolCfgAttributes:

.. field-list-table:: IEC 60807-5-101 Slave ProtocolCfg child element nodes
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.20}|C{0.25}|S{0.55}|
   :header-rows: 1

   * :attr,10: Attribute
     :val,15:  Values or range
     :desc,75: Description
     
   * :attr: .. _ref-IEC101slXMLSettings:
       
            :xmlref:`XMLSettings`
     :val:  See table :numref:`ref-IEC101slXMLSettingsAttributes`
     :desc: XML parse setting specification node. Refer to table :numref:`ref-IEC101slXMLSettingsAttributes` for attribute specification.

   * :attr: .. _ref-IEC101slLinkSettings:
       
            :xmlref:`LinkSettings`
     :val:  See table :numref:`ref-IEC101slLinkSettingsAttributes`
     :desc: Communication link layer timeout and control bit configuration node. Refer to table :numref:`ref-IEC101slLinkSettingsAttributes` for attribute specification.

   * :attr: .. _ref-IEC101slCommsSettings:
       
            :xmlref:`CommsSettings`
     :val:  See table :numref:`ref-IEC101slCommsSettingsAttributes`
     :desc: Communication status (e.g. online and offline) change behavior and related delay configuration node. Refer to table :numref:`ref-IEC101slCommsSettingsAttributes` for attribute specification.

   * :attr: .. _ref-IEC101slASDUSettings:
       
            :xmlref:`ASDUSettings`
     :val:  See table :numref:`ref-IEC101slASDUSettingsAttributes`
     :desc: Various application layer settings configuration node. Refer to table :numref:`ref-IEC101slASDUSettingsAttributes` for attribute specification.

   * :attr: .. _ref-IEC101slTimeouts:
       
            :xmlref:`Timeouts`
     :val:  See table :numref:`ref-IEC101slTimeoutsAttributes`
     :desc: Control command expiration timeout configuration node. Refer to table :numref:`ref-IEC101slTimeoutsAttributes` for attribute specification.

   * :attr: .. _ref-IEC101slTimeSettings:
       
            :xmlref:`TimeSettings`
     :val:  See table :numref:`ref-IEC101slTimeSettingsAttributes`
     :desc: Unique time settings (e.g. time zone) of particular protocol instance. Refer to table :numref:`ref-IEC101slTimeSettingsAttributes` for attribute specification.

   * :attr: .. _ref-IEC101slPeriodic:
       
            :xmlref:`Periodic`
     :val:  See table :numref:`ref-IEC101slPeriodicAttributes`
     :desc: Periodically generated message configuration node. Refer to table :numref:`ref-IEC101slPeriodicAttributes` for attribute specification.

   * :attr: .. _ref-IEC101slBufferSizes:
       
            :xmlref:`BufferSizes`
     :val:  See table :numref:`ref-IEC101slBufferSizesAttributes`
     :desc: Various application layer buffer size configuration node. Refer to table :numref:`ref-IEC101slBufferSizesAttributes` for attribute specification.

.. include-file:: sections/Include/XMLSettings.rstinc "" ":ref:`XMLSettings<ref-IEC101slXMLSettings>`" ".. _ref-IEC101slXMLSettingsAttributes:" "IEC 60807-5-101 Slave XMLSettings attributes"
.. include:: IEC101slConfig/LinkSettings.rst
.. include:: IEC101slConfig/CommsSettings.rst
.. include:: IEC101slConfig/ASDUSettings.rst
.. include-file:: sections/Include/IEC10xslConfig_Timeouts.rstinc "" ":ref:`Timeouts<ref-IEC101slTimeouts>`" ".. _ref-IEC101slTimeoutsAttributes:" "IEC 60807-5-101 Slave Timeouts attributes"
.. include-file:: sections/Include/TimeSettings.rstinc "" ":ref:`TimeSettings<ref-IEC101slTimeSettings>`" ".. _ref-IEC101slTimeSettingsAttributes:" "IEC 60807-5-101/104 Slave TimeSettings attributes" ".. _ref-IEC101slTimeSettingsTimeZone:"
.. include-file:: sections/Include/IEC10xslConfig_Periodic.rstinc "" ":ref:`Periodic<ref-IEC101slPeriodic>`" ".. _ref-IEC101slPeriodicAttributes:" "IEC 60807-5-101 Slave Periodic attributes"
.. include-file:: sections/Include/IEC10xslConfig_BufferSizes.rstinc "" ":ref:`BufferSizes<ref-IEC101slBufferSizes>`" ".. _ref-IEC101slBufferSizesAttributes:" "IEC 60807-5-101 Slave BufferSizes attributes"
.. include-file:: sections/Include/BufferSizesAttribute_ASDUTx.rstinc
