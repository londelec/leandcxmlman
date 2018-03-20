.. include:: global.roles

System configuration
====================

Configuration file **leandc.xml**
---------------------------------

XML configuration file **leandc.xml** contains overall system settings of the leandc firmware and it is the first file
loaded upon system startup. The configuration file name is fixed, it must be stored in the same directory as
leandc firmware and its path can't be changed. If 'leandc.xml' file is not found upon leandc firmware startup,
firmware terminates with an error message indicating the cause of fail.

**leandc.xml** configuration file consists of a root object node :xmlref:`MainConfig` which has 3 mandatory child group
object nodes :ref:`VersionControl<ref-VersionControl>`; :ref:`HardwareCfg<ref-HardwareCfg>` and :ref:`CommunicationCfg<ref-CommunicationCfg>` and 3 optional child group object nodes
:ref:`TraceCfg<ref-TraceCfg>` and :ref:`ClientFilterCfg<ref-ClientFilterCfg>` and :ref:`SupervisionCfg<ref-SupervisionCfg>`, please see the sample below.

.. tip:: Node names are not case sensitive.

.. code-block:: none

   <MainConfig  xmlns="http://www.londelec.com/xmlschemas/leandc/main" … version="2.00">
         <VersionControl conf="4" date="2014-01-18" time="10:08:09"/>
         <HardwareCfg>
            <UART Index="1" Devpath="/dev/ttyS0" Baudrate="9600" DataBits="8" Parity="E" … />
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
   </MainConfig>

.. _ref-HardwareCfg:

HardwareCfg group node
----------------------

:ref:`HardwareCfg<ref-HardwareCfg>` group node contains definitions of physical interfaces such as serial ports and network sockets.
Following XML element nodes are available to define physical interfaces (e.g. Serial ports) or sockets (e.g. TCP server) required for communication:
:ref:`<ref-UART>`; :ref:`<ref-TCPSERVER>`; :ref:`<ref-TCPCLIENT>` and :ref:`<ref-UDP>`.
Attributes of these nodes contain interface's settings.
:ref:`HardwareCfg<ref-HardwareCfg>` group can have multiple child element nodes as shown in the sample below.

.. code-block:: none

   <HardwareCfg>
	<UART Index="1" Devpath="/dev/ttyUSB0" Baudrate="9600"... />
	<UART Index="2" Devpath="/dev/ttyUSB1" Baudrate="9600"... />
	<TCPSERVER Index="33" ServerIPaddr="127.0.0.1" Port="2404"... />
	<TCPCLIENT Index="44" ServerIPaddr="127.0.0.1" Port="2404"... />
	<UDP Index="55" RemoteIPaddr="127.0.0.1" RemotePort="64950"... />
   </HardwareCfg>

.. important::
   | There must be one and only one :ref:`HardwareCfg<ref-HardwareCfg>` group in the root node :xmlref:`MainConfig`.
   | Hardware interfaces defined in the :ref:`HardwareCfg<ref-HardwareCfg>` group must be arranged in the following order:

   | :ref:`<ref-UART>`
   | :ref:`<ref-TCPSERVER>`
   | :ref:`<ref-TCPCLIENT>`
   | :ref:`<ref-UDP>`

.. include:: HardwareCfg/uart.rst
.. include:: HardwareCfg/tcpServer.rst
.. include:: HardwareCfg/tcpClient.rst
.. include:: HardwareCfg/udp.rst

.. _ref-CommunicationCfg:

CommunicationCfg group node
---------------------------

:ref:`CommunicationCfg<ref-CommunicationCfg>` node is used to initialize communication protocol instances and link to physical hardware
interface. Leandc firmware is able to receive data from downstream outstations via various communication
protocols, process the received information and report it upstream to SCADA system our any other data
acquisition unit. Every logical communication link to outstation or upstream Master station has a definition
'communication protocol instance' within this manual and leandc firmware. It represents communication channel
for receiving or sending the data to/from leandc. Communication protocol instances have to be configured under
:ref:`CommunicationCfg<ref-CommunicationCfg>` node, please refer to the sample below containing 4 different communication protocols
(instances).

.. code-block:: none

   <CommunicationCfg>
	<IEC101ma Index="10" HWIndex="2" XMLpath="IEC101ma_test.xml" CommsFlags="0x10"/>
	<IEC101sl Index="5" HWIndex="1" XMLpath="IEC101sl_test.xml"/>
	<IEC104sl Index="12" HWIndex="3" XMLpath="IEC104ma_test.xml" FilterID="2"/>
	<IEC104Rsl Index="13" HWIndex="3" RedundantToIndex="12" FilterID="3"/>
   </CommunicationCfg>

.. important::
   | There must be one and only one :ref:`CommunicationCfg<ref-CommunicationCfg>` group in the root object node :xmlref:`MainConfig`.
   | Communication protocol instances defined in the :ref:`CommunicationCfg<ref-CommunicationCfg>` group must be arranged in the following order:

   | :ref:`<ref-Modbusma>`
   | :ref:`<ref-IEC61850cl>`
   | :ref:`<ref-IEC101ma>`
   | :ref:`<ref-IEC101sl>`
   | :ref:`<ref-IEC103ma>`
   | :ref:`<ref-IEC104ma>`
   | :ref:`<ref-IEC104sl>`
   | :ref:`<ref-IEC104Rsl>`
   | :ref:`<ref-IEC104Csl>`

Every communication protocol instance has a unique element node and settings are described in the following paragraphs.

.. include:: communicationCfg/modbusma.rst
.. include:: communicationCfg/iec61850cl.rst
.. include:: communicationCfg/iec101ma.rst
.. include:: communicationCfg/iec101sl.rst
.. include:: communicationCfg/iec103ma.rst
.. include:: communicationCfg/iec104ma.rst
.. include:: communicationCfg/iec104sl.rst
.. include:: communicationCfg/iec104Rsl.rst
.. include:: communicationCfg/iec104Csl.rst
.. include:: communicationCfg/commsFlags.rst

.. _ref-TraceCfg:

TraceCfg group
--------------

Generic diagnostic information and error messages can be recorded to a system logfile.
Group object node :xmlref:`TraceCfg` and its child element node :xmlref:`SYSLOGFILE` contains settings to enable the system-wide logfile.
:xmlref:`Settings` node contains common settings for all logfiles.
:xmlref:`TraceCfg` may contain only one :xmlref:`SYSLOGFILE` and one :xmlref:`Settings` element node as shown in the sample below.

.. code-block:: none

   <TraceCfg>
	<SYSLOGFILE LogFlags="0" Logfile="Syslog/syslog" Mode="0" HourLimit="4" TimeZone="UTC"/>
	<Settings CleanOlder="60" MinFreespace="5.5"/>
   </TraceCfg>

.. _ref-SYSLOGFILE:

SYSLOGFILE
^^^^^^^^^^

This node contains settings of a system-wide logfile.
.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`<ref-SYSLOGFILE>`"

.. code-block:: none

   <SYSLOGFILE LogFlags="0" Logfile="Syslog/syslog" Mode="0" HourLimit="4" TimeZone="UTC"/>


.. _docref-SYSLOGFILEAttab:

.. include-file:: sections/Include/table_attrs.rstinc "" "SYSLOGFILE attributes"

   * :attr:     :xmlref:`LogFlags`
     :val:      0...255 or 0x00...0xFF
     :def:	0x00
     :desc:     Select type of system messages to be logged. See table :numref:`docref-SYSLOGFILELogFlagsAttab` for description. Logfile will not be created if the value is 0.

   * :attr:     :xmlref:`Logfile`
     :val:      Max 200 chars
     :def:      Syslog/syslog
     :desc:     Name of a logfile excluding extension (e.g. '.log').
		It is possible to specify relative or absolute path as part of the file name.
		Logfile will be created in the default home folder (e.g. '/home/leandc/app') if path is not specified.
		Date when the file was created and extension '.log' will be appended to the file name automatically.
		Logfile will not be created if this attribute is left blank.
		(default value 'Syslog/syslog' where 'Syslog' is the name of the folder and 'syslog' is the name of the file)
		:inlineimportant:`Attribute is case sensitive, observe the case of the path and name of the file when specifying.`

   * :attr:     .. _ref-SYSLOGFILEMode:

                :xmlref:`Mode`\*
     :val:      0...255 or 0x00...0xFF
     :def:	0x00
     :desc:     Logfile initialization settings. See table :numref:`docref-LoggerModeBits` for description. :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:     .. _ref-SYSLOGFILEHourLimit:

                :xmlref:`HourLimit`\*
     :val:      0...12
     :def:	0 hours
     :desc:     Option to create a new file after selected number of hours in order to limit the size of the file.
		(default 0 – only 1 logfile per day will be created)
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:     :xmlref:`TimeZone`
     :val:      Max 200 chars
     :def:	n/a
     :desc:     Adjust time-tags of the recorded information based on the specified time zone.
		:inlineimportant:`Attribute must not be used if not required, there is no default value. Time-tags will not be adjusted if attribute omitted.`
		:inlinetip:`Please see` :ref:`docref-TimeZoneSpecification` :inlinetip:`for additional information.`

.. include-file:: sections/Include/hidden_LogDebugFlags.rstinc "internal" ":numref:`docref-LOGGERDebugFlagsAttab`"

.. tip:: \* There are few samples on how files are created with various :ref:`Mode<ref-SYSLOGFILEMode>` \ and :ref:`HourLimit<ref-SYSLOGFILEHourLimit>` \ attribute settings in section :ref:`docref-LogfileSampleList`.

.. _docref-SYSLOGFILELogFlagsAttab:

.. include-file:: sections/Include/table_flags.rstinc "" "System logfile flags" ":xmlref:`LogFlags`" "Logger flags"
		Logfile will not be created, if the value is 0.

   * :attr:     Bit 0
     :val:      xxxx.xxx0
     :desc:     System information recording to logfile **disabled**

   * :(attr):
     :val:      xxxx.xxx1
     :desc:     System information recording to logfile **enabled**

.. include-file:: sections/Include/hidden_SyslogFlagsBit1.rstinc "internal"

   * :attr:     Bits 1...7
     :val:      Any
     :desc:     Bits reserved for future use

.. include-file:: sections/Include/hidden_LogDebugFlagTable.rstinc "internal" ".. _docref-LOGGERDebugFlagsAttab:"

.. _ref-LogSettings:

Settings
^^^^^^^^

This node contains common settings for all logfiles.
.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`<ref-LogSettings>`"

.. code-block:: none

   <Settings CleanOlder="60" MinFreespace="5.5"/>

.. _docref-LogSettingsAttab:

.. include-file:: sections/Include/table_attrs.rstinc "" "Log Settings attributes"

   * :attr:     .. _ref-SettingsCleanOlder:

  		:xmlref:`CleanOlder`
     :val:      0...255
     :def:	60 days
     :desc:     Remove logfiles which are older than specified number of days.
		Value 0 disables automatic cleanup functionality.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:     .. _ref-SettingsMinFreespace:

		:xmlref:`MinFreespace`
     :val:      0...100
     :def:	2%
     :desc:     Minimal hard drive free space required to record logfiles in percent.
		Logfiles will not be recoreded if available space is less than specified percentage.
		Value 0 disables free space checking and logfiles are recorded until hard drive is full.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`


.. _ref-ClientFilterCfg:

ClientFilterCfg group and IPv4 node
-----------------------------------

Group object node :xmlref:`ClientFilterCfg` and its child element nodes :xmlref:`IPv4` are used to create filters for
remote 'Client' IP address which are allowed to connect to leandc.
.. include-file:: sections/Include/sample_node.rstinc "" ":xmlref:`IPv4`"

.. code-block:: none

   <ClientFilterCfg>
	<IPv4 FilterID="1" ClientIPaddr="192.168.2.14" Mask="32" Name="Only specified IP address"/>
	<IPv4 FilterID="1" ClientIPaddr="192.168.2.55" Mask="32" Name="Only specified IP address"/>
	<IPv4 FilterID="2" ClientIPaddr="192.168.5.0" Mask="24" Name="IP address range"/>
   </ClientFilterCfg>

There are 3 :xmlref:`IPv4` filter nodes configured in the example above.
Please note 2 :xmlref:`IPv4` nodes have the same filter identifier "1".
This will allow clients from either IP address 192.168.2.14 or 192.168.2.55 to connect.

.. _docref-ClientFilterCfgIPv4Attab:

.. include-file:: sections/Include/table_attrs.rstinc "" "IPv4 Client filter attributes"

   * :attr:     :xmlref:`FilterID`
     :val:      1...255
     :def:      n/a
     :desc:     Filter identifier.
		More than one filter may have the same identifier which enables to define multiple addresses or address ranges.
		In order to apply the filter, use this identifier in communication protocol instance attributes :ref:`<ref-IEC104sl>`.\ :ref:`<ref-IEC104slFilterID>`\; :ref:`<ref-IEC104Rsl>`.\ :ref:`<ref-IEC104RslFilterID>` \ or :ref:`<ref-IEC104Csl>`.\ :ref:`<ref-IEC104CslFilterID>`\.

   * :attr:     .. _ref-ClientFilterCfgIpv4ClientIPaddr:

                :xmlref:`ClientIPaddr`
     :val:      0.0.0.0 ... 255.255.255.255
     :def:      n/a
     :desc:     IPv4 TCP client IP address allowed to connect.
		It is possible to define a network subnet and all IP addresses of the subnet will be able to connect.
		Please refer to :ref:`<ref-ClientFilterCfgIpv4Mask>` attribute for network subnet configuration.
		(address 0.0.0.0 can be used to allow connection from any IP address)

   * :attr:     .. _ref-ClientFilterCfgIpv4Mask:

                :xmlref:`Mask`
     :val:      0...32
     :def:      32
     :desc:     Network mask is used in conjunction with :ref:`<ref-ClientFilterCfgIpv4ClientIPaddr>` attribute in order to create a network subnet.
		All IP addresses of the subnet will be able to connect.
		Network mask attribute is a decimal notation of the subnet mask, sometimes called network prefix, refer to table :numref:`docref-NetworkMask` for more information.
		(Mask 0 will allow connection from any IP address; mask 32 will allow connection only from one IP address specified in :ref:`<ref-ClientFilterCfgIpv4ClientIPaddr>` attribute)

.. include-file:: sections/Include/Name.rstinc ""

Network subnets created by various :ref:`<ref-ClientFilterCfgIpv4Mask>` attribute values are summarized in the table below.
It is assumed user has a good understanding of network addressing fundamentals.
Please refer to external sources (e.g. http://www.subnet-calculator.com) for additional information on network addressing and subnet definition.

| Table columns are defined as follows:
| Column 1 contains :ref:`<ref-ClientFilterCfgIpv4Mask>` attribute values;
| Column 2 contains subnet mask in dotted decimal notation;
| Columns 3...6 show network mask in binary notation (just for reference);
| Column 7 contains range of client IP address allowed to connect.

Table is designed as a guidance of how network subnets are created based on sample IP address 192.168.1.1 specified in the :ref:`<ref-ClientFilterCfgIpv4ClientIPaddr>` attribute.

.. _docref-NetworkMask:

.. field-list-table:: Network Mask sample values
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.1}|C{0.2}|C{0.1}|C{0.1}|C{0.1}|C{0.1}|C{0.3}|
   :definition-row: 1
   :header-rows: 1

   * :mask,10:
     :subnet,20:
     :bval1,10:
     :bval2,10:
     :bval3,10:
     :bval4,10:
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

.. _ref-SupervisionCfg:

SupervisionCfg group node
-------------------------

Group object node :ref:`SupervisionCfg<ref-SupervisionCfg>` is used to configure leandc serial port or socket real-time traffic monitoring
and also enables serial server functionality. Real-time traffic monitoring and serial server functionality has
designated supervision instances which are configured under :ref:`SupervisionCfg<ref-SupervisionCfg>` group node, please refer to the
sample below containing 4 different supervision instances.

.. code-block:: none

   <SupervisionCfg>
	<MONRAW SrcHWIndex="1" DstHWIndex="51" Name="Raw monitoring instance"/>
	<MONCOMP SrcHWIndex="2" DstHWIndex="52" SrvHWIndex="53" Name="Compatible mon instance"/>
	<REDIRECT SrcHWIndex="4" DstHWIndex="61" Name="UART redirect instance"/>
	<OVERRIDE SrcHWIndex="3" DstHWIndex="62" SrvHWIndex="63" Name="UART override instance"/>
   </SupervisionCfg>

Every supervision instance has a unique element node and its configuration is described in the following paragraphs.

.. important::
   | Supervision instances must be listed under :ref:`SupervisionCfg<ref-SupervisionCfg>` group node in the following order:

   | :ref:`<ref-MONRAW>`
   | :ref:`<ref-MONCOMP>`
   | :ref:`<ref-REDIRECT>`
   | :ref:`<ref-OVERRIDE>`

.. include:: supervisionCfg/monraw.rst
.. include:: supervisionCfg/moncomp.rst
.. include:: supervisionCfg/redirect.rst
.. include:: supervisionCfg/override.rst

.. include hmiCfg/hmiMain.rst
