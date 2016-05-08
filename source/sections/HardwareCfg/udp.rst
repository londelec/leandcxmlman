
.. _ref-UDP:

UDP
^^^

This node contains settings of a UDP socket.
UDP socket is used to send/receive packets to/from remote host without establishing a connection between the source and the destination.
.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`<ref-UDP>`"

.. code-block:: none

   <UDP Index="1" RemoteIPaddr="127.0.0.1" RemotePort="64950" LocalIPaddr="0.0.0.0" LocalPort="64950" ConnectTimeout="5" Timeout="2" TxDelay="0.1" IdleTimeout="10" Name="LAN1"/>


.. _ref-UDPAttributes:

.. include-file:: sections/Include/table_attrs.rstinc "" "Leandc UDP node"

   * :attr:     .. _ref-UDPIndex:

                :xmlref:`Index`
     :val:      1...254
     :def:      n/a
     :desc:     Index is a unique identifier of the hardware node. It is used as a reference to link a communication protocol instance to this node. :inlinetip:`Indexes don't have to be in a sequential order.`

   * :attr:     .. _ref-UDPRemoteIPaddr:

		:xmlref:`RemoteIPaddr`
     :val:      0.0.0.0 ... 255.255.255.254
     :def:      127.0.0.1 test only
     :desc:     Remote IPv4 address. UDP socket will send messages to this remote address. (default localhost address 127.0.0.1  - for testing purposes only)

   * :attr:     .. _ref-UDPRemotePort:

                :xmlref:`RemotePort`
     :val:      1...65534
     :def:      n/a
     :desc:     Remote UDP port number. UDP socket will send messages to this remote port. (default port for supervision instances is 64950)

   * :attr:     :xmlref:`LocalIPaddr`
     :val:      0.0.0.0 ... 255.255.255.254
     :def:      0.0.0.0
     :desc:     | Local IPv4 address. Ethernet interface with this IP address must exist in the operating system. UDP messages will be received only through Ethernet interface with this address. 
                | IP address 0.0.0.0 can be used to bind a UDP socket to any interface available in the operating system. This will allow leandc to receive UDP messages through any Ethernet interface. :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:     :xmlref:`LocalPort`
     :val:      1...65534
     :def:      same as :ref:`<ref-UDPRemotePort>`
     :desc:     Local UDP port number. UDP messages will be accpted on this port. (default port number is equal to the :ref:`<ref-UDPRemotePort>`) :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:     :xmlref:`ConnectTimeout`
     :val:      1...2\ :sup:`32`\  - 1
     :def:      5 sec
     :desc:     Socket reconnection timeout in seconds. Communication will be suspended for a configured number of seconds if last sent UDP message was rejected. :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:     :xmlref:`Timeout`
     :val:      0.01...42949
     :def:      2 sec
     :desc:     Timeout value in seconds, only used if a serial communication instance (e.g. IEC60870-5-101) is linked to this :ref:`<ref-UDP>` node. New outgoing message will be sent, if there was no reply from outstation within a configured number of seconds. :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:     :xmlref:`TxDelay`
     :val:      0.00001...42949
     :def:      0.1 sec
     :desc:     Transmit delay in seconds, only used if a serial communication instance (e.g. IEC60870-5-101) is linked to this :ref:`<ref-UDP>` node. Outgoing message will be delayed for a configured number of seconds before being sent after received message. :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:     .. _ref-UDPIdleTimeout:

                :xmlref:`IdleTimeout`
     :val:      5...2\ :sup:`32`\  - 1
     :def:      120 sec
     :desc:     Receive idle timeout, only used if :ref:`<ref-OVERRIDE>` supervision instance is linked to this :ref:`<ref-UDP>` node. TCP socket used for service commands will be closed if no data is received from a remote host within this timeout. :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

.. include-file:: sections/Include/Name.rstinc ""
