
.. _ref-PollMessages:

PollMessages group and MSG node
-------------------------------

Group node :ref:`PollMessages<ref-PollMessages>` and child element nodes :ref:`MSG<ref-PollMessages>` contain messages that are being sent to continuously poll outstation data.
All defined messages are sent to outstation in a sequential order.
Data received from outstation can be mapped using :ref:`DI<ref-ModbusmaDI>` and :ref:`AI<ref-ModbusmaAI>` nodes.

.. tip:: \ :ref:`PollMessages<ref-PollMessages>` group and :ref:`MSG<ref-PollMessages>` nodes are optional if :ref:`<ref-ModbusmaHardcoded>`.\ :ref:`<ref-ModbusmaHardcodedType>` is used. Messages required to poll data from a hardcoded device are set-up automatically.

Please see sample :ref:`PollMessages<ref-PollMessages>` group and :ref:`MSG<ref-PollMessages>` child element nodes below.
There are 2 Modbus messages configured using 2 :ref:`MSG<ref-PollMessages>` element nodes.

.. code-block:: none

   <PollMessages>
	<MSG PollMsg="1" Func="3" Reg="0x0055" Count="2" />
	<MSG PollMsg="2" Func="4" Reg="0x0003" Count="1" />
   </PollMessages>

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`MSG<ref-PollMessages>`"

.. code-block:: none

   <MSG PollMsg="1" Func="4" Reg="0x0100" Count="1" Name="Read Input Registers message" />

.. tip:: Attributes of the :ref:`MSG<ref-PollMessages>` element node can be arranged in any order, it will not affect XML file validation.

MSG attributes
^^^^^^^^^^^^^^

.. _docref-PollMessageAttributes:

.. include-file:: sections/Include/table_attrs.rstinc "" "Modbus Master Poll message attributes" ":spec: |C{0.1}|C{0.16}|C{0.1}|S{0.64}|"

.. include-file:: sections/Include/Modbusma_Msgid.rstinc "" ".. _ref-PollMsgId:" ":xmlref:`PollMsg`"

.. include-file:: sections/Include/Modbusma_Func.rstinc "" ".. _ref-PollMsgFunc:" "See table :numref:`docref-ModbusmaPollFuncTab`"

.. include-file:: sections/Include/Modbusma_Reg.rstinc "" ".. _ref-PollMsgReg:" "Data will be read from this register."

.. include-file:: sections/Include/Modbusma_Count.rstinc "" ".. _ref-PollMsgCount:" "read from"

.. include-file:: sections/Include/Name.rstinc ""

MSG.Func
^^^^^^^^

Table below shows supported values of the :ref:`<ref-PollMsgFunc>` attribute.

.. _docref-ModbusmaPollFuncTab:

.. field-list-table:: Modbus Master Poll message functions
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.1}|S{0.5}|
   :header-rows: 1

   * :val,10:   :ref:`<ref-PollMsgFunc>`
     :name,80:  Function Name

   * :val:      3
     :name:     [:lemonobgtext:`Read Holding Registers`]

   * :val:      4
     :name:     [:lemonobgtext:`Read Input Registers`]

   * :val:      Other
     :name:     Function is not supported

