.. _xmlelem-ModbusmaLink:

LinkSettings
^^^^^^^^^^^^

Link layer settings can be specified using attributes of :ref:`xmlelem-ModbusmaLink` element node.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-ModbusmaLink`"

.. code-block:: none

   <LinkSettings Frame="RTU" />


.. include-file:: sections/Include/table_attrs.rstinc "" "tabid-ModbusmaLink" "Modbus Master LinkSettings attributes" ":spec: |C{0.12}|C{0.12}|C{0.1}|S{0.66}|"

   * :attr:	:xmlattr:`Frame`
     :val:	RTU or TCP
     :def:	RTU
     :desc:	Frame format of the Modbus messages.
		:inlinetip:`Please note frame format of all protocol instances sharing the hardware node must be the same.`
		:ref:`xmlelem-uart`\ ; :ref:`xmlelem-udp`
		:inlinetip:`and`
		:ref:`xmlelem-tcpclient`
		:inlinetip:`hardware nodes can be used for Modbus® RTU frame format. Only`
		:ref:`xmlelem-tcpclient`
		:inlinetip:`hardware node can be used for Modbus® TCP frame format.`
