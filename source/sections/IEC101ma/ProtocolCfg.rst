.. _ref-IEC101maProtocolCfg:

ProtocolCfg group node
----------------------

.. include-file:: sections/Include/ProtocolCfg.rstinc "" "IEC60870-5-101 controlling station (Master)" ":ref:`ProtocolCfg<ref-IEC101maProtocolCfg>`"

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

.. include-file:: sections/Include/IEC60870_XMLSettings.rstinc "" ".. _ref-IEC101maXMLSettings:" ":ref:`<ref-IEC101maXMLSettings>`" ".. _docref-IEC101maXMLSettingsAttab:" "IEC60870-5-101 Master XMLSettings attributes"

.. include:: IEC101ma/LinkSettings.rst
.. include:: IEC101ma/CommsSettings.rst
.. include:: IEC101ma/ASDUSettings.rst

.. include-file:: sections/Include/ma_ServiceSettings.rstinc "" ".. _ref-IEC101maServiceSettings:" ":ref:`<ref-IEC101maServiceSettings>`" ".. _docref-IEC101maServiceSettingsAttab:" "IEC60870-5-101 Master ServiceSettings attributes"
.. include-file:: sections/Include/EventMask.rstinc "" ".. _docref-IEC101maServiceEventMaskAttab:" ":numref:`docref-IEC101maServiceEventMaskAttab`" ":ref:`<ref-IEC101maCommsSettingsOfflineDelay>`" ":ref:`<ref-IEC101maCommsSettingsPostOfflineDelay>`"

.. include-file:: sections/Include/ma_Timeouts.rstinc "" ".. _ref-IEC101maTimeouts:" ":ref:`<ref-IEC101maTimeouts>`" ".. _docref-IEC101maTimeoutsAttab:" "IEC60870-5-101 Master Timeouts attributes"
.. include-file:: sections/Include/ma_TimeoutsAppCmd.rstinc
.. include-file:: sections/Include/SelectTimeout.rstinc

.. include-file:: sections/Include/IEC60870_TimeSettings.rstinc "" ".. _ref-IEC101maTimeSettings:" ":ref:`<ref-IEC101maTimeSettings>`" ".. _docref-IEC101maTimeSettingsAttab:" "IEC60870-5-101 Master TimeSettings attributes" ".. _ref-IEC101maTimeSettingsTimeZone:"

.. include:: IEC101ma/Broadcast.rst
.. include:: IEC101ma/Periodic.rst

.. include-file:: sections/Include/IEC10xma_BufferSizes.rstinc "internal" ".. _ref-IEC101maBufferSizes:" ":ref:`<ref-IEC101maBufferSizes>`" ".. _docref-IEC101maBufferSizesAttab:" "IEC60870-5-101 Master BufferSizes attributes"
.. include-file:: sections/Include/IEC60870_DOBufferSize.rstinc "internal"

.. include:: IEC101ma/Miscellaneous.rst
