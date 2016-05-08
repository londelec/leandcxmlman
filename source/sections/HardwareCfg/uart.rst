
.. _ref-UART:

UART
^^^^

This node contains settings of a serial port.
.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`<ref-UART>`"

.. code-block:: none

   <UART Index="1" Devpath="/dev/ttyUSB0" Baudrate="9600" DataBits="8" Parity="E" StopBits="1" Timeout="3" TxDelay="0.5" Interface="RS232" CtrlRdTimer="0.5" Test="Echo" Name="COM1"/>


.. _ref-UARTAttributes:

.. include-file:: sections/Include/table_attrs.rstinc "" "Leandc UART node"

   * :attr:     .. _ref-UARTIndex:

                :xmlref:`Index`
     :val:      1...254
     :def:      n/a
     :desc:     Index is a unique identifier of the hardware node. It is used as a reference to link a communication protocol instance to this node. :inlinetip:`Indexes don't have to be in a sequential order.`

   * :attr:     :xmlref:`Devpath`\*
     :val:      Max 100 chars
     :def:      n/a
     :desc:     Path of the UART device in the Linux operating system. All serial ports are normally located in :xmlref:`'/dev'` folder. Inbuilt serial ports have names :xmlref:`'/dev/ttyS0'`; :xmlref:`'/dev/ttyS1'` and USB to Serial adapter ports :xmlref:`'/dev/ttyUSB0'`; :xmlref:`'/dev/ttyUSB0'`; etc Please refer to table :numref:`ref-SerialPortPath` below for standard paths. :inlineimportant:`Attribute is case sensitive, observe the case of path when specifying.`

   * :attr:     :xmlref:`Baudrate`
     :val:      300...115200bps
     :def:      115200
     :desc:     UART baudrate, currently supported values 300; 600; 1200; 2400; 4800; 9600; 19200; 38400; 57600 and 115200 bits per second.

   * :attr:     :xmlref:`DataBits`
     :val:      7 or 8
     :def:      8 bits
     :desc:     UART data bit count 7 or 8. :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:     :xmlref:`Parity`
     :val:      N; E or O
     :def:      Even
     :desc:     UART parity, currently supported N = None; E = Even; O = Odd

   * :attr:     :xmlref:`StopBits`
     :val:      1 or 2
     :def:      1 bit
     :desc:     UART stop bit count 1 or 2. :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:     :xmlref:`Timeout`
     :val:      0.01...42949
     :def:      n/a
     :desc:     Timeout value in seconds. New outgoing message will be sent, if there was no reply from outstation within a configured number of seconds.

   * :attr:     :xmlref:`TxDelay`
     :val:      0.00001...42949
     :def:      n/a
     :desc:     Transmit delay in seconds. Outgoing message will be delayed for a configured number of seconds before being sent after received message. :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be calculated based on configured baudrate.`

   * :attr:     :xmlref:`Interface`
     :val:      | RS232
		| RS485
		| RS422
     :def:      RS232
     :desc:     Type of physical interface. Only applies if hardware supports UART interface selection by software. :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value RS232 will be used if omitted.`

   * :attr:     .. _ref-UARTCtrlRdTimer:

                :xmlref:`CtrlRdTimer`
     :val:      0 or 0.00001...42949
     :def:      0 sec
     :desc:     UART control line (e.g. DSR, RI pin) reading interval in seconds. UART control lines must be stable for at least 8 consequtive read cycles at a configured interval before state change is reported. Default value 0 disables UART control line reading. :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

.. include-file:: sections/Include/hidden_CtrlRdDebounce.rstinc "internal"

   * :attr:     .. _ref-UARTWatchdog:

                :xmlref:`Watchdog`
     :val:      0 or 5...65535
     :def:      0 min
     :desc:     UART watchdog timer in minutes. System will reboot if this UART hasn't received anything within a configured number of minutes. Default value 0 disables watchdog. :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:     :xmlref:`Test`
     :val:      Echo
     :def:      n/a
     :desc:     Attribute enables port testing mode. UART will echo any data received if this attribute is used. There is no need to disable communication protocol or supervision instances linked to UART when testing. Any testing data received will also be recorded to a communication logfile, if logging is enabled for this hardware node. :inlineimportant:`Attribute must not be used if not required, there is no default value.`

.. include-file:: sections/Include/Name.rstinc ""

\* Standard paths of serial ports are listed in the table :numref:`ref-SerialPortPath` below:

.. _ref-SerialPortPath:

.. field-list-table:: Standard serial port path
   :class: table table-condensed table-bordered table-left table-center-all
   :header-rows: 1
   :spec: |C{0.2}|C{0.4}|C{0.4}|

   * :port,10: Port Number
     :hw1,30:  LEANDC-2/3 path :xmlref:`Devpath` attribute
     :hw2,30:  LEANDC-2/5 path :xmlref:`Devpath` attribute
     :hw3,30:  LEIODC path :xmlref:`Devpath` attribute

   * :port:     COM1
     :hw1:      /dev/ttyS0
     :hw2:      /dev/ttyS0
     :hw3:      /dev/ttyAPP0

   * :port:     COM2
     :hw1:      /dev/ttyAP0
     :hw2:      /dev/ttyS1
     :hw3:      /dev/ttyAPP1

   * :port:     COM3
     :hw1:      /dev/ttyAP1
     :hw2:      /dev/ttyS4
     :hw3:      /dev/ttyAPP2

   * :port:     COM4
     :hw1:      /dev/ttyS1 (LEANDC-2/4 only)
     :hw2:      /dev/ttyS5
     :hw3:      /dev/ttyAPP3 (internal)

   * :port:     COM5
     :hw1:      n/a
     :hw2:      /dev/ttyS2
     :hw3:      n/a

