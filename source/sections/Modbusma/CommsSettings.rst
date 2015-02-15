.. _docref-ModbusmaCommsSettingsAttr:

CommsSettings attributes
^^^^^^^^^^^^^^^^^^^^^^^^

Communication state reporting and related delays can be specified using attributes of :ref:`CommsSettings<ref-ModbusmaCommsSettings>` 
element node.

Please see sample :ref:`CommsSettings<ref-ModbusmaCommsSettings>` node and the table listing all available attributes below.

.. code-block:: none

   <CommsSettings NoRespCount="5"
		  DegradedRetries="5"
		  DegradedTimeout="600"
		  OfflineDelay="10"
                  PostOfflineDelay="1000" />

.. _docref-ModbusmaCommsSettingsAttab:

.. field-list-table:: Modbus Master CommsSettings attributes
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.20}|C{0.25}|S{0.55}|
   :header-rows: 1

   * :attr,10: Attribute
     :val,15:  Values or range
     :desc,75: Description

.. include-file:: sections/Include/serma_CommsSettings.rstinc "" ".. _ref-ModbusmaCommsSettingsNoRespCount:" ".. _ref-ModbusmaCommsSettingsDegradedRetries:" ".. _ref-ModbusmaCommsSettingsDegradedTimeout:"

.. include-file:: sections/Include/serma_OfflineDelay.rstinc "" ".. _ref-ModbusmaCommsSettingsOfflineDelay:"

.. include-file:: sections/Include/PostOfflineDelay.rstinc "" ".. _ref-ModbusmaCommsSettingsPostOfflineDelay:" ":ref:`OfflineDelay<ref-ModbusmaCommsSettingsOfflineDelay>`"

