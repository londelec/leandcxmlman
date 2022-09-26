
.. _docref-IEC10xslAO:
.. _xmlgroup-IEC10xslAO: lelabel=AOTable
.. _xmlelem-IEC10xslAO: lelabel=AO

AOTable group
-------------

.. include-file:: sections/Include/IEC10xsl_DOAO_table.rstinc "" ":ref:`xmlgroup-IEC10xslAO`" ":ref:`xmlelem-IEC10xslAO`" ":numref:`tabid-IEC10xslAO`" "AO" "setpoint"

| The link is created using :ref:`xmlelem-IEC10xslAO`.\ :ref:`xmlattr-IEC10xslAODevice` and :ref:`xmlelem-IEC10xslAO`.\ :ref:`xmlattr-IEC10xslAOIndex` attributes as follows:
| 1. Select the **destination Master protocol instance** - use value of the :ref:`xmlattr-gp101maIndex` attribute of any Master protocol instance and enter this value in :ref:`xmlelem-IEC10xslAO`.\ :ref:`xmlattr-IEC10xslAODevice` attribute.
| 2. Select the **destination AO object** - use value of the :ref:`xmlelem-IEC10xmaAO`.\ :ref:`xmlattr-IEC10xmaAOIndex` attribute of any AO object listed in the IO object table of a Master protocol instance and enter this value in :ref:`xmlelem-IEC10xslAO`.\ :ref:`xmlattr-IEC10xslAOIndex` attribute.

Information object address (IOA) to receive the setpoint command is specified in the :ref:`xmlattr-IEC10xslAOInfAddr` attribute.

Please see sample :ref:`xmlgroup-IEC10xslAO` group and :ref:`xmlelem-IEC10xslAO` element nodes below.
There are 5 setpoint commands defined with 4 :ref:`xmlelem-IEC10xslAO` element nodes.

.. code-block:: none

   <AOTable>
	<AO Device="10" Index="0" InfAddr="1" Policy="0" … />
	<AO Device="10" Index="1" InfAddr="2" Policy="250" … />
	<AO Device="10" Index="-2" InfAddr="3" Policy="0" … />
	<AO Device="10" Index="2" InfAddr="4" Policy="0" Total="2" … />
   </AOTable>

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-IEC10xslAO`"

.. code-block:: none

   <AO Device="10" Index="2" InfAddr="4" qualifier="0x80" Coeff="15.3" Policy="0" TypeID="0" Total="2" Name="Filter value" />

.. include-file:: sections/Include/tip_order.rstinc "" ":ref:`xmlelem-IEC10xslAO`"

AO attributes
^^^^^^^^^^^^^

.. include-file:: sections/Include/table_attrs.rstinc "" "tabid-IEC10xslAO" "IEC60870-5-101/104 Slave AO attributes" ":spec: |C{0.14}|C{0.16}|C{0.1}|S{0.6}|"

.. include-file:: sections/Include/IEC10xsl_Device.rstinc "" ":xmlattr:`Device`" "destination for this AO object" "Destination"

   * :attr:	:xmlattr:`Index`
     :val:	|slindexrange|
     :def:	n/a
     :desc:	Destination AO object. Any AO element of the selected Master protocol instance can be used as a destination.
		Use value of the :ref:`xmlelem-IEC10xmaAO`.\ :ref:`xmlattr-IEC10xmaAOIndex` attribute of any AO object listed in the IO table of the selected Master protocol instance.
		:inlinetip:`Indexes don't have to be arranged in ascending order.`

.. include-file:: sections/Include/IEC10xsl_IOA.rstinc "" "AO" "receive command from"

.. include-file:: sections/Include/IEC60870_qualifier.rstinc "" ":numref:`tabid-IEC10xslAOqualifier`"

   * :attr:	:xmlattr:`Coeff`
     :val:	0 or ±1.18×10\ :sup:`-38` \ ... ±3.4×10\ :sup:`38`\
     :def:	1
     :desc:	Coefficient to multiply the setpoint value before forwarding to linked protocol instance. 
		|optinalattr|

.. include-file:: sections/Include/IEC10xsl_Policy.rstinc ""

.. include-file:: sections/Include/IEC10xsl_TypeID.rstinc "" ":numref:`tabid-IEC10xslAOTypeID`"

.. include-file:: sections/Include/Total.rstinc "" ":ref:`xmlattr-IEC10xslAOIndex` and :ref:`xmlattr-IEC10xslAOInfAddr`" ":ref:`xmlelem-IEC10xslAO`" "16777214"

.. include-file:: sections/Include/Name.rstinc ""

AO.qualifier
^^^^^^^^^^^^

.. include-file:: sections/Include/table_flags8.rstinc "" "tabid-IEC10xslAOqualifier" "IEC60870-5-101/104 Slave AO internal qualifier" ":ref:`xmlattr-IEC10xslAOqualifier`" "AO internal qualifier"

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
     :desc:	AO is **enabled** and command will be processed when received

   * :(attr):
     :val:	1xxx.xxxx
     :desc:	AO is **disabled** and command will be rejected when received

   * :attr:	Bits 0...4
     :val:	Any
     :desc:	Bits reserved for future use

AO.TypeID
^^^^^^^^^

.. field-list-table:: IEC60870-5-101/104 Slave AO TypeID
   :class: table table-condensed table-bordered longtable
   :name: tabid-IEC10xslAOTypeID
   :spec: |C{0.16}|S{0.84}|
   :header-rows: 1

   * :attr,10: TypeID Value
     :desc,90: Description

   * :attr:	48
     :desc:	Only 'Normalized setpoint command' will be accepted and processed (ASDU type 48 [:lemonobgtext:`C_SE_NA_1`])

   * :attr:	49
     :desc:	Only 'Scaled setpoint command' will be accepted and processed (ASDU type 49 [:lemonobgtext:`C_SE_NB_1`])

   * :attr:	50
     :desc:	Only 'Short floating point setpoint command' will be accepted and processed (ASDU type 50 [:lemonobgtext:`C_SE_NC_1`])

   * :attr:	61
     :desc:	Only applicable to IEC60870-5-104 Slave protocol instance;
                Only time-tagged 'Normalized setpoint command' will be accepted and processed (ASDU type 61 [:lemonobgtext:`C_SE_TA_1`])

   * :attr:	62
     :desc:	Only applicable to IEC60870-5-104 Slave protocol instance;
                Only time-tagged 'Scaled setpoint command' will be accepted and processed (ASDU type 62 [:lemonobgtext:`C_SE_TB_1`])

   * :attr:	63
     :desc:	Only applicable to IEC60870-5-104 Slave protocol instance;
                Only time-tagged 'Short floating point setpoint command' will be accepted and processed (ASDU type 63 [:lemonobgtext:`C_SE_TC_1`])

   * :attr:	Other
     :desc:	Undefined, setpoint command received with any ASDU type will be accepted
