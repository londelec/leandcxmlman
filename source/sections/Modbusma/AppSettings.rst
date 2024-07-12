.. _xmlelem-ModbusmaApp:

AppSettings
^^^^^^^^^^^

Application layer settings can be specified using attributes of :ref:`xmlelem-ModbusmaApp` element node.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-ModbusmaApp`"

.. code-block:: none

 <AppSettings AIDeadband="2" AIPercent="0.5" RatioP0="2" ForwardGI="1" CmdRetries="0"/>


.. include-file:: sections/Include/table_attrs.rstinc "" "tabid-ModbusmaApp" "Modbus Master AppSettings attributes" ":spec: |C{0.18}|C{0.14}|C{0.1}|S{0.58}|"

.. include-file:: sections/Include/AI_ThresholdsCmn.rstinc "" ":ref:`xmlelem-ModbusmaAI`" ":ref:`xmlattr-ModbusmaAIDeadband`" ":ref:`xmlattr-ModbusmaAIPercent`"

.. include-file:: sections/Include/serma_RatioP0.rstinc "" ":ref:`xmlattr-ModbusmaPollMsgPriority`"

   * :attr:	:xmlattr:`ForwardGI`
     :val:	0
     :def:	1
     :desc:	**Ignore** General Interrogation command received from upstream station (e.g. SCADA)

   * :(attr):
     :val:	1
     :(def):
     :desc:	**Use** General Interrogation command received from upstream station (e.g. SCADA) to poll DI/AI values by sending all defined Poll Messages one after another without checking message priorities.

   * :attr:	:xmlattr:`CmdRetries`
     :val:	0..255
     :def:	0
     :desc:	Number of repeated attempts to send control command if Exception is received from outstation or response timeout occurs (outstation doesn't reply).
		Value 0 disables retries, command is considered failed and removed instantly if exception is received from outstation.
		However in case of a timeout, the command is repeated for the number of times specified in the :ref:`xmlattr-ModbusmaCommNoRespCount` attribute.

