
.. _ref-IEC61850clDI:

DITable group and DI node
-------------------------

Group node :ref:`DITable<ref-IEC61850clDI>` and child element nodes :ref:`DI<ref-IEC61850clDI>` are used to create DI information objects to receive status information from an IED.
Each created DI can be used as a source for any DI information object defined in the IO table of any Slave protocol instance.
Data received from an IED will be forwarded to the DI information object of the Slave protocol instance and then to the upstream Master station.
Please refer to the section :ref:`docref-IEC10xslDITable` for more information on how to use DI information object as a source.

Please see sample :ref:`DITable<ref-IEC61850clDI>` group and :ref:`DI<ref-IEC61850clDI>` child element nodes below.

.. code-block:: none

   <DITable>
	<DI Index="0" ldInst="LD0" prefix="DA" lnClass="XCBR" lnInst="1" doName="Pos" fc="ST"/>
	<DI Index="1" ldInst="LD0" prefix="DA" lnClass="XCBR" lnInst="1" doName="Loc" fc="ST"/>
   </DITable>

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`DI<ref-IEC61850clDI>`"

.. code-block:: none

   <DI Index="0" ldInst="LD0" prefix="DA" lnClass="XCBR" lnInst="1" doName="Pos" fc="ST" Qualifier="0" InterDelay="10000" IndetDelay="0" daName="stVal" DSnum="1" TrgOps="0x00" intgPd="0" Name="CB position" />

.. tip:: Attributes of the :ref:`DI<ref-IEC61850clDI>` element node can be arranged in any order, it will not affect XML file validation.

DI attributes
^^^^^^^^^^^^^

.. _ref-IEC61850clDIAttributes:

.. include-file:: sections/Include/table_attrs.rstinc "" "IEC61850 Client DI attributes"

.. include-file:: sections/Include/ma_Index.rstinc "" ".. _ref-IEC61850clDIIndex:" "DI"

.. include-file:: sections/Include/IEC61850cl_SCL.rstinc "" "'DA'" "'XCBR'" "'Pos'" "'A.phsA'" "'ST'"

   * :attr:     .. _ref-IEC61850clDIQualifier:
   
		:xmlref:`Qualifier`
     :val:      0...255 or 0x00...0xFF
     :def:      0x00
     :desc:     Internal object qualifier to enable customized data processing.
		See table :numref:`ref-IEC61850clDIqualifierBits` for internal object qualifier description.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

.. include-file:: sections/Include/DI_Idelays.rstinc "" ".. _ref-IEC61850clDIInterDelay:" ".. _ref-IEC61850clDIIndetDelay:"

.. include-file:: sections/Include/hidden_qtname.rstinc "internal"

.. include-file:: sections/Include/IEC61850cl_DIAI.rstinc "" ".. _ref-IEC61850clDIDSnum:" ".. _ref-IEC61850clDITrgOps:" ".. _ref-IEC61850clDIintgPd:" ":numref:`ref-IEC61850clTrgOps`" "stVal"

.. include-file:: sections/Include/Name.rstinc ""

DI.Qualifier
^^^^^^^^^^^^

.. _ref-IEC61850clDIqualifierBits:

.. include-file:: sections/Include/table_flags.rstinc "" "IEC61850 Client DI internal qualifier" ":ref:`<ref-IEC61850clDIQualifier>`" "DI internal qualifier"

   * :attr:     Bit 0
     :val:      xxxx.xxx0
     :desc:     DI object **will not** be inverted (ON = 1; OFF = 0 for [SPS] and [SPC] clases and ON = 2; OFF = 1; INTER = 0; INVALID = 3 for [DPS] and [DPC] clases)

   * :(attr):
     :val:      xxxx.xxx1
     :desc:     DI object **will** be inverted (ON = 0; OFF = 1 for [SPS] and [SPC] clases and ON = 1; OFF = 2; INTER = 0; INVALID = 3 for [DPS] and [DPC] clases)

   * :attr:     Bit 3
     :val:      xxxx.0xxx
     :desc:     **Use original** timetag when event is received from IED

   * :(attr):
     :val:      xxxx.1xxx
     :desc:     **Substitute timetag** with local time when event is received from IED

   * :attr:     Bit 5
     :val:      xx0x.xxxx
     :desc:     Use time tag of the **last** event if Intermediate state of the Double Point object was not reported (because Intermediate state didn't exceed :ref:`<ref-IEC61850clDIInterDelay>`). e.g. in transition ON->INTER->OFF time tag of the INTER->OFF event will be used.

   * :(attr):
     :val:      xx1x.xxxx
     :desc:     Use time tag of the **first** event if Intermediate state of the Double Point object was not reported (because Intermediate state didn't exceed :ref:`<ref-IEC61850clDIInterDelay>`). e.g. in transition ON->INTER->OFF time tag of the ON->INTER event will be used.

   * :attr:     Bit 7
     :val:      0xxx.xxxx
     :desc:     DI is **enabled** and will be processed when received

   * :(attr):
     :val:      1xxx.xxxx
     :desc:     DI is **disabled** and will be discarded when received

   * :attr:     Bits 1;2;4;6
     :val:      Any
     :desc:     Bits reserved for future use
