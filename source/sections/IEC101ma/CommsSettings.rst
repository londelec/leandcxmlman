.. _ref-IEC101maCommsSettings:

CommsSettings
^^^^^^^^^^^^^

Communication state (e.g. online and offline) reporting and related delays can be specified using attributes of :ref:`<ref-IEC101maCommsSettings>` 
element node.

Please see sample :ref:`<ref-IEC101maCommsSettings>` node and the table listing all available attributes below.

.. code-block:: none

   <CommsSettings NoRespCount="5" DegradedRetries="5" DegradedTimeout="600" ControlLockTimer="20" OfflineDelay="10" PostOfflineDelay="1000" OnlineGIDelay="10" />


.. _docref-IEC101maCommsSettingsAttab:

.. include-file:: sections/Include/table_attrs.rstinc "" "IEC60870-5-101 Master CommsSettings attributes" ":spec: |C{0.18}|C{0.1}|C{0.1}|S{0.62}|"

.. include-file:: sections/Include/serma_CommsSettings.rstinc "" ".. _ref-IEC101maCommsSettingsNoRespCount:" ".. _ref-IEC101maCommsSettingsDegradedRetries:" ".. _ref-IEC101maCommsSettingsDegradedTimeout:" ":ref:`<ref-IEC101maCommsSettingsOfflineDelay>`" ":ref:`<ref-IEC101maCommsSettingsDegradedTimeout>`" ":ref:`<ref-IEC101maCommsSettingsDegradedRetries>`"

.. include-file:: sections/Include/IEC10xma_ControlLockTimer.rstinc "" ".. _ref-IEC101maCommsSettingsControlLockTimer:"

.. include-file:: sections/Include/serma_OfflineDelay.rstinc "" ".. _ref-IEC101maCommsSettingsOfflineDelay:" ":ref:`<ref-IEC101maCommsSettingsNoRespCount>`"

.. include-file:: sections/Include/PostOfflineDelay.rstinc "" ".. _ref-IEC101maCommsSettingsPostOfflineDelay:" ":ref:`<ref-IEC101maCommsSettingsOfflineDelay>`"

.. include-file:: sections/Include/IEC10xma_OnlineGIDelay.rstinc "" ".. _ref-IEC101maCommsSettingsOnlineGIDelay:"
