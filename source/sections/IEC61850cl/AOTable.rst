
.. _ref-IEC61850clAO:

AOTable group and AO node
-------------------------

Group node :ref:`AOTable<ref-IEC61850clAO>` and child element nodes :ref:`AO<ref-IEC61850clAO>` are used to create AO information objects for sending setpoint commands to IED.
Each created AO can be used as a destination for any AO information object defined in the IO table of any Slave protocol instance.
Command execution procedure is as follows: Slave protocol instance receives a setpoint command from the upstream Master station and forwards to the destination AO object.
Current communication protocol instance validates and sends a command to IED based on the AO settings configured below.
Please refer to the section :ref:`docref-IEC10xslAOTable` for more information on how to use AO as a destination.

Please see sample :ref:`AOTable<ref-IEC61850clAO>` group and :ref:`AO<ref-IEC61850clAO>` child element nodes below.

.. code-block:: none

   <AOTable>
	<AO Index="0" ldInst="LD0" prefix="GNRL" lnClass="CSWI" lnInst="1" doName="Mod" fc="CO"/>
   </AOTable>

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`AO<ref-IEC61850clAO>`"

.. code-block:: none

   <AO Index="0" ldInst="LD0" prefix="GNRL" lnClass="CSWI" lnInst="1" doName="Mod" fc="CO" Qualifier="0x00" Coeff="1" Name="Mode and Behavior" />

.. include-file:: sections/Include/tip_order.rstinc "" ":ref:`AO<ref-IEC61850clAO>`"

AO attributes
^^^^^^^^^^^^^

.. _ref-IEC61850clAOAttributes:

.. include-file:: sections/Include/table_attrs.rstinc "" "IEC61850 Client AO attributes"

.. include-file:: sections/Include/ma_Index.rstinc "" ".. _ref-IEC61850clAOIndex:" "AO"

.. include-file:: sections/Include/IEC61850cl_SCL.rstinc "" "'GNRL'" "'CSWI'" "'Mod'" "'A.phsA'" "'CO'"

   * :attr:     .. _ref-IEC61850clAOqualifier:

                :xmlref:`Qualifier`
     :val:      0...255 or 0x00...0xFF
     :def:      0x00
     :desc:     Internal object qualifier to enable customized data processing.
		See table :numref:`ref-IEC61850clAOqualifierBits` for internal object qualifier description.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

.. include-file:: sections/Include/AO_Coeff.rstinc "" ".. _ref-IEC61850clAOCoeff:"

.. include-file:: sections/Include/Name.rstinc ""

AO.Qualifier
^^^^^^^^^^^^

.. _ref-IEC61850clAOqualifierBits:

.. include-file:: sections/Include/table_flags.rstinc "" "IEC61850 Client AO internal qualifier" ":ref:`<ref-IEC61850clAOqualifier>`" "AO internal qualifier"

   * :attr:     Bit 7
     :val:      0xxx.xxxx
     :desc:     AO is **enabled**, command will be sent to IED

   * :(attr):
     :val:      1xxx.xxxx
     :desc:     AO is **disabled**, command will not be sent to IED

   * :attr:     Bits 0...6
     :val:      Any
     :desc:     Bits reserved for future use
