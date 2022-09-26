DI/AI.TrgOps
^^^^^^^^^^^^

.. include-file:: sections/Include/table_flags8.rstinc "" "tabid-IEC61850clTrgOps" "IEC61850 Client Trigger Options" ":ref:`xmlattr-IEC61850clDITrgOps`" "Trigger Options"

   * :attr:	Bit 3
     :val:	xxxx.0xxx
     :desc:	Information Report that includes this data object **will not** be generated on Data-update [dupd]

   * :(attr):
     :val:	xxxx.1xxx
     :desc:	Information Report that includes this data object **will** be generated on Data-update [dupd]

   * :attr:	Bit 4
     :val:	xxx0.xxxx
     :desc:	Information Report that includes this data object **will not** be generated periodically [integrity]

   * :(attr):
     :val:	xxx1.xxxx
     :desc:	Information Report that includes this data object **will** be generated periodically [integrity] upon :ref:`xmlelem-IEC61850clDI`.\ :ref:`xmlattr-IEC61850clDIintgPd` \ or :ref:`xmlelem-IEC61850clAI`.\ :ref:`xmlattr-IEC61850clAIintgPd` \ timer expiration.

   * :attr:	Bits 0...2;5...7
     :val:	Any
     :desc:	Bits reserved for future use
