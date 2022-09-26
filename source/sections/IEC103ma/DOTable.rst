
.. _xmlgroup-IEC103maDO: lelabel=DOTable
.. _xmlelem-IEC103maDO: lelabel=DO

DOTable group
-------------

.. include-file:: sections/Include/ma_DOAO_table.rstinc "" ":ref:`xmlgroup-IEC103maDO`" ":ref:`xmlelem-IEC103maDO`" ":numref:`tabid-IEC103maDO`" ":ref:`docref-IEC10xslDO`" "DO" "control" "IED"

In order to send a control command [:lemonobgtext:`FUNCTION TYPE`] and [:lemonobgtext:`INFORMATION NUMBER`] has to be specified in :ref:`xmlattr-IEC103maDOFUN` \ and :ref:`xmlattr-IEC103maDOINF` \ attributes.

Please see sample :ref:`xmlgroup-IEC103maDO` group and :ref:`xmlelem-IEC103maDO` element nodes below.
There are 5 control commands defined with 4 :ref:`xmlelem-IEC103maDO` element nodes.

.. code-block:: none

   <DOTable>
	<DO Index="0" FUN="1" INF="1" Qualifier="0x00"/>
	<DO Index="1" FUN="1" INF="2" Qualifier="0x10"/>
	<DO Index="2" FUN="240" INF="55" Qualifier="0x10"/>
	<DO Index="3" FUN="240" INF="56" Qualifier="0x00" Total="2"/>
   </DOTable>

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-IEC103maDO`"

.. code-block:: none

   <DO Index="0" FUN="1" INF="1" Qualifier="0x00" Total="2" Name="CB position" />

.. include-file:: sections/Include/tip_order.rstinc "" ":ref:`xmlelem-IEC103maDO`"

DO attributes
^^^^^^^^^^^^^

.. include-file:: sections/Include/table_attrs.rstinc "" "tabid-IEC103maDO" "IEC60870-5-103 Master DO attributes" ":spec: |C{0.12}|C{0.14}|C{0.1}|S{0.64}|"

.. include-file:: sections/Include/ma_Index.rstinc "" "DO"

.. include-file:: sections/Include/IEC103ma_FunInf.rstinc "" "DO" "send command to"

.. include-file:: sections/Include/Qualifier.rstinc "" ":numref:`tabid-IEC103maDOQualifier`"

.. include-file:: sections/Include/Total.rstinc "" ":ref:`xmlattr-IEC103maDOIndex` and :ref:`xmlattr-IEC103maDOINF`" ":ref:`xmlelem-IEC103maDO`" "254"

.. include-file:: sections/Include/Name.rstinc ""

DO.Qualifier
^^^^^^^^^^^^

.. include-file:: sections/Include/table_flags8.rstinc "" "tabid-IEC103maDOQualifier" "IEC60870-5-103 Master DO internal Qualifier" ":ref:`xmlattr-IEC103maDOQualifier`" "DO internal qualifier"

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
