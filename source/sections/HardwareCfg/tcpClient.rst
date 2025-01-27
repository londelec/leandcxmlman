
.. _xmlelem-tcpclient:

TCPCLIENT
^^^^^^^^^

This node contains settings of a TCP client socket.
TCP client socket is used to connect to a remote host.
.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-tcpclient`"

.. code-block:: none

   <TCPCLIENT Index="1" ServerIPaddr="127.0.0.1" Port="2404" ConnectTimeout="5" Timeout="2" TxDelay="0.1" IdleTimeout="10" Keepalive="20" Name="LAN1"/>


.. include-file:: sections/Include/table_attrs.rstinc "" "tabid-TcpClient" "TCPCLIENT attributes" ":spec: |C{0.17}|C{0.17}|C{0.1}|S{0.56}|"

   * :attr:	:xmlattr:`Index`
     :val:	|hwindexrange|
     :def:	n/a
     :desc:	Index is a unique identifier of the hardware node. It is used as a reference to link a communication protocol instance to this node.
		:inlinetip:`Indexes don't have to be in a sequential order.`

   * :attr:	:xmlattr:`ServerIPaddr`
     :val:	0.0.0.0 ... 255.255.255.254
     :def:	127.0.0.1 test only
     :desc:	Server IPv4 address. TCP connection will established to this remote address. (default localhost address 127.0.0.1 - for testing purposes only)

   * :attr:	:xmlattr:`Port`
     :val:	1...65534
     :def:	n/a
     :desc:	TCP port number.
		TCP connection will be established to this remote port. (default port for IEC60870-5-104 is 2404)

   * :attr:	:xmlattr:`ConnectTimeout`
     :val:	1...2\ :sup:`32`\  - 1
     :def:	5 sec
     :desc:	TCP socket reconnection timeout in seconds. Connection request (SYN) message will be sent after this timeout which starts when existing connection fails.
		If it is impossible to connect to a remote Server, connection request (SYN) messages will be sent at these intervals.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

.. include-file:: sections/Include/chan_Timeout.rstinc "" "2 sec" " (possibly arriving in multiple TCP segments)"
		| > IEC61850 Client instance - connection will be closed if not all TCP segments of a TPKT message have been received within a configured number of seconds.
		| > Not used for any other communication protocol instances.
		| |optinaldefattr|

.. include-file:: sections/Include/chan_TxDelay.rstinc ""

.. include-file:: sections/Include/TCP_IdleTimeout.rstinc ""

   * :attr:	:xmlattr:`Keepalive`
     :val:	0...2\ :sup:`32`\  - 1
     :def:	0 sec
     :desc:	Keepalive message seding interval normally used for IEC61850 Client instance.
		TCP Socket will be closed if the remote host fails to reply to a keepalive message within configured number of seconds.
		(default is 20 seconds for IEC61850 Client instance)
		|optinaldefattr|

.. include-file:: sections/Include/hidden_Hostname.rstinc "internal" ":ref:`xmlattr-tcpclientServerIPaddr`" ":ref:`xmlattr-tcpclientConnectTimeout`" "Host name of the TCP Server. TCP connection will established"

.. include-file:: sections/Include/Name.rstinc ""
