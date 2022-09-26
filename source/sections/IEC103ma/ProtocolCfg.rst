.. _xmlgroup-IEC103maProtocolCfg: lelabel=ProtocolCfg

ProtocolCfg group
-----------------

.. include-file:: sections/Include/ProtocolCfg.rstinc "" "IEC60870-5-103 controlling station (Master)" ":ref:`xmlgroup-IEC103maProtocolCfg`"

.. code-block:: none

 <ProtocolCfg>
   <LinkSettings … />
   <CommsSettings … />
   <ASDUSettings … />
   <ServiceSettings … />
   <Timeouts … />
   <TimeSettings … />
   <Broadcast … />
   <Periodic … />
 </ProtocolCfg>

.. tip:: All element nodes are optional, default values will be used for attributes of omitted nodes.

.. include:: IEC103ma/LinkSettings.rst
.. include:: IEC103ma/CommsSettings.rst
.. include:: IEC103ma/ASDUSettings.rst

.. include-file:: sections/Include/ma_ServiceSettings.rstinc "" ".. _xmlelem-IEC103maService:" ":ref:`xmlelem-IEC103maService`" "tabid-IEC103maService" "IEC60870-5-103 Master ServiceSettings attributes"
.. include-file:: sections/Include/EventMask.rstinc "" ":ref:`xmlattr-IEC103maServiceEventMask`" "tabid-IEC103maServiceEventMask" ":numref:`tabid-IEC103maServiceEventMask`" ":ref:`xmlattr-IEC103maCommOfflineDelay`" ":ref:`xmlattr-IEC103maCommPostOfflineDelay`"

.. include-file:: sections/Include/serma_Timeouts.rstinc "" ".. _xmlelem-IEC103maTimeouts:" ":ref:`xmlelem-IEC103maTimeouts`" "tabid-IEC103maTimeouts" "IEC60870-5-103 Master Timeouts attributes"
.. include-file:: sections/Include/ma_TimeoutsAppCmd.rstinc ""

.. include-file:: sections/Include/IEC60870_TimeSettings.rstinc "" ".. _xmlelem-IEC103maTimeSettings:" ":ref:`xmlelem-IEC103maTimeSettings`"
.. include-file:: sections/Include/TimeZone.rstinc "" "tabid-IEC103maTimeSettings" "IEC60870-5-103 Master TimeSettings attributes"

.. include:: IEC103ma/Broadcast.rst
.. include:: IEC103ma/Periodic.rst
