.. include:: global.roles

.. _ref-IEC103maConfig:

IEC60870-5-103 Master
=====================

This section describes how to configure IEC60870-5-103 controlling station (Master) communication protocol instance.
Each IEC60870-5-103 controlling station (Master) communication protocol instance must have XML configuration file where its IO object table and additional protocol-related settings will be stored.
One and the same XML configuration file can be used for multiple IEC60870-5-103 controlling station (Master) communication protocol instances, this becomes useful in case if identical sets of IO objects are acquired from several outstations.

Name and location path of the XML configuration file are not predefined, they can be chosen freely.
File name '**Feeder_F1.xml**' will be used as a sample and location path doesn't need to be specified if XML file is stored in the same directory as leandc firmware.
In order to use the XML file for a communication protocol instance, simply enter the name '**Feeder_F1.xml**' in :ref:`<ref-IEC103ma>`.\ :ref:`<ref-IEC103maXMLpath>` \ attribute.

IEC60870-5-103 Master configuration file (e.g. '**Feeder_F1.xml**') must have a root object node :xmlref:`IEC103maConfig` 
which has 5 child group object nodes :ref:`VersionControl<ref-VersionControl>`; :ref:`ProtocolCfg<ref-IEC103maProtocolCfg>`; :ref:`DITable<ref-IEC103maDITable>`; :ref:`AITable<ref-IEC103maAITable>`; :ref:`DOTable<ref-IEC103maDOTable>` please see the 
sample below.

.. code-block:: none

   <IEC103maConfig xmlns="http://www.londelec.com/xmlschemas/leandc/IEC103ma" … version="1.00"> 
      <VersionControl conf="4" date="2014-01-18" time="10:08:09"/>
      <ProtocolCfg> 
         <CommsSettings OfflineDelay="120" />
         <ASDUSettings SUthroughoutDST="1" />
         …
      </ProtocolCfg>
      <DITable> 
         <DI Index="0" qualifier="0" FUN="240" INF="160"/> 
         …
      </DITable> 
      <AITable> 
         <AI Index="0" qualifier="0" FUN="134" INF="148" MEA="0" Coeff="0.09" Percent="0.1"/> 
         …
      </AITable> 
      <DOTable> 
         <DO Index="0" qualifier="0" FUN="240" INF="160" TypeID="0"/> 
         …
      </DOTable> 
   </IEC103maConfig>

:ref:`DITable<ref-IEC103maDITable>`; :ref:`AITable<ref-IEC103maAITable>`; :ref:`DOTable<ref-IEC103maDOTable>` group nodes compose an IO object table of the IEC60870-5-103 controlling station 
(Master) communication protocol instance. Please 
refer to the tables :numref:`ref-IEC103maDIAttributes`; :numref:`ref-IEC103maAIAttributes` and :numref:`ref-IEC103maDOAttributes` for their attributes.
  
.. include:: IEC103ma/ProtocolCfg.rst
.. include:: IEC103ma/DITable.rst
.. include:: IEC103ma/AITable.rst
.. include:: IEC103ma/DOTable.rst
