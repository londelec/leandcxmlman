
.. _xmlgroup-IEC103maDI: lelabel=DITable
.. _xmlelem-IEC103maDI: lelabel=DI

DITable group
-------------

.. include-file:: sections/Include/ma_DIAI_table.rstinc "" ":ref:`xmlgroup-IEC103maDI`" ":ref:`xmlelem-IEC103maDI`" ":numref:`tabid-IEC103maDI`" ":ref:`docref-IEC10xslDI`" "DI" "status information" "IED"

In order to receive status information from IED [:lemonobgtext:`FUNCTION TYPE`] and [:lemonobgtext:`INFORMATION NUMBER`] has to be specified in :ref:`xmlattr-IEC103maDIFUN` \ and :ref:`xmlattr-IEC103maDIINF` \ attributes.

Please see sample :ref:`xmlgroup-IEC103maDI` group and :ref:`xmlelem-IEC103maDI` element nodes below.
There are 5 status information objects defined with 4 :ref:`xmlelem-IEC103maDI` element nodes.

.. code-block:: none

   <DITable>
	<DI Index="0" FUN="1" INF="1" Qualifier="0x00"/>
	<DI Index="1" FUN="1" INF="2" Qualifier="0x10"/>
	<DI Index="2" FUN="240" INF="55" Qualifier="0x10"/>
	<DI Index="3" FUN="240" INF="56" Qualifier="0x00" Total="2"/>
   </DITable>

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-IEC103maDI`"

.. code-block:: none

   <DI Index="0" FUN="1" INF="1" Qualifier="0" InterDelay="10000" IndetDelay="0" OnDelay="0" OffDelay="0" Total="2" Name="CB position" />

.. include-file:: sections/Include/tip_order.rstinc "" ":ref:`xmlelem-IEC103maDI`"

DI attributes
^^^^^^^^^^^^^

.. include-file:: sections/Include/table_attrs.rstinc "" "tabid-IEC103maDI" "IEC60870-5-103 Master DI attributes" ":spec: |C{0.12}|C{0.14}|C{0.1}|S{0.64}|"

.. include-file:: sections/Include/ma_Index.rstinc "" "DI"

.. include-file:: sections/Include/IEC103ma_FunInf.rstinc "" "DI" "receive object from"

.. include-file:: sections/Include/Qualifier.rstinc "" ":numref:`tabid-IEC103maDIQualifier`"

.. include-file:: sections/Include/DI_Idelays.rstinc ""

.. include-file:: sections/Include/DI_Odelays.rstinc ""

.. include-file:: sections/Include/Total.rstinc "" ":ref:`xmlattr-IEC103maDIIndex` and :ref:`xmlattr-IEC103maDIINF`" ":ref:`xmlelem-IEC103maDI`" "254"

.. include-file:: sections/Include/Name.rstinc ""

DI.Qualifier
^^^^^^^^^^^^

.. include-file:: sections/Include/table_flags8.rstinc "" "tabid-IEC103maDIQualifier" "IEC60870-5-103 Master DI internal Qualifier" ":ref:`xmlattr-IEC103maDIQualifier`" "DI internal qualifier"

   * :attr:     Bit 0
     :val:      xxxx.xxx0
     :desc:     DI object **will not** be inverted (ON = 2; OFF = 1; INTER = 0; INVALID = 3)

   * :(attr):
     :val:      xxxx.xxx1
     :desc:     DI object **will** be inverted (ON = 1; OFF = 2; INTER = 0; INVALID = 3)

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
     :desc:     Use time tag of the **last** event if Intermediate state of the Double Point object was not reported (because Intermediate state didn't exceed :ref:`xmlattr-IEC103maDIInterDelay`). e.g. in transition ON->INTER->OFF time tag of the INTER->OFF event will be used.

   * :(attr):
     :val:      xx1x.xxxx
     :desc:     Use time tag of the **first** event if Intermediate state of the Double Point object was not reported (because Intermediate state didn't exceed :ref:`xmlattr-IEC103maDIInterDelay`). e.g. in transition ON->INTER->OFF time tag of the ON->INTER event will be used.

   * :attr:     Bit 7
     :val:      0xxx.xxxx
     :desc:     DI is **enabled** and will be processed when received

   * :(attr):
     :val:      1xxx.xxxx
     :desc:     DI is **disabled** and will be discarded when received

   * :attr:     Bits 3;4;6
     :val:      Any
     :desc:     Bits reserved for future use
