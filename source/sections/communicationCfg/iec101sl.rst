
.. _xmlelem-gp101sl:

IEC101sl
^^^^^^^^

General settings of the IEC60870-5-101 controlled station (Slave) communication protocol instance.
.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-gp101sl`"

.. code-block:: none

   <IEC101sl Index="5" HWIndex="1" XMLpath="IEC101sl_test.xml" LinkAddr="5" ASDUAddr="5" Source="6" CommsFlags="0x80" Name="Serial SCADA"/>


.. include-file:: sections/Include/table_gp.rstinc "" "tabid-gp101sl" "IEC101sl"

.. include-file:: sections/Include/gp_sl_Index.rstinc "" 

.. include-file:: sections/Include/gp_HWIndex.rstinc "" ":ref:`xmlelem-uart`.\ :ref:`xmlattr-UARTIndex`\; :ref:`xmlelem-tcpserver`.\ :ref:`xmlattr-TCPSERVERIndex`\; :ref:`xmlelem-tcpclient`.\ :ref:`xmlattr-TCPCLIENTIndex` or :ref:`xmlelem-udp`.\ :ref:`xmlattr-UDPIndex`"
		:inlinetip:`Multiple` :ref:`xmlelem-gp101sl` :inlinetip:`instances can share the same hardware node.`

.. include-file:: sections/Include/gp_XMLpath.rstinc ""

   * :attr:	:xmlattr:`LinkAddr`
     :val:	1...254 or 1...65534
     :desc:	Link layer address of the communication protocol instance.
		Address of the connected IEC60870-5-101 Master station must be the same.
		Size of the link layer address may be 1 or 2 bytes as set by the :ref:`xmlelem-IEC101slLink`.\ :ref:`xmlattr-IEC101slLinkLinkAddrSize` \ attribute.
		Please note value 255 (if link layer address size is 1 byte) or 65535 (if link layer address size is 2 bytes) is Broadcast address and can't be used.

   * :attr:	:xmlattr:`ASDUAddr`
     :val:	1...254 or 1...65534
     :desc:	Common address of ASDU (CAA).
		It is possible to create more than 1 ASDU for our IEC60870-5-101 Slave station.
		Multiple :ref:`xmlelem-gp101sl` nodes must be created in this case, one for each ASDU.
		All of these :ref:`xmlelem-gp101sl` nodes will have the same :ref:`xmlattr-gp101slLinkAddr` and unique :ref:`xmlattr-gp101slASDUAddr`.
		Size of the common ASDU address may be 1 or 2 bytes as set by the :ref:`xmlelem-IEC101slAsdu`.\ :ref:`xmlattr-IEC101slAsduCAASize` \ attribute.
		Please note value 255 (if ASDU address size is 1 byte) or 65535 (if ASDU address size is 2 bytes) is Broadcast address and can't be used.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, value of the` :ref:`xmlattr-gp101slLinkAddr` :inlinetip:`will be used if omitted.`

.. include-file:: sections/Include/IEC10xsl_Source.rstinc ""

.. include-file:: sections/Include/gp_CommsFlags.rstinc ""

.. include-file:: sections/Include/Name_wodef.rstinc ""

.. include-file:: sections/Include/gp_section.rstinc "" ":ref:`xmlattr-gp101slXMLpath`" ":ref:`docref-IEC101sl`"
