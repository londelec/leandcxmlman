.. _xmlelem-IEC104slMiscellaneous:

Miscellaneous
^^^^^^^^^^^^^

Miscellaneous and project-specific settings can be specified in this node.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-IEC104slMiscellaneous`"

.. code-block:: none

   <Miscellaneous LegacyAIEVinitdelay="2" />


.. include-file:: sections/Include/table_attrs.rstinc "" "tabid-IEC104slMiscellaneous" "IEC60870-5-104 Slave Miscellaneous attributes" ":spec: |C{0.2}|C{0.12}|C{0.1}|S{0.58}|"

   * :attr:	:xmlattr:`LegacyAIEVinitdelay`
     :val:	0...2\ :sup:`32`\  - 1
     :def:	0 sec
     :desc:	Attribute enables specially marked (legacy spontaneous-only) AI object initialization after configured number of seconds on system startup.
		This feature applies only to AI objects that have Legacy :ref:`bitref-IEC10xmaAIqualifierBit2`\ |bittrue| in :ref:`xmlelem-IEC10xmaAI`.\ :ref:`xmlattr-IEC10xmaAIqualifier`.
		By default Legacy AI objects are sent upstream spontaneously with a last known value from internal database whenever downstream outstation goes online e.g. after a communication loss or when Enabled with a Service command.
		Legacy AI events do not have Invalid [:lemonobgtext:`IV`] nor Not Topical [:lemonobgtext:`NT`] bits set, with the exception on system startup.
 		AI events will have value 0 and Invalid [:lemonobgtext:`IV`] bit set when initialized for the first time on startup.
		This is a standard behaviour for Legacy AI events and it is not affected by the use of the :ref:`xmlattr-IEC104slMiscellaneousLegacyAIEVinitdelay` attribute.
		This attribute extends functionality by providing a mechanism to remove Invalid [:lemonobgtext:`IV`] bit after configured number of seconds on system startup.
		Legacy AI objects with value 0 and cleared Invalid [:lemonobgtext:`IV`] bit will be sent with Background scan message(s) after a number of seconds configured in this attribute.
		As a result upstream station (e.g. SCADA) will have a valid legacy AI object (without Invalid [:lemonobgtext:`IV`] bit) with value 0 in the database and 
		will be ready to process the first genuine AI event when it arrives.
