.. include:: global.roles

.. _docref-Spabusma:
.. _xmlgroup-SpabusmaConfig: lelabel=SpabusmaConfig

Spabus Master
=============

This section contains details on how to configure Spabus Master communication protocol instance.
Each Spabus Master instance must have XML configuration file where Spabus messages, IO object table and additional protocol-related settings are stored.
One XML file can be used for multiple communication protocol instances.
It may be useful if multiple IEDs have identical set of IO objects.

.. include-file:: sections/Include/sample_xml.rstinc "" "IED1.xml" ":ref:`xmlelem-gpspabusma`" ":ref:`xmlattr-gpspabusmaXMLpath`"

| Spabus Master configuration file (e.g. 'IED1.xml') must have a root node :ref:`xmlgroup-SpabusmaConfig` which cosists of:
| 2 mandatory groups :ref:`xmlelem-VersionControl` and :ref:`xmlgroup-SpabusmaProtocolCfg`;
| 2 optional message configuration groups :ref:`xmlgroup-SpabusmaPollMessages` and :ref:`xmlgroup-SpabusmaCtrlMessages`;
| 4 optional IO object groups :ref:`xmlgroup-SpabusmaDI`; :ref:`xmlgroup-SpabusmaAI`; :ref:`xmlgroup-SpabusmaDO` and :ref:`xmlgroup-SpabusmaAO`.
| Please see the sample below.

.. code-block:: none

 <SpabusmaConfig xmlns="http://www.londelec.com/xmlschemas/leandc/spabusma" … version="1.00">
   <VersionControl conf="2.00" date="2022-04-01" time="12:00:09"/>
   <ProtocolCfg>
     <CommsSettings NoRespCount="5" DegradedRetries="3" DegradedTimeout="60" OfflineDelay="10" />
     <AppSettings RatioP0="2" RatioL="3" DnumRangeMax="16" ChannelRangeMax="8" />
         …
   </ProtocolCfg>
   <PollMessages>
     <MSG PollMsg="1" Channel="10" Category="V" DataNumber="1/4" Priority="0"/>
         …
   </PollMessages>
   <CtrlMessages>
     <MSG CtrlMsg="1" Channel="10" Category="V" DataNumber="1" Value="5"/>
         …
   </CtrlMessages>
   <DITable>
     <DI Index="0" Request="120V1" OnValue="2" OffValue="1" Total="2"/>
         …
   </DITable>
   <AITable>
     <AI Index="0" PollMsg="1" Coeff="0.09" Deadband="0.1"/>
         …
   </AITable>
   <DOTable>
     <DO Index="0" OnRequest="120V4" OffRequest="120V5" OnValue="1" OffValue="2"/>
         …
   </DOTable>
   <AOTable>
     <AO Index="0" CtrlMsg="1" Coeff="1"/>
         …
   </AOTable>
 </SpabusmaConfig>

:ref:`xmlgroup-SpabusmaPollMessages`; :ref:`xmlgroup-SpabusmaCtrlMessages` groups contain Spabus messages used for communication to outstation.
:ref:`xmlgroup-SpabusmaPollMessages` don't have to be defined if :ref:`xmlelem-SpabusmaDI`.\ :ref:`xmlattr-SpabusmaDIRequest` and :ref:`xmlelem-SpabusmaAI`.\ :ref:`xmlattr-SpabusmaAIRequest` attributes are used.
:ref:`xmlgroup-SpabusmaCtrlMessages` don't have to be defined if :ref:`xmlelem-SpabusmaDO`.\ :ref:`xmlattr-SpabusmaDOOnCtrlMsg` and :ref:`xmlelem-SpabusmaDO`.\ :ref:`xmlattr-SpabusmaDOOffCtrlMsg` attributes are used.

:ref:`xmlgroup-SpabusmaDI`; :ref:`xmlgroup-SpabusmaAI`; :ref:`xmlgroup-SpabusmaDO`; :ref:`xmlgroup-SpabusmaAO` groups make up the IO object table of the Spabus
Master communication protocol instance.
Please refer to the tables :numref:`tabid-SpabusmaDI`; :numref:`tabid-SpabusmaAI`; :numref:`tabid-SpabusmaDO` and :numref:`tabid-SpabusmaAO` for their attributes.

.. include:: Spabusma/ProtocolCfg.rst
.. include:: Spabusma/PollMessages.rst
.. include:: Spabusma/CtrlMessages.rst
.. include:: Spabusma/DITable.rst
.. include:: Spabusma/AITable.rst
.. include:: Spabusma/DOTable.rst
.. include:: Spabusma/AOTable.rst
