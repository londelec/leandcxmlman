
.. _ref-Modbusma:

Modbusma
^^^^^^^^

General settings of the Modbus Master communication protocol instance.
.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`<ref-Modbusma>`"

.. code-block:: none

   <Modbusma Index="10" HWIndex="2" XMLpath="BCDI16_test.xml" Address="5" CommsFlags="0x80" Name="IO device"/>


.. _ref-ModbusmaAttributes:

.. field-list-table:: Modbusma node
   :class: table table-condensed table-bordered longtable
   :header-rows: 1
   :spec: |C{0.20}|C{0.25}|S{0.55}|
   
   * :attr,10: Attribute
     :val,15:  Values or range
     :desc,75: Description

   * :attr:     .. _ref-ModbusmaIndex:

                :xmlref:`Index`
     :val:      1...254
     :desc:     Index is a unique identifier of the communication protocol instance.
		It is used to reference protocol instance from other configuration files e.g. IO object tables 
		(please see :ref:`DI<ref-IEC10xslDI>`.\ :ref:`<ref-IEC10xslDIDevice>`\; :ref:`AI<ref-IEC10xslAI>`.\ :ref:`<ref-IEC10xslAIDevice>`\; :ref:`DO<ref-IEC10xslDO>`.\ :ref:`<ref-IEC10xslDODevice>`\; :ref:`AO<ref-IEC10xslAO>`.\ :ref:`<ref-IEC10xslAODevice>` \ attributes of the Slave protocol instance)
		:inlinetip:`Indexes don't have to be in a sequential order.`

   * :attr:     :xmlref:`HWIndex`
     :val:      1...254
     :desc:     Hardware Index is used to link a communication protocol instance to a hardware node.
		Use value of the :ref:`<ref-UART>`.\ :ref:`<ref-UARTIndex>`\; :ref:`<ref-TCPSERVER>`.\ :ref:`<ref-TCPSERVERIndex>`\; :ref:`<ref-TCPCLIENT>`.\ :ref:`<ref-TCPCLIENTIndex>` \ or :ref:`<ref-UDP>`.\ :ref:`<ref-UDPIndex>` \ attribute as a hardware index in order to link the protocol instance.
		:inlinetip:`Multiple` :ref:`<ref-Modbusma>` :inlinetip:`instances can share the same hardware node.`

.. include-file:: sections/Include/Comms_XMLpath.rstinc "" ".. _ref-ModbusmaXMLpath:"

   * :attr:     :xmlref:`Address`
     :val:      1...254
     :desc:     Device address of outstation.
		Connected station must have the same device address.
		Please note value 255 is Broadcast address and can't be used.

.. include-file:: sections/Include/Comms_CommsFlags.rstinc ""

.. include-file:: sections/Include/Name_wodef.rstinc ""

