
.. _docref-IEC10xslDITable:
.. _ref-IEC10xslDITable:
.. _ref-IEC10xslDI:

DITable group and DI node
-------------------------

Group node :ref:`DITable<ref-IEC10xslDITable>` and child element nodes :ref:`DI<ref-IEC10xslDI>` are used to create DI information objects to send static status 
information and status change events to the upstream Master station.
Each created DI information object needs to have a source of information.
The source is created by linking DI information object to a :ref:`DI<ref-IEC10xslDI>` node of any Master protocol instance. 
(Master protocol instances are defined in :ref:`CommunicationCfg<ref-CommunicationCfg>` group in **leandc.xml** file)

The link is created using :ref:`DI<ref-IEC10xslDI>`.\ :ref:`<ref-IEC10xslDIDevice>` \ and :ref:`DI<ref-IEC10xslDI>`.\ :ref:`<ref-IEC10xslDIIndex>` \ attributes.
The first step is to select the **source Master protocol instance**, use value of the :ref:`<ref-IEC101maIndex>` attribute of any Master protocol instance.
The next step is to select the **source DI object**, use value of the :ref:`DI<ref-IEC10xmaDI>`.\ :ref:`<ref-IEC10xmaDIIndex>` \ attribute of any DI object listed in the IO object table of a Master protocol instance.
Enter the selected values of **source Master protocol instance** in :ref:`DI<ref-IEC10xslDI>`.\ :ref:`<ref-IEC10xslDIDevice>` \
attribute and **source DI object** in :ref:`DI<ref-IEC10xslDI>`.\ :ref:`<ref-IEC10xslDIIndex>` \ attribute.

Information address (IOA) to send DI information object upstream is specified in :ref:`<ref-IEC10xslDIInfAddr>` \ attribute.

Please see sample :ref:`DITable<ref-IEC10xslDITable>` group and :ref:`DI<ref-IEC10xslDI>` child element nodes below. 
There are 5 DI information objects configured using 4 :ref:`DI<ref-IEC10xslDI>` nodes.

.. code-block:: none

   <DITable>
	<DI Device="10" Index="0" InfAddr="1" qualifier="0" GroupMask="0x0001" … />
	<DI Device="10" Index="1" InfAddr="2" qualifier="0x10" TypeID="30"  … />
	<DI Device="10" Index="-2" InfAddr="3" qualifier="0x00" TypeID="30"  … />
	<DI Device="10" Index="2" InfAddr="4" qualifier="0x00" Total="2" … />
   </DITable>

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`DI<ref-IEC10xslDI>`"

.. code-block:: none

   <DI Device="10" Index="0" InfAddr="1" qualifier="0" GroupMask="0x0001" TypeID="30" OffIndex="5" InterDelay="8000" IndetDelay="3500" Total="2" Name="CB position" />

.. include-file:: sections/Include/tip_order.rstinc "" ":ref:`DI<ref-IEC10xslDI>`"

DI attributes
^^^^^^^^^^^^^

.. _ref-IEC10xslDIAttributes:

.. include-file:: sections/Include/table_attrs.rstinc "" "IEC60870-5-101/104 Slave DI attributes"

.. include-file:: sections/Include/IEC10xsl_Device.rstinc "" ".. _ref-IEC10xslDIDevice:" "DI" "source" "Source"

   * :attr:     .. _ref-IEC10xslDIIndex:

                :xmlref:`Index`
     :val:      -8...2\ :sup:`32`\  - 8
     :def:      n/a
     :desc:     Source DI object. Any DI element node of the selected Master protocol instance can be used as a source.
		Use value of the :ref:`DI<ref-IEC10xmaDI>`.\ :ref:`<ref-IEC10xmaDIIndex>` \ attribute of any DI object listed in the IO table of the selected Master protocol instance.
		In addition to regular DIs there are internal indications available.
		Internal indications are used to monitor real-time status of the source protocol instance.
		Each internal indication has a service index and they are summarized in the table :numref:`ref-IEC10xslDIServiceIndex`.
		:inlinetip:`Indexes don't have to be arranged in ascending order.`

.. include-file:: sections/Include/IEC10xsl_IOA.rstinc "" ".. _ref-IEC10xslDIInfAddr:" "DI" "send object to"

   * :attr:     .. _ref-IEC10xslDIqualifier:

                :xmlref:`qualifier`
     :val:      0...255 or 0x00...0xFF
     :def:      0x00
     :desc:     Internal object qualifier to enable customized data processing.
		See table :numref:`ref-IEC10xslDIqualifierBits` for internal object qualifier description.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:     .. _ref-IEC10xslDIGroupMask:

                :xmlref:`GroupMask`
     :val:      0...65535 or 0x0000...0xFFFF
     :def:      0x0000
     :desc:     Include object in Interrogation group/groups.
		Each bit of the group mask attribute needs to be set in order to include object in a particular interrogation group.
		Please refer to the table :numref:`ref-IEC10xslGroupMask` for more information.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:     .. _ref-IEC10xslDITypeID:

                :xmlref:`TypeID`
     :val:      See table :numref:`ref-IEC10xslDITypeIDValues`
     :def:      2 [M_SP_TA_1] or 30 [M_SP_TB_1]
     :desc:     Use this ASDU Type to send a DI event.
		Attribute also affects ASDU type of the static data (e.g. Single or Double status information) being reported to General interrogation request.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:     .. _ref-IEC10xslDIOffIndex:

                :xmlref:`OffIndex`
     :val:      -8...2\ :sup:`32`\  - 8
     :def:      Same as :ref:`<ref-IEC10xslDIIndex>`
     :desc:     DI object index of the second single point used as a source for conversion to double status indication.
		Resulting Double point will have ON value when source DI object specified in :ref:`<ref-IEC10xslDIIndex>` attribute is ON.
		Resulting Double point will have OFF value when source DI object specified in :xmlref:`OffIndex` attribute is ON.
		See table :numref:`ref-IEC10xslDISPIDPI` for additional information.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, no conversion will take place if this attribute is omitted.`

   * :attr:     .. _ref-IEC10xslDIInterDelay:

                :xmlref:`InterDelay`
     :val:      0...2\ :sup:`32`\  - 1
     :def:      10000 msec
     :desc:     Intermediate state reporting delay in milliseconds used when single status information objects are converted to double point objects.
		Intermediate state of the resulting DPI will not be reported if it doesn't exceed configured delay.
		(default value 10000 - event will be generated if Intermediate state lasts longer than 10 seconds)
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:     .. _ref-IEC10xslDIIndetDelay:

                :xmlref:`IndetDelay`
     :val:      0...2\ :sup:`32`\  - 1
     :def:      5000 msec
     :desc:     Indeterminate (error) state reporting delay in milliseconds used when single status information objects are converted to double point objects.
		Indeterminate (error) state of the resulting DPI will not be reported if it doesn't exceed configured delay.
		(default value 5000 - event will be generated if Indeterminate (error) state lasts longer than 5 seconds)
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

.. include-file:: sections/Include/Total.rstinc "" ".. _ref-IEC10xslDITotal:" ":ref:`<ref-IEC10xslDIIndex>` and :ref:`<ref-IEC10xslDIInfAddr>`" ":ref:`DI<ref-IEC10xslDI>`" "16777214"

.. include-file:: sections/Include/Name.rstinc ""

DI.qualifier
^^^^^^^^^^^^

.. _ref-IEC10xslDIqualifierBits:

.. include-file:: sections/Include/table_flags.rstinc "" "IEC60870-5-101/104 Slave DI internal qualifier" ":ref:`<ref-IEC10xslDIqualifier>`" "DI internal qualifier"

   * :attr:     Bit 0
     :val:      xxxx.xxx0
     :desc:     DI object **will not** be inverted (ON = 1; OFF = 0 for [:lectext1:`M_SP_NA_1`] type and ON = 2; OFF = 1; INTER = 0; INVALID = 3 for [:lectext1:`M_DP_NA_1`] type)

   * :(attr):
     :val:      xxxx.xxx1
     :desc:     DI object **will** be inverted (ON = 0; OFF = 1 for [:lectext1:`M_SP_NA_1`] type and ON = 1; OFF = 2; INTER = 0; INVALID = 3 for [:lectext1:`M_DP_NA_1`] type)

   * :attr:     Bit 1
     :val:      xxxx.xx0x
     :desc:     Additional 'Zero' DI event generation **disabled**

   * :(attr):
     :val:      xxxx.xx1x
     :desc:     Additional 'Zero' DI event generation **enabled**. An OFF event will be internally generated following every sent DI ON event. DI object will always have OFF value in Interrogation responses.

   * :attr:     Bit 2
     :val:      xxxx.x0xx
     :desc:     DI events **enabled**. DI event will be sent upstream if state of the object changes or new event is received from the source communication protocol instance

   * :(attr):
     :val:      xxxx.x1xx
     :desc:     DI events **disabled**

   * :attr:     Bit 3
     :val:      xxxx.0xxx
     :desc:     DI object will be **included** in General Interrogation response

   * :(attr):
     :val:      xxxx.1xxx
     :desc:     DI object will be **excluded** from General Interrogation response

.. include-file:: sections/Include/hidden_IEC10xslDIqualifier.rstinc "internal"

   * :attr:     Bit 5
     :val:      xx0x.xxxx
     :desc:     Use time tag of the **last** event when 2 Single Point objects are merged into a Double Point object. e.g. in transition ON->INTER->OFF time tag of the INTER->OFF event will be used for resulting DPI.

   * :(attr):
     :val:      xx1x.xxxx
     :desc:     Use time tag of the **first** event when 2 Single Point objects are merged into a Double Point object. e.g. in transition ON->INTER->OFF time tag of the ON->INTER event will be used for resulting DPI.

   * :attr:     Bit 6
     :val:      x0xx.xxxx
     :desc:     **All** DI events will be sent upstream

   * :(attr):
     :val:      x1xx.xxxx
     :desc:     DI events with **OFF** values or with set [:lectext1:`IV`] bit will be discarded. :inlinetip:`This option is only used for backward compatibility.`

   * :attr:     Bit 7
     :val:      0xxx.xxxx
     :desc:     DI is **enabled** and will be sent upstream

   * :(attr):
     :val:      1xxx.xxxx
     :desc:     DI is **disabled** and will not be sent upstream

   * :attr:     Bit 4
     :val:      Any
     :desc:     Bits reserved for future use

.. include-file:: sections/Include/IEC60870_DI_TypeID.rstinc "" ".. _ref-IEC10xslDITypeIDValues:" "IEC60870-5-101/104 Slave DI TypeID"

DI Service Indexes
^^^^^^^^^^^^^^^^^^

Service digital inputs are internal indications that provide real-time status information of communication protocol instances.
Service indications have negative index values and can be used just as any regular DI indexes.

.. _ref-IEC10xslDIServiceIndex:

.. field-list-table:: IEC60870-5-101/104 Slave Service DI indexes
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.25}|C{0.25}|S{0.5}|
   :header-rows: 1

   * :attr,10: Index value
     :val,10:  Object value
     :desc,80: Description

   * :attr:     -2 
                (0xFFFFFFFE)
     :val:      ON
     :desc:     Communication between leandc and peer station is running, peer station is **Online**. This service index can be used for any protocol instance.

   * :(attr):
     :val:      OFF
     :desc:     Communication between leandc and peer station is lost, peer station is **Offline**. This service index can be used for any protocol instance.

   * :attr:     -3 
                (0xFFFFFFFD)
     :val:      ON
     :desc:     Communication between leandc and peer station is **Enabled**. This service index can be used for any protocol instance.

   * :(attr):
     :val:      OFF
     :desc:     Communication  between leandc and peer station is **Disabled**. This service index can be used for any protocol instance.

   * :attr:     -4\*
                (0xFFFFFFFC)
     :val:      ON
     :desc:     Communication to peer station is **Started**. Refer to the comment below for the list of protocol instances that provide this service indication. 

   * :(attr):
     :val:      OFF
     :desc:     Communication to peer station is **Stopped**. Refer to the comment below for the list of protocol instances that provide this service indication.

   * :attr:     -5 
                (0xFFFFFFFB)
     :val:      ON
     :desc:     Only used for protocol instances linked to UART hardware node; State of the UART Ring Indicator RI pin(9) is **active (+12V)**. This service DI can be used only if  :ref:`<ref-UART>`.\ :ref:`<ref-UARTCtrlRdTimer>` \ attribute is defined.

   * :(attr):
     :val:      OFF
     :desc:     Only used for protocol instances linked to UART hardware node; State of the UART Ring Indicator RI pin(9) is **not active (-12V)**. This service DI can be used only if :ref:`<ref-UART>`.\ :ref:`<ref-UARTCtrlRdTimer>` \ attribute is defined.

   * :attr:     -1 and -6...-8
     :val:      Any
     :desc:     Internal indications reserved for future use

.. tip::

   | \* This service indication only applies to the following protocol instances:
   | IEC60870-5-104 controling station (Master) communication is [:lectext1:`Started`] or [:lectext1:`Stopped`]. ON ([:lectext1:`Started`] state) indicates [:lectext1:`STARTDT_con`] has been received from outstation;
   | IEC60870-5-104 controlled station (Slave) communication is [:lectext1:`Started`] or [:lectext1:`Stopped`]. ON ([:lectext1:`Started`] state) indicates [:lectext1:`STARTDT_act`] message has been received from upstream station;
   | IEC61850 Client association state. ON indicates associated state i.e. [:lectext1:`Initiate-ResponsePDU`] message has been recevied from IED;

DI SPI/DPI conversion
^^^^^^^^^^^^^^^^^^^^^

Single to double point conversion takes place if :ref:`<ref-IEC10xslDIOffIndex>` attribute is used.
Values of source DI objects and resulting DPI object are listed in the truth table below.


.. _ref-IEC10xslDISPIDPI:

.. field-list-table:: IEC60870-5-101/104 Slave SPI/DPI truth table
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.20}|C{0.20}|S{0.55}|
   :header-rows: 1

   * :onval,18: Value of :ref:`<ref-IEC10xslDIIndex>` DI
     :offval,18:  Value of :ref:`<ref-IEC10xslDIOffIndex>` DI
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

Intermediate and Indeterminate state reporting can be delayed using :ref:`<ref-IEC10xslDIInterDelay>` and :ref:`<ref-IEC10xslDIIndetDelay>` attributes respectively.
If ON->INTER->OFF or OFF->INTER->ON transition successfully completes before :ref:`<ref-IEC10xslDIInterDelay>` timer expiration, Intermediate state will not be reported.
Delay setting has to be carefully selected to ensure it always exceeds time required for ON->INTER->OFF or OFF->INTER->ON transitions to complete, to take advantage of this functionality.
If delay attributes are set 0 Intermediate and Indeterminate states will be reported as soon as values of source DI objects become those listed in the table above.

