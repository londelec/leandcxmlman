
.. _xmlelem-gpmodbusma:

Modbusma
^^^^^^^^

General settings of the Modbus Master communication protocol instance.
.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-gpmodbusma`"

.. code-block:: none

   <Modbusma Index="10" HWIndex="2" XMLpath="BCDI16_test.xml" Address="5" CommsFlags="0x80" Name="IO device"/>


.. include-file:: sections/Include/table_gp.rstinc "" "tabid-gpmodbusma" "Modbusma"

.. include-file:: sections/Include/gp_ma_Index.rstinc ""

.. include-file:: sections/Include/gp_HWIndex.rstinc "" ":ref:`xmlelem-uart`.\ :ref:`xmlattr-UARTIndex`\; :ref:`xmlelem-tcpserver`.\ :ref:`xmlattr-TCPSERVERIndex`\; :ref:`xmlelem-tcpclient`.\ :ref:`xmlattr-TCPCLIENTIndex` or :ref:`xmlelem-udp`.\ :ref:`xmlattr-UDPIndex`"
		:inlinetip:`Multiple` :ref:`xmlelem-gpmodbusma` :inlinetip:`instances can share the same hardware node.`

.. include-file:: sections/Include/gp_XMLpath.rstinc ""

   * :attr:	:xmlattr:`Address`
     :val:	0...247 or 255
     :desc:	Device address of outstation.
		The range of addresses for Modbus RTU/ASCII stations is 1...247.
		Address 255 can be used only for Modbus TCP station that doesn't have a device address (also known as Unit Identifier in the context of Modbus TCP).
		Address 0 is Broadcast address and can't be used for Modbus RTU/ASCII stations.
		However address 0 can be used for Modbus TCP station.

.. include-file:: sections/Include/gp_CommsFlags.rstinc ""

.. include-file:: sections/Include/Name_wodef.rstinc ""

.. include-file:: sections/Include/gp_section.rstinc "" ":ref:`xmlattr-gpmodbusmaXMLpath`" ":ref:`docref-Modbusma`"
