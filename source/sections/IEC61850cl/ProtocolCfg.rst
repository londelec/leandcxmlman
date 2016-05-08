.. _ref-IEC61850clProtocolCfg:

ProtocolCfg group node
----------------------

.. include-file:: sections/Include/ProtocolCfg.rstinc "" "IEC61850 Client" ":ref:`ProtocolCfg<ref-IEC61850clProtocolCfg>`"

.. code-block:: none

 <ProtocolCfg>
	<CommsSettings … />
	<TransportSettings … />
	<SessionSettings … />
	<PresentationSettings … />
	<AssociationSettings … />
	<ScsmSettings … />
	<AppSettings … />
        <ServiceSettings … />
	<Timeouts … />
	<Periodic … />
 </ProtocolCfg>

.. tip:: All element nodes are optional, default values will be used for attributes of omitted nodes.

.. include:: IEC61850cl/CommsSettings.rst
.. include:: IEC61850cl/TransportSettings.rst
.. include:: IEC61850cl/SessionSettings.rst
.. include:: IEC61850cl/PresentationSettings.rst
.. include:: IEC61850cl/AssociationSettings.rst
.. include:: IEC61850cl/ScsmSettings.rst
.. include:: IEC61850cl/AppSettings.rst

.. include-file:: sections/Include/ma_ServiceSettings.rstinc "" ".. _ref-IEC61850clServiceSettings:" ":ref:`<ref-IEC61850clServiceSettings>`" ".. _docref-IEC61850clServiceSettingsAttab:" "IEC61850 Client ServiceSettings attributes"
.. include-file:: sections/Include/EventMask.rstinc "" ".. _docref-IEC61850clServiceEventMaskAttab:" ":numref:`docref-IEC61850clServiceEventMaskAttab`" ":ref:`<ref-IEC61850clCommsSettingsOfflineDelay>`" ":ref:`<ref-IEC61850clCommsSettingsPostOfflineDelay>`"

.. include:: IEC61850cl/Timeouts.rst

.. include:: IEC61850cl/Periodic.rst
