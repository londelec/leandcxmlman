
.. _docref-IEC10xslAOTable:
.. _ref-IEC10xslAOTable:
.. _ref-IEC10xslAO:

AOTable group and AO node
-------------------------

Group node :ref:`AOTable<ref-IEC10xslAOTable>` and child element nodes :ref:`AO<ref-IEC10xslAO>` are used to create AO information objects to receive setpoint 
commands from the upstream Master station.
Each created AO information object needs to have a destination to forward the setpoint command.
The destination is created by linking AO information object to a :ref:`AO<ref-IEC10xslAO>` node of any Master protocol instance.
(Master protocol instances are defined in :ref:`CommunicationCfg<ref-CommunicationCfg>` node in **leandc.xml** file)

The link is created using :ref:`AO<ref-IEC10xslAO>`.\ :ref:`<ref-IEC10xslAODevice>` \ and :ref:`AO<ref-IEC10xslAO>`.\ :ref:`<ref-IEC10xslAOIndex>` \ attributes.
The first step is to select the **destination Master protocol instance**, use value of the :ref:`<ref-IEC101maIndex>` attribute of any Master protocol instance.
The next step is to select the **destination AO object**, use value of the :ref:`AO<ref-IEC10xmaAO>`.\ :ref:`<ref-IEC10xmaAOIndex>` \ attribute of any AO object listed in the IO object table of any Master protocol instance.
Enter the selected values of **destination Master protocol instance** in :ref:`AO<ref-IEC10xslAO>`.\ :ref:`<ref-IEC10xslAODevice>` \
attribute and destination AO object in :ref:`AO<ref-IEC10xslAO>`.\ :ref:`<ref-IEC10xslAOIndex>` \ attribute.

Information address (IOA) to receive setpoint command is specified in :ref:`<ref-IEC10xslAOInfAddr>` \ attribute.

Please see sample :ref:`AOTable<ref-IEC10xslAOTable>` group and :ref:`AO<ref-IEC10xslAO>` child element nodes below.
There are 5 AO information objects configured using 4 :ref:`AO<ref-IEC10xslAO>` element nodes.

.. code-block:: none

   <AOTable>
	<AO Device="10" Index="0" InfAddr="1" Policy="0" … />
	<AO Device="10" Index="1" InfAddr="2" Policy="250" … />
	<AO Device="10" Index="-2" InfAddr="3" Policy="0" … />
	<AO Device="10" Index="2" InfAddr="4" Policy="0" Total="2" … />
   </AOTable>

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`AO<ref-IEC10xslAO>`"

.. code-block:: none

   <AO Device="10" Index="2" InfAddr="4" qualifier="0x80" Coeff="15.3" Policy="0" TypeID="0" Total="2" Name="Filter value" />

.. tip:: Attributes of the :ref:`AO<ref-IEC10xslAO>` element node can be arranged in any order, it will not affect the XML file validation.         

AO attributes
^^^^^^^^^^^^^

.. _ref-IEC10xslAOAttributes:

.. include-file:: sections/Include/table_attrs.rstinc "" "IEC60870-5-101/104 Slave AO attributes"

.. include-file:: sections/Include/IEC10xsl_Device.rstinc "" ".. _ref-IEC10xslAODevice:" "AO" "destination" "Destination"

   * :attr:     .. _ref-IEC10xslAOIndex:

                :xmlref:`Index`
     :val:      -8...2\ :sup:`32`\  - 1
     :def:      n/a
     :desc:     Destination AO object. Any AO element node of the selected Master protocol instance can be used as a destination.
		Use value of the :ref:`AO<ref-IEC10xmaAO>`.\ :ref:`<ref-IEC10xmaAOIndex>` \ attribute of any AO object listed in the IO table of the selected Master protocol instance.
		:inlinetip:`Indexes don't have to be arranged in ascending order.`

.. include-file:: sections/Include/IEC10xsl_IOA.rstinc "" ".. _ref-IEC10xslAOInfAddr:" "AO" "receive command from"

   * :attr:     .. _ref-IEC10xslAOqualifier:

                :xmlref:`qualifier`
     :val:      0...255 or 0x00...0xFF
     :def:      0x00
     :desc:     Internal object qualifier to enable customized data processing. See table :numref:`ref-IEC10xslAOqualifierBits` for internal object qualifier description. (default value 0) :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:     .. _ref-IEC10xslAOCoeff:

                :xmlref:`Coeff`
     :val:      0 or ±1.18×10\ :sup:`-38`\ ...±3.4×10\ :sup:`38`\
     :def:      1
     :desc:     Coefficient to multiply the setpoint value before forwarding to linked protocol instance. 
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:     .. _ref-IEC10xslAOPolicy:

                :xmlref:`Policy`
     :val:      0...255
     :def:      0
     :desc:     Command execution policy, see table :numref:`ref-IEC10xslPolicy` for description.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:     .. _ref-IEC10xslAOTypeID:

                :xmlref:`TypeID`
     :val:      See table :numref:`ref-IEC10xslAOTypeIDValues`
     :def:      0 = any
     :desc:     Only accept command if received with this ASDU Type.
		Value 0 disables ASDU type checking and any command is accepted.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

.. include-file:: sections/Include/IEC60870_Total.rstinc "" ".. _ref-IEC10xslAOTotal:" ":ref:`Index<ref-IEC10xslAOIndex>`" ":ref:`InfAddr<ref-IEC10xslAOInfAddr>`" ":ref:`AO<ref-IEC10xslAO>`" "16777214"

.. include-file:: sections/Include/Name.rstinc ""

AO.qualifier
^^^^^^^^^^^^

.. _ref-IEC10xslAOqualifierBits:

.. include-file:: sections/Include/table_flags.rstinc "" "IEC60870-5-101/104 Slave AO internal qualifier" ":ref:`<ref-IEC10xslAOqualifier>`" "AO internal qualifier"

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
     :desc:     AO is **enabled** and command will be processed when received

   * :(attr):
     :val:      1xxx.xxxx
     :desc:     AO is **disabled** and command will be rejected when received

   * :attr:     Bits 0...4
     :val:      Any
     :desc:     Bits reserved for future use

AO.TypeID
^^^^^^^^^

.. _ref-IEC10xslAOTypeIDValues:

.. field-list-table:: IEC60870-5-101/104 Slave AO TypeID
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.20}|S{0.80}|
   :header-rows: 1

   * :attr,10: TypeID Value
     :desc,90: Description

   * :attr:     48
     :desc:     Only 'Normalized setpoint command' will be accepted and processed (ASDU type 48 [C_SE_NA_1])

   * :attr:     49
     :desc:     Only 'Scaled setpoint command' will be accepted and processed (ASDU type 49 [C_SE_NB_1])

   * :attr:     50
     :desc:     Only 'Short floating point setpoint command' will be accepted and processed (ASDU type 50 [C_SE_NC_1])

   * :attr:     61
     :desc:     Only applicable to IEC60870-5-104 Slave protocol instance;
                Only time-tagged 'Normalized setpoint command' will be accepted and processed (ASDU type 61 [C_SE_TA_1])

   * :attr:     62
     :desc:     Only applicable to IEC60870-5-104 Slave protocol instance;
                Only time-tagged 'Scaled setpoint command' will be accepted and processed (ASDU type 62 [C_SE_TB_1])

   * :attr:     63
     :desc:     Only applicable to IEC60870-5-104 Slave protocol instance;
                Only time-tagged 'Short floating point setpoint command' will be accepted and processed (ASDU type 63 [C_SE_TC_1])

   * :attr:     Other
     :desc:     Undefined, setpoint command received with any ASDU type will be accepted
