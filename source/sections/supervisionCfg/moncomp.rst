
.. _ref-MONCOMP:

MONCOMP
^^^^^^^

Traffic through any leandc serial port or socket can be captured and sent to a remote destination for a real time
monitoring. Remote traffic monitoring can be enabled using so called 'compatible monitoring' supervision
instance which requires 2 sockets for its operation. 1st socket will be the destination to send captured data and
the 2nd socket will be used for service commands. Captured data will be sent only if both remote sockets are active/reachable. 
Please see sample :ref:`<ref-MONCOMP>` element node used to
configure compatible monitoring and the table listing all available attributes below.

.. code-block:: none

   <MONCOMP SrcHWIndex="2" DstHWIndex="52" SrvHWIndex="53" Name="Compatible monitoring instance"/>

.. _ref-MONCOMPAttributes:

.. field-list-table:: Leandc MONCOMP node
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.16}|C{0.12}|S{0.72}|
   :header-rows: 1

   * :attr,10: Attribute
     :val,15:  Values or range
     :desc,75: Description

   * :attr:     :xmlref:`SrcHWIndex`
     :val:      1...254
     :desc:     Source index of the hardware node to be monitored. Any of :ref:`UART<ref-UART>`; :ref:`<ref-TCPSERVER>`; :ref:`<ref-TCPCLIENT>` or :ref:`<ref-UDP>` nodes can be used as a source for traffic monitoring.

   * :attr:     :xmlref:`DstHWIndex`
     :val:      1...254
     :desc:     Destination index of the hardware node to send captured traffic. Any of :ref:`<ref-TCPSERVER>` or :ref:`<ref-UDP>` nodes can be used to send the captured traffic as long as the hardware node is not linked to a communication protocol instance.

   * :attr:     :xmlref:`SrvHWIndex`
     :val:      1...254
     :desc:     Index of the hardware node for receiving service commands. Any of :ref:`<ref-TCPCLIENT>` nodes can be used as long as the hardware node is not linked to a communication protocol instance.

.. include-file:: sections/Include/Name_wodef.rstinc ""

Please note :ref:`<ref-TCPSERVER>`.\ :ref:`<ref-TCPSERVERIdleTimeout>` \  attribute will be used to check activity of the service socket.
The service :ref:`<ref-TCPSERVER>` socket will be disconnected if no data is received within a configured number of seconds and also 
the destination socket is disconnected/unreachable.


.. tip:: Default TCP/UDP port for destination node (:xmlref:`DstHWIndex`) is 64950 and service node (:xmlref:`SrvHWIndex`) is 64966.
