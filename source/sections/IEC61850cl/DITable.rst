
.. _xmlgroup-IEC61850clDI: lelabel=DITable
.. _xmlelem-IEC61850clDI: lelabel=DI

DITable group
-------------

.. include-file:: sections/Include/ma_DIAI_table.rstinc "" ":ref:`xmlgroup-IEC61850clDI`" ":ref:`xmlelem-IEC61850clDI`" ":numref:`tabid-IEC61850clDI`" ":ref:`docref-IEC10xslDI`" "DI" "status information" "IED"

Please see sample :ref:`xmlgroup-IEC61850clDI` group and :ref:`xmlelem-IEC61850clDI` element nodes below.
There are 2 status information objects defined in this sample.

.. code-block:: none

   <DITable>
	<DI Index="0" ldInst="LD0" prefix="DA" lnClass="XCBR" lnInst="1" doName="Pos" fc="ST"/>
	<DI Index="1" ldInst="LD0" prefix="DA" lnClass="XCBR" lnInst="1" doName="Loc" fc="ST"/>
   </DITable>

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-IEC61850clDI`"

.. code-block:: none

   <DI Index="0" ldInst="LD0" prefix="DA" lnClass="XCBR" lnInst="1" doName="Pos" fc="ST" Qualifier="0" InterDelay="10000" IndetDelay="0" OnDelay="0" OffDelay="0" OnValues="0x01 0x02" OffValues="5,6" daName="stVal" DSref="ABCLD/LLN0.myds" DSflags="0x00" TrgOps="0x00" intgPd="0" Name="CB position" />

.. include-file:: sections/Include/tip_order.rstinc "" ":ref:`xmlelem-IEC61850clDI`"

DI attributes
^^^^^^^^^^^^^

.. include-file:: sections/Include/table_attrs.rstinc "" "tabid-IEC61850clDI" "IEC61850 Client DI attributes" ":spec: |C{0.12}|C{0.14}|C{0.1}|S{0.64}|"

.. include-file:: sections/Include/ma_Index.rstinc "" "DI"

.. include-file:: sections/Include/IEC61850cl_SCL.rstinc "" "'DA'" "'XCBR'" "'Pos'" "'A.phsA'" "'ST'"

.. include-file:: sections/Include/Qualifier.rstinc "" ":numref:`tabid-IEC61850clDIQualifier`"

.. include-file:: sections/Include/DI_Idelays.rstinc ""

.. include-file:: sections/Include/DI_Odelays.rstinc ""

.. include-file:: sections/Include/hidden_qtname.rstinc "internal"

   * :attr:	:xmlattr:`OnValues`
     :val:	0...65535 or 0x0000...0xFFFF (up to 32)
     :def:	n/a
     :desc:	Values received from IED will result in a DI state ON.
		This setting only applies if basic type of the DI object can have a range of values e.g. [:lemonobgtext:`Enum`], [:lemonobgtext:`INT8`].
		By default received values are decoded to DI states as follows: INTER = 0,4,8; OFF = 1,5,9; ON = 2,6,10; INVALID = 3,7,11.
		This attribute overrides the default decoding and allows to select values that will result in ON state manually.
		Up to 32 values can be specified in decimal or hexadecimal notation separated by whitespaces or commas
		e.g. "2,3 0x05 0xf1".
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, default decoding will apply if omitted. If`
		:ref:`xmlattr-IEC61850clDIOffValues`
		:inlinetip:`attribute is not used, any value received from IED that is not included in`
		:ref:`xmlattr-IEC61850clDIOnValues`
		:inlinetip:`list will result in a DI state OFF. If`
		:ref:`xmlattr-IEC61850clDIOffValues`
		:inlinetip:`attribute is used, any value received from IED that is not included in either attributes will result in a DI state INTER.`

   * :attr:	:xmlattr:`OffValues`
     :val:	0...65535 or 0x0000...0xFFFF (up to 32)
     :def:	n/a
     :desc:	Values received from IED will result in a DI state OFF.
		This setting only applies if basic type of the DI object can have a range of values e.g. [:lemonobgtext:`Enum`], [:lemonobgtext:`INT8`].
		By default received values are decoded to DI states as follows: INTER = 0,4,8; OFF = 1,5,9; ON = 2,6,10; INVALID = 3,7,11.
		This attribute overrides the default decoding and allows to select values that will result in OFF state manually.
		Up to 32 values can be specified in decimal or hexadecimal notation separated by whitespaces or commas
		e.g. "2,3 0x05 0xf1"
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, default decoding will apply if omitted. If`
		:ref:`xmlattr-IEC61850clDIOnValues`
		:inlinetip:`attribute is not used, any value received from IED that is not included in`
		:ref:`xmlattr-IEC61850clDIOffValues`
		:inlinetip:`list will result in a DI state ON. If`
		:ref:`xmlattr-IEC61850clDIOffValues`
		:inlinetip:`attribute is used, any value received from IED that is not included in either attributes will result in a DI state INTER.`

.. include-file:: sections/Include/IEC61850cl_DIAI.rstinc "" ":numref:`tabid-IEC61850clDIDSflags`" ":numref:`tabid-IEC61850clTrgOps`" "stVal"

.. include-file:: sections/Include/Name.rstinc ""

DI.Qualifier
^^^^^^^^^^^^

.. include-file:: sections/Include/table_flags8.rstinc "" "tabid-IEC61850clDIQualifier" "IEC61850 Client DI internal qualifier" ":ref:`xmlattr-IEC61850clDIQualifier`" "DI internal qualifier"

   * :attr:	Bit 0
     :val:	xxxx.xxx0
     :desc:	DI object **will not** be inverted (ON = 1; OFF = 0 for [SPS] and [SPC] classes and ON = 2; OFF = 1; INTER = 0; INVALID = 3 for [DPS] and [DPC] classes)

   * :(attr):
     :val:	xxxx.xxx1
     :desc:	DI object **will** be inverted (ON = 0; OFF = 1 for [SPS] and [SPC] classes and ON = 1; OFF = 2; INTER = 0; INVALID = 3 for [DPS] and [DPC] classes)

   * :attr:	Bit 3
     :val:	xxxx.0xxx
     :desc:	**Use original** timetag when event is received from IED

   * :(attr):
     :val:	xxxx.1xxx
     :desc:	**Substitute timetag** with local time when event is received from IED

   * :attr:	Bit 5
     :val:	xx0x.xxxx
     :desc:	Use time tag of the **last** event if Intermediate state of the Double Point object was not reported (because Intermediate state didn't exceed :ref:`xmlattr-IEC61850clDIInterDelay`). e.g. in transition ON->INTER->OFF time tag of the INTER->OFF event will be used.

   * :(attr):
     :val:	xx1x.xxxx
     :desc:	Use time tag of the **first** event if Intermediate state of the Double Point object was not reported (because Intermediate state didn't exceed :ref:`xmlattr-IEC61850clDIInterDelay`). e.g. in transition ON->INTER->OFF time tag of the ON->INTER event will be used.

   * :attr:	Bit 7
     :val:	0xxx.xxxx
     :desc:	DI is **enabled** and will be processed when received

   * :(attr):
     :val:	1xxx.xxxx
     :desc:	DI is **disabled** and will be discarded when received

   * :attr:	Bits 1;2;4;6
     :val:	Any
     :desc:	Bits reserved for future use

DI.DSflags
^^^^^^^^^^

.. include-file:: sections/Include/table_flags8.rstinc "" "tabid-IEC61850clDIDSflags" "IEC61850 Client DI Dataset flags" ":ref:`xmlattr-IEC61850clDIDSflags`" "Dataset flags"

   * :attr:	Bits 1;0
     :val:	xxxx.xx00
     :desc:	Dataset that is linked to **buffered** Report Block is required for this DI object

   * :(attr):
     :val:	xxxx.xx01
     :desc:	Dataset that is linked to **unbuffered** Report Block is required for this DI object

   * :(attr):
     :val:	xxxx.xx10
     :desc:	Dataset that is linked to **any** Report Block can be used for this DI object

   * :(attr):
     :val:	xxxx.xx11
     :desc:	Reserved for future use

   * :attr:	Bit 5
     :val:	xx0x.xxxx
     :desc:	Use **any** dataset that contains this DI object.

   * :(attr):
     :val:	xx1x.xxxx
     :desc:	Use **referenced only** dataset, that is set by :ref:`xmlattr-IEC61850clDIDSref` attribute.
		No other dataset will be used even if :ref:`xmlattr-IEC61850clDIDSref` dataset doesn't contain this DI object.

   * :attr:	Bits 2;3;6;7
     :val:	Any
     :desc:	Bits reserved for future use
