
.. _ref-CommsFlags:

CommsFlags attribute
^^^^^^^^^^^^^^^^^^^^

Communication flags are used to configure initialization settings of some communication protocol instances. For 
example, outstation polling can be disabled on leandc startup and enabled by user later on issuing a service 
command.

.. _ref-CommsFlagsAttribute:

.. field-list-table:: CommsFlags attribute
   :class: table table-condensed table-bordered longtable
   :header-rows: 1
   :spec: |C{0.20}|C{0.25}|S{0.55}|

   * :attr,10: Bits
     :val,15:  Values
     :desc,75: Description

   * :attr:    :xmlref:`CommsFlags` [xxxx.xxxx]
     :val:     0...0xFF
     :desc:    CommsFlags is 8 bit encoded variable.

   * :attr:    Bit 3
     :val:     xxxx.0xxx
     :desc:    **Reject** new incoming connection to local (leandc's) TCP server socket if a remote TCP client is already connected (default value)

   * :(attr):
     :val:     xxxx.1xxx
     :desc:    **Always accept** new incoming connection to local (leandc's) TCP server socket. This means terminating an exisiting ongoing connection in order to accept the new connection request

   * :attr:    Bit 4
     :val:     xxx0.xxxx
     :desc:    IEC 60870-5-104 controlling station (Master) communication protocol instance **sends** [STARTDT_act] to outstation on leandc startup (default value)

   * :(attr):
     :val:     xxx1.xxxx
     :desc:    IEC 60870-5-104 controlling station (Master) communication protocol instance **doesn't** send [STARTDT_act] to outstation on leandc startup

   * :attr:    Bit 7
     :val:     0xxx.xxxx
     :desc:    Protocol instance is **enabled** on leandc startup. Communication will start automatically (default value)

   * :(attr):
     :val:     1xxx.xxxx
     :desc:    Protocol instance is **disabled** on leandc startup. Commnication will not start automatically, service command (Index="-3") may be used to enable communication at any time. Please see table :numref:`ref-IEC10xslDOServiceIndexValues` for information on service commands.

   * :attr:    Bits 0...2;5;6
     :val:     Any
     :desc:    Bits reserved for future use
