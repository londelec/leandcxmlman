
.. _xmlelem-gp101ma:

IEC101ma
^^^^^^^^

General settings of the IEC60870-5-101 controlling station (Master) communication protocol instance.
.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-gp101ma`"

.. code-block:: none

   <IEC101ma Index="10" HWIndex="2" XMLpath="IEC101ma_test.xml" LinkAddr="5" ASDUAddr="5" CommsFlags="0x80" Name="Radio Comms"/>


.. include-file:: sections/Include/table_gp.rstinc "" "tabid-gp101ma" "IEC101ma"

.. include-file:: sections/Include/gp_ma_Index.rstinc ""

.. include-file:: sections/Include/gp_HWIndex.rstinc "" ":ref:`xmlelem-uart`.\ :ref:`xmlattr-UARTIndex`\; :ref:`xmlelem-tcpserver`.\ :ref:`xmlattr-TCPSERVERIndex`\; :ref:`xmlelem-tcpclient`.\ :ref:`xmlattr-TCPCLIENTIndex` or :ref:`xmlelem-udp`.\ :ref:`xmlattr-UDPIndex`"
		:inlinetip:`Multiple` :ref:`xmlelem-gp101ma` :inlinetip:`instances can share the same hardware node.`

.. include-file:: sections/Include/gp_XMLpath.rstinc ""

   * :attr:	:xmlattr:`LinkAddr`
     :val:	1...254 or 1...65534
     :desc:	Link layer address of the communication protocol instance.
		Address of the connected IEC60870-5-101 Slave station must be the same.
		Size of the link layer address may be 1 or 2 bytes as set by the :ref:`xmlelem-IEC101maLink`.\ :ref:`xmlattr-IEC101maLinkLinkAddrSize` \ attribute.
		Please note value 255 (if link layer address size is 1 byte) or 65535 (if link layer address size is 2 bytes) is Broadcast address and can't be used.

   * :attr:	:xmlattr:`ASDUAddr`
     :val:	1...254 or 1...65534
     :desc:	Common address of ASDU (CAA).
		Connected IEC60870-5-101 Slave station may have 1 or more ASDUs.
		Multiple :ref:`xmlelem-gp101ma` nodes must be created in case peer station has multiple ASDUs, one for each ASDU.
		All of these :ref:`xmlelem-gp101ma` nodes will have the same :ref:`xmlattr-gp101maLinkAddr` and unique :ref:`xmlattr-gp101maASDUAddr`.
		Size of the common ASDU address may be 1 or 2 bytes as set by the :ref:`xmlelem-IEC101maAsdu`.\ :ref:`xmlattr-IEC101maAsduCAASize` \ attribute.
		Please note value 255 (if ASDU address size is 1 byte) or 65535 (if ASDU address size is 2 bytes) is Broadcast address and can't be used.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, value of the` :ref:`xmlattr-gp101maLinkAddr` :inlinetip:`will be used if omitted.`

.. include-file:: sections/Include/gp_CommsFlags.rstinc ""

.. include-file:: sections/Include/Name_wodef.rstinc ""

.. include-file:: sections/Include/gp_section.rstinc "" ":ref:`xmlattr-gp101maXMLpath`" ":ref:`docref-IEC101ma`"
