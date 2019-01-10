
.. _ref-IEC103maDITable:
.. _ref-IEC103maDI:

DITable group and DI node
-------------------------

Group node :ref:`DITable<ref-IEC103maDITable>` and child element nodes :ref:`DI<ref-IEC103maDI>` are used to create DI information objects to receive status
information from the downstream outstation. Each created DI information object can be used as source of
information for any DI information object defined in IO table of the Slave protocol instances. If used as a source,
status information received from an outstation will be forwarded to DI information object of the Slave protocol
instance and then to the upstream Master station. Please refer to the
section :ref:`docref-IEC10xslDITable` for more information on how to use DI information object as a source.

In order to receive a status information from downstream outstation [:lemonobgtext:`FUNCTION TYPE`] and [:lemonobgtext:`INFORMATION NUMBER`]
has to be specified in :ref:`<ref-IEC103maDIFUN>` \ and :ref:`<ref-IEC103maDIINF>` \ attributes.

Please see sample :ref:`DITable<ref-IEC103maDITable>` group and :ref:`DI<ref-IEC103maDI>` child element nodes below.
There are 5 DI information objects configured using 4 :ref:`DI<ref-IEC103maDI>` element nodes.

.. code-block:: none

   <DITable>
	<DI Index="0" FUN="1" INF="1" Qualifier="0x00"/>
	<DI Index="1" FUN="1" INF="2" Qualifier="0x10"/>
	<DI Index="2" FUN="240" INF="55" Qualifier="0x10"/>
	<DI Index="3" FUN="240" INF="56" Qualifier="0x00" Total="2"/>
   </DITable>

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`DI<ref-IEC103maDI>`"

.. code-block:: none

   <DI Index="0" FUN="1" INF="1" Qualifier="0" InterDelay="10000" IndetDelay="0" Total="2" Name="CB position" />

.. include-file:: sections/Include/tip_order.rstinc "" ":ref:`DI<ref-IEC103maDI>`"

DI attributes
^^^^^^^^^^^^^

.. _docref-IEC103maDIAttributes:

.. include-file:: sections/Include/table_attrs.rstinc "" "IEC60870-5-103 Master DI attributes" ":spec: |C{0.12}|C{0.14}|C{0.1}|S{0.64}|"

.. include-file:: sections/Include/ma_Index.rstinc "" ".. _ref-IEC103maDIIndex:" "DI"

.. include-file:: sections/Include/IEC103ma_FunInf.rstinc "" ".. _ref-IEC103maDIFUN:" ".. _ref-IEC103maDIINF:" "DI" "receive object from"

   * :attr:     .. _ref-IEC103maDIQualifier:

                :xmlref:`Qualifier`
     :val:      0...255 or 0x00...0xFF
     :def:      0x00
     :desc:     Internal object qualifier to enable customized data processing.
		See table :numref:`docref-IEC103maDIQualifierBits` for internal object qualifier description.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

.. include-file:: sections/Include/DI_Idelays.rstinc "" ".. _ref-IEC103maDIInterDelay:" ".. _ref-IEC103maDIIndetDelay:"

.. include-file:: sections/Include/Total.rstinc "" ".. _ref-IEC103maDITotal:" ":ref:`<ref-IEC103maDIIndex>` and :ref:`<ref-IEC103maDIINF>`" ":ref:`DI<ref-IEC103maDI>`" "254"

.. include-file:: sections/Include/Name.rstinc ""

DI.Qualifier
^^^^^^^^^^^^

.. _docref-IEC103maDIQualifierBits:

.. include-file:: sections/Include/table_flags.rstinc "" "IEC60870-5-103 Master DI internal Qualifier" ":ref:`<ref-IEC103maDIQualifier>`" "DI internal qualifier"

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

   * :attr:     Bit 5
     :val:      xx0x.xxxx
     :desc:     Use time tag of the **last** event if Intermediate state of the Double Point object was not reported (because Intermediate state didn't exceed :ref:`<ref-IEC103maDIInterDelay>`). e.g. in transition ON->INTER->OFF time tag of the INTER->OFF event will be used.

   * :(attr):
     :val:      xx1x.xxxx
     :desc:     Use time tag of the **first** event if Intermediate state of the Double Point object was not reported (because Intermediate state didn't exceed :ref:`<ref-IEC103maDIInterDelay>`). e.g. in transition ON->INTER->OFF time tag of the ON->INTER event will be used.

   * :attr:     Bit 7
     :val:      0xxx.xxxx
     :desc:     DI is **enabled** and will be processed when received

   * :(attr):
     :val:      1xxx.xxxx
     :desc:     DI is **disabled** and will be discarded when received

   * :attr:     Bits 3;4;6
     :val:      Any
     :desc:     Bits reserved for future use
