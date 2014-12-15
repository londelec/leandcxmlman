
Periodic attributes
^^^^^^^^^^^^^^^^^^^

Periodic intervals of sending various messages can be specified using attributes of :ref:`Periodic<ref-IEC103maPeriodic>` element node.

Please see sample :ref:`Periodic<ref-IEC103maPeriodic>` node and the table listing all available attributes below.

.. code-block:: none

   <Periodic GI="600" TimeSync="0" />

.. _ref-IEC103maPeriodicAttributes:

.. field-list-table:: IEC 60807-5-103 Master Periodic attributes
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.20}|C{0.25}|S{0.55}|
   :header-rows: 1

   * :attr,10: Attribute
     :val,15:  Values or range
     :desc,75: Description
     
   * :attr:    :xmlref:`GI`
     :val:     0...2\ :sup:`32`\  - 1
     :desc:    Periodic General Interrogation command interval in seconds. Value 0 disables periodic General Interrogation command. (default value 0)

   * :attr:    :xmlref:`TimeSync`
     :val:     0...2\ :sup:`32`\  - 1
     :desc:    Periodic Time synchronization command interval in seconds. Value 0 disables time synchronization command. (default value 0)
     