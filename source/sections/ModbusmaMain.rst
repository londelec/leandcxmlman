.. include:: global.roles

.. _docref-Modbusma:
.. _xmlgroup-ModbusmaConfig: lelabel=ModbusmaConfig

Modbus Master
=============

This section contains details on how to configure Modbus RTU/ASCII/TCP Master communication protocol instance.
Each Modbus Master instance must have XML configuration file where Modbus messages, IO object table and additional protocol-related settings are stored.
One XML file can be used for multiple communication protocol instances.
It may be useful if multiple outstations have identical set of IO objects.

.. include-file:: sections/Include/sample_xml.rstinc "" "Device_IO.xml" ":ref:`xmlelem-gpmodbusma`" ":ref:`xmlattr-gpmodbusmaXMLpath`"

| Modbus Master configuration file (e.g. 'Device_IO.xml') must have a root object node :ref:`xmlgroup-ModbusmaConfig` which cosists of:
| 2 mandatory groups :ref:`xmlelem-VersionControl` and :ref:`xmlgroup-ModbusmaProtocolCfg`;
| 3 optional message configuration groups :ref:`xmlgroup-ModbusmaInitMessages`; :ref:`xmlgroup-ModbusmaPollMessages` and :ref:`xmlgroup-ModbusmaCtrlMessages`;
| 4 optional IO object groups :ref:`xmlgroup-ModbusmaDI`; :ref:`xmlgroup-ModbusmaAI`; :ref:`xmlgroup-ModbusmaDO` and :ref:`xmlgroup-ModbusmaAO`.
| Please see the sample below.

.. code-block:: none

 <ModbusmaConfig xmlns="http://www.londelec.com/xmlschemas/leandc/Modbusma" … version="1.00">
   <VersionControl conf="2.00" date="2022-03-19" time="12:00:09"/>
   <ProtocolCfg>
     <LinkSettings Type="RTU" />
     <CommsSettings NoRespCount="5" DegradedRetries="3" DegradedTimeout="60" OfflineDelay="10" />
     <Hardcoded Type="BCAIIS8" />
         …
   </ProtocolCfg>
   <InitMessages>
     <MSG InitMsg="1" Func="17" Data="0x00"/>
         …
   </InitMessages>
   <PollMessages>
     <MSG PollMsg="1" Func="3" Reg="0x0002" Count="1"/>
         …
   </PollMessages>
   <CtrlMessages>
     <MSG CtrlMsg="1" Func="6" Reg="0x000A" Data="0x0000"/>
         …
   </CtrlMessages>
   <DITable>
     <DI Index="0" PollMsg="1" BitOffset="0" Type="1" Total="2"/>
         …
   </DITable>
   <AITable>
     <AI Index="0" PollMsg="1" RegOffset="0" Type="33" Coeff="0.09" Deadband="0.1"/>
         …
   </AITable>
   <DOTable>
     <DO Index="0" CtrlMsg="1" BitOffset="0"/>
         …
   </DOTable>
   <AOTable>
     <AO Index="0" CtrlMsg="1" Coeff="1"/>
         …
   </AOTable>
 </ModbusmaConfig>

:ref:`xmlgroup-ModbusmaInitMessages`; :ref:`xmlgroup-ModbusmaPollMessages`; :ref:`xmlgroup-ModbusmaCtrlMessages` groups contain
Modbus messages used for communication to outstation.
Messages don't have to be defined if device type is specified in :ref:`xmlelem-ModbusmaHardcoded`.\ :ref:`xmlattr-ModbusmaHardcodedType` attribute.

:ref:`xmlgroup-ModbusmaDI`; :ref:`xmlgroup-ModbusmaAI`; :ref:`xmlgroup-ModbusmaDO`; :ref:`xmlgroup-ModbusmaAO` groups make up the IO object table of the Modbus
Master communication protocol instance.
Please refer to the tables :numref:`tabid-ModbusmaDI`; :numref:`tabid-ModbusmaAI`; :numref:`tabid-ModbusmaDO` and :numref:`tabid-ModbusmaAO` for their attributes.

.. include:: Modbusma/ProtocolCfg.rst
.. include:: Modbusma/InitMessages.rst
.. include:: Modbusma/PollMessages.rst
.. include:: Modbusma/CtrlMessages.rst
.. include:: Modbusma/DITable.rst
.. include:: Modbusma/AITable.rst
.. include:: Modbusma/DOTable.rst
.. include:: Modbusma/AOTable.rst
