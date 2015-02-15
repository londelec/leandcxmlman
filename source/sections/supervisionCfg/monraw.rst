
.. _ref-MONRAW:

MONRAW element node
^^^^^^^^^^^^^^^^^^^

Traffic through any leandc serial port or socket can be captured and sent to a remote destination for a real time
monitoring. Remote traffic monitoring can be enabled using so called 'raw monitoring' supervision instance which 
requires only 1 destination socket to send the captured data. Raw monitoring mode will be active as long as
there is a traffic through the monitored port and remote destination is reachable. Please see sample :ref:`MONRAW<ref-MONRAW>` 
element node used to configure raw monitoring and the table listing all available attributes below.

.. code-block:: none

   <MONRAW  SrcHWIndex="1" 
            DstHWIndex="51" 
            Name="Raw monitoring instance"/>

.. _ref-MONRAWAttributes:

.. field-list-table:: Leandc MONRAW node
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

   * :attr:    :xmlref:`Name`
     :val:     Max 100 chars
     :desc:    Freely configurable name, just for reference. :inlinetip:`Name attribute is optional and doesn't have to be included in configuration.`

.. tip::
   | :ref:`UDP<ref-UDP>` socket is recommended as a destination for sending the captured traffic.
   | Default TCP/UDP port for destination node (:xmlref:`DstHWIndex`) is 64950.
