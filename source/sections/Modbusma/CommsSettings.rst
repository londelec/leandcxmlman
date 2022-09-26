.. _xmlelem-ModbusmaComm:

CommsSettings
^^^^^^^^^^^^^

Communication state (e.g. online and offline) change behavior and related delays can be specified in this node.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-ModbusmaComm`"

.. code-block:: none

   <CommsSettings NoRespCount="5" DegradedRetries="5" DegradedTimeout="600" OfflineDelay="10" PostOfflineDelay="1000" />


.. include-file:: sections/Include/table_attrs.rstinc "" "tabid-ModbusmaComm" "Modbus Master CommsSettings attributes" ":spec: |C{0.18}|C{0.1}|C{0.1}|S{0.62}|"

.. include-file:: sections/Include/serma_CommsSettings.rstinc "" ":ref:`xmlattr-ModbusmaCommOfflineDelay`" ":ref:`xmlattr-ModbusmaCommDegradedTimeout`" ":ref:`xmlattr-ModbusmaCommDegradedRetries`" "300 sec"

.. include-file:: sections/Include/serma_OfflineDelay.rstinc "" ":ref:`xmlattr-ModbusmaCommNoRespCount`"

.. include-file:: sections/Include/PostOfflineDelay.rstinc "" ":ref:`xmlattr-ModbusmaCommOfflineDelay`"
