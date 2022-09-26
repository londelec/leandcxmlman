
CommsFlags attribute
^^^^^^^^^^^^^^^^^^^^

Communication flags contain initialization settings of communication protocol instances. 
For example, outstation polling can be permanently disabled on |leandcfw| startup and enabled by user manually issuing a service command.


.. include-file:: sections/Include/table_flags8.rstinc "" "tabid-CommsFlags" "Communication Flags attribute" ":ref:`xmlattr-gp101maCommsFlags`" "Communication initialization flags"

   * :attr:	:bitdef:`3`
     :val:	xxxx.0xxx
     :desc:	**Reject** new incoming connection to our TCP server socket if a remote TCP client is already connected (default value).

   * :(attr):
     :val:	xxxx.1xxx
     :desc:	**Always accept** new incoming connection to our TCP server socket.
		This means terminating an exisiting ongoing connection in order to accept the new connection request.

   * :attr:	Bit 4*
     :val:	xxx0.xxxx
     :desc:	Protocol instance **starts** data exchange on |leandcfw| startup (default value)

   * :(attr):
     :val:	xxx1.xxxx
     :desc:	Protocol instance **doesn't** start data exchange on |leandcfw| startup.
		Data exchange will not start automatically, service command (:ref:`xmlelem-IEC10xslDO`.\ :ref:`xmlattr-IEC10xslDOIndex`\ ="-4") can be used to start data exchange at any time.
		Please see :numref:`tabid-IEC10xslDOServiceIndex` for more information on service commands.

   * :attr:	Bit 7
     :val:	0xxx.xxxx
     :desc:	Protocol instance is **enabled** on |leandcfw| startup.
		Communication will start automatically (default value)

   * :(attr):
     :val:	1xxx.xxxx
     :desc:	Protocol instance is **disabled** on |leandcfw| startup.
		Commnication will not start automatically, service command (:ref:`xmlelem-IEC10xslDO`.\ :ref:`xmlattr-IEC10xslDOIndex`\ ="-3") can be used to enable communication at any time.
		Please see :numref:`tabid-IEC10xslDOServiceIndex` for more information on service commands.

   * :attr:	Bits 0...2;5;6
     :val:	Any
     :desc:	Bits reserved for future use

.. tip::

   | \* This bit only applies to the following protocol instances and is used after TCP connection to the station is established:
   | IEC60870-5-104 controlling station (Master) sends or doesn't send [:lemonobgtext:`STARTDT_act`] automatically to the outstation on |leandcfw| startup;
   | IEC61850 Client sends or doesn't send Association Request to the IED on |leandcfw| startup;
