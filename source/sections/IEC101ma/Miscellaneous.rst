.. _ref-IEC101maMiscellaneous:

Miscellaneous
^^^^^^^^^^^^^

Miscellaneous and project-specific settings can be specified in this node.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`<ref-IEC101maMiscellaneous>`"

.. code-block:: none

   <Miscellaneous TimeSyncIOA="0" DayOfWeek="1"/>


.. _docref-IEC101maMiscellaneousAttab:

.. include-file:: sections/Include/table_attrs.rstinc "" "IEC60870-5-101 Master Miscellaneous attributes"

   * :attr:     :xmlref:`TimeSyncIOA`
     :val:      0...16777215
     :def:      0
     :desc:     Information Object Address (IOA) of outgoing Time Synchronization command

   * :attr:     :xmlref:`DayOfWeek`
     :val:      0
     :def:      1
     :desc:     Day Of Week (DOW) will have **0** value in outgoing Time Synchronization commands

   * :(attr):
     :val:      1
     :(def):
     :desc:     Day Of Week (DOW) will have **actual** value in outgoing Time Synchronization commands
