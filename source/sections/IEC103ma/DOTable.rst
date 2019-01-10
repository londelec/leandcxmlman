
.. _ref-IEC103maDOTable:
.. _ref-IEC103maDO:

DOTable group and DO node
-------------------------

Group node :ref:`DOTable<ref-IEC103maDOTable>` and child element nodes :ref:`DO<ref-IEC103maDO>` are used to create DO information objects to send control
command to the downstream outstation. Each created DO information object can be used as a destination for
any DO information object defined in IO table of the Slave protocol instances. If used as a destination,
procedure is as follows: Slave protocol instance receives control command from the upstream Master station
and forwards to destination DO information object. Then current communication protocol instance prepares and
sends command to the outstation based on DO information object settings. Please refer to the
section :ref:`DOTable<ref-IEC10xslDOTable>` for more information on how to use DO information object as a destination.

In order to send a control command to downstream outstation [:lemonobgtext:`FUNCTION TYPE`] and [:lemonobgtext:`INFORMATION NUMBER`]
has to be specified in :ref:`<ref-IEC103maDOFUN>` \ and :ref:`<ref-IEC103maDOINF>` \ attributes.

Please see sample :ref:`DOTable<ref-IEC103maDOTable>` group and :ref:`DO<ref-IEC103maDO>` child element nodes below.
There are 5 DO information objects configured using 4 :ref:`DO<ref-IEC103maDO>` element nodes.

.. code-block:: none

   <DOTable>
	<DO Index="0" FUN="1" INF="1" Qualifier="0x00"/>
	<DO Index="1" FUN="1" INF="2" Qualifier="0x10"/>
	<DO Index="2" FUN="240" INF="55" Qualifier="0x10"/>
	<DO Index="3" FUN="240" INF="56" Qualifier="0x00" Total="2"/>
   </DOTable>

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`DO<ref-IEC103maDO>`"

.. code-block:: none

   <DO Index="0" FUN="1" INF="1" Qualifier="0x00" Total="2" Name="CB position" />

.. include-file:: sections/Include/tip_order.rstinc "" ":ref:`DO<ref-IEC103maDO>`"

DO attributes
^^^^^^^^^^^^^

.. _docref-IEC103maDOAttributes:

.. include-file:: sections/Include/table_attrs.rstinc "" "IEC60870-5-103 Master DO attributes" ":spec: |C{0.12}|C{0.14}|C{0.1}|S{0.64}|"

.. include-file:: sections/Include/ma_Index.rstinc "" ".. _ref-IEC103maDOIndex:" "DO"

.. include-file:: sections/Include/IEC103ma_FunInf.rstinc "" ".. _ref-IEC103maDOFUN:" ".. _ref-IEC103maDOINF:" "DO" "send command to"

   * :attr:     .. _ref-IEC103maDOQualifier:

                :xmlref:`Qualifier`
     :val:      0...255 or 0x00...0xFF
     :def:      0x00
     :desc:     Internal object qualifier to enable customized data processing.
		See table :numref:`docref-IEC103maDOQualifierBits` for internal object qualifier description.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

.. include-file:: sections/Include/Total.rstinc "" ".. _ref-IEC103maDOTotal:" ":ref:`<ref-IEC103maDOIndex>` and :ref:`<ref-IEC103maDOINF>`" ":ref:`DO<ref-IEC103maDO>`" "254"

.. include-file:: sections/Include/Name.rstinc ""

DO.Qualifier
^^^^^^^^^^^^

.. _docref-IEC103maDOQualifierBits:

.. include-file:: sections/Include/table_flags.rstinc "" "IEC60870-5-103 Master DO internal Qualifier" ":ref:`<ref-IEC103maDOQualifier>`" "DO internal qualifier"

   * :attr:     Bit 0
     :val:      xxxx.xxx0
     :desc:     DO object **will not** be inverted

   * :(attr):
     :val:      xxxx.xxx1
     :desc:     DO object **will** be inverted (OFF → ON; ON → OFF)

   * :attr:     Bit 7
     :val:      0xxx.xxxx
     :desc:     DO is **enabled**, command will be sent to outstation

   * :(attr):
     :val:      1xxx.xxxx
     :desc:     DO is **disabled**, command will not be sent to outstation

   * :attr:     Bits 1...6
     :val:      Any
     :desc:     Bits reserved for future use
