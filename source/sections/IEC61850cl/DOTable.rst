
.. _ref-IEC61850clDO:

DOTable group and DO node
-------------------------

Group node :ref:`DOTable<ref-IEC61850clDO>` and child element nodes :ref:`DO<ref-IEC61850clDO>` are used to create DO information objects for sending control commands to IED.
Each created DO can be used as a destination for any DO information object defined in the IO table of any Slave protocol instance.
Command execution procedure is as follows: Slave protocol instance receives a control command from the upstream Master station and forwards to the destination DO object.
Current communication protocol instance validates and sends a command to IED based on the DO settings configured below.
Please refer to the section :ref:`docref-IEC10xslDOTable` for more information on how to use DO as a destination.

Please see sample :ref:`DOTable<ref-IEC61850clDO>` group and :ref:`DO<ref-IEC61850clDO>` child element nodes below.

.. code-block:: none

   <DOTable>
	<DO Index="0" ldInst="LD0" prefix="GNRL" lnClass="CSWI" lnInst="1" doName="Pos" fc="CO"/>
	<DO Index="1" ldInst="LD0" prefix="GNRL" lnClass="CSWI" lnInst="1" doName="BlkOpn" fc="CO"/>
   </DOTable>

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`DO<ref-IEC61850clDO>`"

.. code-block:: none

   <DO Index="0" ldInst="LD0" prefix="GNRL" lnClass="CSWI" lnInst="1" doName="Pos" fc="CO" Qualifier="0x00" Name="CB command" />

.. include-file:: sections/Include/tip_order.rstinc "" ":ref:`DO<ref-IEC61850clDO>`"

DO attributes
^^^^^^^^^^^^^

.. _ref-IEC61850clDOAttributes:

.. include-file:: sections/Include/table_attrs.rstinc "" "IEC61850 Client DO attributes"

.. include-file:: sections/Include/ma_Index.rstinc "" ".. _ref-IEC61850clDOIndex:" "DO"

.. include-file:: sections/Include/IEC61850cl_SCL.rstinc "" "'GNRL'" "'CSWI'" "'Pos'" "'A.phsA'" "'CO'"

   * :attr:     .. _ref-IEC61850clDOQualifier:

                :xmlref:`Qualifier`
     :val:      0...255 or 0x00...0xFF
     :def:      0x00
     :desc:     Internal object qualifier to enable customized data processing.
		See table :numref:`ref-IEC61850clDOqualifierBits` for internal object qualifier description.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

.. include-file:: sections/Include/Name.rstinc ""

DO.Qualifier
^^^^^^^^^^^^

.. _ref-IEC61850clDOqualifierBits:

.. include-file:: sections/Include/table_flags.rstinc "" "IEC61850 Client DO internal qualifier" ":ref:`<ref-IEC61850clDOQualifier>`" "DO internal qualifier"

   * :attr:     Bit 0
     :val:      xxxx.xxx0
     :desc:     DO object **will not** be inverted

   * :(attr):
     :val:      xxxx.xxx1
     :desc:     DO object **will** be inverted (OFF → ON; ON → OFF)

   * :attr:     Bit 1
     :val:      xxxx.xx0x
     :desc:     [Synchrocheck] control bit is **disabled** in outgoing DO command

   * :(attr):
     :val:      xxxx.xx1x
     :desc:     [Synchrocheck] control bit is **enabled** in outgoing DO command

   * :attr:     Bit 2
     :val:      xxxx.x0xx
     :desc:     [Interlock] control bit is **disabled** in outgoing DO command

   * :(attr):
     :val:      xxxx.x1xx
     :desc:     [Interlock] control bit is **enabled** in outgoing DO command

   * :attr:     Bit 7
     :val:      0xxx.xxxx
     :desc:     DO is **enabled**, command will be sent to IED

   * :(attr):
     :val:      1xxx.xxxx
     :desc:     DO is **disabled**, command will not be sent to IED

   * :attr:     Bits 3...6
     :val:      Any
     :desc:     Bits reserved for future use
