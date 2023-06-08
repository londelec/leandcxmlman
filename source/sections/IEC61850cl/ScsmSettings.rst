.. _xmlelem-IEC61850clScsm:

ScsmSettings
^^^^^^^^^^^^

Specific Communication Service Mapping (IEC61850-8 SCSM) settings can be specified using attributes of :ref:`xmlelem-IEC61850clScsm` element node.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-IEC61850clScsm`"

.. code-block:: none

 <ScsmSettings Flags="0x0800" LogFlags="0x0000"/>


.. include-file:: sections/Include/table_attrs.rstinc "" "tabid-IEC61850clScsm" "IEC61850 Client ScsmSettings attributes" ":spec: |C{0.14}|C{0.18}|C{0.1}|S{0.58}|"

   * :attr:	:xmlattr:`Flags`
     :val:	|flags16range|
     :def:	0x0000
     :desc:	Miscellaneous Specific Communication Service Mapping settings.
		See :numref:`tabid-IEC61850clScsmFlags` for description.

.. include-file:: sections/Include/IEC61850_LogFlags16.rstinc "" ":numref:`tabid-IEC61850clScsmLogFlags`"


.. include-file:: sections/Include/table_flags16.rstinc "" "tabid-IEC61850clScsmFlags" "Specific Communication Service Mapping flags" ":ref:`xmlattr-IEC61850clScsmFlags`" "SCSM flags"

   * :attr:	:bitdef:`4`
     :val:	xxxx.xxxx xxx0.xxxx
     :desc:	**Only array members** are addressed with [:lemonobgtext:`AlternateAccess`].
		Array element itself and its parents are addressed with [:lemonobgtext:`VariableSpecification`] [:lemonobgtext:`name`]. (default value)

   * :(attr):
     :val:	xxxx.xxxx xxx1.xxxx
     :desc:	**Array and its parent elements** are addressed with [:lemonobgtext:`AlternateAccess`].

   * :attr:	:bitdef:`11`
     :val:	xxxx.0xxx xxxx.xxxx
     :desc:	**Only array members** are addressed with [:lemonobgtext:`AlternateAccess`]. (default value)

   * :(attr):
     :val:	xxxx.1xxx xxxx.xxxx
     :desc:	**All elements** are addressed with [:lemonobgtext:`AlternateAccess`].

   * :attr:	Bits 0..3;5..10;12..15
     :val:	Any
     :desc:	Bits reserved for future use


.. include-file:: sections/Include/table_flags16.rstinc "" "tabid-IEC61850clScsmLogFlags" "SCSM informative logger flags" ":ref:`xmlattr-IEC61850clScsmLogFlags`" "Logger flags"

.. include-file:: sections/Include/hidden_SCSM_debuglog.rstinc "internal"

   * :attr:	Bit 4
     :val:	xxxx.xxxx xxx0.xxxx
     :desc:	Names of all LD/LN/RCB/LCB/SGCB/DO/DA **will not be** recorded.

   * :(attr):
     :val:	xxxx.xxxx xxx1.xxxx
     :desc:	Names of all LD/LN/RCB/LCB/SGCB/DO/DA **will be** recorded.
		[:lemonobgtext:`GetNameList`] services.

   * :attr:	Bit 5
     :val:	xxxx.xxxx xx0x.xxxx
     :desc:	Basic types **will not be** recorded.

   * :(attr):
     :val:	xxxx.xxxx xx1x.xxxx
     :desc:	Basic types **will be** recorded.
		[:lemonobgtext:`GetVariableAccessAttributes`] services.

   * :attr:	Bit 6
     :val:	xxxx.xxxx x0xx.xxxx
     :desc:	Dataset contents **will not be** recorded.

   * :(attr):
     :val:	xxxx.xxxx x1xx.xxxx
     :desc:	Dataset contents **will be** recorded.
		[:lemonobgtext:`GetNamedVariableListAttributes`] services.

   * :attr:	Bit 7
     :val:	xxxx.xxxx 0xxx.xxxx
     :desc:	Create and Delete dataset responses **will not be** recorded.

   * :(attr):
     :val:	xxxx.xxxx 1xxx.xxxx
     :desc:	Create and Delete dataset responses **will be** recorded.
		[:lemonobgtext:`DefineNamedVariableList`] and [:lemonobgtext:`DeleteNamedVariableList`] services.

   * :attr:	Bit 8
     :val:	xxxx.xxx0 xxxx.xxxx
     :desc:	Data values **will not be** recorded.

   * :(attr):
     :val:	xxxx.xxx1 xxxx.xxxx
     :desc:	Data values **will be** recorded.
		[:lemonobgtext:`Read`] and [:lemonobgtext:`Write`] services.

   * :attr:	Bits 0...3;9...15
     :val:	Any
     :desc:	Bits reserved for future use
