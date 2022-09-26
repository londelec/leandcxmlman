.. _xmlgroup-IEC101slProtocolCfg: lelabel=ProtocolCfg

ProtocolCfg group
-----------------

.. include-file:: sections/Include/ProtocolCfg.rstinc "" "IEC60870-5-101 controlled station (Slave)" ":ref:`xmlgroup-IEC101slProtocolCfg`"

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

.. include-file:: sections/Include/IEC60870_XMLSettings.rstinc "" ".. _xmlelem-IEC101slXMLSettings:" ":ref:`xmlelem-IEC101slXMLSettings`" "tabid-IEC101slXMLSettings" "IEC60870-5-101 Slave XMLSettings attributes"

.. include:: IEC101sl/LinkSettings.rst
.. include:: IEC101sl/CommsSettings.rst
.. include:: IEC101sl/ASDUSettings.rst

.. include-file:: sections/Include/IEC10xsl_ServiceSettings.rstinc "" ".. _xmlelem-IEC101slService:" ":ref:`xmlelem-IEC101slService`" ":ref:`xmlattr-IEC101slServiceEventMask`" "tabid-IEC101slService" "IEC60870-5-101 Slave ServiceSettings attributes" ":numref:`tabid-IEC101slServiceQuality`"
.. include-file:: sections/Include/EventMask.rstinc "" ":ref:`xmlattr-IEC101slServiceEventMask`" "tabid-IEC101slServiceEventMask" ":numref:`tabid-IEC101slServiceEventMask`" ":ref:`xmlattr-IEC101maCommOfflineDelay`" ":ref:`xmlattr-IEC101maCommPostOfflineDelay`"
.. include-file:: sections/Include/IEC60870_QualityBits.rstinc "" "tabid-IEC101slServiceQuality"

.. include-file:: sections/Include/IEC10xsl_Timeouts.rstinc "" ".. _xmlelem-IEC101slTimeouts:" ":ref:`xmlelem-IEC101slTimeouts`" "tabid-IEC101slTimeouts" "IEC60870-5-101 Slave Timeouts attributes"
.. include-file:: sections/Include/SelectTimeout.rstinc

.. include-file:: sections/Include/IEC60870_TimeSettings.rstinc "" ".. _xmlelem-IEC101slTimeSettings:" ":ref:`xmlelem-IEC101slTimeSettings`"
.. include-file:: sections/Include/TimeZone.rstinc "" "tabid-IEC101slTimeSettings" "IEC60870-5-101 Slave TimeSettings attributes"

.. include-file:: sections/Include/IEC10xsl_Periodic.rstinc "" ".. _xmlelem-IEC101slPeriodic:" ":ref:`xmlelem-IEC101slPeriodic`" "tabid-IEC101slPeriodic" "IEC60870-5-101 Slave Periodic attributes"

.. include:: IEC101sl/BufferSizes.rst
