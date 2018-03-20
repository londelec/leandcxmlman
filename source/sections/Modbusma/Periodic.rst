.. _ref-ModbusmaPeriodic:

Periodic
^^^^^^^^

Periodic intervals to send various messages are specified in this node.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`<ref-ModbusmaPeriodic>`"

.. code-block:: none

   <Periodic TimeSync="0" />

.. _docref-ModbusmaPeriodicAttab:

.. include-file:: sections/Include/table_attrs.rstinc "" "Modbus Master Periodic attributes"

.. include-file:: sections/Include/ma_PeriodicTimeSync.rstinc "" ":inlineimportant:`Time syncronization message must be defined in` :ref:`<ref-ModbusmaTimeSettings>` \ :inlineimportant:`node.` :inlinetip:`Time Synchronization commands are only sent at predefined intervals. This means station Online/Offline status change doesn't trigger time synchronziation command.`"
