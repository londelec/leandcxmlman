.. _xmlelem-IEC61850clPeriodic:

Periodic
^^^^^^^^

Periodic intervals to send various messages are specified in this node.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-IEC61850clPeriodic`"

.. code-block:: none

   <Periodic GI="600" intgPd="60000" />

.. include-file:: sections/Include/ma_Periodic.rstinc "" "tabid-IEC61850clPeriodic" "IEC61850 Client Periodic attributes"

   * :attr:	:xmlattr:`intgPd`
     :val:	|uint32range|
     :def:	0 msec
     :desc:	Common interval in milliseconds for generating periodic integrity reports [IEC61850-7-2:2010].
		This attribute is used for all DI/AI objects which doesn’t have :ref:`xmlelem-IEC61850clDI`.\ :ref:`xmlattr-IEC61850clDIintgPd` \ or :ref:`xmlelem-IEC61850clAI`.\ :ref:`xmlattr-IEC61850clAIintgPd` \ attribute specified in their element node.
		Value 0 disables integrity reports.

