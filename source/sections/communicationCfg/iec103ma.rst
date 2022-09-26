
.. _xmlelem-gp103ma:

IEC103ma
^^^^^^^^

General settings of the IEC60870-5-103 controlling station (Master) communication protocol instance.
.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-gp103ma`"

.. code-block:: none

   <IEC103ma Index="20" HWIndex="3" XMLpath="Feeder_F1.xml" LinkAddr="5" ASDUAddr="5" CommsFlags="0x80" Name="Feeder_IED1"/>


.. include-file:: sections/Include/table_gp.rstinc "" "tabid-gp103ma" "IEC103ma"

.. include-file:: sections/Include/gp_ma_Index.rstinc "" 

.. include-file:: sections/Include/gp_HWIndex.rstinc "" ":ref:`xmlelem-uart`.\ :ref:`xmlattr-UARTIndex`\; :ref:`xmlelem-tcpserver`.\ :ref:`xmlattr-TCPSERVERIndex`\; :ref:`xmlelem-tcpclient`.\ :ref:`xmlattr-TCPCLIENTIndex` or :ref:`xmlelem-udp`.\ :ref:`xmlattr-UDPIndex`"
		:inlinetip:`Multiple` :ref:`xmlelem-gp103ma` :inlinetip:`instances can share the same hardware node.`

.. include-file:: sections/Include/gp_XMLpath.rstinc ""

   * :attr:	:xmlattr:`LinkAddr`
     :val:	1...254
     :desc:	Link layer address of the communication protocol instance.
		Address of the connected IEC60870-5-103 Slave station (e.g. IED) must be the same.
		Please note value 255 is Broadcast address and can't be used.

   * :attr:	:xmlattr:`ASDUAddr`
     :val:	1...254
     :desc:	Common address of ASDU (CAA).
		Only one ASDU per IEC60870-5-103 Master station is supported.
		Address of the connected IEC60870-5-103 Slave station (e.g. IED) must be the same.
		Please note value 255 is Broadcast address and can't be used.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, value of the` :ref:`xmlattr-gp103maLinkAddr` :inlinetip:`will be used if omitted.`

.. include-file:: sections/Include/gp_CommsFlags.rstinc ""

.. include-file:: sections/Include/Name_wodef.rstinc ""

.. include-file:: sections/Include/gp_section.rstinc "" ":ref:`xmlattr-gp103maXMLpath`" ":ref:`docref-IEC103ma`"
