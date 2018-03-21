.. include:: global.roles

.. _ref-IEC61850clMain:

IEC61850 Client
===============

This section describes how to configure IEC61850 Client communication protocol
instance. IEC61850 standard specifies a System Configuration Language (SCL) for files which are
used to store configuration data of the IED. Most commonly used files are IED Capability Description (ICD),
Configured IED Description (CID) and System Configuration Description (SCD). CID or SCD file is
required for each IEC61850 Client communication protocol instance. It contains communication capabilities
and settings of a Server station (IED) we would like to communicate to. In addition to CID/SCD file
a XML configuration file is required. It contains IO object table and additional protocol-related settings.
The same pairs of CID/SCD and XML files can be used for multiple IEC61850 Client communication protocol instances.
It becomes very useful if multiple outstations have identical sets of IO objects.

Name and location path of the configuration files is not predefined, it can be chosen freely.
Files '**IED_IO.xml**' and '**IED.cid**' are used as a sample.
Enter names of the files in :ref:`<ref-IEC61850cl>`.\ :ref:`<ref-IEC61850clXMLpath>` \ and :ref:`<ref-IEC61850cl>`.\ :ref:`<ref-IEC61850clCIDpath>` \ attributes of a communication protocol instance created in **leandc.xml** as follows:
:ref:`<ref-IEC61850clXMLpath>`\ ="IED_IO.xml" and :ref:`<ref-IEC61850clCIDpath>`\ ="IED.cid" .
Location path doesn't have to be specified if the files are stored in the default directory (/home/leandc/app).

IEC61850 Client configuration file (e.g. '**IED_IO.xml**') must have a root object node :xmlref:`IEC61850clConfig` which has
2 mandatory child group object nodes :ref:`VersionControl<ref-VersionControl>`; :ref:`ProtocolCfg<ref-IEC61850clProtocolCfg>`
and 4 optional child group object nodes :ref:`DITable<ref-IEC61850clDI>`; :ref:`AITable<ref-IEC61850clAI>`; :ref:`DOTable<ref-IEC61850clDO>`; :ref:`AOTable<ref-IEC61850clAO>`
please see the sample below.

.. code-block:: none

   <IEC61850clConfig xmlns="http://www.londelec.com/xmlschemas/leandc/IEC61850cl" … version="1.00">
      <VersionControl conf="4.00" date="2016-01-25" time="12:00:09"/>
      <ProtocolCfg>
         <CommsSettings OfflineDelay="10"/>
	 <TransportSettings CallingTSEL="0x0A" SourceREF="0x04"/>
         …
      </ProtocolCfg>
      <DITable>
         <DI Index="0" ldInst="LD0" prefix="DA" lnClass="XCBR" lnInst="1" doName="Pos" fc="ST"/>
         …
      </DITable>
      <AITable>
         <AI Index="0" ldInst="LD0" prefix="CPH" lnClass="MMXU" lnInst="1" doName="A.phsA" fc="MX"/>
         …
      </AITable>
      <DOTable>
         <DO Index="0" ldInst="LD0" prefix="GNRL" lnClass="CSWI" lnInst="1" doName="Pos" fc="CO"/>
         …
      </DOTable>
      <AOTable>
         <AO Index="0" ldInst="LD0" prefix="GNRL" lnClass="CSWI" lnInst="1" doName="Mod" fc="CO"/>
         …
      </AOTable>
   </IEC61850clConfig>

:ref:`DITable<ref-IEC61850clDI>`; :ref:`AITable<ref-IEC61850clAI>`; :ref:`DOTable<ref-IEC61850clDO>`; :ref:`AOTable<ref-IEC61850clAO>` group nodes form the IO object table
of the IEC61850 Client communication protocol instance. Please
refer to the tables :numref:`ref-IEC61850clDIAttributes`; :numref:`ref-IEC61850clAIAttributes`; :numref:`ref-IEC61850clDOAttributes` and :numref:`ref-IEC61850clAOAttributes` for their attributes.

.. include:: IEC61850cl/ProtocolCfg.rst
.. include:: IEC61850cl/DITable.rst
.. include:: IEC61850cl/AITable.rst
.. include:: IEC61850cl/TrgOps.rst
.. include:: IEC61850cl/DOTable.rst
.. include:: IEC61850cl/AOTable.rst
