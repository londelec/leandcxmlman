.. _xmlelem-IEC101maMiscellaneous:

Miscellaneous
^^^^^^^^^^^^^

Miscellaneous and project-specific settings can be specified in this node.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-IEC101maMiscellaneous`"

.. code-block:: none

   <Miscellaneous TimeSyncIOA="0" DayOfWeek="1"/>


.. include-file:: sections/Include/table_attrs.rstinc "" "tabid-IEC101maMiscellaneous" "IEC60870-5-101 Master Miscellaneous attributes" ":spec: |C{0.14}|C{0.14}|C{0.1}|S{0.62}|"

   * :attr:	:xmlattr:`TimeSyncIOA`
     :val:	0...16777215
     :def:	0
     :desc:	Information Object Address [:lemonobgtext:`IOA`] of outgoing Time Synchronization command

   * :attr:	:xmlattr:`DayOfWeek`
     :val:	0
     :def:	1
     :desc:	Day Of Week (DOW) will have **0** value in outgoing Time Synchronization commands

   * :(attr):
     :val:	1
     :(def):
     :desc:	Day Of Week (DOW) will have **actual** value in outgoing Time Synchronization commands
