.. _ref-IEC104maProtocolCfg:

ProtocolCfg group node
----------------------

.. include-file:: sections/Include/ProtocolCfg.rstinc "" "IEC60870-5-104 controlling station (Master)" ":ref:`ProtocolCfg<ref-IEC104maProtocolCfg>`"

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

.. include-file:: sections/Include/IEC60870_XMLSettings.rstinc "" ".. _ref-IEC104maXMLSettings:" ":ref:`<ref-IEC104maXMLSettings>`" ".. _docref-IEC104maXMLSettingsAttab:" "IEC60870-5-104 Master XMLSettings attributes"

.. include:: IEC104ma/TransportSettings.rst
.. include:: IEC104ma/CommsSettings.rst
.. include:: IEC104ma/ASDUSettings.rst

.. include-file:: sections/Include/ma_ServiceSettings.rstinc "" ".. _ref-IEC104maServiceSettings:" ":ref:`<ref-IEC104maServiceSettings>`" ".. _docref-IEC104maServiceSettingsAttab:" "IEC60870-5-104 Master ServiceSettings attributes"
.. include-file:: sections/Include/EventMask.rstinc "" ".. _docref-IEC104maServiceEventMaskAttab:" ":numref:`docref-IEC104maServiceEventMaskAttab`" ":ref:`<ref-IEC104maCommsSettingsOfflineDelay>`" ":ref:`<ref-IEC104maCommsSettingsPostOfflineDelay>`"

.. include-file:: sections/Include/ma_Timeouts.rstinc "" ".. _ref-IEC104maTimeouts:" ":ref:`<ref-IEC104maTimeouts>`" ".. _docref-IEC104maTimeoutsAttab:" "IEC60870-5-104 Master Timeouts attributes"
.. include-file:: sections/Include/ma_TimeoutsAppCmd.rstinc
.. include-file:: sections/Include/SelectTimeout.rstinc

.. include-file:: sections/Include/IEC60870_TimeSettings.rstinc "" ".. _ref-IEC104maTimeSettings:" ":ref:`<ref-IEC104maTimeSettings>`" ".. _docref-IEC104maTimeSettingsAttab:" "IEC60870-5-104 Master TimeSettings attributes" ".. _ref-IEC104maTimeSettingsTimeZone:"

.. include:: IEC104ma/Broadcast.rst
.. include:: IEC104ma/Periodic.rst

.. include-file:: sections/Include/IEC10xma_BufferSizes.rstinc "internal" ".. _ref-IEC104maBufferSizes:" ":ref:`<ref-IEC104maBufferSizes>`" ".. _docref-IEC104maBufferSizesAttab:" "IEC60870-5-104 Master BufferSizes attributes"
.. include-file:: sections/Include/IEC60870_DOBufferSize.rstinc "internal"
