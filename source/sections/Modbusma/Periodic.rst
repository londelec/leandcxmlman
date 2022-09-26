.. _xmlelem-ModbusmaPeriodic:

Periodic
^^^^^^^^

Periodic intervals to send various messages are specified in this node.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-ModbusmaPeriodic`"

.. code-block:: none

   <Periodic TimeSync="0" />


.. include-file:: sections/Include/table_attrs.rstinc "" "tabid-ModbusmaPeriodic" "Modbus Master Periodic attributes" ":spec: |C{0.12}|C{0.1}|C{0.1}|S{0.68}|"

.. include-file:: sections/Include/ma_PeriodicTimeSync.rstinc "" ":inlineimportant:`Time synchronization message must be defined in` :ref:`xmlelem-ModbusmaTime` \ :inlineimportant:`node.` :inlinetip:`Time Synchronization commands are only sent at predefined intervals. This means station Online/Offline status change doesn't trigger time synchronization command.`"
