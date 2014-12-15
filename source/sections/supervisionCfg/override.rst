
.. _ref-OVERRIDE:

OVERRIDE element node
^^^^^^^^^^^^^^^^^^^^^

Serial server functionality in leandc enables to send data from one serial port to another over the network in a 
transparent mode as if these serial ports where connected together with a direct cable. However sometimes it is 
useful to enable serial server functionality only temporarily and return the port to a normal operation when it is no 
longer required. It can be used to e.g. temporarily poll or configure a serial device connected to leandc and 
return to normal operation mode after configuration is complete. Temporary serial server functionality can be 
enabled using so called override supervision instance which requires 2 sockets for its operation. 1st socket will 
be the destination to redirect serial data and the 2nd socket will be used for service commands. Serial server 
functionality will be automatically enabled only if both remote destination and socket for service commands are 
active/reachable. Please see sample :ref:`OVERRIDE<ref-OVERRIDE>` element node used to configure temporary serial server and 
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

   * :attr:    :xmlref:`SrcHWIndex`
     :val:     1...254
     :desc:    Index of the :ref:`UART<ref-UART>` node to be temporarily overridden. Data received through this UART will be temporarily redirected to a destination hardware node and data received from a destination hardware node will be temporarily redirected to this UART.

   * :attr:    :xmlref:`DstHWIndex`
     :val:     1...254
     :desc:    Destination index of the hardware node to temporarily redirect the UART data. Any of :ref:`TCPSERVER<ref-TCPSERVER>`; :ref:`TCPCLIENT<ref-TCPCLIENT>` or :ref:`UDP<ref-UDP>` nodes can be used as destination where data received through source UART will be temporarily sent. Data received from a destination hardware node will be temporarily redirected to source UART.

   * :attr:    :xmlref:`SrvHWIndex`
     :val:     1...254
     :desc:    Index of the hardware node for receiving service commands. Any of :ref:`TCPSERVER<ref-TCPSERVER>` or :ref:`TCPCLIENT<ref-TCPCLIENT>` nodes can be used for service commands providing they aren't linked to a communication protocol instance.

   * :attr:    :xmlref:`Name`
     :val:     Max 100 chars
     :desc:    Freely configurable name, just for reference. :inlinetip:`Name attribute is optional and doesn't have to be included in configuration.`

Please note :ref:`TCPSERVER<ref-TCPSERVER>`.\ :ref:`IdleTimeout<ref-TCPSERVERIdleTimeout>` \ and :ref:`TCPCLIENT<ref-TCPCLIENT>`.\ :ref:`IdleTimeout<ref-TCPCLIENTIdleTimeout>` \ attributes will be used to check activity of 
both destination and service sockets. The destination and service :ref:`TCPSERVER<ref-TCPSERVER>` or :ref:`TCPCLIENT<ref-TCPCLIENT>` sockets will be 
disconnected if no data is received within a configured number of seconds. Also the service :ref:`TCPSERVER<ref-TCPSERVER>` or 
:ref:`TCPCLIENT<ref-TCPCLIENT>` sockets will be disconnected if no data is received within a number of seconds configured in the 
destination socket UDP.IdleTimeout attribute. This means there has to be an ongoing communication to prevent 
TCP sockets from being automatically disconnected.


.. tip:: Default port for destination node (linked with :xmlref:`DstHWIndex`) is 64950 and service node (linked with :xmlref:`SrcHWIndex`) is 64966.
