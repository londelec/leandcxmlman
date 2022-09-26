.. _xmlelem-ModbusmaTimeouts:

Timeouts
^^^^^^^^

Timeout values can be specified in this node.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-ModbusmaTimeouts`"

.. code-block:: none

   <Timeouts Application="30" Command="10" t35="0.01" />


.. include-file:: sections/Include/table_attrs.rstinc "" "tabid-ModbusmaTimeouts" "Modbus Master Timeouts attributes" ":spec: |C{0.12}|C{0.16}|C{0.1}|S{0.62}|"

.. include-file:: sections/Include/ma_TimeoutsAppCmd.rstinc ""

   * :attr:	:xmlattr:`t35`
     :val:	0.00001...42949
     :def:	0.01 sec
     :desc:	Receive line idle detection timer (:lemonobgtext:`t3.5` in the communication standard).
		Incoming message analyze begins when idle in the receive line exceeds configured number of seconds.
