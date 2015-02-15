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
        <ServiceSettings … />
	<Timeouts … />
 </ProtocolCfg>

.. tip:: All element nodes are optional, default values will be used for attributes of omitted nodes.

.. _docref-ModbusmaProtocolCfgNotab:

.. field-list-table:: Modbus Master ProtocolCfg child element nodes
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.20}|C{0.25}|S{0.55}|
   :header-rows: 1

   * :attr,10: Node
     :val,15:  Attributes
     :desc,75: Description

   * :attr:    .. _ref-ModbusmaLinkSettings:
       
               :xmlref:`LinkSettings`
     :val:     See table :numref:`docref-ModbusmaLinkSettingsAttab`
     :desc:    Communication link settings configuration node. Refer to section :ref:`docref-ModbusmaLinkSettingsAttr` for details.

   * :attr:    .. _ref-ModbusmaCommsSettings:
       
               :xmlref:`CommsSettings`
     :val:     See table :numref:`docref-ModbusmaCommsSettingsAttab`
     :desc:    Communication status (e.g. online and offline) reporting and related delay configuration node. Refer to section :ref:`docref-ModbusmaCommsSettingsAttr` for details.

   * :attr:    .. _ref-ModbusmaHardcoded:
       
               :xmlref:`Hardcoded`
     :val:     See table :numref:`docref-ModbusmaHardcodedAttab`
     :desc:    Predefined Modbus device specification node. Refer to section :ref:`docref-ModbusmaHardcodedAttr` for details.

   * :attr:    .. _ref-ModbusmaAppSettings:
       
               :xmlref:`AppSettings`
     :val:     See table :numref:`docref-ModbusmaAppSettingsAttab`
     :desc:    Various application layer settings configuration node. Refer to section :ref:`docref-ModbusmaAppSettingsAttr` for details.

   * :attr: .. _ref-ModbusmaServiceSettings:
       
            :xmlref:`ServiceSettings`
     :val:  See table :numref:`docref-ModbusmaServiceSettingsAttab`
     :desc: Service settings configuration node. Refer to section :ref:`docref-ModbusmaServiceSettingsAttr` for details.

   * :attr:    .. _ref-ModbusmaTimeouts:
       
               :xmlref:`Timeouts`
     :val:     See table :numref:`docref-ModbusmaTimeoutsAttab`
     :desc:    Various timeout configuration node. Refer to section :ref:`docref-ModbusmaTimeoutsAttr` for details.


.. include:: Modbusma/LinkSettings.rst
.. include:: Modbusma/CommsSettings.rst
.. include:: Modbusma/Hardcoded.rst
.. include:: Modbusma/AppSettings.rst

.. include-file:: sections/Include/ma_ServiceSettings.rstinc "" ".. _docref-ModbusmaServiceSettingsAttr:" ":ref:`ServiceSettings<ref-ModbusmaServiceSettings>`" ".. _docref-ModbusmaServiceSettingsAttab:" "Modbus Master ServiceSettings attributes"
.. include-file:: sections/Include/EventMask.rstinc "" ".. _docref-ModbusmaServiceEventMaskAttab:" ":numref:`docref-ModbusmaServiceEventMaskAttab`" ":ref:`OfflineDelay<ref-ModbusmaCommsSettingsOfflineDelay>`" ":ref:`PostOfflineDelay<ref-ModbusmaCommsSettingsPostOfflineDelay>`"

.. include:: Modbusma/Timeouts.rst
