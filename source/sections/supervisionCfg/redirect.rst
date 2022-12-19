
.. _xmlelem-redirect:

REDIRECT
^^^^^^^^

Serial server functionality allows to send data from one serial port to another over the network transparently as if these serial ports where connected together with a direct cable.
In order to permanently enable serial server functionality so called :ref:`xmlelem-redirect` supervision instance can be used.
It requires only 1 destination socket to send the redirected data.
Serial data will be redirected as long as remote destination is reachable.
Please see sample :ref:`xmlelem-redirect` element and all available attributes below.

.. code-block:: none

   <REDIRECT SrcHWIndex="4" DstHWIndex="61" SrvHWIndex="53" Name="UART redirect"/>

.. include-file:: sections/Include/table_superv.rstinc "" "tabid-redirect" "REDIRECT"

   * :attr:	:xmlattr:`SrcHWIndex`
     :val:	|hwindexrange|
     :desc:	Index of the :ref:`xmlelem-uart` node to be redirected.
		Data received through this serial port will be redirected to a destination hardware node and data received from a destination hardware node will be redirected to this serial port.
		No communication protocol instances must be linked to :ref:`xmlelem-uart` node in order to use it for redirection.
		Also serial port must not be linked to any other :ref:`xmlgroup-SupervisionCfg` node.

   * :attr:	:xmlattr:`DstHWIndex`
     :val:	|hwindexrange|
     :desc:	Destination index of the hardware node to redirect the data.
		Any of :ref:`xmlelem-tcpserver`; :ref:`xmlelem-tcpclient` or :ref:`xmlelem-udp` nodes can be used as destination.
		Data received from a destination hardware node will be redirected to the serial port.

   * :attr:	:xmlattr:`SrvHWIndex`
     :val:	|hwindexrange|
     :desc:	Index of the hardware node for receiving service commands.
		Any of :ref:`xmlelem-tcpserver` nodes can be used as long as the hardware node is not linked to a communication protocol instance.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration.`

.. include-file:: sections/Include/Name_wodef.rstinc ""

Please note :ref:`xmlelem-tcpserver`.\ :ref:`xmlattr-TCPSERVERIdleTimeout` \ and :ref:`xmlelem-tcpclient`.\ :ref:`xmlattr-TCPCLIENTIdleTimeout` \ attributes will be used to check activity of 
the destination socket. The destination :ref:`xmlelem-tcpserver` or :ref:`xmlelem-tcpclient` sockets will be disconnected if no data is 
received within a configured number of seconds. This means there has to be an ongoing communication to 
prevent TCP sockets from being automatically disconnected. This doesn't apply to UDP socket.

.. tip:: Default TCP/UDP port for destination node (:ref:`xmlattr-redirectDstHWIndex`) is 64950.
