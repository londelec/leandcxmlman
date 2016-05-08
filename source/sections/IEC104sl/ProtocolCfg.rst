
.. _ref-IEC104slProtocolCfg:

ProtocolCfg group node
----------------------

.. include-file:: sections/Include/ProtocolCfg.rstinc "" "IEC60870-5-104 controlled station (Slave)" ":ref:`ProtocolCfg<ref-IEC104slProtocolCfg>`"

.. code-block:: none

   <ProtocolCfg>
      <XMLSettings … />
      <TransportSettings … />
      <CommsSettings … />
      <ASDUSettings … />
      <ServiceSettings … />
      <Timeouts … />
      <TimeSettings … />
      <Periodic … />
      <BufferSizes … />
      <Miscellaneous … />
   </ProtocolCfg>

.. tip:: All element nodes are optional, default values will be used for attributes of omitted nodes.

.. include-file:: sections/Include/IEC60870_XMLSettings.rstinc "" ".. _ref-IEC104slXMLSettings:" ":ref:`<ref-IEC104slXMLSettings>`" ".. _docref-IEC104slXMLSettingsAttab:" "IEC60870-5-104 Slave XMLSettings attributes"

.. include:: IEC104sl/TransportSettings.rst
.. include:: IEC104sl/CommsSettings.rst
.. include:: IEC104sl/ASDUSettings.rst

.. include-file:: sections/Include/IEC10xsl_ServiceSettings.rstinc "" ".. _ref-IEC104slServiceSettings:" ":ref:`<ref-IEC104slServiceSettings>`" ".. _docref-IEC104slServiceSettingsAttab:" "IEC60870-5-104 Slave ServiceSettings attributes" ":numref:`docref-IEC104slServiceQualityBitsAttab`"
.. include-file:: sections/Include/EventMask.rstinc "" ".. _docref-IEC104slServiceEventMaskAttab:" ":numref:`docref-IEC104slServiceEventMaskAttab`" ":ref:`<ref-IEC101maCommsSettingsOfflineDelay>`" ":ref:`<ref-IEC101maCommsSettingsPostOfflineDelay>`"
.. include-file:: sections/Include/IEC60870_QualityBits.rstinc "" ".. _docref-IEC104slServiceQualityBitsAttab:"

.. include-file:: sections/Include/IEC10xsl_Timeouts.rstinc "" ".. _ref-IEC104slTimeouts:" ":ref:`<ref-IEC104slTimeouts>`" ".. _docref-IEC104slTimeoutsAttab:" "IEC60870-5-104 Slave Timeouts attributes"
.. include-file:: sections/Include/SelectTimeout.rstinc

.. include-file:: sections/Include/IEC60870_TimeSettings.rstinc "" ".. _ref-IEC104slTimeSettings:" ":ref:`<ref-IEC104slTimeSettings>`" ".. _docref-IEC104slTimeSettingsAttab:" "IEC60870-5-104 Slave TimeSettings attributes" ".. _ref-IEC104slTimeSettingsTimeZone:"
.. include-file:: sections/Include/IEC10xsl_Periodic.rstinc "" ".. _ref-IEC104slPeriodic:" ":ref:`<ref-IEC104slPeriodic>`" ".. _docref-IEC104slPeriodicAttab:" "IEC60870-5-104 Slave Periodic attributes"

.. include:: IEC104sl/BufferSizes.rst
.. include:: IEC104sl/Miscellaneous.rst
