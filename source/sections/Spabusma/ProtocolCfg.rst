.. _xmlgroup-SpabusmaProtocolCfg: lelabel=ProtocolCfg

ProtocolCfg group
-----------------

.. include-file:: sections/Include/ProtocolCfg.rstinc "" "Spabus Master" ":ref:`xmlgroup-SpabusmaProtocolCfg`"

.. code-block:: none

 <ProtocolCfg>
   <LinkSettings … />
   <CommsSettings … />
   <AppSettings … />
   <ServiceSettings … />
   <Timeouts … />
   <TimeSettings … />
   <Periodic … />
 </ProtocolCfg>

.. tip:: All elements are optional, default values will be used for attributes of omitted nodes.

.. include:: Spabusma/LinkSettings.rst
.. include:: Spabusma/CommsSettings.rst
.. include:: Spabusma/AppSettings.rst

.. include-file:: sections/Include/ma_ServiceSettings.rstinc "" ".. _xmlelem-SpabusmaService:" ":ref:`xmlelem-SpabusmaService`" "tabid-SpabusmaService" "Spabus Master ServiceSettings attributes"
.. include-file:: sections/Include/EventMask.rstinc "" ":ref:`xmlattr-SpabusmaServiceEventMask`" "tabid-SpabusmaServiceEventMask" ":numref:`tabid-SpabusmaServiceEventMask`" ":ref:`xmlattr-SpabusmaCommOfflineDelay`" ":ref:`xmlattr-SpabusmaCommPostOfflineDelay`"

.. include-file:: sections/Include/serma_Timeouts.rstinc "" ".. _xmlelem-SpabusmaTimeouts:" ":ref:`xmlelem-SpabusmaTimeouts`" "tabid-SpabusmaTimeouts" "Spabus Master Timeouts attributes"
.. include-file:: sections/Include/ma_TimeoutsAppCmd.rstinc ""

.. include:: Spabusma/TimeSettings.rst
.. include:: Spabusma/Periodic.rst
