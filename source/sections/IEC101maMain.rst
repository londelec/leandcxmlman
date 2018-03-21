.. include:: global.roles

.. _docref-IEC101maConfig:
.. _ref-IEC101maConfig:

IEC60870-5-101 Master
=====================

This section describes how to configure IEC60870-5-101 controlling station (Master) communication protocol
instance. Each IEC60870-5-101 controlling station (Master) communication protocol instance must have XML
configuration file where its IO object table and additional protocol-related settings will be stored. One and the
same XML configuration file can be used for multiple IEC60870-5-101 controlling station (Master)
communication protocol instances, this becomes useful in case if identical sets of IO objects are acquired from
several outstations.

.. include-file:: sections/Include/sample_xml.rstinc "" "IEC101ma_test.xml" ":ref:`<ref-IEC101ma>`" ":ref:`<ref-IEC101maXMLpath>`"

IEC60870-5-101 Master configuration file (e.g. '**IEC101ma_test.xml**') must have a root object node
:xmlref:`IEC101maConfig` which has 5 child group object nodes :ref:`VersionControl<ref-VersionControl>`; :ref:`ProtocolCfg<ref-IEC101maProtocolCfg>`; :ref:`DITable<ref-IEC10xmaDITable>`; :ref:`AITable<ref-IEC10xmaAITable>`;
:ref:`DOTable<ref-IEC10xmaDOTable>`; :ref:`AOTable<ref-IEC10xmaAOTable>` please see the sample below.

.. code-block:: none

   <IEC101maConfig xmlns="http://www.londelec.com/xmlschemas/leandc/IEC101ma" …  version="1.00">
      <VersionControl conf="4" date="2014-01-18" time="10:08:09"/>
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
   </IEC101maConfig>

:ref:`DITable<ref-IEC10xmaDITable>`; :ref:`AITable<ref-IEC10xmaAITable>`; :ref:`DOTable<ref-IEC10xmaDOTable>`; :ref:`AOTable<ref-IEC10xmaAOTable>` group nodes compose an IO object table and they are common for
IEC60870-5-101 and IEC60870-5-104 controlling station (Master) communication protocol instances. Please
refer to the tables :numref:`ref-IEC10xmaDIAttributes`; :numref:`ref-IEC10xmaAIAttributes`; :numref:`ref-IEC10xmaDOAttributes` and :numref:`ref-IEC10xmaAOAttributes` for their attributes.

.. include:: IEC101ma/ProtocolCfg.rst
