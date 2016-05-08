.. _ref-IEC61850clPeriodic:

Periodic
^^^^^^^^

Periodic intervals to send various messages are specified in this node.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`<ref-IEC61850clPeriodic>`"

.. code-block:: none

   <Periodic GI="600" intgPd="60000" />

.. include-file:: sections/Include/ma_Periodic.rstinc "" ".. _docref-IEC61850clPeriodicAttab:" "IEC61850 Client Periodic attributes"

   * :attr:     :xmlref:`intgPd`
     :val:      0...2\ :sup:`32`\  - 2
     :def:      0 msec
     :desc:     Common interval in milliseconds for generating periodic integrity reports [IEC61850-7-2:2010].
		This attribute is used for all DI/AI objects which doesn’t have :ref:`DI<ref-IEC61850clDI>`.\ :ref:`<ref-IEC61850clDIintgPd>` \ or :ref:`AI<ref-IEC61850clAI>`.\ :ref:`<ref-IEC61850clAIintgPd>` \ attribute specified in their element node.
		Value 0 disables integrity reports.

