.. include:: global.roles

.. _docref-IEC104sl:
.. _xmlgroup-IEC104slConfig: lelabel=IEC104slConfig

IEC60870-5-104 Slave
====================

.. include-file:: sections/Include/IEC60870_root.rstinc "" "IEC60870-5-104 controlled station (Slave)" "need to be reported to several Master stations"

.. include-file:: sections/Include/sample_xml.rstinc "" "IEC104sl_test.xml" ":ref:`xmlelem-gp104sl`" ":ref:`xmlattr-gp104slXMLpath`"

| IEC60870-5-104 Slave configuration file (e.g. 'IEC104sl_test.xml') must have a root node :ref:`xmlgroup-IEC104slConfig` which cosists of:
| 2 mandatory groups :ref:`xmlelem-VersionControl` and :ref:`xmlgroup-IEC104slProtocolCfg`; 
| 5 optional IO object groups :ref:`xmlgroup-IEC10xslAuto`; :ref:`xmlgroup-IEC10xslDI`; :ref:`xmlgroup-IEC10xslAI`; :ref:`xmlgroup-IEC10xslDO` and :ref:`xmlgroup-IEC10xslAO`.
| Please see the sample below.

.. code-block:: none

 <IEC104slConfig xmlns="http://www.londelec.com/xmlschemas/leandc/IEC104sl" … version="1.00">
   <VersionControl conf="4" date="2022-01-18" time="10:08:09"/>
   <ProtocolCfg>
     <XMLSettings IOAOverlap="1" />
     <CommsSettings OfflineDelay="120" />
         …
   </ProtocolCfg>
   <AutoCfg>
     <AUTO Source="1" Name="RTU1"/>
         …
   </AutoCfg>
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
 </IEC104slConfig>

:ref:`xmlgroup-IEC10xslDI`; :ref:`xmlgroup-IEC10xslAI`; :ref:`xmlgroup-IEC10xslDO`; :ref:`xmlgroup-IEC10xslAO` groups make up the IO object table.
They are identical for IEC60870-5-101 and IEC60870-5-104 controlled station (Slave) communication protocol instances.
IO object table can be created manually by populating these groups or
:ref:`xmlgroup-IEC10xslAuto` group can be used to automatically include all IO objects of the source communication instance.

.. include:: IEC104sl/ProtocolCfg.rst
