
.. _xmlgroup-IEC10xmaDI: lelabel=DITable
.. _xmlelem-IEC10xmaDI: lelabel=DI

DITable group
-------------

.. include-file:: sections/Include/ma_DIAI_table.rstinc "" ":ref:`xmlgroup-IEC10xmaDI`" ":ref:`xmlelem-IEC10xmaDI`" ":numref:`tabid-IEC10xmaDI`" ":ref:`docref-IEC10xslDI`" "DI" "status information" "outstation"

In order to receive status information from outstation information object address (IOA) needs to be specified in the :ref:`xmlattr-IEC10xmaDIInfAddr` \ attribute.
Status information is processed when received from outstation with any of the following ASDU types:
1 [:lemonobgtext:`M_SP_NA_1`]; 2 [:lemonobgtext:`M_SP_TA_1`]; 3 [:lemonobgtext:`M_DP_NA_1`];
4 [:lemonobgtext:`M_DP_TA_1`]; 30 [:lemonobgtext:`M_SP_TB_1`]; 31 [:lemonobgtext:`M_DP_TB_1`]

Please see sample :ref:`xmlgroup-IEC10xmaDI` group and :ref:`xmlelem-IEC10xmaDI` element nodes below.
There are 5 status information objects defined with 4 :ref:`xmlelem-IEC10xmaDI` element nodes.

.. code-block:: none

   <DITable>
	<DI Index="0" InfAddr="1" qualifier="0x00" />
	<DI Index="1" InfAddr="2" qualifier="0x10" />
	<DI Index="2" InfAddr="3" qualifier="0x10" TypeID="31"/>
	<DI Index="3" InfAddr="4" qualifier="0x00" Total="2"/>
   </DITable>

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-IEC10xmaDI`"

.. code-block:: none

   <DI Index="0" InfAddr="1" qualifier="0" InterDelay="10000" IndetDelay="0" TypeID="31" Total="2" Name="CB position" />

.. include-file:: sections/Include/tip_order.rstinc "" ":ref:`xmlelem-IEC10xmaDI`"

DI attributes
^^^^^^^^^^^^^

.. include-file:: sections/Include/table_attrs.rstinc "" "tabid-IEC10xmaDI" "IEC60870-5-101/104 Master DI attributes" ":spec: |C{0.12}|C{0.14}|C{0.12}|S{0.62}|"

.. include-file:: sections/Include/ma_Index.rstinc "" "DI"

.. include-file:: sections/Include/IEC10xma_IOA.rstinc "" "DI" "receive object from"

.. include-file:: sections/Include/IEC60870_qualifier.rstinc "" ":numref:`tabid-IEC10xmaDIqualifier`"

.. include-file:: sections/Include/DI_Idelays.rstinc ""

.. include-file:: sections/Include/IEC10xma_DIAI_TypeID.rstinc "" "DI" ":numref:`tabid-IEC10xmaDITypeID`"

.. include-file:: sections/Include/Total.rstinc "" ":ref:`xmlattr-IEC10xmaDIIndex` and :ref:`xmlattr-IEC10xmaDIInfAddr`" ":ref:`xmlelem-IEC10xmaDI`" "16777214"

.. include-file:: sections/Include/Name.rstinc ""

DI.qualifier
^^^^^^^^^^^^

.. include-file:: sections/Include/table_flags8.rstinc "" "tabid-IEC10xmaDIqualifier" "IEC60870-5-101/104 Master DI internal qualifier" ":ref:`xmlattr-IEC10xmaDIqualifier`" "DI internal qualifier"

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
     :desc:	Additional 'Zero' DI event generation **enabled**. An OFF event will be internally generated following every sent DI ON event. Static DI object will be set to OFF value, static value is used when Slave protocol instance responds to an Interrogation.

   * :attr:	Bit 2
     :val:	xxxx.x0xx
     :desc:	Event is generated only if a DI object **state has changed**

   * :(attr):
     :val:	xxxx.x1xx
     :desc:	Event is generated **every time** DI object is received from outstation.
		Also invalid [:lemonobgtext:`IV`] flag is automatically cleared when outstation goes online which ensures this DI object is always valid.
		:inlinetip:`This option is only used for backward compatibility.`

   * :attr:	:bitdef:`3`
     :val:	xxxx.0xxx
     :desc:	**Use original** timetag when event is received from outstation

   * :(attr):
     :val:	xxxx.1xxx
     :desc:	**Substitute timetag** with local time when event is received from outstation

   * :attr:	:bitdef:`5`
     :val:	xx0x.xxxx
     :desc:	Use time tag of the **last** event if Intermediate state of the Double Point object was not reported (because Intermediate state didn't exceed :ref:`xmlattr-IEC10xmaDIInterDelay`). e.g. in transition ON->INTER->OFF time tag of the INTER->OFF event will be used.

   * :(attr):
     :val:	xx1x.xxxx
     :desc:	Use time tag of the **first** event if Intermediate state of the Double Point object was not reported (because Intermediate state didn't exceed :ref:`xmlattr-IEC10xmaDIInterDelay`). e.g. in transition ON->INTER->OFF time tag of the ON->INTER event will be used.

   * :attr:	Bit 7
     :val:	0xxx.xxxx
     :desc:	DI is **enabled** and will be processed when received

   * :(attr):
     :val:	1xxx.xxxx
     :desc:	DI is **disabled** and will be discarded when received

   * :attr:	Bits 4;6
     :val:	Any
     :desc:	Bits reserved for future use

.. include-file:: sections/Include/IEC60870_DI_TypeID.rstinc "" "tabid-IEC10xmaDITypeID" "IEC60870-5-101/104 Master DI TypeID"
