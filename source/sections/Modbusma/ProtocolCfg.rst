
.. _ref-ModbusmaProtocolCfg:

ProtocolCfg group node
----------------------

Protocol-related settings of the Modbus Master communication protocol instance 
are configured using various child element nodes under :ref:`ProtocolCfg<ref-ModbusmaProtocolCfg>` group node. 

.. important:: It is essential to keep element nodes in the listed order otherwise it will affect the XML file validation.

Please see sample :ref:`ProtocolCfg<ref-ModbusmaProtocolCfg>` group node and the table listing all available child element nodes below. 

.. code-block:: none

 <ProtocolCfg>
	<LinkSettings … />
	<CommsSettings … />
	<Hardcoded … />
	<AppSettings … />
	<Timeouts … />
 </ProtocolCfg>

.. tip:: All element nodes are optional, default values will be used for attributes of omitted nodes.

.. _ref-ModbusmaProtocolCfgAttributes:

.. field-list-table:: Modbus Master ProtocolCfg child element nodes
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.20}|C{0.25}|S{0.55}|
   :header-rows: 1

   * :attr,10: Attribute
     :val,15:  Values or range
     :desc,75: Description

   * :attr:    .. _ref-ModbusmaLinkSettings:
       
               :xmlref:`LinkSettings`
     :val:     See table :numref:`ref-ModbusmaLinkSettingsAttributesTab`
     :desc:    Communication link settings configuration node. Refer to section :ref:`LinkSettings Attributes<ref-ModbusmaLinkSettingsAttributes>` for detailed specification.

   * :attr:    .. _ref-ModbusmaCommsSettings:
       
               :xmlref:`CommsSettings`
     :val:     See table :numref:`ref-ModbusmaCommsSettingsAttributesTab`
     :desc:    Communication status (e.g. online and offline) reporting and related delay configuration node. Refer to section :ref:`CommsSettings Attributes<ref-ModbusmaCommsSettingsAttributes>` for detailed specification.

   * :attr:    .. _ref-ModbusmaHardcoded:
       
               :xmlref:`Hardcoded`
     :val:     See table :numref:`ref-ModbusmaHardcodedAttributesTab`
     :desc:    Predefined Modbus device specification node. Refer to section :ref:`Hardcoded Attributes<ref-ModbusmaHardcodedAttributes>` for detailed specification.

   * :attr:    .. _ref-ModbusmaAppSettings:
       
               :xmlref:`AppSettings`
     :val:     See table :numref:`ref-ModbusmaAppSettingsAttributesTab`
     :desc:    Various application layer settings configuration node. Refer to section :ref:`AppSettings Attributes<ref-ModbusmaAppSettingsAttributes>` for detailed specification.

   * :attr:    .. _ref-ModbusmaTimeouts:
       
               :xmlref:`Timeouts`
     :val:     See table :numref:`ref-ModbusmaTimeoutsAttributesTab`
     :desc:    Various timeout configuration node. Refer to section :ref:`Timeouts Attributes<ref-ModbusmaTimeoutsAttributes>` for detailed specification.


.. include:: Modbusma/LinkSettings.rst
.. include:: Modbusma/CommsSettings.rst
.. include:: Modbusma/Hardcoded.rst
.. include:: Modbusma/AppSettings.rst
.. include:: Modbusma/Timeouts.rst
    
