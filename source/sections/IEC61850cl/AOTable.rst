
.. _xmlgroup-IEC61850clAO: lelabel=AOTable
.. _xmlelem-IEC61850clAO: lelabel=AO

AOTable group
-------------

.. include-file:: sections/Include/ma_DOAO_table.rstinc "" ":ref:`xmlgroup-IEC61850clAO`" ":ref:`xmlelem-IEC61850clAO`" ":numref:`tabid-IEC61850clAO`" ":ref:`docref-IEC10xslAO`" "AO" "setpoint" "IED"

Please see sample :ref:`xmlgroup-IEC61850clAO` group and :ref:`xmlelem-IEC61850clAO` element nodes below.
There is 1 setpoint command defined in this sample.

.. code-block:: none

   <AOTable>
	<AO Index="0" ldInst="LD0" prefix="GNRL" lnClass="CSWI" lnInst="1" doName="Mod" fc="CO"/>
   </AOTable>

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-IEC61850clAO`"

.. code-block:: none

   <AO Index="0" ldInst="LD0" prefix="GNRL" lnClass="CSWI" lnInst="1" doName="Mod" fc="CO" Qualifier="0x00" Coeff="1" Name="Mode and Behavior" />

.. include-file:: sections/Include/tip_order.rstinc "" ":ref:`xmlelem-IEC61850clAO`"

AO attributes
^^^^^^^^^^^^^

.. include-file:: sections/Include/table_attrs.rstinc "" "tabid-IEC61850clAO" "IEC61850 Client AO attributes" ":spec: |C{0.12}|C{0.14}|C{0.1}|S{0.64}|"

.. include-file:: sections/Include/ma_Index.rstinc "" "AO"

.. include-file:: sections/Include/IEC61850cl_SCL.rstinc "" "'GNRL'" "'CSWI'" "'Mod'" "'A.phsA'" "'CO'"

.. include-file:: sections/Include/Qualifier.rstinc "" ":numref:`tabid-IEC61850clAOQualifier`"

.. include-file:: sections/Include/AO_Coeff.rstinc ""

.. include-file:: sections/Include/Name.rstinc ""

AO.Qualifier
^^^^^^^^^^^^

.. include-file:: sections/Include/table_flags8.rstinc "" "tabid-IEC61850clAOQualifier" "IEC61850 Client AO internal qualifier" ":ref:`xmlattr-IEC61850clAOqualifier`" "AO internal qualifier"

   * :attr:	:bitdef:`1`
     :val:	xxxx.xx0x
     :desc:	[:lemonobgtext:`Synchrocheck`] control bit is **disabled** in outgoing AO command

   * :(attr):
     :val:	xxxx.xx1x
     :desc:	[:lemonobgtext:`Synchrocheck`] control bit is **enabled** in outgoing AO command

   * :attr:	:bitdef:`2`
     :val:	xxxx.x0xx
     :desc:	[:lemonobgtext:`Interlock`] control bit is **disabled** in outgoing AO command

   * :(attr):
     :val:	xxxx.x1xx
     :desc:	[:lemonobgtext:`Interlock`] control bit is **enabled** in outgoing AO command

   * :attr:	Bit 6
     :val:	x0xx.xxxx
     :desc:	[:lemonobgtext:`Test`] bit of the control structure is **cleared**

   * :(attr):
     :val:	x1xx.xxxx
     :desc:	[:lemonobgtext:`Test`] bit of the control structure is **set**

   * :attr:	Bit 7
     :val:	0xxx.xxxx
     :desc:	AO is **enabled**, command will be sent to IED

   * :(attr):
     :val:	1xxx.xxxx
     :desc:	AO is **disabled**, command will not be sent to IED

   * :attr:	Bits 0;3;4
     :val:	Any
     :desc:	Bits reserved for future use
