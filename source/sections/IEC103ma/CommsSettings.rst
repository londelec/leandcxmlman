.. _ref-IEC103maCommsSettings:

CommsSettings
^^^^^^^^^^^^^

Communication state (e.g. online and offline) change behavior and related delays can be specified in this node.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`<ref-IEC103maCommsSettings>`"

.. code-block:: none

   <CommsSettings NoRespCount="5" DegradedRetries="5" DegradedTimeout="600" ControlLockTimer="20" OfflineDelay="10" PostOfflineDelay="1000" OnlineGIDelay="10" />


.. _docref-IEC103maCommsSettingsAttab:

.. include-file:: sections/Include/table_attrs.rstinc "" "IEC60870-5-103 Master CommsSettings attributes" ":spec: |C{0.18}|C{0.1}|C{0.1}|S{0.62}|"

.. include-file:: sections/Include/serma_CommsSettings.rstinc "" ".. _ref-IEC103maCommsSettingsNoRespCount:" ".. _ref-IEC103maCommsSettingsDegradedRetries:" ".. _ref-IEC103maCommsSettingsDegradedTimeout:" ":ref:`<ref-IEC103maCommsSettingsOfflineDelay>`" ":ref:`<ref-IEC103maCommsSettingsDegradedTimeout>`" ":ref:`<ref-IEC103maCommsSettingsDegradedRetries>`"

.. include-file:: sections/Include/IEC10xma_ControlLockTimer.rstinc "" ".. _ref-IEC103maCommsSettingsControlLockTimer:"

.. include-file:: sections/Include/serma_OfflineDelay.rstinc "" ".. _ref-IEC103maCommsSettingsOfflineDelay:" ":ref:`<ref-IEC103maCommsSettingsNoRespCount>`"

.. include-file:: sections/Include/PostOfflineDelay.rstinc "" ".. _ref-IEC103maCommsSettingsPostOfflineDelay:" ":ref:`<ref-IEC103maCommsSettingsOfflineDelay>`"

.. include-file:: sections/Include/IEC10xma_OnlineGIDelay.rstinc "" ".. _ref-IEC103maCommsSettingsOnlineGIDelay:"
