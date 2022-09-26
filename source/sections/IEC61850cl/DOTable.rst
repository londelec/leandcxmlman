
.. _xmlgroup-IEC61850clDO: lelabel=DOTable
.. _xmlelem-IEC61850clDO: lelabel=DO

DOTable group
-------------

.. include-file:: sections/Include/ma_DOAO_table.rstinc "" ":ref:`xmlgroup-IEC61850clDO`" ":ref:`xmlelem-IEC61850clDO`" ":numref:`tabid-IEC61850clDO`" ":ref:`docref-IEC10xslDO`" "DO" "control" "IED"

Please see sample :ref:`xmlgroup-IEC61850clDO` group and :ref:`xmlelem-IEC61850clDO` element nodes below.
There are 2 control commands defined in this sample.

.. code-block:: none

   <DOTable>
	<DO Index="0" ldInst="LD0" prefix="GNRL" lnClass="CSWI" lnInst="1" doName="Pos" fc="CO"/>
	<DO Index="1" ldInst="LD0" prefix="GNRL" lnClass="CSWI" lnInst="1" doName="BlkOpn" fc="CO"/>
   </DOTable>

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-IEC61850clDO`"

.. code-block:: none

   <DO Index="0" ldInst="LD0" prefix="GNRL" lnClass="CSWI" lnInst="1" doName="Pos" fc="CO" Qualifier="0x00" Name="CB command" />

.. include-file:: sections/Include/tip_order.rstinc "" ":ref:`xmlelem-IEC61850clDO`"

DO attributes
^^^^^^^^^^^^^

.. include-file:: sections/Include/table_attrs.rstinc "" "tabid-IEC61850clDO" "IEC61850 Client DO attributes" ":spec: |C{0.12}|C{0.14}|C{0.1}|S{0.64}|"

.. include-file:: sections/Include/ma_Index.rstinc "" "DO"

.. include-file:: sections/Include/IEC61850cl_SCL.rstinc "" "'GNRL'" "'CSWI'" "'Pos'" "'A.phsA'" "'CO'"

.. include-file:: sections/Include/Qualifier.rstinc "" ":numref:`tabid-IEC61850clDOQualifier`"

.. include-file:: sections/Include/Name.rstinc ""

DO.Qualifier
^^^^^^^^^^^^

.. include-file:: sections/Include/table_flags8.rstinc "" "tabid-IEC61850clDOQualifier" "IEC61850 Client DO internal qualifier" ":ref:`xmlattr-IEC61850clDOQualifier`" "DO internal qualifier"

   * :attr:	Bit 0
     :val:	xxxx.xxx0
     :desc:	DO object **will not** be inverted

   * :(attr):
     :val:	xxxx.xxx1
     :desc:	DO object **will** be inverted (OFF → ON; ON → OFF)

   * :attr:	Bit 1
     :val:	xxxx.xx0x
     :desc:	[:lemonobgtext:`Synchrocheck`] control bit is **disabled** in outgoing DO command

   * :(attr):
     :val:	xxxx.xx1x
     :desc:	[:lemonobgtext:`Synchrocheck`] control bit is **enabled** in outgoing DO command

   * :attr:	Bit 2
     :val:	xxxx.x0xx
     :desc:	[:lemonobgtext:`Interlock`] control bit is **disabled** in outgoing DO command

   * :(attr):
     :val:	xxxx.x1xx
     :desc:	[:lemonobgtext:`Interlock`] control bit is **enabled** in outgoing DO command

   * :attr:	:bitdef:`6`
     :val:	x0xx.xxxx
     :desc:	[:lemonobgtext:`Test`] bit of the control structure is **cleared**

   * :(attr):
     :val:	x1xx.xxxx
     :desc:	[:lemonobgtext:`Test`] bit of the control structure is **set**

   * :attr:	Bit 7
     :val:	0xxx.xxxx
     :desc:	DO is **enabled**, command will be sent to IED

   * :(attr):
     :val:	1xxx.xxxx
     :desc:	DO is **disabled**, command will not be sent to IED

   * :attr:	Bits 3...5
     :val:	Any
     :desc:	Bits reserved for future use
