.. _xmlelem-SpabusmaPeriodic:

Periodic
^^^^^^^^

Periodic intervals to send various messages are specified in this node.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-SpabusmaPeriodic`"

.. code-block:: none

   <Periodic TimeSync="0" PreciseSync="0" DIPoll="120"/>


.. include-file:: sections/Include/table_attrs.rstinc "" "tabid-SpabusmaPeriodic" "Spabus Master Periodic attributes" ":spec: |C{0.12}|C{0.1}|C{0.1}|S{0.68}|"

.. include-file:: sections/Include/ma_PeriodicTimeSync.rstinc "" "This attribute enables Date :lemonobgtext:`WD` synchronization message. :inlinetip:`Time Synchronization commands are only sent at predefined intervals. This means station Online/Offline status change doesn't trigger time synchronization command.`"

   * :attr:	:xmlattr:`PreciseSync`
     :val:	|uint32range|
     :def:	0 sec
     :desc:	Precise Time synchronization command interval in seconds.
		Value 0 disables periodic precise time synchronization command.
		This attribute enables Time :lemonobgtext:`WT` synchronization message.
		:inlinetip:`Time Synchronization commands are only sent at predefined intervals. This means station Online/Offline status change doesn't trigger time synchronization command.`

   * :attr:	:xmlattr:`DIPoll`
     :val:	|uint32range|
     :def:	0 sec
     :desc:	Periodic polling of DI values in seconds.
		This setting only applies if DI values are excluded from continuous polling (are requested only during IED initialization) with :ref:`bitref-SpabusmaAppFlagsBit0`\ |bittrue| in :ref:`xmlelem-SpabusmaApp`.\ :ref:`xmlattr-SpabusmaAppFlags`.

