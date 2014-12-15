.. include:: global.roles

.. _ref-ModbusmaMain:

Modbus Master configuration
===================================

This section describes how to configure Modbus RTU/ASCII/TCP Master communication protocol 
instance. Each Modbus Master communication protocol instance must have XML 
configuration file where its IO object table and additional protocol-related settings are stored.
XML configuration file can be used for multiple Modbus Master 
communication protocol instances, this becomes useful in case if multiple outstations have identical sets of IO objects.

Name and location path of the XML configuration file is not predefined, it can be chosen freely. File name 
'**Device_IO.xml**' will be used as a sample. Location path doesn't need to be specified if XML file is stored in 
the same directory as leandc firmware. In order to use the XML file for a communication protocol instance, 
simply enter the name '**Device_IO.xml**' in :ref:`Modbusma<ref-ModbusmaMain>`.\ :ref:`XMLpath<ref-ModbusmaXMLpath>` \ attribute.

Modbus Master configuration file (e.g. '**Device_IO.xml**') must have a root object node :xmlref:`ModbusmaConfig` which has 
2 mandatory child group object nodes :ref:`VersionControl<ref-VersionControl>`; :ref:`ProtocolCfg<ref-ModbusmaProtocolCfg>` 
and 3 optional child group object nodes :ref:`DITable<ref-ModbusmaDI>`; :ref:`AITable<ref-ModbusmaAI>`; :ref:`DOTable<ref-ModbusmaDO>` please see the 
sample below.

.. code-block:: none

   <ModbusmaConfig xmlns="http://www.londelec.com/xmlschemas/leandc/Modbusma" … version="1.00"> 
      <VersionControl conf="4.00" date="2014-11-25" time="12:00:09"/>
      <ProtocolCfg> 
         <LinkSettings Type="RTU" />
         <CommsSettings NoRespCount="5" DegradedRetries="3" DegradedTimeout="60" OfflineDelay="10" />
	 <Hardcoded Type="BCAIIS8" />
         …
      </ProtocolCfg>
      <DITable>
         <DI Index="0" qualifier="0" Total="2"/>
         …
      </DITable>
      <AITable>
         <AI Index="0" qualifier="0" Coeff="0.09" Deadband="0.1"/>
         …
      </AITable>
      <DOTable>
         <DO Index="0" qualifier="0" Total="2"/>
         …
      </DOTable>
   </ModbusmaConfig>

:ref:`DITable<ref-ModbusmaDI>`; :ref:`AITable<ref-ModbusmaAI>`; :ref:`DOTable<ref-ModbusmaDO>` group nodes compose an IO object table of the Modbus 
Master communication protocol instance. Please 
refer to the tables :numref:`ref-ModbusmaDIAttributes`; :numref:`ref-ModbusmaAIAttributes` and :numref:`ref-ModbusmaDOAttributes` for their attributes.
  
.. include:: Modbusma/ProtocolCfg.rst
.. include:: Modbusma/DITable.rst
.. include:: Modbusma/AITable.rst
.. include:: Modbusma/DOTable.rst
