.. _xmlgroup-IEC61850clProtocolCfg: lelabel=ProtocolCfg

ProtocolCfg group
-----------------

.. include-file:: sections/Include/ProtocolCfg.rstinc "" "IEC61850 Client" ":ref:`xmlgroup-IEC61850clProtocolCfg`"

.. code-block:: none

 <ProtocolCfg>
   <CommsSettings … />
   <TransportSettings … />
   <SessionSettings … />
   <PresentationSettings … />
   <AssociationSettings … />
   <MMSSettings … />
   <ScsmSettings … />
   <AcsiSettings … />
   <AppSettings … />
   <ServiceSettings … />
   <Timeouts … />
   <Periodic … />
 </ProtocolCfg>

.. tip:: All element nodes are optional, default values will be used for attributes of omitted nodes.

.. include:: IEC61850cl/CommsSettings.rst
.. include:: IEC61850cl/TransportSettings.rst
.. include:: IEC61850cl/SessionSettings.rst
.. include:: IEC61850cl/PresentationSettings.rst
.. include:: IEC61850cl/AssociationSettings.rst
.. include:: IEC61850cl/MmsSettings.rst


.. include-file:: sections/Include/table_flags8.rstinc "" "tabid-IEC61850clLogFlags" "IEC61850 Client informative logger flags" ":ref:`xmlattr-IEC61850clMmsLogFlags`" "Logger flags"

   * :attr:	Bit 0
     :val:	xxxx.xxx0
     :desc:	Basic level of logging **Disabled** (default value)

   * :(attr):
     :val:	xxxx.xxx1
     :desc:	Basic level of logging **Enabled**.
		Only generic information will be recorded to communication logfile.

   * :attr:	Bit 1
     :val:	xxxx.xx0x
     :desc:	Verbose level of logging **Disabled** (default value)

   * :(attr):
     :val:	xxxx.xx1x
     :desc:	Verbose level of logging **Enabled**.
		Values of all received data fields will be recorded to communication logfile.

.. include-file:: sections/Include/hidden_IEC61850_debuglog.rstinc "internal"

   * :attr:	Bits 2...7
     :val:	Any
     :desc:	Bits reserved for future use

| Informative logger flags summarized in this table apply to the following layers: 
|  :ref:`xmlelem-IEC61850clTransport`.\ :ref:`xmlattr-IEC61850clTransportLogFlags`
|  :ref:`xmlelem-IEC61850clSession`.\ :ref:`xmlattr-IEC61850clSessionLogFlags`
|  :ref:`xmlelem-IEC61850clPresentation`.\ :ref:`xmlattr-IEC61850clPresentationLogFlags`
|  :ref:`xmlelem-IEC61850clAssociation`.\ :ref:`xmlattr-IEC61850clAssociationLogFlags`
|  :ref:`xmlelem-IEC61850clMms`.\ :ref:`xmlattr-IEC61850clMmsLogFlags`

.. include:: IEC61850cl/ScsmSettings.rst
.. include:: IEC61850cl/AcsiSettings.rst
.. include:: IEC61850cl/AppSettings.rst

.. include-file:: sections/Include/ma_ServiceSettings.rstinc "" ".. _xmlelem-IEC61850clService:" ":ref:`xmlelem-IEC61850clService`" "tabid-IEC61850clService" "IEC61850 Client ServiceSettings attributes"
.. include-file:: sections/Include/EventMask.rstinc "" ":ref:`xmlattr-IEC61850clServiceEventMask`" "tabid-IEC61850clServiceEventMask" ":numref:`tabid-IEC61850clServiceEventMask`" ":ref:`xmlattr-IEC61850clCommOfflineDelay`" ":ref:`xmlattr-IEC61850clCommPostOfflineDelay`"

.. include:: IEC61850cl/Timeouts.rst

.. include:: IEC61850cl/Periodic.rst
