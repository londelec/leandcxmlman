
.. _ref-REDIRECT:

REDIRECT element node
^^^^^^^^^^^^^^^^^^^^^

Serial server functionality enables to send data from one serial port to another over the network in a 
transparently as if these serial ports where connected together with a direct cable. In order to permanently 
enable serial server functionality in leandc so called 'redirect' supervision instance can be used. It requires only 1 
destination socket to send the redirected data. Serial data will be redirected as long as remote destination is
reachable. Please see sample :ref:`REDIRECT<ref-REDIRECT>` element node used to configure serial server and the table listing all 
available attributes below.

.. code-block:: none

   <REDIRECT SrcHWIndex="4" DstHWIndex="61" Name="UART redirect instance"/>

.. _ref-REDIRECTAttributes:

.. field-list-table:: Leandc REDIRECT node
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.20}|C{0.25}|S{0.55}|
   :header-rows: 1

   * :attr,10: Attribute
     :val,15:  Values or range
     :desc,75: Description

   * :attr:    :xmlref:`SrcHWIndex`
     :val:     1...254
     :desc:    Index of the :ref:`UART<ref-UART>` node to be redirected. Data received through this UART will be redirected to a destination hardware node and data received from a destination hardware node will be redirected to this UART. No communication protocol instances must be linked to :ref:`UART<ref-UART>` node in order to use it for redirection.

   * :attr:    :xmlref:`DstHWIndex`
     :val:     1...254
     :desc:    Destination index of the hardware node to redirect the data. Any of :ref:`TCPSERVER<ref-TCPSERVER>`; :ref:`TCPCLIENT<ref-TCPCLIENT>` or :ref:`UDP<ref-UDP>` nodes can be used as destination. Data received from a destination hardware node will be redirected to UART.

   * :attr:    :xmlref:`Name`
     :val:     Max 100 chars
     :desc:    Freely configurable name, just for reference. :inlinetip:`Name attribute is optional and doesn't have to be included in configuration.`

Please note :ref:`TCPSERVER<ref-TCPSERVER>`.\ :ref:`IdleTimeout<ref-TCPSERVERIdleTimeout>` \ and :ref:`TCPCLIENT<ref-TCPCLIENT>`.\ :ref:`IdleTimeout<ref-TCPCLIENTIdleTimeout>` \ attributes will be used to check activity of 
the destination socket. The destination :ref:`TCPSERVER<ref-TCPSERVER>` or :ref:`TCPCLIENT<ref-TCPCLIENT>` sockets will be disconnected if no data is 
received within a configured number of seconds. This means there has to be an ongoing communication to 
prevent TCP sockets from being automatically disconnected. This doesn't apply to UDP socket.

.. tip:: Default TCP/UDP port for destination node (:xmlref:`DstHWIndex`) is 64950.
