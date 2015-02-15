
.. _ref-UDP:

UDP element node
^^^^^^^^^^^^^^^^

Settings of the UDP sockets are configured using :ref:`UDP<ref-UDP>` element node. Please see sample :ref:`UDP<ref-UDP>` element node 
and the table listing all available attributes below.

.. code-block:: none

   <UDP     Index="1"
            RemoteIPaddr="127.0.0.1"
            RemotePort="64950"
            LocalIPaddr="0.0.0.0"
            LocalPort="64950"
            ConnectTimeout="5"
            Timeout="2"
            TxDelay="0.1"
            IdleTimeout="10"
            Name="LAN1"/>

.. _ref-UDPAttributes:

.. field-list-table:: Leandc UDP node
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.20}|C{0.25}|S{0.55}|
   :header-rows: 1

   * :attr,10: Attribute
     :val,15:  Values or range
     :desc,75: Description

   * :attr:    .. _ref-UDPIndex:
       
               :xmlref:`Index`
     :val:     1...254
     :desc:    Index is a unique identifier of the hardware node. It is used as a reference to link a communication protocol instance to this node. :inlinetip:`Indexes don't have to be in a sequential order.`

   * :attr:    :xmlref:`RemoteIPaddr`
     :val:     0.0.0.0 ... 255.255.255.254
     :desc:    Remote IPv4 address. UDP socket will send messages to this remote address. (default localhost address 127.0.0.1 (only for testing purposes))

   * :attr:    .. _ref-UDPRemotePort:
       
               :xmlref:`RemotePort`
     :val:     1...65534
     :desc:    Remote UDP port number. UDP socket will send messages to this remote port. (default port for supervision instances is 64950)

   * :attr:    :xmlref:`LocalIPaddr`
     :val:     0.0.0.0 ... 255.255.255.254
     :desc:    | Local IPv4 address. Local Ethernet interface with this IP address must exist in the operating system for leandc to use it (bind a socket to it). UDP messages will be received only through Ethernet interface using this local address. 
               | IP address 0.0.0.0 can be used to bind a leandc socket to any interface available in the operating system. This will allow leandc to receive UDP messages through any of running Ethernet interfaces. (default address 0.0.0.0) :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:    :xmlref:`LocalPort`
     :val:     1...65534
     :desc:    Local UDP port number. This local port will accept UDP messages. (default port number is equal to the :ref:`RemotePort<ref-UDPRemotePort>`) :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:    :xmlref:`ConnectTimeout`
     :val:     1...2\ :sup:`32`\  - 1
     :desc:    Socket reconnection timeout in seconds. Communication will be suspended for a configured number of seconds if last UDP message sent was rejected (default 5 seconds) :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:    :xmlref:`Timeout`
     :val:     0.01...42949
     :desc:    Timeout value in seconds, only used if a serial communication instance (e.g. IEC 60870-5-101) is linked to this :ref:`UDP<ref-UDP>` node. New outgoing message will be sent, if there was no reply from outstation within a configured number of seconds. (default 2 seconds) :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:    :xmlref:`TxDelay`
     :val:     0.00001...42949
     :desc:    Transmit delay in seconds, only used if a serial communication instance (e.g. IEC 60870-5-101) is linked to this :ref:`UDP<ref-UDP>` node. Outgoing message will be delayed for a configured number of seconds before being sent after received message. (default 0.1 seconds) :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:    :xmlref:`IdleTimeout`
     :val:     5...2\ :sup:`32`\  - 1
     :desc:    Receive idle timeout, only used if :ref:`OVERRIDE<ref-OVERRIDE>` supervision instance is linked to this :ref:`UDP<ref-UDP>` node. TCP socket used for service commands will be closed if no data is received from a remote host within this timeout (default 120 seconds) :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:    :xmlref:`Name`
     :val:     Max 100 chars
     :desc:    Freely configurable name, just for reference. :inlinetip:`Name attribute is optional and doesn't have to be included in configuration.`
