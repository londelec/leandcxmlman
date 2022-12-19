
.. _xmlelem-udp:

UDP
^^^

This node contains settings of a UDP socket.
UDP is used to send/receive packets to/from remote host without establishing a connection between the source and the destination.
.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-udp`"

.. code-block:: none

   <UDP Index="1" RemoteIPaddr="127.0.0.1" RemotePort="64950" LocalIPaddr="0.0.0.0" LocalPort="64950" ConnectTimeout="5" Timeout="2" TxDelay="0.1" IdleTimeout="10" Name="LAN1"/>


.. include-file:: sections/Include/table_attrs.rstinc "" "tabid-Udp" "UDP attributes" ":spec: |C{0.17}|C{0.17}|C{0.13}|S{0.53}|"

   * :attr:	:xmlattr:`Index`
     :val:	|hwindexrange|
     :def:	n/a
     :desc:	Index is a unique identifier of the hardware node.
		It is used as a reference to link a communication protocol instance to this node.
		:inlinetip:`Indexes don't have to be in a sequential order.`

   * :attr:	:xmlattr:`RemoteIPaddr`
     :val:	0.0.0.0 ... 255.255.255.254
     :def:	127.0.0.1 test only
     :desc:	Remote IPv4 address.
		UDP messages will be sent to this remote address.
		(default localhost address 127.0.0.1  - for testing purposes only)

   * :attr:	:xmlattr:`RemotePort`
     :val:	1...65534
     :def:	n/a
     :desc:	Remote UDP port number.
		UDP messages will be sent to this remote port.
		(default port for supervision instances is 64950)

   * :attr:	:xmlattr:`LocalIPaddr`
     :val:	0.0.0.0 ... 255.255.255.254
     :def:	0.0.0.0
     :desc:	| Local IPv4 address. Ethernet interface with this IP address must exist in the |opsystem|. UDP messages will be received only through Ethernet interface with this address. 
		| IP address 0.0.0.0 can be used to listen for UDP messages on any interface available in the |opsystem|. This allows |leandcapp| to receive UDP messages through any Ethernet interface. |optinaldefattr|

   * :attr:	:xmlattr:`LocalPort`
     :val:	1...65534
     :def:	same as :ref:`xmlattr-UDPRemotePort`
     :desc:	Local UDP port number. UDP messages will be accepted on this port. (default port number is equal to the :ref:`xmlattr-UDPRemotePort`)
		|optinaldefattr|

   * :attr:	:xmlattr:`ConnectTimeout`
     :val:	1...2\ :sup:`32`\  - 1
     :def:	5 sec
     :desc:	Reconnection timeout in seconds.
		Communication will be suspended for a configured number of seconds if last sent UDP message was rejected.
		|optinaldefattr|

.. include-file:: sections/Include/chan_Timeout.rstinc "" "2 sec" " (possibly arriving in multiple UDP datagrams)"
		| > Not used for any other communication protocol instances.
		| |optinaldefattr|

.. include-file:: sections/Include/chan_TxDelay.rstinc ""

   * :attr:	:xmlattr:`IdleTimeout`
     :val:	5...2\ :sup:`32`\  - 1
     :def:	120 sec
     :desc:	Receive idle timeout, only used if :ref:`xmlelem-override` supervision instance is linked.
		TCP socket used for service commands will be closed if no data is received from a remote host within a configured number of seconds.
		|optinaldefattr|

.. include-file:: sections/Include/hidden_Hostname.rstinc "internal" ":ref:`xmlattr-udpRemoteIPaddr`" ":ref:`xmlattr-udpConnectTimeout`" "Host name of the UDP peer. We will send UDP messages"

.. include-file:: sections/Include/Name.rstinc ""
