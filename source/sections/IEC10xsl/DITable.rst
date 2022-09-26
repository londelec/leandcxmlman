
.. _docref-IEC10xslDI:
.. _xmlgroup-IEC10xslDI: lelabel=DITable
.. _xmlelem-IEC10xslDI: lelabel=DI

DITable group
-------------

.. include-file:: sections/Include/IEC10xsl_DIAI_table.rstinc "" ":ref:`xmlgroup-IEC10xslDI`" ":ref:`xmlelem-IEC10xslDI`" ":numref:`tabid-IEC10xslDI`" "DI" "status information"

| The link is created using :ref:`xmlelem-IEC10xslDI`.\ :ref:`xmlattr-IEC10xslDIDevice` and :ref:`xmlelem-IEC10xslDI`.\ :ref:`xmlattr-IEC10xslDIIndex` attributes as follows:
| 1. Select the **source Master protocol instance** - use value of the :ref:`xmlattr-gp101maIndex` attribute of any Master protocol instance and enter this value in :ref:`xmlelem-IEC10xslDI`.\ :ref:`xmlattr-IEC10xslDIDevice` attribute.
| 2. Select the **source DI object** - use value of the :ref:`xmlelem-IEC10xmaDI`.\ :ref:`xmlattr-IEC10xmaDIIndex` attribute of any DI object listed in the IO object table of a Master protocol instance and enter this value in :ref:`xmlelem-IEC10xslDI`.\ :ref:`xmlattr-IEC10xslDIIndex` attribute.

Information object address (IOA) to send status information object upstream is specified in :ref:`xmlattr-IEC10xslDIInfAddr` attribute.

Please see sample :ref:`xmlgroup-IEC10xslDI` group and :ref:`xmlelem-IEC10xslDI` element nodes below. 
There are 5 status information objects defined with 4 :ref:`xmlelem-IEC10xslDI` element nodes.

.. code-block:: none

   <DITable>
	<DI Device="10" Index="0" InfAddr="1" qualifier="0" GroupMask="0x0001" … />
	<DI Device="10" Index="1" InfAddr="2" qualifier="0x10" TypeID="30"  … />
	<DI Device="10" Index="-2" InfAddr="3" qualifier="0x00" TypeID="30"  … />
	<DI Device="10" Index="2" InfAddr="4" qualifier="0x00" Total="2" … />
   </DITable>

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-IEC10xslDI`"

.. code-block:: none

   <DI Device="10" Index="0" InfAddr="1" qualifier="0" GroupMask="0x0001" TypeID="30" OffIndex="5" InterDelay="8000" IndetDelay="3500" Total="2" Name="CB position" />

.. include-file:: sections/Include/tip_order.rstinc "" ":ref:`xmlelem-IEC10xslDI`"

DI attributes
^^^^^^^^^^^^^

.. include-file:: sections/Include/table_attrs.rstinc "" "tabid-IEC10xslDI" "IEC60870-5-101/104 Slave DI attributes" ":spec: |C{0.14}|C{0.16}|C{0.15}|S{0.55}|"

.. include-file:: sections/Include/IEC10xsl_Device.rstinc "" ":xmlattr:`Device`" "source for this DI object" "Source"

   * :attr:	:xmlattr:`Index`
     :val:	|slindexrange|
     :def:	n/a
     :desc:	Source DI object. Any DI element of the selected Master protocol instance can be used as a source.
		Use value of the :ref:`xmlelem-IEC10xmaDI`.\ :ref:`xmlattr-IEC10xmaDIIndex` attribute of any DI object listed in the IO table of the selected Master protocol instance.
		In addition to regular DIs there are internal indications available.
		Internal indications are used to monitor real-time status of the source protocol instance.
		Each internal indication has a service index and they are summarized in the :numref:`tabid-IEC10xslDIServiceIndex`.
		:inlinetip:`Indexes don't have to be arranged in ascending order.`

.. include-file:: sections/Include/IEC10xsl_IOA.rstinc "" "DI" "send object to"

.. include-file:: sections/Include/IEC60870_qualifier.rstinc "" ":numref:`tabid-IEC10xslDIqualifier`"

.. include-file:: sections/Include/IEC10xsl_GroupMask.rstinc "" ":xmlattr:`GroupMask`" "object"

   * :attr:	:xmlattr:`TypeID`
     :val:	See :numref:`tabid-IEC10xslDITypeID`
     :def:	2 [:lemonobgtext:`M_SP_TA_1`] or 30 [:lemonobgtext:`M_SP_TB_1`]
     :desc:	Use this ASDU Type to send a DI event.
		Attribute also affects ASDU type of the static data (e.g. Single or Double status information) being reported to General interrogation request.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:	:xmlattr:`OffIndex`
     :val:	-8...2\ :sup:`32`\  - 8
     :def:	Same as :ref:`xmlattr-IEC10xslDIIndex`
     :desc:	DI object index of the second single point used as a source for conversion to double status indication.
		Resulting Double point will have ON value when source DI object specified in :ref:`xmlattr-IEC10xslDIIndex` attribute is ON.
		Resulting Double point will have OFF value when source DI object specified in :ref:`xmlattr-IEC10xslDIOffIndex` attribute is ON.
		See :numref:`tabid-IEC10xslDISPIDPI` for additional information.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, no conversion will take place if this attribute is omitted.`

   * :attr:	:xmlattr:`InterDelay`
     :val:	|uint32range|
     :def:	10000 msec
     :desc:	Intermediate state reporting delay in milliseconds used when single status information objects are converted to double point objects.
		Intermediate state of the resulting DPI will not be reported if it doesn't exceed configured delay.
		(default value 10000 - event will be generated if Intermediate state lasts longer than 10 seconds)
		This attribute has a higher priority than IEC101sl and IEC104sl :ref:`xmlelem-IEC101slAsdu`.\ :ref:`xmlattr-IEC101slAsduDIInterDelay`\ .
		|optinalattr|

   * :attr:	:xmlattr:`IndetDelay`
     :val:	|uint32range|
     :def:	5000 msec
     :desc:	Indeterminate (error) state reporting delay in milliseconds used when single status information objects are converted to double point objects.
		Indeterminate (error) state of the resulting DPI will not be reported if it doesn't exceed configured delay.
		(default value 5000 - event will be generated if Indeterminate (error) state lasts longer than 5 seconds)
		This attribute has a higher priority than IEC101sl and IEC104sl :ref:`xmlelem-IEC101slAsdu`.\ :ref:`xmlattr-IEC101slAsduDIIndetDelay`\ .
		|optinalattr|

.. include-file:: sections/Include/Total.rstinc "" ":ref:`xmlattr-IEC10xslDIIndex` and :ref:`xmlattr-IEC10xslDIInfAddr`" ":ref:`xmlelem-IEC10xslDI`" "16777214"

.. include-file:: sections/Include/Name.rstinc ""

DI.qualifier
^^^^^^^^^^^^

.. include-file:: sections/Include/table_flags8.rstinc "" "tabid-IEC10xslDIqualifier" "IEC60870-5-101/104 Slave DI internal qualifier" ":ref:`xmlattr-IEC10xslDIqualifier`" "DI internal qualifier"

   * :attr:	Bit 0
     :val:	xxxx.xxx0
     :desc:	DI object **will not** be inverted (ON = 1; OFF = 0 for [:lemonobgtext:`M_SP_NA_1`] type and ON = 2; OFF = 1; INTER = 0; INVALID = 3 for [:lemonobgtext:`M_DP_NA_1`] type)

   * :(attr):
     :val:	xxxx.xxx1
     :desc:	DI object **will** be inverted (ON = 0; OFF = 1 for [:lemonobgtext:`M_SP_NA_1`] type and ON = 1; OFF = 2; INTER = 0; INVALID = 3 for [:lemonobgtext:`M_DP_NA_1`] type)

   * :attr:	Bit 1
     :val:	xxxx.xx0x
     :desc:	Additional 'Zero' DI event generation **disabled**

   * :(attr):
     :val:	xxxx.xx1x
     :desc:	Additional 'Zero' DI event generation **enabled**. An OFF event will be internally generated following every sent DI ON event. DI object will always have OFF value in Interrogation responses.

   * :attr:	Bit 2
     :val:	xxxx.x0xx
     :desc:	DI events **enabled**. DI event will be sent upstream if state of the object changes or new event is received from the source communication protocol instance

   * :(attr):
     :val:	xxxx.x1xx
     :desc:	DI events **disabled**

   * :attr:	Bit 3
     :val:	xxxx.0xxx
     :desc:	DI object will be **included** in General Interrogation response

   * :(attr):
     :val:	xxxx.1xxx
     :desc:	DI object will be **excluded** from General Interrogation response

.. include-file:: sections/Include/hidden_IEC10xslDIqualifier.rstinc "internal"

   * :attr:	:bitdef:`5`
     :val:	xx0x.xxxx
     :desc:	Use time tag of the **last** event when 2 Single Point objects are merged into a Double Point object. e.g. in transition ON->INTER->OFF time tag of the INTER->OFF event will be used for resulting DPI.

   * :(attr):
     :val:	xx1x.xxxx
     :desc:	Use time tag of the **first** event when 2 Single Point objects are merged into a Double Point object. e.g. in transition ON->INTER->OFF time tag of the ON->INTER event will be used for resulting DPI.

   * :attr:	Bit 6
     :val:	x0xx.xxxx
     :desc:	**All** DI events will be sent upstream

   * :(attr):
     :val:	x1xx.xxxx
     :desc:	DI events with **OFF** values or with set [:lemonobgtext:`IV`] bit will be discarded. :inlinetip:`This option is only used for backward compatibility.`

   * :attr:	Bit 7
     :val:	0xxx.xxxx
     :desc:	DI is **enabled** and will be sent upstream

   * :(attr):
     :val:	1xxx.xxxx
     :desc:	DI is **disabled** and will not be sent upstream

   * :attr:	Bit 4
     :val:	Any
     :desc:	Bits reserved for future use

.. include-file:: sections/Include/IEC60870_DI_TypeID.rstinc "" "tabid-IEC10xslDITypeID" "IEC60870-5-101/104 Slave DI TypeID"

DI Service Indexes
^^^^^^^^^^^^^^^^^^

Service digital inputs are internal indications that provide real-time status information of communication protocol instances.
Service indications have negative index values and can be used just as any regular DI indexes.

.. field-list-table:: IEC60870-5-101/104 Slave Service DI indexes
   :class: table table-condensed table-bordered longtable
   :name: tabid-IEC10xslDIServiceIndex
   :spec: |C{0.19}|C{0.1}|S{0.71}|
   :header-rows: 1

   * :attr,10: Index value
     :val,10:  Object value
     :desc,80: Description

   * :attr:	-2 
		(0xFFFFFFFE)
     :val:	ON
     :desc:	Communication between leandc and peer station is running, peer station is **Online**. This service index can be used for any protocol instance.

   * :(attr):
     :val:	OFF
     :desc:	Communication between leandc and peer station is lost, peer station is **Offline**. This service index can be used for any protocol instance.

   * :attr:	-3 
 		(0xFFFFFFFD)
     :val:	ON
     :desc:	Communication between leandc and peer station is **Enabled**. This service index can be used for any protocol instance.

   * :(attr):
     :val:	OFF
     :desc:	Communication  between leandc and peer station is **Disabled**. This service index can be used for any protocol instance.

   * :attr:	-4\*
		(0xFFFFFFFC)
     :val:	ON
     :desc:	Communication to peer station is **Started**. Refer to the comment below for the list of protocol instances that provide this service indication. 

   * :(attr):
     :val:	OFF
     :desc:	Communication to peer station is **Stopped**. Refer to the comment below for the list of protocol instances that provide this service indication.

   * :attr:	-5 
		(0xFFFFFFFB)
     :val:	ON
     :desc:	Only used for protocol instances linked to UART hardware node; State of the UART Ring Indicator RI pin(9) is **active (+12V)**.
		This service DI can be used only if :ref:`xmlelem-uart`.\ :ref:`xmlattr-UARTCtrlRdTimer` \ attribute is defined.

   * :(attr):
     :val:	OFF
     :desc:	Only used for protocol instances linked to UART hardware node; State of the UART Ring Indicator RI pin(9) is **not active (-12V)**.
		This service DI can be used only if :ref:`xmlelem-uart`.\ :ref:`xmlattr-UARTCtrlRdTimer` \ attribute is defined.

   * :attr:	-1 and -6...-8
     :val:	Any
     :desc:	Internal indications reserved for future use

.. tip::

   | \* This service indication only applies to the following protocol instances:
   | IEC60870-5-104 controlling station (Master) communication is [:lemonobgtext:`Started`] or [:lemonobgtext:`Stopped`]. ON ([:lemonobgtext:`Started`] state) indicates [:lemonobgtext:`STARTDT_con`] has been received from outstation;
   | IEC60870-5-104 controlled station (Slave) communication is [:lemonobgtext:`Started`] or [:lemonobgtext:`Stopped`]. ON ([:lemonobgtext:`Started`] state) indicates [:lemonobgtext:`STARTDT_act`] message has been received from upstream station;
   | IEC61850 Client association state. ON indicates associated state i.e. [:lemonobgtext:`Initiate-ResponsePDU`] message has been received from IED;

DI SPI/DPI conversion
^^^^^^^^^^^^^^^^^^^^^

Single to double point conversion takes place if :ref:`xmlattr-IEC10xslDIOffIndex` attribute is used.
Values of source DI objects and resulting DPI object are listed in the truth table below.

.. field-list-table:: IEC60870-5-101/104 Slave SPI/DPI truth table
   :class: table table-condensed table-bordered longtable
   :name: tabid-IEC10xslDISPIDPI
   :spec: |C{0.14}|C{0.14}|S{0.55}|
   :header-rows: 1

   * :onval,18: Value of :ref:`xmlattr-IEC10xslDIIndex` DI
     :offval,18:  Value of :ref:`xmlattr-IEC10xslDIOffIndex` DI
     :result,64: Resulting DPI

   * :onval:    OFF (0)
     :offval:   OFF (0)
     :result:   Intermediate (0)

   * :onval:    OFF (0)
     :offval:   ON (1)
     :result:   OFF (1)

   * :onval:    ON (1)
     :offval:   OFF (0)
     :result:   ON (2)

   * :onval:    ON (1)
     :offval:   ON (1)
     :result:   Indeterminate (error) (3)

   * :onval:    Other
     :offval:   Other
     :result:   Indeterminate (error) (3)

Intermediate and Indeterminate state reporting can be delayed using :ref:`xmlattr-IEC10xslDIInterDelay` and :ref:`xmlattr-IEC10xslDIIndetDelay` attributes respectively.
If ON->INTER->OFF or OFF->INTER->ON transition successfully completes before :ref:`xmlattr-IEC10xslDIInterDelay` timer expiration, Intermediate state will not be reported.
Delay setting has to be carefully selected to ensure it always exceeds time required for ON->INTER->OFF or OFF->INTER->ON transitions to complete, to take advantage of this functionality.
If delay attributes are set 0 Intermediate and Indeterminate states will be reported as soon as values of source DI objects become those listed in the table above.

