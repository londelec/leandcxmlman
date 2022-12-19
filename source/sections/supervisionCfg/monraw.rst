
.. _xmlelem-monraw:

MONRAW
^^^^^^

Traffic through any serial port can be captured and sent to a remote destination for a real time monitoring.
Remote traffic monitoring can be enabled using so called 'raw monitoring' supervision instance which requires only 1 destination socket to send the captured data.
Raw monitoring mode will be active as long as there is a traffic through the monitored port and remote destination is reachable.
Please see sample :ref:`xmlelem-monraw` element all available attributes below.

.. code-block:: none

   <MONRAW SrcHWIndex="1" DstHWIndex="51" Name="Raw monitoring instance"/>

.. include-file:: sections/Include/table_superv.rstinc "" "tabid-monraw" "MONRAW"

   * :attr:	:xmlattr:`SrcHWIndex`
     :val:	|hwindexrange|
     :desc:	Source index of the serial port to be monitored.
		Any :ref:`xmlelem-uart` node can be used as a source for traffic monitoring.
		Please note serial port must not be linked to any other :ref:`xmlgroup-SupervisionCfg` node.

   * :attr:	:xmlattr:`DstHWIndex`
     :val:	|hwindexrange|
     :desc:	Destination index of the hardware node to send captured traffic.
		Any of :ref:`xmlelem-tcpserver` or :ref:`xmlelem-udp` nodes can be used to send captured traffic as long as the hardware node is not linked to a communication protocol instance.

.. include-file:: sections/Include/Name_wodef.rstinc ""

.. tip::
   | :ref:`xmlelem-udp` socket is recommended as a destination for sending the captured traffic.
   | Default TCP/UDP port for destination node (:ref:`xmlattr-monrawDstHWIndex`) is 64950.
