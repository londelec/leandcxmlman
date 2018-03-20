
.. _ref-IEC10xmaAOTable:
.. _ref-IEC10xmaAO:

AOTable group and AO node
-------------------------

Group node :ref:`AOTable<ref-IEC10xmaAOTable>` and child element nodes :ref:`AO<ref-IEC10xmaAO>` are used to create AO information objects for sending setpoint commands to the downstream outstation.
Each created AO can be used as a destination for any AO information object defined in the IO table of any Slave protocol instance.
Command execution procedure is as follows: Slave protocol instance receives a setpoint command from the upstream Master station and forwards to the destination AO object.
Current communication protocol instance validates and sends a command to the outstation based on the AO settings configured below.
Please refer to the section :ref:`docref-IEC10xslAOTable` for more information on how to use AO as a destination.

Please see sample :ref:`AOTable<ref-IEC10xmaAOTable>` group and :ref:`AO<ref-IEC10xmaAO>` child element nodes below.
There are 5 AO information objects configured using 4 :ref:`AO<ref-IEC10xmaAO>` element nodes.

.. code-block:: none

   <AOTable>
	<AO Index="0" InfAddr="1" TypeID="48"/>
	<AO Index="1" InfAddr="2" TypeID="49"/>
	<AO Index="2" InfAddr="3" Coeff="3.3"/>
	<AO Index="3" InfAddr="4" Total="2"/>
   </AOTable>

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`AO<ref-IEC10xmaAO>`"

.. code-block:: none

   <AO Index="0" InfAddr="1" qualifier="0x00" Coeff="11.6" TypeID="50" Total="2" Name="Filter value" />

.. include-file:: sections/Include/tip_order.rstinc "" ":ref:`AO<ref-IEC10xmaAO>`"

AO attributes
^^^^^^^^^^^^^

.. _ref-IEC10xmaAOAttributes:

.. include-file:: sections/Include/table_attrs.rstinc "" "IEC60870-5-101/104 Master AO attributes"

.. include-file:: sections/Include/ma_Index.rstinc "" ".. _ref-IEC10xmaAOIndex:" "AO"

.. include-file:: sections/Include/IEC10xma_IOA.rstinc "" ".. _ref-IEC10xmaAOInfAddr:" "AO" "send setpoint command to"

   * :attr:     .. _ref-IEC10xmaAOqualifier:

                :xmlref:`qualifier`
     :val:      0...255 or 0x00...0xFF
     :def:      0x00
     :desc:     Internal object qualifier to enable customized data processing.
		See table :numref:`ref-IEC10xmaAOqualifierBits` for internal object qualifier description.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

.. include-file:: sections/Include/AO_Coeff.rstinc "" ".. _ref-IEC10xmaAOCoeff:"

   * :attr:     .. _ref-IEC10xmaAOTypeID:

                :xmlref:`TypeID`
     :val:      See table :numref:`ref-IEC10xmaAOTypeIDValues`
     :def:      transparent
     :desc:     Send command with the defined ASDU Type.
		ASDU type is transparent if neither this attribute nor communication protocol generic attribute (e.g. IEC101ma or IEC104ma :ref:`<ref-IEC101maASDUSettings>`.\ :ref:`<ref-IEC101maASDUSettingsAOType>` \) is used.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration.`

.. include-file:: sections/Include/Total.rstinc "" ".. _ref-IEC10xmaAOTotal:" ":ref:`<ref-IEC10xmaAOIndex>` and :ref:`<ref-IEC10xmaAOInfAddr>`" ":ref:`AO<ref-IEC10xmaAO>`" "16777214"

.. include-file:: sections/Include/Name.rstinc ""

AO.qualifier
^^^^^^^^^^^^

.. _ref-IEC10xmaAOqualifierBits:

.. include-file:: sections/Include/table_flags.rstinc "" "IEC60870-5-101/104 Master AO internal qualifier" ":ref:`<ref-IEC10xmaAOqualifier>`" "AO internal qualifier"

   * :attr:     Bit 6
     :val:      x0xx.xxxx
     :desc:     **Direct-Execute** setpoint command will be sent

   * :(attr):
     :val:      x1xx.xxxx
     :desc:     **Select and Execute** setpoint commands will be sent

   * :attr:     Bit 7
     :val:      0xxx.xxxx
     :desc:     AO is **enabled**, command will be sent to outstation

   * :(attr):
     :val:      1xxx.xxxx
     :desc:     AO is **disabled**, command will not be sent to outstation

   * :attr:     Bits 0...5
     :val:      Any
     :desc:     Bits reserved for future use

AO.TypeID
^^^^^^^^^

.. _ref-IEC10xmaAOTypeIDValues:

.. field-list-table:: IEC60870-5-101/104 Master AO TypeID
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.20}|S{0.80}|
   :header-rows: 1

   * :attr,10: TypeID Value
     :desc,90: Description

   * :attr:     48
     :desc:     'Normalized setpoint command' will be sent (ASDU type 48 [:lectext1:`C_SE_NA_1`])

   * :attr:     49
     :desc:     'Scaled setpoint command' will be sent (ASDU type 49 [:lectext1:`C_SE_NB_1`])

   * :attr:     50
     :desc:     'Short floating point setpoint command' will be sent (ASDU type 50 [:lectext1:`C_SE_NC_1`])

   * :attr:     61
     :desc:     Only applicable to IEC60870-5-104 Master protocol instance;
                Time-tagged 'Normalized setpoint command' will be sent (ASDU type 61 [:lectext1:`C_SE_TA_1`])

   * :attr:     62
     :desc:     Only applicable to IEC60870-5-104 Master protocol instance;
                Time-tagged 'Scaled setpoint command' will be sent (ASDU type 62 [:lectext1:`C_SE_TB_1`])

   * :attr:     63
     :desc:     Only applicable to IEC60870-5-104 Master protocol instance;
                Time-tagged 'Short floating point setpoint command' will be sent (ASDU type 63 [:lectext1:`C_SE_TC_1`])

   * :attr:     Other
     :desc:     Transparent, ASDU TypeID of the outgoing command will be the same as received from upstream Master station
