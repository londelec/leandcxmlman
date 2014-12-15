
Broadcast attributes
^^^^^^^^^^^^^^^^^^^^

Broadcast common address of ASDU (CAA) usage for various commands can be specified using attributes of 
:ref:`Broadcast<ref-IEC104maBroadcast>` element node.

Please see sample :ref:`Broadcast<ref-IEC104maBroadcast>` node and the table listing all available attributes below.

.. code-block:: none

   <Broadcast GI="1" />

.. _ref-IEC104maBroadcastAttributes:

.. field-list-table:: IEC 60807-5-104 Master Broadcast attributes
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.20}|C{0.25}|S{0.55}|
   :header-rows: 1

   * :attr,10:  Attribute
     :val,15:   Values or range
     :desc,75:  Description
     
   * :attr:     .. _ref-IEC104maBroadcastGI:
            
                :xmlref:`GI`
     :val:      0
     :desc:     Send General interrogation commands with **individual** common addresses of ASDU (CAA) (default value 0)

   * :(attr):
     :val:      1
     :desc:     Send General interrogation commands with **broadcast** common address of ASDU (CAA). Broadcast address is 65535
     