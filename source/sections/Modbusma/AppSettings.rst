.. _xmlelem-ModbusmaApp:

AppSettings
^^^^^^^^^^^

Application layer settings can be specified using attributes of :ref:`xmlelem-ModbusmaApp` element node.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-ModbusmaApp`"

.. code-block:: none

 <AppSettings AIDeadband="2" AIPercent="0.5" RatioP0="2"/>


.. include-file:: sections/Include/table_attrs.rstinc "" "tabid-ModbusmaApp" "Modbus Master AppSettings attributes" ":spec: |C{0.18}|C{0.14}|C{0.1}|S{0.58}|"

.. include-file:: sections/Include/AI_ThresholdsCmn.rstinc "" ":ref:`xmlelem-ModbusmaAI`" ":ref:`xmlattr-ModbusmaAIDeadband`" ":ref:`xmlattr-ModbusmaAIPercent`"

.. include-file:: sections/Include/serma_RatioP0.rstinc "" ":ref:`xmlattr-ModbusmaPollMsgPriority`"
