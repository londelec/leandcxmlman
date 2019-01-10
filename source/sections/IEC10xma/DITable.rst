
.. _ref-IEC10xmaDITable:
.. _ref-IEC10xmaDI:

DITable group and DI node
-------------------------

Group node :ref:`DITable<ref-IEC10xmaDITable>` and child element nodes :ref:`DI<ref-IEC10xmaDI>` are used to create DI information objects to receive status information from the downstream outstation.
Each created DI can be used as a source for any DI information object defined in the IO table of any Slave protocol instance.
Data received from the outstation will be forwarded to the DI information object of the Slave protocol instance and then to the upstream Master station.
Please refer to the section :ref:`docref-IEC10xslDITable` for more information on how to use DI information object as a source.

In order to receive status information from downstream outstation information object address (IOA) needs to be
specified in the :ref:`InfAddr<ref-IEC10xmaDIInfAddr>` \ attribute.
Status information is processed when received with any of the following ASDU types:
1 [:lemonobgtext:`M_SP_NA_1`]; 2 [:lemonobgtext:`M_SP_TA_1`]; 3 [:lemonobgtext:`M_DP_NA_1`];
4 [:lemonobgtext:`M_DP_TA_1`]; 30 [:lemonobgtext:`M_SP_TB_1`]; 31 [:lemonobgtext:`M_DP_TB_1`]

Please see sample :ref:`DITable<ref-IEC10xmaDITable>` group and :ref:`DI<ref-IEC10xmaDI>` child element nodes below.
There are 5 DI information objects configured using 4 :ref:`DI<ref-IEC10xmaDI>` element nodes.

.. code-block:: none

   <DITable>
	<DI Index="0" InfAddr="1" qualifier="0x00" />
	<DI Index="1" InfAddr="2" qualifier="0x10" />
	<DI Index="2" InfAddr="3" qualifier="0x10" TypeID="31"/>
	<DI Index="3" InfAddr="4" qualifier="0x00" Total="2"/>
   </DITable>

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`DI<ref-IEC10xmaDI>`"

.. code-block:: none

   <DI Index="0" InfAddr="1" qualifier="0" InterDelay="10000" IndetDelay="0" TypeID="31" Total="2" Name="CB position" />

.. include-file:: sections/Include/tip_order.rstinc "" ":ref:`DI<ref-IEC10xmaDI>`"

DI attributes
^^^^^^^^^^^^^

.. _docref-IEC10xmaDIAttributes:

.. include-file:: sections/Include/table_attrs.rstinc "" "IEC60870-5-101/104 Master DI attributes" ":spec: |C{0.12}|C{0.14}|C{0.12}|S{0.62}|"

.. include-file:: sections/Include/ma_Index.rstinc "" ".. _ref-IEC10xmaDIIndex:" "DI"

.. include-file:: sections/Include/IEC10xma_IOA.rstinc "" ".. _ref-IEC10xmaDIInfAddr:" "DI" "receive object from"

   * :attr:     .. _ref-IEC10xmaDIqualifier:

                :xmlref:`qualifier`
     :val:      0...255 or 0x00...0xFF
     :def:      0x00
     :desc:     Internal object qualifier to enable customized data processing.
		See table :numref:`docref-IEC10xmaDIqualifierBits` for internal object qualifier description.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

.. include-file:: sections/Include/DI_Idelays.rstinc "" ".. _ref-IEC10xmaDIInterDelay:" ".. _ref-IEC10xmaDIIndetDelay:"

   * :attr:     .. _ref-IEC10xmaDITypeID:

                :xmlref:`TypeID`
     :val:      See table :numref:`docref-IEC10xmaDITypeIDValues`
     :def:      transparent
     :desc:     Use this ASDU type to send a DI object upstream, if transparent ASDUs are enabled in Slave protocol instance with :ref:`<ref-IEC101slASDUSettings>`.\ :ref:`<ref-IEC101slASDUSettingsTranspTypes>` \ attribute.
		This ASDU type will be used to report object regardless of the received ASDU type.
		There is no default value, attribute must not be specified if not used.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration.
		ASDU type received from outstation will be used to report object upstream if transparent ASDUs are enabled in Slave protocol instance with` :ref:`<ref-IEC101slASDUSettings>`.\ :ref:`<ref-IEC101slASDUSettingsTranspTypes>` \ :inlinetip:`attribute.`

.. include-file:: sections/Include/Total.rstinc "" ".. _ref-IEC10xmaDITotal:" ":ref:`<ref-IEC10xmaDIIndex>` and :ref:`<ref-IEC10xmaDIInfAddr>`" ":ref:`DI<ref-IEC10xmaDI>`" "16777214"

.. include-file:: sections/Include/Name.rstinc ""

DI.qualifier
^^^^^^^^^^^^

.. _docref-IEC10xmaDIqualifierBits:

.. include-file:: sections/Include/table_flags.rstinc "" "IEC60870-5-101/104 Master DI internal qualifier" ":ref:`<ref-IEC10xmaDIqualifier>`" "DI internal qualifier"

   * :attr:     Bit 0
     :val:      xxxx.xxx0
     :desc:     DI object **will not** be inverted (ON = 1; OFF = 0 for [:lemonobgtext:`M_SP_NA_1`] type and ON = 2; OFF = 1; INTER = 0; INVALID = 3 for [:lemonobgtext:`M_DP_NA_1`] type)

   * :(attr):
     :val:      xxxx.xxx1
     :desc:     DI object **will** be inverted (ON = 0; OFF = 1 for [:lemonobgtext:`M_SP_NA_1`] type and ON = 1; OFF = 2; INTER = 0; INVALID = 3 for [:lemonobgtext:`M_DP_NA_1`] type)

   * :attr:     Bit 1
     :val:      xxxx.xx0x
     :desc:     Additional 'Zero' DI event generation **disabled**

   * :(attr):
     :val:      xxxx.xx1x
     :desc:     Additional 'Zero' DI event generation **enabled**. An OFF event will be internally generated following every sent DI ON event. Static DI object will be set to OFF value, static value is used when Slave protocol instance responds to an Interrogation.

   * :attr:     Bit 2
     :val:      xxxx.x0xx
     :desc:	Event is generated only if a DI object **state has changed**

   * :(attr):
     :val:      xxxx.x1xx
     :desc:	Event is generated **every time** DI object is received from outstation.
		Also invalid [:lemonobgtext:`IV`] flag is automatically cleared when outstation goes online which ensures this DI object is always valid.
		:inlinetip:`This option is only used for backward compatibility.`

   * :attr:     Bit 3
     :val:      xxxx.0xxx
     :desc:     **Use original** timetag when event is received from outstation

   * :(attr):
     :val:      xxxx.1xxx
     :desc:     **Substitute timetag** with local time when event is received from outstation

   * :attr:     Bit 5
     :val:      xx0x.xxxx
     :desc:     Use time tag of the **last** event if Intermediate state of the Double Point object was not reported (because Intermediate state didn't exceed :ref:`<ref-IEC10xmaDIInterDelay>`). e.g. in transition ON->INTER->OFF time tag of the INTER->OFF event will be used.

   * :(attr):
     :val:      xx1x.xxxx
     :desc:     Use time tag of the **first** event if Intermediate state of the Double Point object was not reported (because Intermediate state didn't exceed :ref:`<ref-IEC10xmaDIInterDelay>`). e.g. in transition ON->INTER->OFF time tag of the ON->INTER event will be used.

   * :attr:     Bit 7
     :val:      0xxx.xxxx
     :desc:     DI is **enabled** and will be processed when received

   * :(attr):
     :val:      1xxx.xxxx
     :desc:     DI is **disabled** and will be discarded when received

   * :attr:     Bits 4;6
     :val:      Any
     :desc:     Bits reserved for future use

.. include-file:: sections/Include/IEC60870_DI_TypeID.rstinc "" ".. _docref-IEC10xmaDITypeIDValues:" "IEC60870-5-101/104 Master DI TypeID"
