
.. _xmlelem-moncomp:

MONCOMP
^^^^^^^

Traffic through any serial port can be captured and sent to a remote destination for a real time monitoring.
Remote traffic monitoring can be enabled using so called 'compatible monitoring' supervision instance which requires 2 sockets for its operation.
The 1st socket is destination to send the captured data and the 2nd socket is used for service commands.
Captured data will be sent only if both remote sockets are active/reachable.
This mode is compatible with Moxa serial server driver, please refer to the latest NPort_installation manual for more information.
Please see sample :ref:`xmlelem-moncomp` element and all available attributes below.

.. code-block:: none

   <MONCOMP SrcHWIndex="2" DstHWIndex="52" SrvHWIndex="53" Name="Compatible monitoring instance"/>

.. include-file:: sections/Include/table_superv.rstinc "" "tabid-moncomp" "MONCOMP"

   * :attr:	:xmlattr:`SrcHWIndex`
     :val:	|hwindexrange|
     :desc:	Source index of the serial port node to be monitored.
		Any :ref:`xmlelem-uart` node can be used as a source for traffic monitoring.
		Please note serial port must not be linked to any other :ref:`xmlgroup-SupervisionCfg` node.

   * :attr:	:xmlattr:`DstHWIndex`
     :val:	|hwindexrange|
     :desc:	Destination index of the hardware node to send captured traffic.
		Any of :ref:`xmlelem-tcpserver` or :ref:`xmlelem-udp` nodes can be used to send the captured traffic as long as the hardware node is not linked to a communication protocol instance.

   * :attr:	:xmlattr:`SrvHWIndex`
     :val:	|hwindexrange|
     :desc:	Index of the hardware node for receiving service commands.
		Any of :ref:`xmlelem-tcpserver` nodes can be used as long as the hardware node is not linked to a communication protocol instance.

.. include-file:: sections/Include/Name_wodef.rstinc ""

Please note :ref:`xmlelem-tcpserver`.\ :ref:`xmlattr-TCPSERVERIdleTimeout` \  attribute will be used to check activity of the service socket.
The service :ref:`xmlelem-tcpserver` socket will be disconnected if no data is received within a configured number of seconds and also 
the destination socket is disconnected/unreachable.


.. tip:: Default TCP/UDP port for destination node (:ref:`xmlattr-moncompDstHWIndex`) is 64950 and service node (:ref:`xmlattr-moncompSrvHWIndex`) is 64966.
