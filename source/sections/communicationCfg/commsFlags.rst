
.. _ref-CommsFlags:

CommsFlags attribute
^^^^^^^^^^^^^^^^^^^^

Communication flags contain initialization settings of communication protocol instances. 
For example, outstation polling can be permanently disabled on leandc startup and enabled manually by user issuing a service command.

.. _ref-CommsFlagsAttribute:

.. include-file:: sections/Include/table_flags.rstinc "" "CommsFlags attribute" ":xmlref:`CommsFlags`" "Communication initialization flags"

   * :attr:     Bit 3
     :val:      xxxx.0xxx
     :desc:     **Reject** new incoming connection to local (leandc's) TCP server socket if a remote TCP client is already connected (default value)

   * :(attr):
     :val:      xxxx.1xxx
     :desc:     **Always accept** new incoming connection to local (leandc's) TCP server socket. This means terminating an exisiting ongoing connection in order to accept the new connection request

   * :attr:     Bit 4*
     :val:      xxx0.xxxx
     :desc:     Protocol instance **starts** data exchange on leandc startup (default value)

   * :(attr):
     :val:      xxx1.xxxx
     :desc:     Protocol instance **doesn't** start data exchange on leandc startup. Data exchange will not start automatically, service command (Index="-4") may be used to start data exchange at any time. Please see table :numref:`ref-IEC10xslDOServiceIndex` for more information on service commands.

   * :attr:     Bit 7
     :val:      0xxx.xxxx
     :desc:     Protocol instance is **enabled** on leandc startup. Communication will start automatically (default value)

   * :(attr):
     :val:      1xxx.xxxx
     :desc:     Protocol instance is **disabled** on leandc startup. Commnication will not start automatically, service command (Index="-3") may be used to enable communication at any time. Please see table :numref:`ref-IEC10xslDOServiceIndex` for more information on service commands.

   * :attr:     Bits 0...2;5;6
     :val:      Any
     :desc:     Bits reserved for future use

.. tip::

   | \* This bit only applies to the following protocol instances and is used after TCP connection to the station is established:
   | IEC60870-5-104 controlling station (Master) sends or doesn't send [STARTDT_act] automatically to the outstation on leandc startup;
   | IEC61850 Client sends or doesn't send Association Request to the IED on leandc startup;
