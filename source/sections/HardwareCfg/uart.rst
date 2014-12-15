
.. _ref-UART:

UART element node
^^^^^^^^^^^^^^^^^   

Settings of the serial ports are configured using :ref:`UART<ref-UART>` element node. Please see sample :ref:`UART<ref-UART>` element node 
and the table listing all available attributes below.

.. code-block:: none

   <UART    Index="1"
            Devpath="/dev/ttyUSB0"
            Baudrate="9600"
            DataBits="8"
            Parity="E"
            StopBits="1"
            Timeout="3"
            TxDelay="0.5"
            CtrlRdTimer="0.5"
            CtrlRdDebounce="8" 
            Name="COM1"/>

.. _ref-UARTAttributes:
      
.. field-list-table:: Leandc UART node
   :class: table table-condensed table-bordered longtable
   :header-rows: 1
   :spec: |C{0.20}|C{0.25}|S{0.55}|

   * :attr,10: Attribute
     :val,15:  Values or range
     :desc,75: Description

   * :attr:    .. _ref-UARTIndex:
   
               :xmlref:`Index`
     :val:     1...254
     :desc:    Index is a unique identifier of the hardware node. It is used as a reference to link a communication protocol instance to this node. :inlinetip:`Indexes don't have to be in a sequential order.`

   * :attr:    :xmlref:`Devpath`\*
     :val:     Max 100 chars
     :desc:    Path of the UART device in the Linux operating system. All serial ports are normally located under :xmlref:`'/dev'` folder. Inbuilt serial ports are referenced as :xmlref:`'/dev/ttyS0'`; :xmlref:`'/dev/ttyS1'` and USB to Serial adapters are referenced as :xmlref:`'/dev/ttyUSB0'`; :xmlref:`'/dev/ttyUSB0'`; etc Please refer to table :numref:`ref-SerialPortPath` below for standard paths. :inlineimportant:`Attribute is case sensitive, observe the case of path when specifying.`

   * :attr:    :xmlref:`Baudrate`
     :val:     300...115200bps
     :desc:    UART baudrate, currently supported values 300; 600; 1200; 2400; 4800; 9600; 19200; 38400; 57600 and 115200 bits per second (default 115200bps)

   * :attr:    :xmlref:`DataBits`
     :val:     7 or 8
     :desc:    UART data bit count 7 or 8 (default 8 bits) :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used is omitted.`

   * :attr:    :xmlref:`Parity`
     :val:     N; E or O
     :desc:    UART parity, currently supported N = None; E = Even; O = Odd (default E = Even)

   * :attr:    :xmlref:`StopBits`
     :val:     1 or 2
     :desc:    UART stop bit count 1 or 2 (default 1 bit) :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used is omitted.`

   * :attr:    :xmlref:`Timeout`
     :val:     0.01...42949
     :desc:    Timeout value in seconds. New outgoing message will be sent, if there was no reply from outstation within a configured number of seconds.

   * :attr:    :xmlref:`TxDelay`
     :val:     0.00001...42949
     :desc:    Transmit delay in seconds. Outgoing message will be delayed for a configured number of seconds before being sent after previously received message. :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be calculated based on configured baudrate.`

   * :attr:    .. _ref-UARTCtrlRdTimer:
       
               :xmlref:`CtrlRdTimer`
     :val:     0 or 0.00001...42949
     :desc:    UART control line (e.g. DSR, RI pin) reading interval in seconds. UART control lines must remain in the same state for least 8 times configured interval before state change will be reported. Default value 0 disables UART control line reading. :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

.. include-file:: sections/Include/UartAttribute_CtrlRdDebounce.rstinc "internal"

   * :attr:    :xmlref:`Name`
     :val:     Max 100 chars
     :desc:    Freely configurable name, just for reference. :inlinetip:`Name attribute is optional and doesn't have to be included in configuration.`
   
\* Standard paths of serial ports are summarized in the table :numref:`ref-SerialPortPath` below:

.. _ref-SerialPortPath:

.. field-list-table:: Standard serial port path
   :class: table table-condensed table-bordered table-left table-center-all
   :header-rows: 1
   :spec: |C{0.2}|C{0.4}|C{0.4}|

   * :attr,20: Port Number
     :val,40:  LEANDC-2/3 path :xmlref:`Devpath` attribute
     :desc,40: LEANDC-2/5 path :xmlref:`Devpath` attribute

   * :attr:    COM1
     :val:     /dev/ttyS0
     :desc:    /dev/ttyS0

   * :attr:    COM2
     :val:     /dev/ttyAP0
     :desc:    /dev/ttyS1

   * :attr:    COM3
     :val:     /dev/ttyAP1
     :desc:    /dev/ttyS4

   * :attr:    COM4
     :val:     n/a
     :desc:    /dev/ttyS5

   * :attr:    COM5
     :val:     n/a
     :desc:    /dev/ttyS2
     