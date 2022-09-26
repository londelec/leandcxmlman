
.. _docref-IEC10xslDO:
.. _xmlgroup-IEC10xslDO: lelabel=DOTable
.. _xmlelem-IEC10xslDO: lelabel=DO

DOTable group
-------------

.. include-file:: sections/Include/IEC10xsl_DOAO_table.rstinc "" ":ref:`xmlgroup-IEC10xslDO`" ":ref:`xmlelem-IEC10xslDO`" ":numref:`tabid-IEC10xslDO`" "DO" "control"

| The link is created using :ref:`xmlelem-IEC10xslDO`.\ :ref:`xmlattr-IEC10xslDODevice` and :ref:`xmlelem-IEC10xslDO`.\ :ref:`xmlattr-IEC10xslDOIndex` attributes as follows:
| 1. Select the **destination Master protocol instance** - use value of the :ref:`xmlattr-gp101maIndex` attribute of any Master protocol instance and enter this value in :ref:`xmlelem-IEC10xslDO`.\ :ref:`xmlattr-IEC10xslDODevice` attribute.
| 2. Select the **destination DO object** - use value of the :ref:`xmlelem-IEC10xmaDO`.\ :ref:`xmlattr-IEC10xmaDOIndex` attribute of any DO object listed in the IO object table of a Master protocol instance enter this value in :ref:`xmlelem-IEC10xslDO`.\ :ref:`xmlattr-IEC10xslDOIndex` \ attribute.

Information object address (IOA) to receive the control command is specified in the :ref:`xmlattr-IEC10xslDOInfAddr` attribute.

Please see sample :ref:`xmlgroup-IEC10xslDO` group and :ref:`xmlelem-IEC10xslDO` element nodes below.
There are 5 control commands defined with 4 :ref:`xmlelem-IEC10xslDO` element nodes.

.. code-block:: none

   <DOTable>
	<DO Device="10" Index="0" InfAddr="1" Policy="0" … />
	<DO Device="10" Index="1" InfAddr="2" Policy="250" … />
	<DO Device="10" Index="-2" InfAddr="3" Policy="0" … />
	<DO Device="10" Index="2" InfAddr="4" Policy="0" Total="2" … />
   </DOTable>

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-IEC10xslDO`"

.. code-block:: none

   <DO Device="10" Index="2" InfAddr="4" qualifier="0x10" Policy="0" TypeID="0" OffIndex="33" Total="2" Name="CB command" />

.. include-file:: sections/Include/tip_order.rstinc "" ":ref:`xmlelem-IEC10xslDO`"

DO attributes
^^^^^^^^^^^^^

.. include-file:: sections/Include/table_attrs.rstinc "" "tabid-IEC10xslDO" "IEC60870-5-101/104 Slave DO attributes" ":spec: |C{0.14}|C{0.16}|C{0.1}|S{0.6}|"

.. include-file:: sections/Include/IEC10xsl_Device.rstinc "" ":xmlattr:`Device`" "destination for this DO object" "Destination"

   * :attr:	:xmlattr:`Index`
     :val:	|slindexrange|
     :def:	n/a
     :desc:	Destination DO object. Any DO element of the selected Master protocol instance can be used as a destination.
		Use value of the :ref:`xmlelem-IEC10xmaDO`.\ :ref:`xmlattr-IEC10xmaDOIndex` attribute of any DO object listed in the IO table of the selected Master protocol instance.
		In addition to regular DOs there are internal controls available.
		Internal controls are used to change real-time state of the destination protocol instance.
		Each internal control has a service index and they are summarized in the :numref:`tabid-IEC10xslDOServiceIndex`.
		:inlinetip:`Indexes don't have to be arranged in ascending order.`

.. include-file:: sections/Include/IEC10xsl_IOA.rstinc "" "DO" "receive command from"

.. include-file:: sections/Include/IEC60870_qualifier.rstinc "" ":numref:`tabid-IEC10xslDOqualifier`"

.. include-file:: sections/Include/IEC10xsl_Policy.rstinc ""

.. include-file:: sections/Include/IEC10xsl_TypeID.rstinc "" ":numref:`tabid-IEC10xslDOTypeID`"

   * :attr:	:xmlattr:`OffIndex`
     :val:	0...2\ :sup:`32`\  - 1
     :def:	Same as :ref:`xmlattr-IEC10xslDOIndex`
     :desc:	Destination object for OFF command.
		Attribute enables feature to send ON and OFF commands to different destination objects.
		If ON command is received, it will be forwarded to destination object specified in :ref:`xmlattr-IEC10xslDOIndex` attribute.
		If OFF command is received, it will be forwarded to destination object specified in :ref:`xmlattr-IEC10xslDOOffIndex` attribute.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, ON and OFF commands will be sent to the same destination object if this attribute is omitted.`

.. include-file:: sections/Include/Total.rstinc "" ":ref:`xmlattr-IEC10xslDOIndex` and :ref:`xmlattr-IEC10xslDOInfAddr`" ":ref:`xmlelem-IEC10xslDO`" "16777214"

.. include-file:: sections/Include/Name.rstinc ""

DO.qualifier
^^^^^^^^^^^^

.. include-file:: sections/Include/table_flags8.rstinc "" "tabid-IEC10xslDOqualifier" "IEC60870-5-101/104 Slave DO internal qualifier" ":ref:`xmlattr-IEC10xslDOqualifier`" "DO internal qualifier"

   * :attr:	:bitdef:`0`
     :val:	xxxx.xxx0
     :desc:	DO object **will not** be inverted

   * :(attr):
     :val:	xxxx.xxx1
     :desc:	DI object **will** be inverted (OFF → ON; ON → OFF)

   * :attr:	Bits 6;5
     :val:	x00x.xxxx
     :desc:	**Direct-Execute** and **Select-before-Execute** commands are accepted

   * :(attr):
     :val:	x01x.xxxx
     :desc:	Only **Direct-Execute** commands are accepted

   * :(attr):
     :val:	x10x.xxxx
     :desc:	Only **Select-Before-Execute** commands are accepted

   * :(attr):
     :val:	x11x.xxxx
     :desc:	Reserved for future use

   * :attr:	Bit 7
     :val:	0xxx.xxxx
     :desc:	DO is **enabled** and command will be processed when received

   * :(attr):
     :val:	1xxx.xxxx
     :desc:	DO is **disabled** and command will be rejected when received

   * :attr:	Bits 1...4
     :val:	Any
     :desc:	Bits reserved for future use

DO.TypeID
^^^^^^^^^

.. field-list-table:: IEC60870-5-101/104 Slave DO TypeID
   :class: table table-condensed table-bordered longtable
   :name: tabid-IEC10xslDOTypeID
   :spec: |C{0.16}|S{0.84}|
   :header-rows: 1

   * :attr,10: TypeID Value
     :desc,90: Description

   * :attr:	45
     :desc:	Only 'Single command' will be accepted and processed (ASDU type 45 [:lemonobgtext:`C_SC_NA_1`])

   * :attr:	46
     :desc:	Only 'Double command' will be accepted and processed (ASDU type 46 [:lemonobgtext:`C_DC_NA_1`])

   * :attr:	47
     :desc:	Only 'Regulating step command' will be accepted and processed (ASDU type 47 [:lemonobgtext:`C_RC_NA_1`])

   * :attr:	58
     :desc:	Only applicable to IEC60870-5-104 Slave protocol instance;
                Only time-tagged 'Single command' will be accepted and processed (ASDU type 58 [:lemonobgtext:`C_SC_TA_1`])

   * :attr:	59
     :desc:	Only applicable to IEC60870-5-104 Slave protocol instance;
                Only time-tagged 'Double command' will be accepted and processed (ASDU type 59 [:lemonobgtext:`C_DC_TA_1`])

   * :attr:	60
     :desc:	Only applicable to IEC60870-5-104 Slave protocol instance;
                Only time-tagged 'Regulating step command' will be accepted and processed (ASDU type 59 [:lemonobgtext:`C_RC_TA_1`])

   * :attr:	Other
     :desc:	Undefined, control command received with any ASDU type will be accepted


DO Service Indexes
^^^^^^^^^^^^^^^^^^

Service digital outputs are internal controls that enable to change operation state of communication protocol instances.
Service controls have negative index values and can be used just as any regular DO indexes.

.. field-list-table:: IEC60870-5-101/104 Slave Service DO indexes
   :class: table table-condensed table-bordered longtable
   :name: tabid-IEC10xslDOServiceIndex
   :spec: |C{0.19}|C{0.14}|S{0.67}|
   :header-rows: 1

   * :attr,10: Index value
     :val,10:  Object value
     :desc,80: Description

   * :attr:	-2
		(0xFFFFFFFE)
     :val:	ON or OFF
     :desc:	| Send forced **Poll** only applicable to the following communication protocol instances:
		| IEC60870-5-101/3/4 Master - Send General Interrogation command (ASDU type 100 [:lemonobgtext:`C_IC_NA_1`]) to downstream outstation;
		| IEC61850 Client - Send General Interrogation by setting [:lemonobgtext:`GI`] bit of all enabled Report Control Blocks;
		| Spabus Master - Read all DI values if DI requests are excluded from regular polling with :ref:`bitref-SpabusmaAppFlagsBit0`\ |bittrue| in :ref:`xmlelem-SpabusmaApp`.\ :ref:`xmlattr-SpabusmaAppFlags`.

   * :attr:	-3
		(0xFFFFFFFD)
     :val:	ON
     :desc:	**Enable** communication to the station. This service index can be used for any protocol instance.

   * :(attr):
     :val:	OFF
     :desc:	**Disable** communication to the station. his service index can be used for any protocol instance.

   * :attr:	-4\*
		(0xFFFFFFFC)
     :val:	ON
     :desc:	**Start** communication to the downstream station. Refer to the comment below for the types of messages being sent.

   * :(attr):
     :val:	OFF
     :desc:	**Stop** communication to the downstream station. Refer to the comment below for the types of messages being sent.

   * :attr:	-5
		(0xFFFFFFFB)
     :val:	ON or OFF
     :desc:	Only applicable to IEC60870-5-101/104 Master communication protocol instances.
		Send **Reset Process** command (ASDU type 105 [:lemonobgtext:`C_RP_NA_1`]) to the downstream station.

   * :attr:	-1 and -6...-8
     :val:	Any
     :desc:	Service commands reserved for future use

.. tip::

   | \* This service command only applies to the following protocol instances:
   | IEC60870-5-104 controlling station (Master) send [:lemonobgtext:`STARTDT_act`] or [:lemonobgtext:`STOPDT_act`] to the downstream station;
   | IEC61850 Client send MMS [:lemonobgtext:`Initiate-RequestPDU`] or [:lemonobgtext:`Conclude-RequestPDU`] to the IED;
