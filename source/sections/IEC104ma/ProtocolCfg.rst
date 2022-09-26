.. _xmlgroup-IEC104maProtocolCfg: lelabel=ProtocolCfg

ProtocolCfg group
-----------------

.. include-file:: sections/Include/ProtocolCfg.rstinc "" "IEC60870-5-104 controlling station (Master)" ":ref:`xmlgroup-IEC104maProtocolCfg`"

.. code-block:: none

 <ProtocolCfg> 
   <XMLSettings … />
   <TransportSettings … />
   <CommsSettings … />
   <ASDUSettings … />
   <ServiceSettings … />
   <Timeouts … />
   <TimeSettings … />
   <Broadcast … />
   <Periodic … />
 </ProtocolCfg>

.. tip:: All element nodes are optional, default values will be used for attributes of omitted nodes.

.. include-file:: sections/Include/IEC60870_XMLSettings.rstinc "" ".. _xmlelem-IEC104maXMLSettings:" ":ref:`xmlelem-IEC104maXMLSettings`" "tabid-IEC104maXMLSettings" "IEC60870-5-104 Master XMLSettings attributes"

.. include:: IEC104ma/TransportSettings.rst
.. include:: IEC104ma/CommsSettings.rst
.. include:: IEC104ma/ASDUSettings.rst

.. include-file:: sections/Include/ma_ServiceSettings.rstinc "" ".. _xmlelem-IEC104maService:" ":ref:`xmlelem-IEC104maService`" "tabid-IEC104maService" "IEC60870-5-104 Master ServiceSettings attributes"
.. include-file:: sections/Include/EventMask.rstinc "" ":ref:`xmlattr-IEC104maServiceEventMask`" "tabid-IEC104maServiceEventMask" ":numref:`tabid-IEC104maServiceEventMask`" ":ref:`xmlattr-IEC104maCommOfflineDelay`" ":ref:`xmlattr-IEC104maCommPostOfflineDelay`"

.. include-file:: sections/Include/IEC10xma_Timeouts.rstinc "" ".. _xmlelem-IEC104maTimeouts:" ":ref:`xmlelem-IEC104maTimeouts`" "tabid-IEC104maTimeouts" "IEC60870-5-104 Master Timeouts attributes"
.. include-file:: sections/Include/ma_TimeoutsAppCmd.rstinc ""
.. include-file:: sections/Include/SelectTimeout.rstinc ""

.. include-file:: sections/Include/IEC60870_TimeSettings.rstinc "" ".. _xmlelem-IEC104maTimeSettings:" ":ref:`xmlelem-IEC104maTimeSettings`"
.. include-file:: sections/Include/TimeZone.rstinc "" "tabid-IEC104maTimeSettings" "IEC60870-5-104 Master TimeSettings attributes"

.. include:: IEC104ma/Broadcast.rst
.. include:: IEC104ma/Periodic.rst

.. include-file:: sections/Include/IEC10xma_BufferSizes.rstinc "internal" ".. _xmlelem-IEC104maBufferSizes:" ":ref:`xmlelem-IEC104maBufferSizes`" "tabid-IEC104maBufferSizes" "IEC60870-5-104 Master BufferSizes attributes"
.. include-file:: sections/Include/IEC60870_DOBufferSize.rstinc "internal"
