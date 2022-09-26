.. _xmlgroup-ModbusmaProtocolCfg: lelabel=ProtocolCfg

ProtocolCfg group
-----------------

.. include-file:: sections/Include/ProtocolCfg.rstinc "" "Modbus Master" ":ref:`xmlgroup-ModbusmaProtocolCfg`"

.. code-block:: none

 <ProtocolCfg>
   <LinkSettings … />
   <CommsSettings … />
   <Hardcoded … />
   <AppSettings … />
   <ServiceSettings … />
   <Timeouts … />
   <TimeSettings … />
   <Periodic … />
 </ProtocolCfg>

.. tip:: All element nodes are optional, default values will be used for attributes of omitted nodes.

.. include:: Modbusma/LinkSettings.rst
.. include:: Modbusma/CommsSettings.rst
.. include:: Modbusma/Hardcoded.rst
.. include:: Modbusma/AppSettings.rst

.. include-file:: sections/Include/ma_ServiceSettings.rstinc "" ".. _xmlelem-ModbusmaService:" ":ref:`xmlelem-ModbusmaService`" "tabid-ModbusmaService" "Modbus Master ServiceSettings attributes"
.. include-file:: sections/Include/EventMask.rstinc "" ":ref:`xmlattr-ModbusmaServiceEventMask`" "tabid-ModbusmaServiceEventMask" ":numref:`tabid-ModbusmaServiceEventMask`" ":ref:`xmlattr-ModbusmaCommOfflineDelay`" ":ref:`xmlattr-ModbusmaCommPostOfflineDelay`"

.. include:: Modbusma/Timeouts.rst
.. include:: Modbusma/TimeSettings.rst
.. include:: Modbusma/Periodic.rst
