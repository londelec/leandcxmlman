
.. _xmlelem-uart:

UART
^^^^

This node contains settings of a serial port.
.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-uart`"

.. code-block:: none

   <UART Index="1" COM="3" Devpath="/dev/ttyUSB0" Baudrate="9600" DataBits="8" Parity="E" StopBits="1" Timeout="3" TxDelay="0.5" MaxTxDelay="4" MaxStations="5" Interface="RS232" CtrlRdTimer="0.5" Watchdog="0" Test="Echo" Name="COM1"/>


.. include-file:: sections/Include/table_attrs.rstinc "" "tabid-Uart" "UART attributes" ":spec: |C{0.14}|C{0.17}|C{0.1}|S{0.59}|"

   * :attr:	:xmlattr:`Index`
     :val:	|hwindexrange|
     :def:	n/a
     :desc:	Index is a unique identifier of the hardware node.
		It is used as a reference to link a communication protocol instance to this node.
		:inlinetip:`Indexes don't have to be in a sequential order.`

   * :attr:	:xmlattr:`COM`

		\*
     :val:	0...16
     :def:	n/a
     :desc:	Serial port number. 
		Number of the inbuilt serial port when running |leandcapp| on a supported hardware.
		Please refer to :numref:`tabid-UartHardwares` below for a list of currently supported hardwares.
		If you are running |leandcapp| on a hardware that is not supported or want to use a serial port other than inbuilt (e.g. USB to Serial adapter), please use :ref:`xmlattr-UARTCOM`\ ="0" and specify path of the UART device in :ref:`xmlattr-UARTDevpath` attribute.
		:ref:`xmlattr-UARTDevpath` attribute has higher priority and value of :ref:`xmlattr-UARTCOM` will be ignored if :ref:`xmlattr-UARTDevpath` is used.

   * :attr:	:xmlattr:`Devpath`
     :val:	Max 100 chars
     :def:	n/a
     :desc:	Path of the UART device in the |linuxos|.
		All serial ports can normally be found in '/dev' directory.
		On standard hardwares inbuilt serial ports have names '/dev/ttyS0'; '/dev/ttyS1' and USB to Serial adapter ports '/dev/ttyUSB0'; '/dev/ttyUSB0'; etc
		:inlineimportant:`Attribute is case sensitive, observe the case of path when specifying.`
		:inlinetip:`Attribute is optional, path of the UART device will be resolved automatically from` :ref:`xmlattr-UARTCOM` \ :inlinetip:`number, if omitted.`

   * :attr:	:xmlattr:`Baudrate`
     :val:	300...115200bps
     :def:	115200
     :desc:	UART baudrate, currently supported values 300; 600; 1200; 2400; 4800; 9600; 19200; 38400; 57600 and 115200 bits per second.

   * :attr:	:xmlattr:`DataBits`
     :val:	7 or 8
     :def:	8 bits
     :desc:	UART data bit count 7 or 8.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:	:xmlattr:`Parity`
     :val:	N; E or O
     :def:	Even
     :desc:	UART parity, currently supported N = None; E = Even; O = Odd

   * :attr:	:xmlattr:`StopBits`
     :val:	1 or 2
     :def:	1 bit
     :desc:	UART stop bit count 1 or 2.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

.. include-file:: sections/Include/chan_Timeout.rstinc "" "n/a" ""

   * :attr:	:xmlattr:`TxDelay`
     :val:	0.00001...42949
     :def:	n/a
     :desc:	Transmit delay in seconds. Time interval in seconds between received and sent message.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be calculated based on a configured baudrate. The default value is calculated as 'TxDelay = 44 / baudrate' e.g. for a baudrate of 9600 the TxDelay is 4.583msec.`

   * :attr:	:xmlattr:`MaxTxDelay`
     :val:	0 or 0.1...42949
     :def:	0
     :desc:	Dynamic (maximal) transmit delay in seconds.
		Time interval in seconds between received and sent message in case serial port is used to communicate to only one outstation.
		Transmit delay is automatically adjusted depending on a number of outstations being communicated to via the serial port.
		Disabled stations are excluded from dynamic transmit delay calculation.
		Default value 0 disables dynamic transmit delay feature and :ref:`xmlattr-UARTTxDelay` value is used.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration,` :ref:`xmlattr-UARTTxDelay` \ :inlinetip:`value value will be used if omitted.`

   * :attr:	:xmlattr:`MaxStations`
     :val:	1...64
     :def:	8
     :desc:	Maximal number of stations for a dynamic transmit delay.
		If a number of outstations exceed the configured value, automatic transmit delay adjustment is disabled and :ref:`xmlattr-UARTTxDelay` value is used.
		Disabled stations are excluded from dynamic transmit delay calculation.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:	:xmlattr:`Interface`
     :val:	| RS232
		| RS485
		| RS422
     :def:	RS232
     :desc:	Type of physical interface. Only applies if hardware supports UART interface selection by software.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value RS232 will be used if omitted.`

   * :attr:	:xmlattr:`CtrlRdTimer`
     :val:	0 or 0.00001...42949
     :def:	0 sec
     :desc:	UART control line (e.g. DSR, RI pin) reading interval in seconds.
		UART control lines must be stable for at least 8 consequtive read cycles at a configured interval before state change is reported.
		Default value 0 disables UART control line reading.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

.. include-file:: sections/Include/hidden_CtrlRdDebounce.rstinc "internal"

   * :attr:	:xmlattr:`Watchdog`
     :val:	0 or 5...65535
     :def:	0 min
     :desc:	UART watchdog timer in minutes. System will reboot if this UART hasn't received anything within a configured number of minutes.
		Default value 0 disables watchdog.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:	:xmlattr:`Test`
     :val:	Echo
     :def:	n/a
     :desc:	Attribute enables port testing mode.
		UART will echo any data received if this attribute is used.
		There is no need to disable communication protocol or supervision instances linked to UART when testing.
		Any testing data received will also be recorded to a communication logfile, if logging is enabled for this hardware node.
		:inlineimportant:`Attribute must not be used if not required, there is no default value.`

.. include-file:: sections/Include/Name.rstinc ""

\* Supported hardwares on which :ref:`xmlattr-UARTCOM` attribute can be used are listed in the :numref:`tabid-UartHardwares` below:

.. field-list-table:: Supported hardwares and serial port numbers
   :class: table table-condensed table-bordered table-left table-center-all
   :name: tabid-UartHardwares
   :header-rows: 1
   :spec: |C{0.14}|C{0.11}|C{0.11}|C{0.11}|C{0.11}|C{0.11}|C{0.11}|C{0.11}|C{0.11}|

   * :hw,11:	Hardware
     :com1,11:	:ref:`xmlattr-UARTCOM` = 1
     :com2,11:	:ref:`xmlattr-UARTCOM` = 2
     :com3,11:	:ref:`xmlattr-UARTCOM` = 3
     :com4,11:	:ref:`xmlattr-UARTCOM` = 4
     :com5,11:	:ref:`xmlattr-UARTCOM` = 5
     :com6,11:	:ref:`xmlattr-UARTCOM` = 6
     :com7,11:	:ref:`xmlattr-UARTCOM` = 7
     :com8,11:	:ref:`xmlattr-UARTCOM` = 8

   * :hw:	UNO-1150G (LEANDC-2/3(4))
     :com1:	/dev/ttyS0
     :com2:	/dev/ttyAP0
     :com3:	/dev/ttyAP1
     :com4:	/dev/ttyS1 (LEANDC-2/4 only)
     :com5:	n/a
     :com6:	n/a
     :com7:	n/a
     :com8:	n/a

   * :hw:	ARK-3202F (LEANDC-2/5)
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

   * :hw:	ARK-2120F (LEANDC-3/6)
     :com1:	/dev/ttyS0
     :com2:	/dev/ttyS1
     :com3:	variable
     :com4:	variable
     :com5:	variable
     :com6:	variable
     :com7:	n/a
     :com8:	n/a

   * :hw:	ARK-3360F
     :com1:	/dev/ttyS0
     :com2:	/dev/ttyS1
     :com3:	variable
     :com4:	variable
     :com5:	variable
     :com6:	variable
     :com7:	n/a
     :com8:	n/a

   * :hw:	UNO-2484F (LEANDC-4/8)
     :com1:	/dev/ttyS0
     :com2:	/dev/ttyS1
     :com3:	/dev/ttyS2
     :com4:	/dev/ttyS3
     :com5:	/dev/ttyS4
     :com6:	/dev/ttyS5
     :com7:	/dev/ttyS6
     :com8:	/dev/ttyS7

   * :hw:	UNO-1372G (LEANDC-4/4)
     :com1:	/dev/ttyS0
     :com2:	/dev/ttyS1
     :com3:	/dev/ttyS2
     :com4:	/dev/ttyS4
     :com5:	n/a
     :com6:	n/a
     :com7:	n/a
     :com8:	n/a

