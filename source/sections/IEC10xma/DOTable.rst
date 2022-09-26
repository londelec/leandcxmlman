
.. _xmlgroup-IEC10xmaDO: lelabel=DOTable
.. _xmlelem-IEC10xmaDO: lelabel=DO

DOTable group
-------------

.. include-file:: sections/Include/ma_DOAO_table.rstinc "" ":ref:`xmlgroup-IEC10xmaDO`" ":ref:`xmlelem-IEC10xmaDO`" ":numref:`tabid-IEC10xmaDO`" ":ref:`docref-IEC10xslDO`" "DO" "control" "outstation"

Please see sample :ref:`xmlgroup-IEC10xmaDO` group and :ref:`xmlelem-IEC10xmaDO` element nodes below.
There are 5 control commands defined with 4 :ref:`xmlelem-IEC10xmaDO` element nodes.

.. code-block:: none

   <DOTable>
	<DO Index="0" InfAddr="1" qualifier="0x00" TypeID="45"/>
	<DO Index="1" InfAddr="2" qualifier="0x10" TypeID="46"/>
	<DO Index="2" InfAddr="3" qualifier="0x10" QOC="3"/>
	<DO Index="3" InfAddr="4" qualifier="0x00" Total="2"/>
   </DOTable>

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-IEC10xmaDO`"

.. code-block:: none

   <DO Index="0" InfAddr="1" qualifier="0x00" QOC="0" TypeID="46" Total="2" Name="CB command" />

.. include-file:: sections/Include/tip_order.rstinc "" ":ref:`xmlelem-IEC10xmaDO`"

DO attributes
^^^^^^^^^^^^^

.. include-file:: sections/Include/table_attrs.rstinc "" "tabid-IEC10xmaDO" "IEC60870-5-101/104 Master DO attributes" ":spec: |C{0.12}|C{0.14}|C{0.12}|S{0.62}|"

.. include-file:: sections/Include/ma_Index.rstinc "" "DO"

.. include-file:: sections/Include/IEC10xma_IOA.rstinc "" "DO" "send control command to"

.. include-file:: sections/Include/IEC60870_qualifier.rstinc "" ":numref:`tabid-IEC10xmaDOqualifier`"

   * :attr:	:xmlattr:`QOC`
     :val:	|flags8range|
     :def:	0
     :desc:	Qualifier Of Command (QOC) is used to define specify short/long pulse information for the outgoing command.
		See :numref:`tabid-IEC10xmaDOQOC` values.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

.. include-file:: sections/Include/IEC10xma_DOAO_TypeID.rstinc "" ":numref:`tabid-IEC10xmaDOTypeID`" ":ref:`xmlattr-IEC101maAsduDOType`"

.. include-file:: sections/Include/Total.rstinc "" ":ref:`xmlattr-IEC10xmaDOIndex` and :ref:`xmlattr-IEC10xmaDOInfAddr`" ":ref:`xmlelem-IEC10xmaDO`" "16777214"

.. include-file:: sections/Include/Name.rstinc ""

DO.qualifier
^^^^^^^^^^^^

.. include-file:: sections/Include/table_flags8.rstinc "" "tabid-IEC10xmaDOqualifier" "IEC60870-5-101/104 Master DO internal qualifier" ":ref:`xmlattr-IEC10xmaDOqualifier`" "DO internal qualifier"

   * :attr:	:bitdef:`0`
     :val:	xxxx.xxx0
     :desc:	DO object **will not** be inverted

   * :(attr):
     :val:	xxxx.xxx1
     :desc:	DO object **will** be inverted (OFF → ON; ON → OFF)

   * :attr:	Bit 6
     :val:	x0xx.xxxx
     :desc:	**Direct Execute** control command will be sent

   * :(attr):
     :val:	x1xx.xxxx
     :desc:	**Select and Execute** control commands will be sent

   * :attr:	Bit 7
     :val:	0xxx.xxxx
     :desc:	DO is **enabled**, command will be sent to outstation

   * :(attr):
     :val:	1xxx.xxxx
     :desc:	DO is **disabled**, command will not be sent to outstation

   * :attr:	Bits 1...5
     :val:	Any
     :desc:	Bits reserved for future use

DO.TypeID
^^^^^^^^^

.. field-list-table:: IEC60870-5-101/104 Master DO TypeID
   :class: table table-condensed table-bordered longtable
   :name: tabid-IEC10xmaDOTypeID
   :spec: |C{0.16}|S{0.84}|
   :header-rows: 1

   * :attr,10: TypeID Value
     :desc,90: Description

   * :attr:	45
     :desc:	'Single command' will be sent (ASDU type 45 [:lemonobgtext:`C_SC_NA_1`])

   * :attr:	46
     :desc:	'Double command' will be sent (ASDU type 46 [:lemonobgtext:`C_DC_NA_1`])

   * :attr:	47
     :desc:	'Regulating step command' will be sent (ASDU type 47 [:lemonobgtext:`C_RC_NA_1`])

   * :attr:	58
     :desc:	Only applicable to IEC60870-5-104 Master protocol instance;
                Time-tagged 'Single command' will be sent (ASDU type 58 [:lemonobgtext:`C_SC_TA_1`])

   * :attr:	59
     :desc:	Only applicable to IEC60870-5-104 Master protocol instance;
                Time-tagged 'Double command' will be sent (ASDU type 59 [:lemonobgtext:`C_DC_TA_1`])

   * :attr:	60
     :desc:	Only applicable to IEC60870-5-104 Master protocol instance;
                Time-tagged 'Regulating step command' will be sent (ASDU type 60 [:lemonobgtext:`C_RC_TA_1`])

   * :attr:	Other
     :desc:	Transparent, ASDU TypeID of the outgoing command will be the same as received from upstream Master station

DO.QOC
^^^^^^

.. field-list-table:: IEC60870-5-101/104 Master QOC
   :class: table table-condensed table-bordered longtable
   :name: tabid-IEC10xmaDOQOC
   :spec: |C{0.16}|S{0.84}|
   :header-rows: 1

   * :attr,10: QOC Values
     :desc,90: Description

   * :attr:	0
     :desc:	Command will be sent with [:lemonobgtext:`no additional definition`]

   * :attr:	1
     :desc:	Command will be sent with [:lemonobgtext:`short-pulse duration`]

   * :attr:	2
     :desc:	Command will be sent with [:lemonobgtext:`long-pulse duration`]

   * :attr:	3
     :desc:	Command will be sent with [:lemonobgtext:`persistent output`]

   * :attr:	128
     :desc:	Command will be sent with the same information as received from upstream station. This is a transparent mode.

   * :attr:	4...31
     :desc:	Reserved for [:lemonobgtext:`compatible range`] and [:lemonobgtext:`private range`] as per IEC60870-5-101 standard

   * :attr:	Other
     :desc:	Undefined, don't use
