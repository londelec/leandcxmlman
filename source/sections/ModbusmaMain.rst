.. include:: global.roles

.. _ref-ModbusmaMain:

Modbus Master
=============

This section describes how to configure Modbus RTU/ASCII/TCP Master communication protocol
instance. Each Modbus Master communication protocol instance must have XML
configuration file where Modbus messages, IO object table and additional protocol-related settings are stored.
One XML file can be used for multiple Modbus Master communication protocol instances.
It becomes very useful if multiple outstations have identical sets of IO objects.

Name and location path of the XML configuration file is not predefined, it can be chosen freely. File name
'**Device_IO.xml**' will be used as a sample. Location path doesn't have to be specified if XML file is stored in
the same directory as leandc.xml file. In order to use the XML file as for a communication protocol instance,
enter the name '**Device_IO.xml**' in :ref:`<ref-Modbusma>`.\ :ref:`<ref-ModbusmaXMLpath>` \ attribute.

Modbus Master configuration file (e.g. '**Device_IO.xml**') must have a root object node :xmlref:`ModbusmaConfig` which has
2 mandatory child group object nodes :ref:`VersionControl<ref-VersionControl>`; :ref:`ProtocolCfg<ref-ModbusmaProtocolCfg>`,
3 optional message configuration nodes :ref:`InitMessages<ref-InitMessages>`; :ref:`PollMessages<ref-PollMessages>`; :ref:`CtrlMessages<ref-CtrlMessages>`
and 3 optional child group object nodes :ref:`DITable<ref-ModbusmaDI>`; :ref:`AITable<ref-ModbusmaAI>`; :ref:`DOTable<ref-ModbusmaDO>`.
Please see the sample below.

.. code-block:: none

   <ModbusmaConfig xmlns="http://www.londelec.com/xmlschemas/leandc/Modbusma" … version="1.00">
      <VersionControl conf="2.00" date="2018-03-19" time="12:00:09"/>
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
   </ModbusmaConfig>

:ref:`InitMessages<ref-InitMessages>`; :ref:`PollMessages<ref-PollMessages>`; :ref:`CtrlMessages<ref-CtrlMessages>` group nodes contain
Modbus messages used for communication to outstation.
Messages don't have to be defined if any of Hardcoded device types is specified.

:ref:`DITable<ref-ModbusmaDI>`; :ref:`AITable<ref-ModbusmaAI>`; :ref:`DOTable<ref-ModbusmaDO>` group nodes make up an IO object table of the Modbus
Master communication protocol instance.
Please refer to the tables :numref:`docref-ModbusmaDIAttributes`; :numref:`docref-ModbusmaAIAttributes` and :numref:`docref-ModbusmaDOAttributes` for their attributes.

.. include:: Modbusma/ProtocolCfg.rst
.. include:: Modbusma/InitMessages.rst
.. include:: Modbusma/PollMessages.rst
.. include:: Modbusma/CtrlMessages.rst
.. include:: Modbusma/DITable.rst
.. include:: Modbusma/AITable.rst
.. include:: Modbusma/DOTable.rst
