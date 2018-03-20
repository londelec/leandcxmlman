
.. _docref-IEC10xslDOTable:
.. _ref-IEC10xslDOTable:
.. _ref-IEC10xslDO:

DOTable group and DO node
-------------------------

Group node :ref:`DOTable<ref-IEC10xslDOTable>` and child element nodes :ref:`DO<ref-IEC10xslDO>` are used to create DO information objects to receive control 
commands from the upstream Master station.
Each created DO information object needs to have a destination to forward the control command.
The destination is created by linking DO information object to a :ref:`DO<ref-IEC10xslDO>` node of any Master protocol instance.
(Master protocol instances are defined in :ref:`CommunicationCfg<ref-CommunicationCfg>` group in **leandc.xml** file)

The link is created using :ref:`DO<ref-IEC10xslDO>`.\ :ref:`<ref-IEC10xslDODevice>` \ and :ref:`DO<ref-IEC10xslDO>`.\ :ref:`<ref-IEC10xslDOIndex>` \ attributes.
The first step is to select the **destination Master protocol instance**, use value of the :ref:`<ref-IEC101maIndex>` attribute of any Master protocol instance.
The next step is to select the **destination DO object**, use value of the :ref:`DO<ref-IEC10xslDO>`.\ :ref:`<ref-IEC10xslDOIndex>` \ attribute of any DO object listed in the IO object table of any Master protocol instance.
Enter the selected values of **destination Master protocol instance** in :ref:`DO<ref-IEC10xslDO>`.\ :ref:`<ref-IEC10xslDODevice>` \
attribute and **destination DO object** in :ref:`DO<ref-IEC10xslDO>`.\ :ref:`<ref-IEC10xslDOIndex>` \ attribute.

Information address (IOA) to receive control command is specified in :ref:`<ref-IEC10xslDOInfAddr>` \ attribute.

Please see sample :ref:`DOTable<ref-IEC10xslDOTable>` group and :ref:`DO<ref-IEC10xslDO>` child element nodes below.
There are 5 DO information objects configured using 4 :ref:`DO<ref-IEC10xslDO>` element nodes.

.. code-block:: none

   <DOTable>
	<DO Device="10" Index="0" InfAddr="1" Policy="0" … />
	<DO Device="10" Index="1" InfAddr="2" Policy="250" … />
	<DO Device="10" Index="-2" InfAddr="3" Policy="0" … />
	<DO Device="10" Index="2" InfAddr="4" Policy="0" Total="2" … />
   </DOTable>

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`DO<ref-IEC10xslDO>`"

.. code-block:: none

   <DO Device="10" Index="2" InfAddr="4" qualifier="0x10" Policy="0" TypeID="0" OffIndex="33" Total="2" Name="CB command" />

.. include-file:: sections/Include/tip_order.rstinc "" ":ref:`DO<ref-IEC10xslDO>`"

DO attributes
^^^^^^^^^^^^^

.. _ref-IEC10xslDOAttributes:

.. include-file:: sections/Include/table_attrs.rstinc "" "IEC60870-5-101/104 Slave DO attributes"

.. include-file:: sections/Include/IEC10xsl_Device.rstinc "" ".. _ref-IEC10xslDODevice:" "DO" "destination" "Destination"

   * :attr:     .. _ref-IEC10xslDOIndex:

                :xmlref:`Index`
     :val:      -8...2\ :sup:`32`\  - 8
     :def:      n/a
     :desc:     Destination DO object. Any DO element node of the selected Master protocol instance can be used as a destination.
		Use value of the :ref:`DO<ref-IEC10xmaDO>`.\ :ref:`Index<ref-IEC10xmaDOIndex>` \ attribute of any DO object listed in the IO table of the selected Master protocol instance.
		In addition to regular DOs there are internal controls available.
		Internal controls are used to change real-time state of the destination protocol instance.
		Each internal control has a service index and they are summarized in the table :numref:`ref-IEC10xslDOServiceIndex`.
		:inlinetip:`Indexes don't have to be arranged in ascending order.`

.. include-file:: sections/Include/IEC10xsl_IOA.rstinc "" ".. _ref-IEC10xslDOInfAddr:" "DO" "receive command from"

   * :attr:     .. _ref-IEC10xslDOqualifier:

                :xmlref:`qualifier`
     :val:      0...255 or 0x00...0xFF
     :def:      0x00
     :desc:     Internal object qualifier to enable customized data processing.
		See table :numref:`ref-IEC10xslDOqualifierBits` for internal object qualifier description.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:     .. _ref-IEC10xslDOPolicy:

                :xmlref:`Policy`
     :val:      0...255
     :def:      0
     :desc:     Command execution policy, see table :numref:`ref-IEC10xslPolicy` for description.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:     .. _ref-IEC10xslDOTypeID:

                :xmlref:`TypeID`
     :val:      See table :numref:`ref-IEC10xslDOTypeIDValues`
     :def:      0 = any
     :desc:     Only accept command if received with this ASDU Type.
		Value 0 disables ASDU type checking and any command is accepted.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:     .. _ref-IEC10xslDOOffIndex:

                :xmlref:`OffIndex`
     :val:      0...2\ :sup:`32`\  - 1
     :def:      Same as :ref:`<ref-IEC10xslDOIndex>`
     :desc:     Destination object for OFF command.
		Attribute enables feature to send ON and OFF commands to different destination objects.
		If ON command is received, it will be forwarded to destination object specified in :ref:`<ref-IEC10xslDOIndex>` attribute.
		If OFF command is received, it will be forwarded to destination object specified in :xmlref:`OffIndex` attribute.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, ON and OFF commands will be sent to the same destination object if this attribute is omitted.`

.. include-file:: sections/Include/Total.rstinc "" ".. _ref-IEC10xslDOTotal:" ":ref:`<ref-IEC10xslDOIndex>` and :ref:`<ref-IEC10xslDOInfAddr>`" ":ref:`DO<ref-IEC10xslDO>`" "16777214"

.. include-file:: sections/Include/Name.rstinc ""

DO.qualifier
^^^^^^^^^^^^

.. _ref-IEC10xslDOqualifierBits:

.. include-file:: sections/Include/table_flags.rstinc "" "IEC60870-5-101/104 Slave DO internal qualifier" ":ref:`<ref-IEC10xslDOqualifier>`" "DO internal qualifier"

   * :attr:     Bit 0
     :val:      xxxx.xxx0
     :desc:     DO object **will not** be inverted

   * :(attr):
     :val:      xxxx.xxx1
     :desc:     DI object **will** be inverted (OFF → ON; ON → OFF)

   * :attr:     Bits 6;5
     :val:      x00x.xxxx
     :desc:     **Direct-Execute** and **Select-before-Execute** commands are accepted

   * :(attr):
     :val:      x01x.xxxx
     :desc:     Only **Direct-Execute** commands are accepted

   * :(attr):
     :val:      x10x.xxxx
     :desc:     Only **Select-Before-Execute** commands are accepted

   * :(attr):
     :val:      x11x.xxxx
     :desc:     Reserved for future use

   * :attr:     Bit 7
     :val:      0xxx.xxxx
     :desc:     DO is **enabled** and command will be processed when received

   * :(attr):
     :val:      1xxx.xxxx
     :desc:     DO is **disabled** and command will be rejected when received

   * :attr:     Bits 1...4
     :val:      Any
     :desc:     Bits reserved for future use

DO.TypeID
^^^^^^^^^

.. _ref-IEC10xslDOTypeIDValues:

.. field-list-table:: IEC60870-5-101/104 Slave DO TypeID
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.20}|S{0.80}|
   :header-rows: 1

   * :attr,10: TypeID Value
     :desc,90: Description

   * :attr:     45
     :desc:     Only 'Single command' will be accepted and processed (ASDU type 45 [:lectext1:`C_SC_NA_1`])

   * :attr:     46
     :desc:     Only 'Double command' will be accepted and processed (ASDU type 46 [:lectext1:`C_DC_NA_1`])

   * :attr:     47
     :desc:     Only 'Regulating step command' will be accepted and processed (ASDU type 47 [:lectext1:`C_RC_NA_1`])

   * :attr:     58
     :desc:     Only applicable to IEC60870-5-104 Slave protocol instance;
                Only time-tagged 'Single command' will be accepted and processed (ASDU type 58 [:lectext1:`C_SC_TA_1`])

   * :attr:     59
     :desc:     Only applicable to IEC60870-5-104 Slave protocol instance;
                Only time-tagged 'Double command' will be accepted and processed (ASDU type 59 [:lectext1:`C_DC_TA_1`])

   * :attr:     60
     :desc:     Only applicable to IEC60870-5-104 Slave protocol instance;
                Only time-tagged 'Regulating step command' will be accepted and processed (ASDU type 59 [:lectext1:`C_RC_TA_1`])

   * :attr:     Other
     :desc:     Undefined, control command received with any ASDU type will be accepted


DO Service Indexes
^^^^^^^^^^^^^^^^^^

Service digital outputs are internal controls that enable to change operation state of communication protocol instances.
Service controls have negative index values and can be used just as any regular DO indexes.

.. _ref-IEC10xslDOServiceIndex:

.. field-list-table:: IEC60870-5-101/104 Slave Service DO indexes
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.25}|C{0.25}|S{0.5}|
   :header-rows: 1

   * :attr,10: Index value
     :val,10:  Object value
     :desc,80: Description

   * :attr:     -2
                (0xFFFFFFFE)
     :val:      ON or OFF
     :desc:     Only applicable to Master communication protocol instances; Send forced **Poll** (e.g. General Interrogation) to downstream outstation.

   * :attr:     -3
                (0xFFFFFFFD)
     :val:      ON
     :desc:     **Enable** communication to the station. This service index can be used for any protocol instance.

   * :(attr):
     :val:      OFF
     :desc:     **Disable** communication to the station. his service index can be used for any protocol instance.

   * :attr:     -4\*
                (0xFFFFFFFC)
     :val:      ON
     :desc:     **Start** communication to the downstream station. Refer to the comment below for the types of messages being sent.

   * :(attr):
     :val:      OFF
     :desc:     **Stop** communication to the downstream station. Refer to the comment below for the types of messages being sent.

   * :attr:     -5
                (0xFFFFFFFB)
     :val:      ON or OFF
     :desc:     Only applicable to IEC60870-5-101/104 Master communication protocol instances; Send **Reset Process** command (ASDU type 105 [:lectext1:`C_RP_NA_1`]) to the downstream station

   * :attr:     -1 and -6...-8
     :val:      Any
     :desc:     Service commands reserved for future use

.. tip::

   | \* This service command only applies to the following protocol instances:
   | IEC60870-5-104 controlling station (Master) send [:lectext1:`STARTDT_act`] or [:lectext1:`STOPDT_act`] to the downstream station;
   | IEC61850 Client send MMS [:lectext1:`Initiate-RequestPDU`] or [:lectext1:`Conclude-RequestPDU`] to the IED;
