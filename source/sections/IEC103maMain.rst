.. include:: global.roles

.. _docref-IEC103ma:
.. _xmlgroup-IEC103maConfig: lelabel=IEC103maConfig

IEC60870-5-103 Master
=====================

.. include-file:: sections/Include/IEC60870_root.rstinc "" "IEC60870-5-103 controlling station (Master)" "is acquired from several IEDs"

.. include-file:: sections/Include/sample_xml.rstinc "" "IEC103ma_test.xml" ":ref:`xmlelem-gp103ma`" ":ref:`xmlattr-gp103maXMLpath`"

| IEC60870-5-103 Master configuration file (e.g. 'IEC103ma_test.xml') must have a root node :ref:`xmlgroup-IEC103maConfig` which cosists of:
| 2 mandatory groups :ref:`xmlelem-VersionControl` and :ref:`xmlgroup-IEC103maProtocolCfg`; 
| 3 optional IO object groups :ref:`xmlgroup-IEC103maDI`; :ref:`xmlgroup-IEC103maAI` and :ref:`xmlgroup-IEC103maDO`.
| Please see the sample below.

.. code-block:: none

 <IEC103maConfig xmlns="http://www.londelec.com/xmlschemas/leandc/IEC103ma" … version="1.00">
   <VersionControl conf="4" date="2022-01-18" time="10:08:09"/>
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

:ref:`xmlgroup-IEC103maDI`; :ref:`xmlgroup-IEC103maAI`; :ref:`xmlgroup-IEC103maDO` groups make up the IO object table of the
IEC60870-5-103 controlling station (Master) communication protocol instance.
Please refer to the tables :numref:`tabid-IEC103maDI`; :numref:`tabid-IEC103maAI` and :numref:`tabid-IEC103maDO` for their attributes.

.. include:: IEC103ma/ProtocolCfg.rst
.. include:: IEC103ma/DITable.rst
.. include:: IEC103ma/AITable.rst
.. include:: IEC103ma/DOTable.rst
