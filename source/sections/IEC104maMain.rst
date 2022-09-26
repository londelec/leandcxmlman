.. include:: global.roles

.. _docref-IEC104ma:
.. _xmlgroup-IEC104maConfig: lelabel=IEC104maConfig

IEC60870-5-104 Master
=====================

.. include-file:: sections/Include/IEC60870_root.rstinc "" "IEC60870-5-104 controlling station (Master)" "is acquired from several outstations"

.. include-file:: sections/Include/sample_xml.rstinc "" "IEC104ma_test.xml" ":ref:`xmlelem-gp104ma`" ":ref:`xmlattr-gp104maXMLpath`"

| IEC60870-5-104 Master configuration file (e.g. 'IEC104ma_test.xml') must have a root node :ref:`xmlgroup-IEC104maConfig` which cosists of:
| 2 mandatory groups :ref:`xmlelem-VersionControl` and :ref:`xmlgroup-IEC104maProtocolCfg`;
| 4 optional IO object groups :ref:`xmlgroup-IEC10xmaDI`; :ref:`xmlgroup-IEC10xmaAI`; :ref:`xmlgroup-IEC10xmaDO` and :ref:`xmlgroup-IEC10xmaAO`.
| Please see the sample below.

.. code-block:: none

 <IEC104maConfig xmlns="http://www.londelec.com/xmlschemas/leandc/IEC104ma" …  version="1.00">
   <VersionControl conf="4" date="2022-01-18" time="10:08:09"/>
   <ProtocolCfg>
     <XMLSettings IOAOverlap="1" />
     <CommsSettings OfflineDelay="120" />
         …
   </ProtocolCfg>
   <DITable>
     <DI Index="0" InfAddr="1" qualifier="0x10" Total="16"/>
         …
   </DITable>
   <AITable>
     <AI Index="0" InfAddr="1" qualifier="0x00" Total="16" Coeff="1"/>
         …
   </AITable>
   <DOTable>
     <DO Index="0" InfAddr="1" TypeID="46" Total="16"/>
         …
   </DOTable>
   <AOTable>
     <AO Index="0" InfAddr="1" TypeID="50" Total="16"/>
         …
   </AOTable>
 </IEC104maConfig>

:ref:`xmlgroup-IEC10xmaDI`; :ref:`xmlgroup-IEC10xmaAI`; :ref:`xmlgroup-IEC10xmaDO`; :ref:`xmlgroup-IEC10xmaAO` groups make up the IO object table.
They are identical for IEC60870-5-101 and IEC60870-5-104 controlling station (Master) communication protocol instances.
Please refer to the tables :numref:`tabid-IEC10xmaDI`; :numref:`tabid-IEC10xmaAI`; :numref:`tabid-IEC10xmaDO` and :numref:`tabid-IEC10xmaAO` for their attributes.

.. include:: IEC104ma/ProtocolCfg.rst
