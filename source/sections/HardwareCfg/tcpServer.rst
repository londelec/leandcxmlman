
.. _xmlelem-tcpserver:

TCPSERVER
^^^^^^^^^

This node contains settings of a TCP server socket.
TCP server socket is used to accept connections from remote hosts.
.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-tcpserver`"

.. code-block:: none

   <TCPSERVER Index="1" ServerIPaddr="127.0.0.1" Port="2404" Timeout="2" TxDelay="0.1" IdleTimeout="10" Name="LAN1"/>


.. include-file:: sections/Include/table_attrs.rstinc "" "tabid-TcpServer" "TCPSERVER attributes" ":spec: |C{0.14}|C{0.17}|C{0.1}|S{0.59}|"

   * :attr:	:xmlattr:`Index`
     :val:	|hwindexrange|
     :def:	n/a
     :desc:	Index is a unique identifier of the hardware node.
		It is used as a reference to link a communication protocol instance to this node. :inlinetip:`Indexes don't have to be in a sequential order.`

   * :attr:	:xmlattr:`ServerIPaddr`
     :val:	0.0.0.0 ... 255.255.255.254
     :def:	0.0.0.0
     :desc:	| Server IPv4 address. Ethernet interface with this IP address must exist in the |opsystem|. Remote TCP clients will be able to connect only through Ethernet interface with this address.
		| IP address 0.0.0.0 can be used to bind a :ref:`xmlelem-tcpserver` socket to any interface available in the |opsystem|. This will allow TCP clients to connect through any Ethernet interface.

   * :attr:	:xmlattr:`Port`
     :val:	1...65534
     :def:	n/a
     :desc:	TCP port number.
		Unlimited number of incoming TCP connection requests will be accepted on this port as long as there is a communication protocol or supervision instance available to handle the new connection.
		(default port for IEC60870-5-104 is 2404)

.. include-file:: sections/Include/chan_Timeout.rstinc "" "2 sec" " (possibly arriving in multiple TCP segments)"
		| > IEC61850 instance - connection will be closed if not all TCP segments of a TPKT message have been received within a configured number of seconds.
		| > Not used for any other communication protocol instances.
		| |optinaldefattr|

.. include-file:: sections/Include/chan_TxDelay.rstinc ""

.. include-file:: sections/Include/TCP_IdleTimeout.rstinc ""

.. include-file:: sections/Include/Name.rstinc ""
