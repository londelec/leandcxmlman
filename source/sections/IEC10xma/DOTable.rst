
.. _ref-IEC10xmaDOTable:
.. _ref-IEC10xmaDO:

DOTable group and DO node
-------------------------

Group node :ref:`DOTable<ref-IEC10xmaDOTable>` and child element nodes :ref:`DO<ref-IEC10xmaDO>` are used to create DO information objects for sending control command to the downstream outstation. 
Each created DO can be used as a destination for any DO information object defined in the IO table of any Slave protocol instance.
Command execution procedure is as follows: Slave protocol instance receives a control command from the upstream Master station and forwards to the destination DO object.
Current communication protocol instance validates and sends a command to the outstation based on the DO settings configured below.
Please refer to the section :ref:`docref-IEC10xslDOTable` for more information on how to use DO as a destination.

Please see sample :ref:`DOTable<ref-IEC10xmaDOTable>` group and :ref:`DO<ref-IEC10xmaDO>` child element nodes below.
There are 5 DO information objects configured using 4 :ref:`DO<ref-IEC10xmaDO>` element nodes.

.. code-block:: none

   <DOTable>
	<DO Index="0" InfAddr="1" qualifier="0x00" TypeID="45"/>
	<DO Index="1" InfAddr="2" qualifier="0x10" TypeID="46"/>
	<DO Index="2" InfAddr="3" qualifier="0x10" QOC="3"/>
	<DO Index="3" InfAddr="4" qualifier="0x00" Total="2"/>
   </DOTable>

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`DO<ref-IEC10xmaDO>`"

.. code-block:: none

   <DO Index="0" InfAddr="1" qualifier="0x00" QOC="0" TypeID="46" Total="2" Name="CB command" />

.. tip:: Attributes of the :ref:`DO<ref-IEC10xmaDO>` element node can be arranged in any order, it will not affect the XML file validation.         

DO attributes
^^^^^^^^^^^^^

.. _ref-IEC10xmaDOAttributes:

.. include-file:: sections/Include/table_attrs.rstinc "" "IEC60870-5-101/104 Master DO attributes"

.. include-file:: sections/Include/ma_Index.rstinc "" ".. _ref-IEC10xmaDOIndex:" "DO"

.. include-file:: sections/Include/IEC10xma_IOA.rstinc "" ".. _ref-IEC10xmaDOInfAddr:" "DO" "send control command to"

   * :attr:     .. _ref-IEC10xmaDOqualifier:

		:xmlref:`qualifier`
     :val:      0...255 or 0x00...0xFF
     :def:      0x00
     :desc:     Internal object qualifier to enable customized data processing.
		See table :numref:`ref-IEC10xmaDOqualifierBits` for internal object qualifier description.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:     .. _ref-IEC10xmaDOQOC:

                :xmlref:`QOC`
     :val:      0...255 or 0x00...0xFF
     :def:      0
     :desc:     Qualifier Of Command (QOC) is used to define specify short/long pulse information for the outgoing command.
		See table :numref:`ref-IEC10xmaDOQOCValues` values.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:     .. _ref-IEC10xmaDOTypeID:

                :xmlref:`TypeID`
     :val:      See table :numref:`ref-IEC10xmaDOTypeIDValues`
     :def:      transparent
     :desc:     Send command with the defined ASDU Type.
		ASDU type is transparent if neither this attribute nor communication protocol generic attribute (e.g. IEC101ma or IEC104ma :ref:`<ref-IEC101maASDUSettings>`.\ :ref:`<ref-IEC101maASDUSettingsDOType>` \) is used.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration.`

.. include-file:: sections/Include/IEC60870_Total.rstinc "" ".. _ref-IEC10xmaDOTotal:" ":ref:`Index<ref-IEC10xmaDOIndex>`" ":ref:`InfAddr<ref-IEC10xmaDOInfAddr>`" ":ref:`DO<ref-IEC10xmaDO>`" "16777214"

.. include-file:: sections/Include/Name.rstinc ""

DO.qualifier
^^^^^^^^^^^^

.. _ref-IEC10xmaDOqualifierBits:

.. include-file:: sections/Include/table_flags.rstinc "" " IEC60870-5-101/104 Master DO internal qualifier" ":ref:`<ref-IEC10xmaDOqualifier>`" "DO internal qualifier"

   * :attr:     Bit 0
     :val:      xxxx.xxx0
     :desc:     DO object **will not** be inverted

   * :(attr):
     :val:      xxxx.xxx1
     :desc:     DO object **will** be inverted (OFF → ON; ON → OFF)

   * :attr:     Bit 6
     :val:      x0xx.xxxx
     :desc:     **Direct Execute** control command will be sent

   * :(attr):
     :val:      x1xx.xxxx
     :desc:     **Select and Execute** control commands will be sent

   * :attr:     Bit 7
     :val:      0xxx.xxxx
     :desc:     DO is **enabled**, command will be sent to outstation

   * :(attr):
     :val:      1xxx.xxxx
     :desc:     DO is **disabled**, command will not be sent to outstation

   * :attr:     Bits 1...5
     :val:      Any
     :desc:     Bits reserved for future use

DO.TypeID
^^^^^^^^^

.. _ref-IEC10xmaDOTypeIDValues:

.. field-list-table:: IEC60870-5-101/104 Master DO TypeID
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.20}|S{0.80}|
   :header-rows: 1

   * :attr,10: TypeID Value
     :desc,90: Description

   * :attr:     45
     :desc:     'Single command' will be sent (ASDU type 45 [C_SC_NA_1])

   * :attr:     46
     :desc:     'Double command' will be sent (ASDU type 46 [C_DC_NA_1])

   * :attr:     47
     :desc:     'Regulating step command' will be sent (ASDU type 47 [C_RC_NA_1])

   * :attr:     58
     :desc:     Only applicable to IEC60870-5-104 Master protocol instance;
                Time-tagged 'Single command' will be sent (ASDU type 58 [C_SC_TA_1])

   * :attr:     59
     :desc:     Only applicable to IEC60870-5-104 Master protocol instance;
                Time-tagged 'Double command' will be sent (ASDU type 59 [C_DC_TA_1])

   * :attr:     60
     :desc:     Only applicable to IEC60870-5-104 Master protocol instance;
                Time-tagged 'Regulating step command' will be sent (ASDU type 60 [C_RC_TA_1])

   * :attr:     Other
     :desc:     Transparent, ASDU TypeID of the outgoing command will be the same as received from upstream Master station

DO.QOC
^^^^^^

.. _ref-IEC10xmaDOQOCValues:

.. field-list-table:: IEC60870-5-101/104 Master QOC
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.20}|S{0.80}|
   :header-rows: 1

   * :attr,10: QOC Values
     :desc,90: Description

   * :attr:     0
     :desc:     Command will be sent with [no additional definition]

   * :attr:     1
     :desc:     Command will be sent with [short-pulse duration]

   * :attr:     2
     :desc:     Command will be sent with [long-pulse duration]

   * :attr:     3
     :desc:     Command will be sent with [persistent output]

   * :attr:     128
     :desc:     Command will be sent with the same information as received from upstream station. This is a transparent mode.

   * :attr:     4...31
     :desc:     Reserved for [compatible range] and [private range] as per IEC60870-5-101 standard

   * :attr:     Other
     :desc:     Undefined, don't use
