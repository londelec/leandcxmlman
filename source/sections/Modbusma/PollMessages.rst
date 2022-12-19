
.. _xmlgroup-ModbusmaPollMessages: lelabel=PollMessages
.. _xmlelem-ModbusmaPollMsg: lelabel=MSG

PollMessages group
------------------

Group node :ref:`xmlgroup-ModbusmaPollMessages` and child element nodes :ref:`xmlelem-ModbusmaPollMsg` contain messages that are being sent to continuously poll outstation data.
All defined messages are sent to outstation in a sequential order.
Data received from outstation can be mapped using :ref:`xmlelem-ModbusmaDI` and :ref:`xmlelem-ModbusmaAI` nodes.

.. tip:: \ :ref:`xmlgroup-ModbusmaPollMessages` group and :ref:`xmlelem-ModbusmaPollMsg` nodes are optional if :ref:`xmlelem-ModbusmaHardcoded`.\ :ref:`xmlattr-ModbusmaHardcodedType` is used. Messages required to poll data from a hardcoded device are set-up automatically.

Please see sample :ref:`xmlgroup-ModbusmaPollMessages` group and :ref:`xmlelem-ModbusmaPollMsg` child element nodes below.
There are 2 Modbus messages configured using 2 :ref:`xmlelem-ModbusmaPollMsg` element nodes.

.. code-block:: none

   <PollMessages>
	<MSG PollMsg="1" Func="3" Reg="0x0055" Count="2" />
	<MSG PollMsg="2" Func="4" Reg="0x0003" Count="1" />
   </PollMessages>

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-ModbusmaPollMsg`"

.. code-block:: none

   <MSG PollMsg="1" Func="4" Reg="0x0100" Count="1" Priority="0" Name="Read Input Registers message" />

.. tip:: Attributes of the :ref:`xmlelem-ModbusmaPollMsg` element node can be arranged in any order, it will not affect XML file validation.

Poll MSG attributes
^^^^^^^^^^^^^^^^^^^

.. include-file:: sections/Include/table_attrs.rstinc "" "tabid-ModbusmaPollMsg" "Modbus Master Poll message attributes" ":spec: |C{0.1}|C{0.16}|C{0.1}|S{0.64}|"

.. include-file:: sections/Include/serma_Msgid.rstinc "" ":xmlattr:`PollMsg`"

.. include-file:: sections/Include/Modbusma_Func.rstinc "" "See :numref:`tabid-ModbusmaPollMsgFunc`"

.. include-file:: sections/Include/Modbusma_Reg.rstinc "" "Data will be read from this register."

.. include-file:: sections/Include/Modbusma_Count.rstinc "" "read from"

.. include-file:: sections/Include/serma_MsgPriority.rstinc "" ":ref:`xmlattr-ModbusmaAppRatioP0`"

.. include-file:: sections/Include/Name.rstinc ""

Poll MSG.Func
^^^^^^^^^^^^^

Table below shows supported values of the :ref:`xmlattr-ModbusmaPollMsgFunc` attribute.

.. field-list-table:: Modbus Master Poll message functions
   :class: table table-condensed table-bordered longtable
   :name: tabid-ModbusmaPollMsgFunc
   :spec: |C{0.1}|S{0.5}|
   :header-rows: 1

   * :val,10,center:	:ref:`xmlattr-ModbusmaPollMsgFunc`
     :name,80:		Function Name

   * :val:	3
     :name:	[:lemonobgtext:`Read Holding Registers`]

   * :val:	4
     :name:	[:lemonobgtext:`Read Input Registers`]

   * :val:	Other
     :name:	Function is not supported

