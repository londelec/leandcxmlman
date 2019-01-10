.. _ref-ModbusmaCommsSettings:

CommsSettings
^^^^^^^^^^^^^

Communication state (e.g. online and offline) change behavior and related delays can be specified in this node.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`<ref-ModbusmaCommsSettings>`"

.. code-block:: none

   <CommsSettings NoRespCount="5" DegradedRetries="5" DegradedTimeout="600" OfflineDelay="10" PostOfflineDelay="1000" />


.. _docref-ModbusmaCommsSettingsAttab:

.. include-file:: sections/Include/table_attrs.rstinc "" "Modbus Master CommsSettings attributes" ":spec: |C{0.18}|C{0.1}|C{0.1}|S{0.62}|"

.. include-file:: sections/Include/serma_CommsSettings.rstinc "" ".. _ref-ModbusmaCommsSettingsNoRespCount:" ".. _ref-ModbusmaCommsSettingsDegradedRetries:" ".. _ref-ModbusmaCommsSettingsDegradedTimeout:" ":ref:`<ref-ModbusmaCommsSettingsOfflineDelay>`" ":ref:`<ref-ModbusmaCommsSettingsDegradedTimeout>`" ":ref:`<ref-ModbusmaCommsSettingsDegradedRetries>`"

.. include-file:: sections/Include/serma_OfflineDelay.rstinc "" ".. _ref-ModbusmaCommsSettingsOfflineDelay:" ":ref:`<ref-ModbusmaCommsSettingsNoRespCount>`"

.. include-file:: sections/Include/PostOfflineDelay.rstinc "" ".. _ref-ModbusmaCommsSettingsPostOfflineDelay:" ":ref:`OfflineDelay<ref-ModbusmaCommsSettingsOfflineDelay>`"
