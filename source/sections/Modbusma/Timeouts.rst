.. _docref-ModbusmaTimeoutsAttr:

Timeouts attributes
^^^^^^^^^^^^^^^^^^^

Timeout values can be specified using attributes of :ref:`Timeouts<ref-ModbusmaTimeouts>` element node.

Please see sample :ref:`Timeouts<ref-ModbusmaTimeouts>` node and the table listing all available attributes below.

.. code-block:: none

   <Timeouts Application="30" Command="10" t35="0.01" />

.. _docref-ModbusmaTimeoutsAttab:

.. field-list-table:: Modbus Master Timeouts attributes
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.20}|C{0.25}|S{0.55}|
   :header-rows: 1

   * :attr,10:  Attribute
     :val,15:   Values or range
     :desc,75:  Description

.. include-file:: sections/Include/ma_TimeoutsAppCmd.rstinc

   * :attr:     .. _ref-ModbusmaTimeoutst35:
            
                :xmlref:`t35`
     :val:      0.00001...42949
     :desc:     Receive line idle detection timer (t3.5 in the communication standard). Incoming message analyze begins when idle in the receive line exceeds configured number of seconds (default 0.01 seconds)
