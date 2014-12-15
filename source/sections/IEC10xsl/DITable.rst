
.. _docref-IEC10xslDITable:
.. _ref-IEC10xslDITable:
.. _ref-IEC10xslDI:

DITable group and DI node
-------------------------

Group node :ref:`DITable<ref-IEC10xslDITable>` and child element nodes :ref:`DI<ref-IEC10xslDI>` are used to create DI information objects to send static status 
information and status change events to the upstream Master station. Each created DI information object needs 
to have a source of information. The source is created by linking DI information object to a :ref:`DI<ref-IEC10xslDI>` node of any 
Master protocol instance that is defined in leandc. (Master protocol instances are defined under 
:ref:`CommunicationCfg<ref-CommunicationCfg>` node in **leandc.xml** file)

The link is created using :ref:`DI<ref-IEC10xslDI>`.\ :ref:`Device<ref-IEC10xslDIDevice>` \ and :ref:`DI<ref-IEC10xslDI>`.\ :ref:`Index<ref-IEC10xslDIIndex>` \ attributes. The first step is to select the **source Master 
protocol instance**, use value of the :ref:`Index<ref-IEC101maIndex>` attribute of any Master protocol instance. The next step is to select 
the **source DI object**, use value of the :ref:`DI<ref-IEC10xmaDI>`.\ :ref:`Index<ref-IEC10xmaDIIndex>` \ attribute of any DI object listed in the IO object table of a 
Master protocol instance. Enter the selected values of **source Master protocol instance** in :ref:`DI<ref-IEC10xslDI>`.\ :ref:`Device<ref-IEC10xslDIDevice>` \ 
attribute and **source DI object** in :ref:`DI<ref-IEC10xslDI>`.\ :ref:`Index<ref-IEC10xslDIIndex>` \ attribute.

Information address (IOA) for sending DI information object upstream is entered in :ref:`DI<ref-IEC10xslDI>`.\ :ref:`InfAddr<ref-IEC10xslDIInfAddr>` \ attribute.

Please see sample :ref:`DITable<ref-IEC10xslDITable>` group node and :ref:`DI<ref-IEC10xslDI>` child element nodes below. 
There are 5 DI information objects configured using 4 :ref:`DI<ref-IEC10xslDI>` element nodes.

.. code-block:: none

   <DITable> 
	<DI Device="10" Index="0" InfAddr="1" qualifier="0" GroupMask="0x0001" … />
	<DI Device="10" Index="1" InfAddr="2" qualifier="0x10" TypeID="30"  … />
	<DI Device="10" Index="-2" InfAddr="3" qualifier="0x00" TypeID="30"  … />
	<DI Device="10" Index="2" InfAddr="4" qualifier="0x00" Total="2" … />
   </DITable>
   
Please see sample :ref:`DI<ref-IEC10xslDI>` element node below listing all available attributes.
            
.. code-block:: none
            
   <DI  Device="10"
	Index="0"
	InfAddr="1"
	qualifier="0"
	GroupMask="0x0001"
	TypeID="30"
	Total="2"
	Name="CB position" />
      
.. tip:: Attributes of the :ref:`DI<ref-IEC10xslDI>` element node can be arranged in any order, it will not affect the XML file validation.         

DI attributes
^^^^^^^^^^^^^

.. _ref-IEC10xslDIAttributes:

.. field-list-table:: IEC 60807-5-101/104 Slave DI attributes
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.20}|C{0.25}|S{0.55}|
   :header-rows: 1

   * :attr,10: Attribute
     :val,15:  Values or range
     :desc,75: Description

   * :attr:    .. _ref-IEC10xslDIDevice:
               
               :xmlref:`Device`
     :val:     1...254
     :desc:    Source communication protocol instance. Any Master protocol instance listed in :ref:`CommunicationCfg<ref-CommunicationCfg>` group can be used as a source. Use value of the Master protocol instance :ref:`Index<ref-IEC101maIndex>` attribute in order to link DI to it. :inlinetip:`Attribute is optional and doesn't have to be included in configuration, value of the` :ref:`IEC101sl<ref-IEC101sl>`.\ :ref:`Source<ref-IEC101slSource>` \ or :ref:`IEC104sl<ref-IEC104sl>`.\ :ref:`Source<ref-IEC104slSource>` \ :inlinetip:`attributes will be used if omitted.`

   * :attr:    .. _ref-IEC10xslDIIndex:
   
               :xmlref:`Index`
     :val:     -8...2\ :sup:`32`\  - 8
     :desc:    Source DI object. Any DI element node of the selected Master protocol instance can be used as a source. Use value of the :ref:`DI<ref-IEC10xmaDI>`.\ :ref:`Index<ref-IEC10xmaDIIndex>` \ attribute of any DI object listed in the IO table of the selected Master protocol instance. Apart from regular indexes, there are some Service index values available, those are designed to monitor the status of the linked Master protocol instance. Service index values are summarized in the table :numref:`ref-IEC10xslDIServiceIndex`. :inlinetip:`Indexes don't have to be arranged in an ascending order.`

   * :attr:    .. _ref-IEC10xslDIInfAddr:
   
               :xmlref:`InfAddr`
     :val:     1...16777215
     :desc:    Information Object Address (IOA) of the DI object. This IOA will be used to send object to upstream Master station. :inlinetip:`Addresses don't have to be arranged in an ascending order.`

   * :attr:    .. _ref-IEC10xslDIqualifier:
   
               :xmlref:`qualifier`
     :val:     See table :numref:`ref-IEC10xslDIqualifierBits` for description
     :desc:    Internal object qualifier to enable customized data processing. See table :numref:`ref-IEC10xslDIqualifierBits` for internal object qualifier description. (default value 0) :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:    .. _ref-IEC10xslDIGroupMask:
   
               :xmlref:`GroupMask`
     :val:     0...0xFFFF
     :desc:    Include object in Interrogation group/groups. Each bit of the group mask attribute needs to be set in order to include object in a particular interrogation group. Please refer to the table :numref:`ref-IEC10xslGroupMask` for more information. (default value 0) :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:    .. _ref-IEC10xslDITypeID:
   
               :xmlref:`TypeID`
     :val:     See table :numref:`ref-IEC10xslDITypeIDValues` for description
     :desc:    Use this ASDU Type to send a DI event. Attribute also affects ASDU type of the static data (e.g. Single or Double status information) being reported to General interrogation request (default value depends on the protocol type, refer to table :numref:`ref-IEC10xslDITypeIDValues`). :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:    .. _ref-IEC10xslDITotal:
   
               :xmlref:`Total`
     :val:     1...16777215
     :desc:    Total number of information objects. Attribute is used to create sequence of information objects with consecutive :ref:`DI<ref-IEC10xslDI>`.\ :ref:`Index<ref-IEC10xslDIIndex>` \ and :ref:`DI<ref-IEC10xslDI>`.\ :ref:`InfAddr<ref-IEC10xslDIInfAddr>` \ attribute values without a need to create individual :ref:`DI<ref-IEC10xslDI>` nodes for each information object. (default value 1; only 1 object is created with this :ref:`DI<ref-IEC10xslDI>` node) :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:    .. _ref-IEC10xslDIName:
   
               :xmlref:`Name`
     :val:     Max 100 chars
     :desc:    Freely configurable name, just for reference. :inlinetip:`Name attribute is optional and doesn't have to be included in configuration.`

DI.qualifier
^^^^^^^^^^^^

.. _ref-IEC10xslDIqualifierBits:

.. field-list-table:: IEC 60807-5-101/104 Slave DI internal qualifier
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.20}|C{0.25}|S{0.55}|
   :header-rows: 1

   * :attr,10: Bits
     :val,10:  Values
     :desc,80: Description

   * :attr:    qualifier [xxxx.xxxx]
     :val:     0...0xFF
     :desc:    DI internal qualifier has 8 data bits

   * :attr:    Bit 0
     :val:     xxxx.xxx0
     :desc:    DI object **will not** be inverted (ON = 1; OFF = 0 for [M_SP_NA_1] type and ON = 2; OFF = 1; INTER = 0; INVALID = 3 for [M_DP_NA_1] type)

   * :(attr):
     :val:     xxxx.xxx1
     :desc:    DI object **will** be inverted (ON = 0; OFF = 1 for [M_SP_NA_1] type and ON = 1; OFF = 2; INTER = 0; INVALID = 3 for [M_DP_NA_1] type)

   * :attr:    Bit 1
     :val:     xxxx.xx0x
     :desc:    Additional 'Zero' DI event generation **disabled**

   * :(attr):
     :val:     xxxx.xx1x
     :desc:    Additional 'Zero' DI event generation **enabled**. An OFF event will be internally generated following every sent DI ON event. DI object will always have OFF value in Interrogation responses.

   * :attr:    Bit 2
     :val:     xxxx.x0xx
     :desc:    DI events **enabled**. DI event will be sent upstream if state of the object changes or new event is received from the source communication protocol instance

   * :(attr):
     :val:     xxxx.x1xx
     :desc:    DI events **disabled**

   * :attr:    Bit 3
     :val:     xxxx.0xxx
     :desc:    DI object will be **included** in General Interrogation response

   * :(attr):
     :val:     xxxx.1xxx
     :desc:    DI object will be **excluded** from General Interrogation response
 
   * :attr:    Bit 6
     :val:     x0xx.xxxx
     :desc:    **All** DI events will be sent upstream

   * :(attr):
     :val:     x1xx.xxxx
     :desc:    DI events with **OFF** values or with set **[IV]** bit will be discarded. :inlinetip:`This option is only used for backward compatibility.`

   * :attr:    Bit 7
     :val:     0xxx.xxxx
     :desc:    DI is **enabled** and will be sent upstream

   * :(attr):
     :val:     1xxx.xxxx
     :desc:    DI is **disabled** and will not be sent upstream

   * :attr:    Bits 4;5
     :val:     Any
     :desc:    Bits reserved for future use

DI.TypeID
^^^^^^^^^

.. _ref-IEC10xslDITypeIDValues:

.. include:: IEC10xDITypeID.rst
   
DI Service Indexes
^^^^^^^^^^^^^^^^^^

There are some Service DI indexes available allowing to monitor real-time operational status of the 
communication protocol instances. These indexes have negative decimal values allowing then to be easily 
distinguished from regular indexes used for linking.

.. _ref-IEC10xslDIServiceIndex:

.. field-list-table:: IEC 60807-5-101/104 Slave Service DI indexes
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.25}|C{0.25}|S{0.5}|
   :header-rows: 1

   * :attr,10: Index value
     :val,10:  Object value
     :desc,80: Description

   * :attr:    -2 
               (0xFFFFFFFE)
     :val:     ON
     :desc:    Communication between leandc and peer station is running, peer station is **Online**. This service index can be used for any protocol instance.
   
   * :(attr):
     :val:     OFF
     :desc:    Communication between leandc and peer station is lost, peer station is **Offline**. This service index can be used for any protocol instance.
   
   * :attr:    -3 
               (0xFFFFFFFD)
     :val:     ON
     :desc:    Communication between leandc and peer station is **Enabled**. This service index can be used for any protocol instance.
   
   * :(attr):
     :val:     OFF
     :desc:    Communication  between leandc and peer station is **Disabled**. This service index can be used for any protocol instance.
   
   * :attr:    -4 
               (0xFFFFFFFC)
     :val:     ON
     :desc:    Only applicable to IEC60870-5-104 Master/Slave protocol instances; communication is in a [**Started**] state, [STARTDT_act] message is sent and [STARTDT_con] message is received.
   
   * :(attr):
     :val:     OFF
     :desc:    Only applicable to IEC60870-5-104 Master/Slave protocol instances; communication is in a [**Stopped**] state, [STARTDT_act] message hasn't been sent or [STOPPED_act] message hasn't been received.
   
   * :attr:    -5 
               (0xFFFFFFFB)
     :val:     ON
     :desc:    Only used for protocol instances linked to UART hardware node; State of the UART Ring Indicator RI pin(9) is **active (+12V)**. This service DI can be used only if  :ref:`UART<ref-UART>`.\ :ref:`CtrlRdTimer<ref-UARTCtrlRdTimer>` \ attribute is defined.
   
   * :(attr):
     :val:     OFF
     :desc:    Only used for protocol instances linked to UART hardware node; State of the UART Ring Indicator RI pin(9) is **not active (-12V)**. This service DI can be used only if :ref:`UART<ref-UART>`.\ :ref:`CtrlRdTimer<ref-UARTCtrlRdTimer>` \ attribute is defined.

   * :attr:    -1 and -6...-8
     :val:     Any
     :desc:    Internal indications reserved for future use
   
