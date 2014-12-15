
.. _ref-MONCOMP:

MONCOMP element node
^^^^^^^^^^^^^^^^^^^^

Traffic through any leandc serial port or socket can be captured and sent to a remote destination for a real time 
monitoring. Remote traffic monitoring can be enabled using so called compatible monitoring supervision 
instance which requires 2 sockets for its operation. 1st socket will be the destination to send captured data and 
the 2nd socket will be used for service commands. Captured data will be send only if both remote destination 
and socket for service commands are active/reachable. Please see sample :ref:`MONCOMP<ref-MONCOMP>` element node used to 
configure compatible monitoring and the table listing all available attributes below.

.. code-block:: none

   <MONCOMP SrcHWIndex="2" DstHWIndex="52" SrvHWIndex="53" Name="Compatible monitoring instance"/>

.. _ref-MONCOMPAttributes:

.. field-list-table:: Leandc MONCOMP node
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.20}|C{0.25}|S{0.55}|
   :header-rows: 1

   * :attr,10: Attribute
     :val,15:  Values or range
     :desc,75: Description

   * :attr:    :xmlref:`SrcHWIndex`
     :val:     1...254
     :desc:    Source index of the hardware node to be monitored. Any of :ref:`UART<ref-UART>`; :ref:`TCPSERVER<ref-TCPSERVER>`; :ref:`TCPCLIENT<ref-TCPCLIENT>` or :ref:`UDP<ref-UDP>` nodes can be used as a source for traffic monitoring.

   * :attr:    :xmlref:`DstHWIndex`
     :val:     1...254
     :desc:    Destination index of the hardware node to send captured traffic. Any of :ref:`TCPSERVER<ref-TCPSERVER>` or :ref:`UDP<ref-UDP>` nodes can be used to send captured traffic providing they aren't linked to a communication protocol instance.

   * :attr:    :xmlref:`SrvHWIndex`
     :val:     1...254
     :desc:    Index of the hardware node for receiving service commands. Any of :ref:`TCPCLIENT<ref-TCPCLIENT>` nodes can be used for service commands providing they aren't linked to a communication protocol instance.

   * :attr:    :xmlref:`Name`
     :val:     Max 100 chars
     :desc:    Freely configurable name, just for reference. :inlinetip:`Name attribute is optional and doesn't have to be included in configuration.`

Please note :ref:`TCPSERVER<ref-TCPSERVER>`.\ :ref:`IdleTimeout<ref-TCPSERVERIdleTimeout>` \  attribute will be used to check activity of the service socket. The service 
:ref:`TCPSERVER<ref-TCPSERVER>` socket will be disconnected if no data is received within a configured number of seconds and also 
the destination socket is disconnected/unreachable.


.. tip:: Default port for destination node (linked with :xmlref:`DstHWIndex`) is 64950 and service node (linked with :xmlref:`SrcHWIndex`) is 64966.
