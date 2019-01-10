DI/AI.TrgOps
^^^^^^^^^^^^

.. _docref-IEC61850clTrgOps:

.. include-file:: sections/Include/table_flags.rstinc "" "IEC61850 Client Trigger Options" ":xmlref:`TrgOps`" "Trigger Options"

   * :attr:     Bit 3
     :val:      xxxx.0xxx
     :desc:     Information Report that includes this data object **will not** be generated on Data-update [dupd]

   * :(attr):
     :val:      xxxx.1xxx
     :desc:     Information Report that includes this data object **will** be generated on Data-update [dupd]

   * :attr:     Bit 4
     :val:      xxx0.xxxx
     :desc:     Information Report that includes this data object **will not** be generated periodically [integrity]

   * :(attr):
     :val:      xxx1.xxxx
     :desc:     Information Report that includes this data object **will** be generated periodically [integrity] upon :ref:`DI<ref-IEC61850clDI>`.\ :ref:`intgPd<ref-IEC61850clDIintgPd>` \ or :ref:`AI<ref-IEC61850clAI>`.\ :ref:`intgPd<ref-IEC61850clAIintgPd>` \ timer expiration.

   * :attr:     Bits 0...2;5...7
     :val:      Any
     :desc:     Bits reserved for future use
