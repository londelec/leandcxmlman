.. include:: global.roles

.. _docref-IEC101slConfig:
.. _ref-IEC101slConfig:

IEC60870-5-101 Slave configuration
==================================

This section describes how to configure IEC 60870-5-101 controlled station (Slave) communication protocol 
instance. Each IEC 60870-5-101 controlled station (Slave) communication protocol instance must have XML 
configuration file where its IO object table and additional protocol-related settings will be stored. One and the 
same XML configuration file can be used for multiple IEC 60870-5-101 controlled station (Slave) communication 
protocol instances, this becomes useful in case if identical IO objects need to be reported to several Master stations.

Name and location path of the XML configuration file are not predefined, they can be chosen freely. File name 
'**IEC101sl_test.xml**' will be used as a sample and location path doesn't need to be specified if XML file is stored 
in the same directory as leandc firmware. In order to use the XML file for a communication protocol instance, 
simply enter the name '**IEC101sl_test.xml**' in the :ref:`IEC101sl<ref-IEC101sl>`.\ :ref:`XMLpath<ref-IEC101slXMLpath>` \ attribute.

IEC60870-5-101 Slave configuration file (e.g. 'IEC101sl_test.xml') must have a root object node 
:xmlref:`IEC101slConfig` which has 6 child group object nodes :ref:`VersionControl<ref-VersionControl>`; :ref:`ProtocolCfg<ref-IEC101slProtocolCfg>`; :ref:`DITable<ref-IEC10xslDITable>`; :ref:`AITable<ref-IEC10xslAITable>`; :ref:`DOTable<ref-IEC10xslDOTable>`; :ref:`AOTable<ref-IEC10xslAOTable>` please see the sample below.

.. code-block:: none

   <IEC101slConfig xmlns="http://www.londelec.com/xmlschemas/leandc/IEC101sl" … version="1.00"> 
         <VersionControl conf="4" date="2014-01-18" time="10:08:09"/>
         <ProtocolCfg> 
            <XMLSettings IOAOverlap="1" />
            <CommsSettings OfflineDelay="120" />
            …
         </ProtocolCfg> 
         <DITable> 
            <DI Device="10" Index="0" InfAddr="1" qualifier="0x10"/> 
            …
         </DITable> 
         <AITable> 
            <AI Device="10" Index="0" InfAddr="10" qualifier="0x00" Coeff="1.0"/> 
            …
         </AITable> 
         <DOTable> 
            <DO Device="10" Index="0" InfAddr="1"/> 
            …
         </DOTable> 
         <AOTable> 
            <AO Device="10" Index="0" InfAddr="1"/> 
            …
         </AOTable> 
   </IEC101slConfig>

:ref:`DITable<ref-IEC10xslDITable>`; :ref:`AITable<ref-IEC10xslAITable>`; :ref:`DOTable<ref-IEC10xslDOTable>`; :ref:`AOTable<ref-IEC10xslAOTable>` group nodes compose an IO object table and they are common for 
IEC60870-5-101 and IEC60870-5-104 controlled station (Slave) communication protocol instances. Please 
refer to the tables :numref:`ref-IEC10xslDIAttributes`; :numref:`ref-IEC10xslAIAttributes`; :numref:`ref-IEC10xslDOAttributes` and :numref:`ref-IEC10xslAOAttributes` for their attributes.   
   
.. include:: IEC101slConfig/ProtocolCfg.rst
