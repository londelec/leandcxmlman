.. _ref-ModbusmaProtocolCfg:

ProtocolCfg group node
----------------------

.. include-file:: sections/Include/ProtocolCfg.rstinc "" "Modbus Master" ":ref:`ProtocolCfg<ref-ModbusmaProtocolCfg>`"

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

.. include:: Modbusma/LinkSettings.rst
.. include:: Modbusma/CommsSettings.rst
.. include:: Modbusma/Hardcoded.rst
.. include:: Modbusma/AppSettings.rst

.. include-file:: sections/Include/ma_ServiceSettings.rstinc "" ".. _ref-ModbusmaServiceSettings:" ":ref:`<ref-ModbusmaServiceSettings>`" ".. _docref-ModbusmaServiceSettingsAttab:" "Modbus Master ServiceSettings attributes"
.. include-file:: sections/Include/EventMask.rstinc "" ".. _docref-ModbusmaServiceEventMaskAttab:" ":numref:`docref-ModbusmaServiceEventMaskAttab`" ":ref:`<ref-ModbusmaCommsSettingsOfflineDelay>`" ":ref:`<ref-ModbusmaCommsSettingsPostOfflineDelay>`"

.. include:: Modbusma/Timeouts.rst
