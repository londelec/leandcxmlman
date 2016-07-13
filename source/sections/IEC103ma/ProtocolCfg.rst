.. _ref-IEC103maProtocolCfg:

ProtocolCfg group node
----------------------

.. include-file:: sections/Include/ProtocolCfg.rstinc "" "IEC60870-5-103 controlling station (Master)" ":ref:`ProtocolCfg<ref-IEC103maProtocolCfg>`"

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

.. include-file:: sections/Include/ma_ServiceSettings.rstinc "" ".. _ref-IEC103maServiceSettings:" ":ref:`<ref-IEC103maServiceSettings>`" ".. _docref-IEC103maServiceSettingsAttab:" "IEC60870-5-103 Master ServiceSettings attributes"
.. include-file:: sections/Include/EventMask.rstinc "" ".. _docref-IEC103maServiceEventMaskAttab:" ":numref:`docref-IEC103maServiceEventMaskAttab`" ":ref:`<ref-IEC103maCommsSettingsOfflineDelay>`" ":ref:`<ref-IEC103maCommsSettingsPostOfflineDelay>`"

.. include:: IEC103ma/Timeouts.rst
.. include-file:: sections/Include/IEC60870_TimeSettings.rstinc "" ".. _ref-IEC103maTimeSettings:" ":ref:`<ref-IEC103maTimeSettings>`" ".. _docref-IEC103maTimeSettingsAttab:" "IEC60870-5-103 Master TimeSettings attributes" ".. _ref-IEC103maTimeSettingsTimeZone:"

.. include:: IEC103ma/Broadcast.rst
.. include:: IEC103ma/Periodic.rst
