
.. _xmlelem-override:

OVERRIDE
^^^^^^^^

Serial server functionality allows to send data from one serial port to another over the network transparently as if these serial ports where connected together with a direct cable.
:ref:`xmlelem-override` instance provides an option to temporary override normal operation of the serial port and enable serial server functionality that allows to send data from a remote host over the network to this serial port.
It becomes useful in situations where serial server functionality is required only for a short period of time and serial port has to be returned to a normal operation when it is no longer needed.
This can be used to e.g. poll or configure any serial device and automatically resume normal operation afterwards.
:ref:`xmlelem-override` supervision instance requires 2 sockets for operation.
The 1st socket is a destination for the redirected serial data and the 2nd socket is used for service commands.
Serial server functionality will be automatically enabled only if both sockets are active/reachable.
This mode is compatible with Moxa serial server driver, please refer to the latest NPort_installation manual for more information.
Please see sample :ref:`xmlelem-override` element and all available attributes below.

.. code-block:: none

   <OVERRIDE SrcHWIndex="3" DstHWIndex="62" SrvHWIndex="63" Name="UART override (temporary)"/>

.. include-file:: sections/Include/table_superv.rstinc "" "tabid-override" "OVERRIDE"

   * :attr:	:xmlattr:`SrcHWIndex`
     :val:	|hwindexrange|
     :desc:	Index of the :ref:`xmlelem-uart` node to be temporarily overridden.
		Data received through this serial port will be temporarily redirected to a destination hardware node and data received from a destination hardware node will be temporarily redirected to this serial port.
		Please note serial port must not be linked to any other :ref:`xmlgroup-SupervisionCfg` node.

   * :attr:	:xmlattr:`DstHWIndex`
     :val:	|hwindexrange|
     :desc:	Destination index of the hardware node to temporarily redirect the serial port data.
		Any of :ref:`xmlelem-tcpserver`; :ref:`xmlelem-tcpclient` or :ref:`xmlelem-udp` nodes can be used as destination.
		Data received from a destination hardware node will be temporarily redirected to the serial port.

   * :attr:	:xmlattr:`SrvHWIndex`
     :val:	|hwindexrange|
     :desc:	Index of the hardware node for receiving service commands.
		Any of :ref:`xmlelem-tcpserver` or :ref:`xmlelem-tcpclient` nodes can be used as long as the hardware node is not linked to a communication protocol instance.

.. include-file:: sections/Include/Name_wodef.rstinc ""

Please note :ref:`xmlelem-tcpserver`.\ :ref:`xmlattr-TCPSERVERIdleTimeout` \ and :ref:`xmlelem-tcpclient`.\ :ref:`xmlattr-TCPCLIENTIdleTimeout` \ attributes will be used to check activity of 
both destination and service sockets. The destination and service :ref:`xmlelem-tcpserver` or :ref:`xmlelem-tcpclient` sockets will be 
disconnected if no data is received within a configured number of seconds. Also the service :ref:`xmlelem-tcpserver` or 
:ref:`xmlelem-tcpclient` sockets will be disconnected if no data is received within a number of seconds configured in the 
destination socket :ref:`xmlelem-udp`.\ :ref:`xmlattr-UDPIdleTimeout` \ attribute. This means there has to be an ongoing communication to prevent 
TCP sockets from being automatically disconnected.


.. tip:: Default TCP/UDP port for destination node (:ref:`xmlattr-overrideDstHWIndex`) is 64950 and service node (:ref:`xmlattr-overrideSrvHWIndex`) is 64966.
