
.. _xmlgroup-IEC10xmaAO: lelabel=AOTable
.. _xmlelem-IEC10xmaAO: lelabel=AO

AOTable group
-------------

.. include-file:: sections/Include/ma_DOAO_table.rstinc "" ":ref:`xmlgroup-IEC10xmaAO`" ":ref:`xmlelem-IEC10xmaAO`" ":numref:`tabid-IEC10xmaAO`" ":ref:`docref-IEC10xslAO`" "AO" "setpoint" "outstation"

Please see sample :ref:`xmlgroup-IEC10xmaAO` group and :ref:`xmlelem-IEC10xmaAO` element nodes below.
There are 5 setpoint commands defined with 4 :ref:`xmlelem-IEC10xmaAO` element nodes.

.. code-block:: none

   <AOTable>
	<AO Index="0" InfAddr="1" TypeID="48"/>
	<AO Index="1" InfAddr="2" TypeID="49"/>
	<AO Index="2" InfAddr="3" Coeff="3.3"/>
	<AO Index="3" InfAddr="4" Total="2"/>
   </AOTable>

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-IEC10xmaAO`"

.. code-block:: none

   <AO Index="0" InfAddr="1" qualifier="0x00" Coeff="11.6" TypeID="50" Total="2" Name="Filter value" />

.. include-file:: sections/Include/tip_order.rstinc "" ":ref:`xmlelem-IEC10xmaAO`"

AO attributes
^^^^^^^^^^^^^

.. include-file:: sections/Include/table_attrs.rstinc "" "tabid-IEC10xmaAO" "IEC60870-5-101/104 Master AO attributes" ":spec: |C{0.12}|C{0.16}|C{0.12}|S{0.6}|"

.. include-file:: sections/Include/ma_Index.rstinc "" "AO"

.. include-file:: sections/Include/IEC10xma_IOA.rstinc "" "AO" "send setpoint command to"

.. include-file:: sections/Include/IEC60870_qualifier.rstinc "" ":numref:`tabid-IEC10xmaAOqualifier`"

.. include-file:: sections/Include/AO_Coeff.rstinc ""

.. include-file:: sections/Include/IEC10xma_DOAO_TypeID.rstinc "" ":numref:`tabid-IEC10xmaAOTypeID`" ":ref:`xmlattr-IEC101maAsduAOType`"

.. include-file:: sections/Include/Total.rstinc "" ":ref:`xmlattr-IEC10xmaAOIndex` and :ref:`xmlattr-IEC10xmaAOInfAddr`" ":ref:`xmlelem-IEC10xmaAO`" "16777214"

.. include-file:: sections/Include/Name.rstinc ""

AO.qualifier
^^^^^^^^^^^^

.. include-file:: sections/Include/table_flags8.rstinc "" "tabid-IEC10xmaAOqualifier" "IEC60870-5-101/104 Master AO internal qualifier" ":ref:`xmlattr-IEC10xmaAOqualifier`" "AO internal qualifier"

   * :attr:	Bit 6
     :val:	x0xx.xxxx
     :desc:	**Direct-Execute** setpoint command will be sent

   * :(attr):
     :val:	x1xx.xxxx
     :desc:	**Select and Execute** setpoint commands will be sent

   * :attr:	Bit 7
     :val:	0xxx.xxxx
     :desc:	AO is **enabled**, command will be sent to outstation

   * :(attr):
     :val:	1xxx.xxxx
     :desc:	AO is **disabled**, command will not be sent to outstation

   * :attr:	Bits 0...5
     :val:	Any
     :desc:	Bits reserved for future use

AO.TypeID
^^^^^^^^^

.. field-list-table:: IEC60870-5-101/104 Master AO TypeID
   :class: table table-condensed table-bordered longtable
   :name: tabid-IEC10xmaAOTypeID
   :spec: |C{0.16}|S{0.84}|
   :header-rows: 1

   * :attr,10,center:	:ref:`xmlattr-IEC10xmaAOTypeID`
     :desc,90:		Description

   * :attr:	48
     :desc:	'Normalized setpoint command' will be sent (ASDU type 48 [:lemonobgtext:`C_SE_NA_1`])

   * :attr:	49
     :desc:	'Scaled setpoint command' will be sent (ASDU type 49 [:lemonobgtext:`C_SE_NB_1`])

   * :attr:	50
     :desc:	'Short floating point setpoint command' will be sent (ASDU type 50 [:lemonobgtext:`C_SE_NC_1`])

   * :attr:	61
     :desc:	Only applicable to IEC60870-5-104 Master protocol instance;
                Time-tagged 'Normalized setpoint command' will be sent (ASDU type 61 [:lemonobgtext:`C_SE_TA_1`])

   * :attr:	62
     :desc:	Only applicable to IEC60870-5-104 Master protocol instance;
                Time-tagged 'Scaled setpoint command' will be sent (ASDU type 62 [:lemonobgtext:`C_SE_TB_1`])

   * :attr:	63
     :desc:	Only applicable to IEC60870-5-104 Master protocol instance;
                Time-tagged 'Short floating point setpoint command' will be sent (ASDU type 63 [:lemonobgtext:`C_SE_TC_1`])

   * :attr:	Other
     :desc:	Transparent, ASDU TypeID of the outgoing command will be the same as received from upstream Master station
