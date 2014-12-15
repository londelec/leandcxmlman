
.. _ref-TCPSERVER:

TCPSERVER element node
^^^^^^^^^^^^^^^^^^^^^^

Settings of the TCP server sockets are configured using :ref:`TCPSERVER<ref-TCPSERVER>` element node. Please see sample 
:ref:`TCPSERVER<ref-TCPSERVER>` element node and the table listing all available attributes below.

.. code-block:: none

   <TCPSERVER  Index="1"
            ServerIPaddr="127.0.0.1"
            Port="2404"
            Timeout="2"
            TxDelay="0.1"
            IdleTimeout="10"
            Name="LAN1"/>

.. _ref-TCPSERVERAttributes:

.. field-list-table:: Leandc TCPSERVER node
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.20}|C{0.25}|S{0.55}|
   :header-rows: 1

   * :attr,10: Attribute
     :val,15:  Values or range
     :desc,75: Description

   * :attr:    .. _ref-TCPSERVERIndex:
       
               :xmlref:`Index`
     :val:     1...254
     :desc:    Index is a unique identifier of the hardware node. It is used as a reference to link a communication protocol instance to this node. :inlinetip:`Indexes don't have to be in a sequential order.`

   * :attr:    :xmlref:`ServerIPaddr`
     :val:     0.0.0.0 ... 255.255.255.254
     :desc:    Server IPv4 address. There must be a local Ethernet interface with this address assigned in order for leandc to open the socket. Remote TCP clients will be available to connect only through Ethernet interface with this local address. Address 0.0.0.0 can be used to allow TCP clients to connect through any running Ethernet interface. (default address 0.0.0.0 (only for testing purposes))

   * :attr:    :xmlref:`Port`
     :val:     1...65534
     :desc:    TCP port number. This local port will accept unlimited incoming TCP connections as long as there is a communication protocol or supervision instance available to handle the new connection. (default port for IEC 60870-5-104 is 2404)

   * :attr:    :xmlref:`Timeout`
     :val:     0.01...42949
     :desc:    Timeout value in seconds, only used if serial protocol is linked to this :ref:`TCPSERVER<ref-TCPSERVER>` node. New outgoing message will be sent, if there was no reply from outstation within a configured number of seconds. (default 2 seconds) :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:    :xmlref:`TxDelay`
     :val:     0.00001...42949
     :desc:    Transmit delay in seconds, only used if serial protocol is linked to this :ref:`TCPSERVER<ref-TCPSERVER>` node. Outgoing message will be delayed for a configured number of seconds before being sent after previously received message. (default 0.1 seconds) :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:    .. _ref-TCPSERVERIdleTimeout:
   
               :xmlref:`IdleTimeout`
     :val:     5...2\ :sup:`32`\  - 1
     :desc:    Receive idle timeout, only used if serial protocol or supervision instance is linked to this :ref:`TCPSERVER<ref-TCPSERVER>` node. TCP socket will be closed if no data is received from peer within this timeout. (default 120 seconds) :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:    :xmlref:`Name`
     :val:     Max 100 chars
     :desc:    Freely configurable name, just for reference. :inlinetip:`Name attribute is optional and doesn't have to be included in configuration.`
