.. include:: global.roles

.. _docref-IEC61850cl:
.. _xmlgroup-IEC61850clConfig: lelabel=IEC61850clConfig

IEC61850 Client
===============

This section contains details on how to configure IEC61850 Client communication protocol instance.
IEC61850 standard specifies the System Configuration Language (SCL) for files which are used to store configuration data of the IED. 
Most commonly used files are IED Capability Description (ICD), Configured IED Description (CID) and System Configuration Description (SCD).
CID or SCD file is required for each IEC61850 Client communication protocol instance.
It contains communication capabilities and settings of the Server station (IED) we need to communicate to.
In addition to CID/SCD file a XML configuration file is required.
It contains IO object table and additional protocol-related settings.
The same pair of CID/SCD and XML files can be used for multiple communication protocol instances.
It may be useful if multiple IEDs have identical set of IO objects.

Name and location path of the configuration files is not predefined, it can be chosen freely.
Files 'IED_IO.xml' and 'IED.cid' are used as a sample.
Enter names of the files in :ref:`xmlelem-gp61850cl`.\ :ref:`xmlattr-gp61850clXMLpath` \ and :ref:`xmlelem-gp61850cl`.\ :ref:`xmlattr-gp61850clSCLpath` \ attributes of the communication protocol instance created in |leandcxml| as follows:
:ref:`xmlattr-gp61850clXMLpath`\ ="IED_IO.xml" and :ref:`xmlattr-gp61850clSCLpath`\ ="IED.cid" .
Location path doesn't have to be specified if the files are located in the default directory (|leandcapp|).

| IEC61850 Client configuration file (e.g. 'IED_IO.xml') must have a root node :ref:`xmlgroup-IEC61850clConfig` which cosists of:
| 2 mandatory groups :ref:`xmlelem-VersionControl` and :ref:`xmlgroup-IEC61850clProtocolCfg`;
| 4 optional IO object groups :ref:`xmlgroup-IEC61850clDI`; :ref:`xmlgroup-IEC61850clAI`; :ref:`xmlgroup-IEC61850clDO` and :ref:`xmlgroup-IEC61850clAO`.
| Please see the sample below.

.. code-block:: none

 <IEC61850clConfig xmlns="http://www.londelec.com/xmlschemas/leandc/IEC61850cl" … version="1.00">
   <VersionControl conf="4.00" date="2022-01-25" time="12:00:09"/>
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

:ref:`xmlgroup-IEC61850clDI`; :ref:`xmlgroup-IEC61850clAI`; :ref:`xmlgroup-IEC61850clDO`; :ref:`xmlgroup-IEC61850clAO` groups make up the IO object table
of the IEC61850 Client communication protocol instance.
Please refer to the tables :numref:`tabid-IEC61850clDI`; :numref:`tabid-IEC61850clAI`; :numref:`tabid-IEC61850clDO` and :numref:`tabid-IEC61850clAO` for their attributes.

.. include:: IEC61850cl/ProtocolCfg.rst
.. include:: IEC61850cl/DITable.rst
.. include:: IEC61850cl/AITable.rst
.. include:: IEC61850cl/TrgOps.rst
.. include:: IEC61850cl/DOTable.rst
.. include:: IEC61850cl/AOTable.rst
