.. _ref-ModbusmaTimeouts:

Timeouts
^^^^^^^^

Timeout values can be specified in this node.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`<ref-ModbusmaTimeouts>`"

.. code-block:: none

   <Timeouts Application="30" Command="10" t35="0.01" />


.. _docref-ModbusmaTimeoutsAttab:

.. include-file:: sections/Include/table_attrs.rstinc "" "Modbus Master Timeouts attributes"

.. include-file:: sections/Include/ma_TimeoutsAppCmd.rstinc

   * :attr:     .. _ref-ModbusmaTimeoutst35:

                :xmlref:`t35`
     :val:      0.00001...42949
     :def:      0.01 sec
     :desc:     Receive line idle detection timer (:lectext1:`t3.5` in the communication standard).
		Incoming message analyze begins when idle in the receive line exceeds configured number of seconds.
