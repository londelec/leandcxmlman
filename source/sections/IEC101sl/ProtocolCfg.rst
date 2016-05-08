.. _ref-IEC101slProtocolCfg:

ProtocolCfg group node
----------------------

.. include-file:: sections/Include/ProtocolCfg.rstinc "" "IEC60870-5-101 controlled station (Slave)" ":ref:`ProtocolCfg<ref-IEC101slProtocolCfg>`"

.. code-block:: none

   <ProtocolCfg>
      <XMLSettings … />
      <LinkSettings … />
      <CommsSettings … />
      <ASDUSettings … />
      <ServiceSettings … />
      <Timeouts … />
      <TimeSettings … />
      <Periodic … />
      <BufferSizes … />
   </ProtocolCfg>

.. tip:: All element nodes are optional, default values will be used for attributes of omitted nodes.

.. include-file:: sections/Include/IEC60870_XMLSettings.rstinc "" ".. _ref-IEC101slXMLSettings:" ":ref:`<ref-IEC101slXMLSettings>`" ".. _docref-IEC101slXMLSettingsAttab:" "IEC60870-5-101 Slave XMLSettings attributes"

.. include:: IEC101sl/LinkSettings.rst
.. include:: IEC101sl/CommsSettings.rst
.. include:: IEC101sl/ASDUSettings.rst

.. include-file:: sections/Include/IEC10xsl_ServiceSettings.rstinc "" ".. _ref-IEC101slServiceSettings:" ":ref:`<ref-IEC101slServiceSettings>`" ".. _docref-IEC101slServiceSettingsAttab:" "IEC60870-5-101 Slave ServiceSettings attributes" ":numref:`docref-IEC101slServiceQualityBitsAttab`"
.. include-file:: sections/Include/EventMask.rstinc "" ".. _docref-IEC101slServiceEventMaskAttab:" ":numref:`docref-IEC101slServiceEventMaskAttab`" ":ref:`<ref-IEC101maCommsSettingsOfflineDelay>`" ":ref:`<ref-IEC101maCommsSettingsPostOfflineDelay>`"
.. include-file:: sections/Include/IEC60870_QualityBits.rstinc "" ".. _docref-IEC101slServiceQualityBitsAttab:"

.. include-file:: sections/Include/IEC10xsl_Timeouts.rstinc "" ".. _ref-IEC101slTimeouts:" ":ref:`<ref-IEC101slTimeouts>`" ".. _docref-IEC101slTimeoutsAttab:" "IEC60870-5-101 Slave Timeouts attributes"
.. include-file:: sections/Include/SelectTimeout.rstinc

.. include-file:: sections/Include/IEC60870_TimeSettings.rstinc "" ".. _ref-IEC101slTimeSettings:" ":ref:`<ref-IEC101slTimeSettings>`" ".. _docref-IEC101slTimeSettingsAttab:" "IEC60870-5-101 Slave TimeSettings attributes" ".. _ref-IEC101slTimeSettingsTimeZone:"
.. include-file:: sections/Include/IEC10xsl_Periodic.rstinc "" ".. _ref-IEC101slPeriodic:" ":ref:`<ref-IEC101slPeriodic>`" ".. _docref-IEC101slPeriodicAttab:" "IEC60870-5-101 Slave Periodic attributes"

.. include:: IEC101sl/BufferSizes.rst
