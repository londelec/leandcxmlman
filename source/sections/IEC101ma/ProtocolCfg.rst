.. _xmlgroup-IEC101maProtocolCfg: lelabel=ProtocolCfg

ProtocolCfg group
-----------------

.. include-file:: sections/Include/ProtocolCfg.rstinc "" "IEC60870-5-101 controlling station (Master)" ":ref:`xmlgroup-IEC101maProtocolCfg`"

.. code-block:: none

 <ProtocolCfg> 
   <XMLSettings … />
   <LinkSettings … />
   <CommsSettings … />
   <ASDUSettings … />
   <ServiceSettings … />
   <Timeouts … />
   <TimeSettings … />
   <Broadcast … />
   <Periodic … />
   <Miscellaneous … />
 </ProtocolCfg>

.. tip:: All element nodes are optional, default values will be used for attributes of omitted nodes.

.. include-file:: sections/Include/IEC60870_XMLSettings.rstinc "" ".. _xmlelem-IEC101maXMLSettings:" ":ref:`xmlelem-IEC101maXMLSettings`" "tabid-IEC101maXMLSettings" "IEC60870-5-101 Master XMLSettings attributes"

.. include:: IEC101ma/LinkSettings.rst
.. include:: IEC101ma/CommsSettings.rst
.. include:: IEC101ma/ASDUSettings.rst

.. include-file:: sections/Include/ma_ServiceSettings.rstinc "" ".. _xmlelem-IEC101maService:" ":ref:`xmlelem-IEC101maService`" "tabid-IEC101maService" "IEC60870-5-101 Master ServiceSettings attributes"
.. include-file:: sections/Include/EventMask.rstinc "" ":ref:`xmlattr-IEC101maServiceEventMask`" "tabid-IEC101maServiceEventMask" ":numref:`tabid-IEC101maServiceEventMask`" ":ref:`xmlattr-IEC101maCommOfflineDelay`" ":ref:`xmlattr-IEC101maCommPostOfflineDelay`"

.. include-file:: sections/Include/IEC10xma_Timeouts.rstinc "" ".. _xmlelem-IEC101maTimeouts:" ":ref:`xmlelem-IEC101maTimeouts`" "tabid-IEC101maTimeouts" "IEC60870-5-101 Master Timeouts attributes"
.. include-file:: sections/Include/ma_TimeoutsAppCmd.rstinc ""
.. include-file:: sections/Include/SelectTimeout.rstinc ""

.. include-file:: sections/Include/IEC60870_TimeSettings.rstinc "" ".. _xmlelem-IEC101maTimeSettings:" ":ref:`xmlelem-IEC101maTimeSettings`"
.. include-file:: sections/Include/TimeZone.rstinc "" "tabid-IEC101maTimeSettings" "IEC60870-5-101 Master TimeSettings attributes"

.. include:: IEC101ma/Broadcast.rst
.. include:: IEC101ma/Periodic.rst

.. include-file:: sections/Include/IEC10xma_BufferSizes.rstinc "internal" ".. _xmlelem-IEC101maBufferSizes:" ":ref:`xmlelem-IEC101maBufferSizes`" "tabid-IEC101maBufferSizes" "IEC60870-5-101 Master BufferSizes attributes"
.. include-file:: sections/Include/IEC60870_DOBufferSize.rstinc "internal"

.. include:: IEC101ma/Miscellaneous.rst
