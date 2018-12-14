
.. _ref-UART:

UART
^^^^

This node contains settings of a serial port.
.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`<ref-UART>`"

.. code-block:: none

   <UART Index="1" COM="3" Devpath="/dev/ttyUSB0" Baudrate="9600" DataBits="8" Parity="E" StopBits="1" Timeout="3" TxDelay="0.5" Interface="RS232" CtrlRdTimer="0.5" Test="Echo" Name="COM1"/>


.. _ref-UARTAttributes:

.. include-file:: sections/Include/table_attrs.rstinc "" "Leandc UART node"

   * :attr:     .. _ref-UARTIndex:

		:xmlref:`Index`
     :val:      1...254
     :def:      n/a
     :desc:     Index is a unique identifier of the hardware node.
		It is used as a reference to link a communication protocol instance to this node.
		:inlinetip:`Indexes don't have to be in a sequential order.`

   * :attr:     .. _ref-UARTCOM:

		:xmlref:`COM`

		\*
     :val:	0...16
     :def:	n/a
     :desc:	Serial port number. 
		Number of the inbuilt serial port when running leandc on a supported hardware.
		Please refer to table :numref:`ref-SerialHardwares` below for a list of currently supported hardwares.
		If you are running leandc on a hardware that is not supported or want to use a serial port other than inbuilt (e.g. USB to Serial adapter), please use :xmlref:`COM="0"` and specify path of the UART device in :ref:`<ref-UARTDevpath>` attribute.
		:ref:`<ref-UARTDevpath>` attribute has higher priority and value of :ref:`<ref-UARTCOM>` will be ignored if :ref:`<ref-UARTDevpath>` is used.

   * :attr:     .. _ref-UARTDevpath:

		:xmlref:`Devpath`
     :val:	Max 100 chars
     :def:	n/a
     :desc:	Path of the UART device in the Linux operating system.
		All serial ports can normally be found in '/dev' directory.
		On standard hardwares inbuilt serial ports have names '/dev/ttyS0'; '/dev/ttyS1' and USB to Serial adapter ports '/dev/ttyUSB0'; '/dev/ttyUSB0'; etc
		:inlineimportant:`Attribute is case sensitive, observe the case of path when specifying.`
		:inlinetip:`Attribute is optional, path of the UART device will be resolved automatically from` :ref:`<ref-UARTCOM>` \ :inlinetip:`number, if omitted.`

   * :attr:     :xmlref:`Baudrate`
     :val:      300...115200bps
     :def:      115200
     :desc:     UART baudrate, currently supported values 300; 600; 1200; 2400; 4800; 9600; 19200; 38400; 57600 and 115200 bits per second.

   * :attr:     :xmlref:`DataBits`
     :val:      7 or 8
     :def:      8 bits
     :desc:     UART data bit count 7 or 8.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:     :xmlref:`Parity`
     :val:      N; E or O
     :def:      Even
     :desc:     UART parity, currently supported N = None; E = Even; O = Odd

   * :attr:     :xmlref:`StopBits`
     :val:      1 or 2
     :def:      1 bit
     :desc:     UART stop bit count 1 or 2.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:     :xmlref:`Timeout`
     :val:      0.01...42949
     :def:      n/a
     :desc:     Timeout value in seconds. New outgoing message will be sent, if there was no reply from outstation within a configured number of seconds.

   * :attr:     :xmlref:`TxDelay`
     :val:      0.00001...42949
     :def:      n/a
     :desc:     Transmit delay in seconds. Time interval in seconds between received and sent message.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be calculated based on a configured baudrate.`

   * :attr:     :xmlref:`MaxTxDelay`
     :val:      0 or 0.1...42949
     :def:      0
     :desc:     Dynamic (maximal) transmit delay in seconds. 
		Time interval in seconds between received and sent message in case serial port is used to communicate to only one outstation.
		Transmit delay is automatically adjusted depending on a number of outstations being communicated to via the serial port.
		Disabled stations are excluded from dynamic transmit delay calculation.
		Default value 0 disables dynamic transmit delay feature and :xmlref:`TxDelay` value is used.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration,` :xmlref:`TxDelay` :inlinetip:`value value will be used if omitted.`

   * :attr:     :xmlref:`MaxStations`
     :val:      1...64
     :def:      8
     :desc:     Maximal number of stations for a dynamic transmit delay.
		If a number of outstations exceed the configured value, automatic transmit delay adjustment is disabled and :xmlref:`TxDelay` value is used.
		Disabled stations are excluded from dynamic transmit delay calculation.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:     :xmlref:`Interface`
     :val:      | RS232
		| RS485
		| RS422
     :def:      RS232
     :desc:     Type of physical interface. Only applies if hardware supports UART interface selection by software.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value RS232 will be used if omitted.`

   * :attr:     .. _ref-UARTCtrlRdTimer:

                :xmlref:`CtrlRdTimer`
     :val:      0 or 0.00001...42949
     :def:      0 sec
     :desc:     UART control line (e.g. DSR, RI pin) reading interval in seconds.
		UART control lines must be stable for at least 8 consequtive read cycles at a configured interval before state change is reported.
		Default value 0 disables UART control line reading.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

.. include-file:: sections/Include/hidden_CtrlRdDebounce.rstinc "internal"

   * :attr:     .. _ref-UARTWatchdog:

                :xmlref:`Watchdog`
     :val:      0 or 5...65535
     :def:      0 min
     :desc:     UART watchdog timer in minutes. System will reboot if this UART hasn't received anything within a configured number of minutes.
		Default value 0 disables watchdog.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:     :xmlref:`Test`
     :val:      Echo
     :def:      n/a
     :desc:     Attribute enables port testing mode.
		UART will echo any data received if this attribute is used.
		There is no need to disable communication protocol or supervision instances linked to UART when testing.
		Any testing data received will also be recorded to a communication logfile, if logging is enabled for this hardware node.
		:inlineimportant:`Attribute must not be used if not required, there is no default value.`

.. include-file:: sections/Include/Name.rstinc ""

\* Supported hardwares on which :ref:`<ref-UARTCOM>` attribute can be used are listed in the table :numref:`ref-SerialHardwares` below:

.. _ref-SerialHardwares:

.. field-list-table:: Supported hardwares and serial port numbers
   :class: table table-condensed table-bordered table-left table-center-all
   :header-rows: 1
   :spec: |C{0.2}|C{0.4}|C{0.4}|

   * :hw,11:	Hardware
     :com1,11:	:ref:`<ref-UARTCOM>` = 1
     :com2,11:	:ref:`<ref-UARTCOM>` = 2
     :com3,11:	:ref:`<ref-UARTCOM>` = 3
     :com4,11:	:ref:`<ref-UARTCOM>` = 4
     :com5,11:	:ref:`<ref-UARTCOM>` = 5
     :com6,11:	:ref:`<ref-UARTCOM>` = 6
     :com7,11:	:ref:`<ref-UARTCOM>` = 7
     :com8,11:	:ref:`<ref-UARTCOM>` = 8

   * :hw:	LEANDC-2/3(4) (UNO-1150G)
     :com1:	/dev/ttyS0
     :com2:	/dev/ttyAP0
     :com3:	/dev/ttyAP1
     :com4:	/dev/ttyS1 (LEANDC-2/4 only)
     :com5:	n/a
     :com6:	n/a
     :com7:	n/a
     :com8:	n/a

   * :hw:	LEANDC-2/5 (ARK-3202F)
     :com1:	/dev/ttyS0
     :com2:	/dev/ttyS1
     :com3:	variable
     :com4:	variable
     :com5:	variable
     :com6:	n/a
     :com7:	n/a
     :com8:	n/a

   * :hw:	LEIODC-x
     :com1:	/dev/ttyAPP0
     :com2:	/dev/ttyAPP1
     :com3:	/dev/ttyAPP2
     :com4:	/dev/ttyAPP3 (internal)
     :com5:	n/a
     :com6:	n/a
     :com7:	n/a
     :com8:	n/a

   * :hw:	LEANDC-3/6 (ARK-2120F)
     :com1:	/dev/ttyS0
     :com2:	/dev/ttyS1
     :com3:	variable
     :com4:	variable
     :com5:	variable
     :com6:	variable
     :com7:	n/a
     :com8:	n/a

   * :hw:	LEANDC-3/6 (ARK-3360F)
     :com1:	/dev/ttyS0
     :com2:	/dev/ttyS1
     :com3:	variable
     :com4:	variable
     :com5:	variable
     :com6:	variable
     :com7:	n/a
     :com8:	n/a

   * :hw:	LEANDC-4/8 (UNO-2484F)
     :com1:	/dev/ttyS0
     :com2:	/dev/ttyS1
     :com3:	/dev/ttyS2
     :com4:	/dev/ttyS3
     :com5:	/dev/ttyS4
     :com6:	/dev/ttyS5
     :com7:	/dev/ttyS6
     :com8:	/dev/ttyS7

