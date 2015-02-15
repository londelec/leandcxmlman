.. _docref-IEC101maMiscellaneousAttr:

Miscellaneous attributes
^^^^^^^^^^^^^^^^^^^^^^^^

Miscellaneous and project-specific settings can be specified using attributes of :ref:`Miscellaneous<ref-IEC101maMiscellaneous>` element node.

Please see sample :ref:`Miscellaneous<ref-IEC101maMiscellaneous>` node and the table listing all available attributes below.

.. code-block:: none

   <Miscellaneous TimeSyncIOA="0" DayOfWeek="1"/>

.. _docref-IEC101maMiscellaneousAttab:

.. field-list-table:: IEC 60870-5-101 Master Miscellaneous attributes
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.20}|C{0.25}|S{0.55}|
   :header-rows: 1

   * :attr,10: Attribute
     :val,15:  Values or range
     :desc,75: Description
     
   * :attr:    :xmlref:`TimeSyncIOA`
     :val:     0...16777215
     :desc:    Information Object Address (IOA) of outgoing Time Synchronization command (default 0)

   * :attr:    :xmlref:`DayOfWeek`
     :val:     0
     :desc:    Day Of Week (DOW) will have **0** value in outgoing Time Synchronization commands

   * :(attr):
     :val:     1
     :desc:    Day Of Week (DOW) will have **actual** value in outgoing Time Synchronization commands (default value)
