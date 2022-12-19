.. include:: global.roles

.. _xmlgroup-MainConfig: lelabel=MainConfig

System configuration
====================

Configuration file |leandcxml|
------------------------------

XML configuration file |leandcxml| contains main settings of the |leandcapp| and it is the first file loaded on startup.
The name of the file is fixed and it must be stored in the default application directory |leandcdir| .
If |leandcxml| file is not found on startup, application terminates with an error message indicating the cause.

|leandcxml| configuration file consists of a root node :ref:`xmlgroup-MainConfig` which has 3 mandatory groups
:ref:`xmlelem-VersionControl`; :ref:`xmlgroup-HardwareCfg` and :ref:`xmlgroup-CommunicationCfg` and 4 optional groups
:ref:`xmlgroup-TraceCfg`; :ref:`xmlgroup-clientfilter`; :ref:`xmlgroup-SupervisionCfg` and :ref:`xmlgroup-InternalCfg`, please see the sample below.

.. code-block:: none

 <MainConfig xmlns="http://www.londelec.com/xmlschemas/leandc/main" … version="1.00">
   <VersionControl conf="4.00" date="2022-05-31" time="10:08:09"/>
   <HardwareCfg>
     <UART Index="1" COM="1" Baudrate="9600" DataBits="8" Parity="E" … />
            …
   </HardwareCfg>
   <CommunicationCfg>
     <IEC101ma Index="10" HWIndex="100" XMLpath="IEC101ma_test.xml" LinkAddr="1"/>
            …
   </CommunicationCfg>
   <TraceCfg>
     <SYSLOGFILE LogFlags="0x00" Mode="0" HourLimit="0" Logfile="Syslog/syslog"/>
            …
   </TraceCfg>
   <ClientFilterCfg>
     <IPv4 FilterID="1" ClientIPaddr="10.19.0.21" Mask="32"/>
            …
   </ClientFilterCfg>
   <SupervisionCfg>
     <MONRAW SrcHWIndex="11" DstHWIndex="10" SrvHWIndex="9"/>
            …
   </SupervisionCfg>
   <InternalCfg>
     <PLC Index="99" XMLpath="myplc.xml"/>
   </InternalCfg>
 </MainConfig>

.. _xmlgroup-HardwareCfg: lelabel=HardwareCfg

HardwareCfg group
-----------------

:ref:`xmlgroup-HardwareCfg` group contains definitions of physical interfaces such as serial ports and network sockets.
The following elements are available to define physical interfaces (e.g. Serial ports) or sockets (e.g. TCP server) required for communication:
:ref:`xmlelem-uart`; :ref:`xmlelem-tcpserver`; :ref:`xmlelem-tcpclient` and :ref:`xmlelem-udp`.
Attributes of these elements contain interface's settings.
:ref:`xmlgroup-HardwareCfg` group can have multiple child elements as shown in the sample below.

.. code-block:: none

   <HardwareCfg>
	<UART Index="1" Devpath="/dev/ttyUSB0" Baudrate="9600" … />
	<UART Index="2" Devpath="/dev/ttyUSB1" Baudrate="9600" … />
	<TCPSERVER Index="33" ServerIPaddr="127.0.0.1" Port="2404" … />
	<TCPCLIENT Index="44" ServerIPaddr="127.0.0.1" Port="2404" … />
	<UDP Index="55" RemoteIPaddr="127.0.0.1" RemotePort="64950" … />
   </HardwareCfg>

.. important::
   | There must be one and only one :ref:`xmlgroup-HardwareCfg` group in the root node :ref:`xmlgroup-MainConfig`.
   | Hardware interfaces defined in the :ref:`xmlgroup-HardwareCfg` group must be arranged in the following order:

   | :ref:`xmlelem-uart`
   | :ref:`xmlelem-tcpserver`
   | :ref:`xmlelem-tcpclient`
   | :ref:`xmlelem-udp`

.. include:: HardwareCfg/uart.rst
.. include:: HardwareCfg/tcpServer.rst
.. include:: HardwareCfg/tcpClient.rst
.. include:: HardwareCfg/udp.rst

.. _xmlgroup-CommunicationCfg: lelabel=CommunicationCfg

CommunicationCfg group
----------------------

:ref:`xmlgroup-CommunicationCfg` group is used to initialize communication protocol instances and link them to physical hardware interfaces.
|leandcapp| is able to receive data from downstream outstations using various communication protocols,
process the received information and report it upstream to SCADA our any other data acquisition entity.
Every logical communication link to outstation or upstream station has a definition 'communication protocol instance' within this manual.
It represents communication channel for receiving or sending the data.
Communication protocol instances are defined in :ref:`xmlgroup-CommunicationCfg` group,
please refer to the sample below containing 4 different communication protocols (instances).

.. code-block:: none

   <CommunicationCfg>
	<IEC101ma Index="10" HWIndex="2" XMLpath="IEC101ma_test.xml" CommsFlags="0x10"/>
	<IEC101sl Index="5" HWIndex="1" XMLpath="IEC101sl_test.xml"/>
	<IEC104sl Index="12" HWIndex="3" XMLpath="IEC104ma_test.xml" FilterID="2"/>
	<IEC104Rsl Index="13" HWIndex="3" RedundantToIndex="12" FilterID="3"/>
   </CommunicationCfg>

.. important::
   | There must be one and only one :ref:`xmlgroup-CommunicationCfg` group in the root node :ref:`xmlgroup-MainConfig`.
   | Communication protocol instances defined in the :ref:`xmlgroup-CommunicationCfg` group must be arranged in the following order:

   | :ref:`xmlelem-gpmodbusma`
   | :ref:`xmlelem-gpspabusma`
   | :ref:`xmlelem-gp61850cl`
   | :ref:`xmlelem-gp101ma`
   | :ref:`xmlelem-gp101sl`
   | :ref:`xmlelem-gp103ma`
   | :ref:`xmlelem-gp104ma`
   | :ref:`xmlelem-gp104sl`
   | :ref:`xmlelem-gp104rsl`
   | :ref:`xmlelem-gp104csl`

Every communication protocol instance has a unique element and settings are described in the following sections.

.. include:: communicationCfg/modbusma.rst
.. include:: communicationCfg/spabusma.rst
.. include:: communicationCfg/iec61850cl.rst
.. include:: communicationCfg/iec101ma.rst
.. include:: communicationCfg/iec101sl.rst
.. include:: communicationCfg/iec103ma.rst
.. include:: communicationCfg/iec104ma.rst
.. include:: communicationCfg/iec104sl.rst
.. include:: communicationCfg/iec104Rsl.rst
.. include:: communicationCfg/iec104Csl.rst
.. include:: communicationCfg/commsFlags.rst

.. _xmlgroup-TraceCfg: lelabel=TraceCfg

TraceCfg group
--------------

Generic diagnostic information and error messages can be recorded to a system logfile.
:ref:`xmlgroup-TraceCfg` group and its child element :ref:`xmlelem-syslogfile` contains settings to enable the system-wide logfile.
:ref:`xmlelem-logsettings` contains common settings that apply to all logfiles.
:ref:`xmlgroup-TraceCfg` may contain only one :ref:`xmlelem-syslogfile` and one :ref:`xmlelem-logsettings` element as shown in the sample below.

.. code-block:: none

   <TraceCfg>
	<SYSLOGFILE LogFlags="0" Logfile="Syslog/syslog" Mode="0" HourLimit="4" TimeZone="UTC"/>
	<Settings CleanOlder="60" MinFreespace="5.5"/>
   </TraceCfg>

.. _xmlelem-syslogfile:

SYSLOGFILE
^^^^^^^^^^

This element contains settings of a system-wide logfile.
.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-syslogfile`"

.. code-block:: none

   <SYSLOGFILE LogFlags="0" Logfile="Syslog/syslog" Mode="0" HourLimit="4" TimeZone="UTC"/>


.. include-file:: sections/Include/table_attrs.rstinc "" "tabid-syslogfile" "SYSLOGFILE attributes" ":spec: |C{0.14}|C{0.12}|C{0.1}|S{0.64}|"

   * :attr:	:xmlattr:`LogFlags`
     :val:	|flags8range|
     :def:	0x00
     :desc:	Select type of system messages to be logged. See :numref:`tabid-syslogfileLogFlags` for description. Logfile will not be created if the value is 0.

.. include-file:: sections/Include/log_Logfile.rstinc "" ".log" "(default value 'Syslog/syslog' where 'Syslog' is the name of the directory and 'syslog' is the name of the file)"

.. include-file:: sections/Include/log_ModeHourLimit.rstinc "" "0x00" "0" "(default 0 – only 1 logfile a day will be created)"

.. include-file:: sections/Include/log_TimeZone.rstinc ""

.. include-file:: sections/Include/hidden_LogDebugFlags.rstinc "internal" ":numref:`tabid-syslogfileDebugFlags`"

.. tip:: \* There are few samples on how files are created with various :ref:`xmlattr-syslogfileMode` \ and :ref:`xmlattr-syslogfileHourLimit` \ attribute settings in section :ref:`docref-LogfileSampleList`.


.. include-file:: sections/Include/table_flags8.rstinc "" "tabid-syslogfileLogFlags" "System logfile flags" ":ref:`xmlattr-syslogfileLogFlags`" "Logger flags"
		Logfile will not be created if the value is 0.

   * :attr:	Bit 0
     :val:	xxxx.xxx0
     :desc:	Error message recording to logfile **disabled**

   * :(attr):
     :val:	xxxx.xxx1
     :desc:	Error message recording to logfile **enabled**

   * :attr:	Bit 1
     :val:	xxxx.xx0x
     :desc:	Warning message recording to logfile **disabled**

   * :(attr):
     :val:	xxxx.xx1x
     :desc:	Warning message recording to logfile **enabled**

   * :attr:	Bit 2
     :val:	xxxx.x0xx
     :desc:	Information message recording to logfile **disabled**

   * :(attr):
     :val:	xxxx.x1xx
     :desc:	Information message recording to logfile **enabled**

   * :attr:	Bits 3...7
     :val:	Any
     :desc:	Bits reserved for future use


.. include-file:: sections/Include/hidden_LogDebugFlagTable.rstinc "internal" "tabid-syslogfileDebugFlags" ":ref:`xmlattr-syslogfileDebugFlags`"

.. _xmlelem-logsettings:

Settings
^^^^^^^^

This element contains common settings that apply to all logfiles.
.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-logsettings`"

.. code-block:: none

   <Settings CleanOlder="60" MinFreespace="5.5"/>


.. include-file:: sections/Include/table_attrs.rstinc "" "tabid-LogSettings" "Log Settings attributes" ":spec: |C{0.16}|C{0.12}|C{0.1}|S{0.62}|"

   * :attr:	:xmlattr:`CleanOlder`
     :val:	0...255
     :def:	60 days
     :desc:	Remove logfiles which are older than specified number of days.
		Value 0 disables automatic cleanup functionality.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:	:xmlattr:`MinFreespace`
     :val:	0...100
     :def:	2%
     :desc:	Minimal hard drive free space required to record logfiles in percent.
		Logfiles will not be recoreded if available space is less than specified percentage.
		Value 0 disables free space checking and logfiles are recorded until hard drive is full.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`


.. _xmlgroup-clientfilter: lelabel=ClientFilterCfg
.. _xmlelem-filterIPv4: lelabel=IPv4

ClientFilterCfg group
---------------------

:ref:`xmlgroup-clientfilter` group and its child element :ref:`xmlelem-filterIPv4` are used to create filters for
remote 'Client' IP address which are allowed to connect to our TCP Server sockets.
.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-filterIPv4`"

.. code-block:: none

   <ClientFilterCfg>
	<IPv4 FilterID="1" ClientIPaddr="192.168.2.14" Mask="32" Name="Only specified IP address"/>
	<IPv4 FilterID="1" ClientIPaddr="192.168.2.55" Mask="32" Name="Only specified IP address"/>
	<IPv4 FilterID="2" ClientIPaddr="192.168.5.0" Mask="24" Name="IP address range"/>
   </ClientFilterCfg>

There are 3 :ref:`xmlelem-filterIPv4` filters configured in the example above.
Please note 2 :ref:`xmlelem-filterIPv4` nodes have the same filter identifier "1".
This will allow clients from either IP address 192.168.2.14 or 192.168.2.55 to connect.


.. include-file:: sections/Include/table_attrs.rstinc "" "tabid-filterIPv4" "IPv4 Client filter attributes" ":spec: |C{0.14}|C{0.17}|C{0.1}|S{0.59}|"

   * :attr:	:xmlattr:`FilterID`
     :val:	|filteridrange|
     :def:	n/a
     :desc:	Filter identifier.
		More than one filter may have the same identifier which enables to define multiple addresses or address ranges.
		In order to apply the filter, use this identifier in communication protocol instance attributes :ref:`xmlelem-gp104sl`.\ :ref:`xmlattr-gp104slFilterID`\; :ref:`xmlelem-gp104Rsl`.\ :ref:`xmlattr-gp104RslFilterID` \ or :ref:`xmlelem-gp104Csl`.\ :ref:`xmlattr-gp104CslFilterID`\.

   * :attr:	:xmlattr:`ClientIPaddr`
     :val:	0.0.0.0 ... 255.255.255.255
     :def:	n/a
     :desc:	IPv4 TCP client IP address allowed to connect.
		It is possible to define a network subnet and all IP addresses of the subnet will be able to connect.
		Please refer to :ref:`xmlattr-filterIPv4Mask` attribute for network subnet configuration.
		(address 0.0.0.0 can be used to allow connection from any IP address)

   * :attr:	:xmlattr:`Mask`
     :val:	0...32
     :def:	32
     :desc:	Network mask is used in conjunction with :ref:`xmlattr-filterIPv4ClientIPaddr` attribute in order to create a network subnet.
		All IP addresses of the subnet will be able to connect.
		Network mask attribute is a decimal notation of the subnet mask, sometimes called network prefix, refer to :numref:`tabid-NetworkMask` for more information.
		(Mask 0 will allow connection from any IP address; mask 32 will allow connection only from one IP address specified in :ref:`xmlattr-filterIPv4ClientIPaddr` attribute)

.. include-file:: sections/Include/Name.rstinc ""

Network subnets created by various :ref:`xmlattr-filterIPv4Mask` attribute values are summarized in the table below.
It is assumed user has a good understanding of network addressing fundamentals.
Please refer to external sources (e.g. http://www.subnet-calculator.com) for additional information on network addressing and subnet definition.

.. include-html:: ../_html/netcalc.html
   :latex-tip: Interactive network mask calculator can be found in the current HTML manual

| Table columns are defined as follows:
| Column 1 contains :ref:`xmlattr-filterIPv4Mask` attribute values;
| Column 2 contains subnet mask in dotted decimal notation;
| Columns 3...6 show network mask in binary notation (just for reference);
| Column 7 contains range of client IP address allowed to connect.

Table is designed as a guidance of how network subnets are created based on sample IP address 192.168.1.1 specified in the :ref:`xmlattr-filterIPv4ClientIPaddr` attribute.


.. field-list-table:: Network Mask sample values
   :class: table table-condensed table-bordered longtable
   :name: tabid-NetworkMask
   :spec: |C{0.1}|C{0.2}|C{0.1}|C{0.1}|C{0.1}|C{0.1}|C{0.3}|
   :definition-row: 1
   :header-rows: 1

   * :mask,10,center:
     :subnet,20,center:
     :bval1,10,center:
     :bval2,10,center:
     :bval3,10,center:
     :bval4,10,center:
     :iprange,30:

   * :mask:          Mask
     :subnet:        Subnet mask
     :bval1..bval4:  Subnet mask binary value
     :iprange:       IP range allowed to connect

   * :mask:          0
     :subnet:        0.0.0.0
     :bval1:         0000 0000
     :bval2:         0000 0000
     :bval3:         0000 0000
     :bval4:         0000 0000
     :iprange:       Mask off – any client IPv4 address allowed

   * :mask:          1
     :subnet:        128.0.0.0
     :bval1:         1000 0000
     :bval2:         0000 0000
     :bval3:         0000 0000
     :bval4:         0000 0000
     :iprange:       128.0.0.0 to 255.255.255.255

   * :mask:          2
     :subnet:        192.0.0.0
     :bval1:         1100 0000
     :bval2:         0000 0000
     :bval3:         0000 0000
     :bval4:         0000 0000
     :iprange:       192.0.0.0 to 255.255.255.255

   * :mask:          3
     :subnet:        224.0.0.0
     :bval1:         1110 0000
     :bval2:         0000 0000
     :bval3:         0000 0000
     :bval4:         0000 0000
     :iprange:       192.0.0.0 to 223.255.255.255

   * :mask:          ...
     :subnet:
     :bval1:
     :bval2:
     :bval3:
     :bval4:
     :iprange:

   * :mask:          24
     :subnet:        255.255.255.0
     :bval1:         1111 1111
     :bval2:         1111 1111
     :bval3:         1111 1111
     :bval4:         0000 0000
     :iprange:       192.168.1.0 to 192.168.1.255

   * :mask:          25
     :subnet:        255.255.255.128
     :bval1:         1111 1111
     :bval2:         1111 1111
     :bval3:         1111 1111
     :bval4:         1000 0000
     :iprange:       192.168.1.0 to 192.168.1.127

   * :mask:          26
     :subnet:        255.255.255.192
     :bval1:         1111 1111
     :bval2:         1111 1111
     :bval3:         1111 1111
     :bval4:         1100 0000
     :iprange:       192.168.1.0 to 192.168.1.63

   * :mask:          27
     :subnet:        255.255.255.224
     :bval1:         1111 1111
     :bval2:         1111 1111
     :bval3:         1111 1111
     :bval4:         1110 0000
     :iprange:       192.168.1.0 to 192.168.1.31

   * :mask:          28
     :subnet:        255.255.255.240
     :bval1:         1111 1111
     :bval2:         1111 1111
     :bval3:         1111 1111
     :bval4:         1111 0000
     :iprange:       192.168.1.0 to 192.168.1.15

   * :mask:          29
     :subnet:        255.255.255.248
     :bval1:         1111 1111
     :bval2:         1111 1111
     :bval3:         1111 1111
     :bval4:         1111 1000
     :iprange:       192.168.1.0 to 192.168.1.7

   * :mask:          30
     :subnet:        255.255.255.252
     :bval1:         1111 1111
     :bval2:         1111 1111
     :bval3:         1111 1111
     :bval4:         1111 1100
     :iprange:       192.168.1.0 to 192.168.1.3

   * :mask:          31
     :subnet:        255.255.255.254
     :bval1:         1111 1111
     :bval2:         1111 1111
     :bval3:         1111 1111
     :bval4:         1111 1110
     :iprange:       192.168.1.0 to 192.168.1.1

   * :mask:          32
     :subnet:        255.255.255.255
     :bval1:         1111 1111
     :bval2:         1111 1111
     :bval3:         1111 1111
     :bval4:         1111 1111
     :iprange:       Only 192.168.1.1 allowed to connect


.. _xmlgroup-SupervisionCfg: lelabel=SupervisionCfg

SupervisionCfg group
--------------------

:ref:`xmlgroup-SupervisionCfg` group is used to enable real-time monitoring of the serial port or socket traffic
and also provides serial server functionality. Real-time traffic monitoring and serial server functionality has
designated supervision instances which are configured under :ref:`xmlgroup-SupervisionCfg` group, please refer to the
sample below containing 4 different supervision instances.

.. code-block:: none

 <SupervisionCfg>
   <MONRAW SrcHWIndex="1" DstHWIndex="51" Name="Raw monitoring instance"/>
   <MONCOMP SrcHWIndex="2" DstHWIndex="52" SrvHWIndex="53" Name="Compatible mon instance"/>
   <REDIRECT SrcHWIndex="4" DstHWIndex="61" Name="UART redirect instance"/>
   <OVERRIDE SrcHWIndex="3" DstHWIndex="62" SrvHWIndex="63" Name="UART override instance"/>
 </SupervisionCfg>

Every supervision instance has a unique element and its configuration is described in the following sections.

.. important::
   | Supervision instances must be listed under :ref:`xmlgroup-SupervisionCfg` group in the following order:

   | :ref:`xmlelem-monraw`
   | :ref:`xmlelem-moncomp`
   | :ref:`xmlelem-redirect`
   | :ref:`xmlelem-override`

.. include:: supervisionCfg/monraw.rst
.. include:: supervisionCfg/moncomp.rst
.. include:: supervisionCfg/redirect.rst
.. include:: supervisionCfg/override.rst


.. _xmlgroup-InternalCfg: lelabel=InternalCfg

InternalCfg group
-----------------

:ref:`xmlgroup-InternalCfg` group is used to enable internal data processing.
This includes performing logic operations such as 'OR' and 'AND' - a simplified PLC functionality.
At the moment :ref:`xmlgroup-InternalCfg` group can have only one element :ref:`xmlelem-gpplc` and its configuration is described in the following section.
More elements will be added in the future.
Please refer to the sample below containing a :ref:`xmlelem-gpplc` instance.

.. code-block:: none

 <InternalCfg>
   <PLC Index="99" XMLpath="myplc.xml"/>
 </InternalCfg>

.. important:: Only one :ref:`xmlelem-gpplc` element can be defined in :ref:`xmlgroup-InternalCfg` group.


.. include:: internalCfg/plc.rst
