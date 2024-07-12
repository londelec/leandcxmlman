.. _xmlgroup-IEC104slProtocolCfg: lelabel=ProtocolCfg

ProtocolCfg group
-----------------

.. include-file:: sections/Include/ProtocolCfg.rstinc "" "IEC60870-5-104 controlled station (Slave)" ":ref:`xmlgroup-IEC104slProtocolCfg`"

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

.. include-file:: sections/Include/IEC60870_XMLSettings.rstinc "" ".. _xmlelem-IEC104slXMLSettings:" ":ref:`xmlelem-IEC104slXMLSettings`" "tabid-IEC104slXMLSettings" "IEC60870-5-104 Slave XMLSettings attributes"

.. include:: IEC104sl/TransportSettings.rst
.. include:: IEC104sl/CommsSettings.rst
.. include:: IEC104sl/ASDUSettings.rst

.. include-file:: sections/Include/IEC10xsl_ServiceSettings.rstinc "" ".. _xmlelem-IEC104slService:" ":ref:`xmlelem-IEC104slService`" ":ref:`xmlattr-IEC104slServiceEventMask`" "tabid-IEC104slService" "IEC60870-5-104 Slave ServiceSettings attributes" ":numref:`tabid-IEC104slServiceQuality`"
.. include-file:: sections/Include/EventMask.rstinc "" ":ref:`xmlattr-IEC104slServiceEventMask`" "tabid-IEC104slServiceEventMask" ":numref:`tabid-IEC104slServiceEventMask`" ":ref:`xmlattr-IEC101maCommOfflineDelay`" ":ref:`xmlattr-IEC101maCommPostOfflineDelay`"
.. include-file:: sections/Include/IEC60870_QualityBits.rstinc "" "tabid-IEC104slServiceQuality"

.. include-file:: sections/Include/IEC10xsl_Timeouts.rstinc "" ".. _xmlelem-IEC104slTimeouts:" ":ref:`xmlelem-IEC104slTimeouts`" "tabid-IEC104slTimeouts" "IEC60870-5-104 Slave Timeouts attributes"
.. include-file:: sections/Include/SelectTimeout.rstinc
.. include-file:: sections/Include/CmdForwardTimeout.rstinc

.. include-file:: sections/Include/IEC60870_TimeSettings.rstinc "" ".. _xmlelem-IEC104slTimeSettings:" ":ref:`xmlelem-IEC104slTimeSettings`"
.. include-file:: sections/Include/TimeZone.rstinc "" "tabid-IEC104slTimeSettings" "IEC60870-5-104 Slave TimeSettings attributes"

.. include-file:: sections/Include/IEC10xsl_Periodic.rstinc "" ".. _xmlelem-IEC104slPeriodic:" ":ref:`xmlelem-IEC104slPeriodic`" "tabid-IEC104slPeriodic" "IEC60870-5-104 Slave Periodic attributes"

.. include:: IEC104sl/BufferSizes.rst
.. include:: IEC104sl/Miscellaneous.rst
