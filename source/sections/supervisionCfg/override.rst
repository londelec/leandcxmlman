
.. _ref-OVERRIDE:

OVERRIDE
^^^^^^^^

Serial server functionality enables to send data from one serial port to another over network
transparently as if these serial ports where connected together with a cable. Sometimes it is
useful to enable serial server functionality only temporarily and return port to a normal operation when it is no
longer needed. Temporary serial server functionality can be used to e.g. poll or configure a serial device connected to LEANDC
and serial port has to resume normal operation afterwards. 'Override' supervision instance provides temporary override of the normal 
operation of the serial port enabling remote data to be transferred through this port. It requires 2 sockets for operation: 1st socket is 
destination for the redirected serial data and the 2nd socket is used for service commands. Serial server
functionality will be automatically enabled only if both sockets are active/reachable. 
Please see sample :ref:`<ref-OVERRIDE>` element node used to configure temporary serial server and 
the table listing all available attributes below.

.. code-block:: none

   <OVERRIDE SrcHWIndex="3" DstHWIndex="62" SrvHWIndex="63" Name="UART override instance"/>

.. _ref-OVERRIDEAttributes:

.. field-list-table:: Leandc OVERRIDE node
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.20}|C{0.25}|S{0.55}|
   :header-rows: 1

   * :attr,10: Attribute
     :val,15:  Values or range
     :desc,75: Description

   * :attr:     :xmlref:`SrcHWIndex`
     :val:      1...254
     :desc:     Index of the :ref:`<ref-UART>` node to be temporarily overridden. Data received through this UART will be temporarily redirected to a destination hardware node and data received from a destination hardware node will be temporarily redirected to this UART.

   * :attr:     :xmlref:`DstHWIndex`
     :val:      1...254
     :desc:     Destination index of the hardware node to temporarily redirect the UART data. Any of :ref:`<ref-TCPSERVER>`; :ref:`<ref-TCPCLIENT>` or :ref:`<ref-UDP>` nodes can be used as destination. Data received from a destination hardware node will be temporarily redirected to source UART.

   * :attr:     :xmlref:`SrvHWIndex`
     :val:      1...254
     :desc:     Index of the hardware node for receiving service commands. Any of :ref:`<ref-TCPSERVER>` or :ref:`<ref-TCPCLIENT>` nodes can be used as long as the hardware node is not linked to a communication protocol instance.

.. include-file:: sections/Include/Name_wodef.rstinc ""

Please note :ref:`<ref-TCPSERVER>`.\ :ref:`<ref-TCPSERVERIdleTimeout>` \ and :ref:`<ref-TCPCLIENT>`.\ :ref:`<ref-TCPCLIENTIdleTimeout>` \ attributes will be used to check activity of 
both destination and service sockets. The destination and service :ref:`<ref-TCPSERVER>` or :ref:`<ref-TCPCLIENT>` sockets will be 
disconnected if no data is received within a configured number of seconds. Also the service :ref:`<ref-TCPSERVER>` or 
:ref:`<ref-TCPCLIENT>` sockets will be disconnected if no data is received within a number of seconds configured in the 
destination socket :ref:`<ref-UDP>`.\ :ref:`<ref-UDPIdleTimeout>` \ attribute. This means there has to be an ongoing communication to prevent 
TCP sockets from being automatically disconnected.


.. tip:: Default TCP/UDP port for destination node (:xmlref:`DstHWIndex`) is 64950 and service node (:xmlref:`SrvHWIndex`) is 64966.
