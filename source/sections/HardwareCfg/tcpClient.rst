
.. _ref-TCPCLIENT:

TCPCLIENT
^^^^^^^^^

This node contains settings of a TCP client socket.
TCP client socket is used to connect to a remote host.
.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`<ref-TCPCLIENT>`"

.. code-block:: none

   <TCPCLIENT Index="1" ServerIPaddr="127.0.0.1" Port="2404" ConnectTimeout="5" Timeout="2" TxDelay="0.1" IdleTimeout="10" Keepalive="20" Name="LAN1"/>


.. _ref-TCPCLIENTAttributes:

.. include-file:: sections/Include/table_attrs.rstinc "" "Leandc TCPCLIENT node"

   * :attr:     .. _ref-TCPCLIENTIndex:

                :xmlref:`Index`
     :val:      1...254
     :def:      n/a
     :desc:     Index is a unique identifier of the hardware node. It is used as a reference to link a communication protocol instance to this node. :inlinetip:`Indexes don't have to be in a sequential order.`

   * :attr:     .. _ref-TCPCLIENTIPaddr:

		:xmlref:`ServerIPaddr`
     :val:      0.0.0.0 ... 255.255.255.254
     :def:      127.0.0.1 test only
     :desc:     Server IPv4 address. TCP connection will established to this remote address. (default localhost address 127.0.0.1 - for testing purposes only)

   * :attr:     .. _ref-TCPCLIENTPort:

		:xmlref:`Port`
     :val:      1...65534
     :def:      n/a
     :desc:     TCP port number. TCP connection will be established to this remote port. (default port for IEC60870-5-104 is 2404)

   * :attr:     :xmlref:`ConnectTimeout`
     :val:      1...2\ :sup:`32`\  - 1
     :def:      5 sec
     :desc:     TCP socket reconnection timeout in seconds. Connection request (SYN) message will be sent after this timeout which starts when existing connection fails. If it is impossible to connect to a remote Server, connection request (SYN) messages will be sent at these intervals. :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

.. include-file:: sections/Include/TCPser_Timeouts.rstinc "" ":ref:`<ref-TCPCLIENT>`" ".. _ref-TCPCLIENTIdleTimeout:" 

   * :attr:     .. _ref-TCPCLIENTKeepalive:

                :xmlref:`Keepalive`
     :val:      0...2\ :sup:`32`\  - 1
     :def:      0 sec
     :desc:     Keepalive message seding interval normally used for IEC61850 Client instance. TCP Socket will be closed if the remote host fails to reply to a keepalive message within configured number of seconds. (default is 20 seconds for IEC61850 Client instance) :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

.. include-file:: sections/Include/Name.rstinc ""
