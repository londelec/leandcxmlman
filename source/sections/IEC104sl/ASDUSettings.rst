.. _xmlelem-IEC104slAsdu:

ASDUSettings
^^^^^^^^^^^^

Application layer settings can be specified using attributes of :ref:`xmlelem-IEC104slAsdu` element node.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-IEC104slAsdu`"

.. code-block:: none

   <ASDUSettings InvalidEvent="1" SUthroughoutDST="1" DIEventType="31" AIEventType="36" DOType="46" AOType="50" DOProc="2" AOProc="0" DIInterDelay="8000" DIIndetDelay="3500" DIEventStartup="1" AIEventStartup="1" TimeSync="1" TranspTypes="1" orCat="3" Flags="0x00" ForwardGI="1" CommandLatency="300" />


.. include-file:: sections/Include/table_attrs.rstinc "" "tabid-IEC104slAsdu" "IEC60870-5-104 Slave ASDUSettings attributes" ":spec: |C{0.2}|C{0.12}|C{0.14}|S{0.54}|"

.. include-file:: sections/Include/IEC60870_InvalidEvent.rstinc ""

.. include-file:: sections/Include/IEC60870_SUthroughoutDST.rstinc ""

   * :attr:	:xmlattr:`DIEventType`
     :val:	See :numref:`tabid-IEC10xslDITypeID`
     :def:	30 [:lemonobgtext:`M_SP_TB_1`]
     :desc:	Use this ASDU type to send DI events which don't have :ref:`xmlelem-IEC10xslDI`.\ :ref:`xmlattr-IEC10xslDITypeID` \ attribute specified in their element node.
		This setting also affects ASDU type of the static data (e.g. Single or Double status information) reported to a General Interrogation request.
		(default value 30 – 'Single-point Information', DI event will be sent using ASDU type 30 [:lemonobgtext:`M_SP_TB_1`], **CP56time2A**, full time)

   * :attr:	:xmlattr:`AIEventType`
     :val:	See :numref:`tabid-IEC10xslAITypeID`
     :def:	36 [:lemonobgtext:`M_ME_TF_1`]
     :desc:	Use this ASDU type to send AI events which don't have :ref:`xmlelem-IEC10xslAI`.\ :ref:`xmlattr-IEC10xslAITypeID` \ attribute specified in their element node.
		This setting also affects ASDU type of the static data (e.g. Normalized, Scaled, Short floating point) reported to a General Interrogation request.
		(default value 36 – 'Short floating point', AI event will be sent using ASDU type 36 [:lemonobgtext:`M_ME_TF_1`], **CP56time2A**, full time)

.. include-file:: sections/Include/IEC10xsl_ASDU.rstinc "" ":numref:`tabid-IEC104slAsduFlags`"

.. include-file:: sections/Include/IEC60870_ForwardGI.rstinc ""

   * :attr:	:xmlattr:`CommandLatency`
     :val:	0...2\ :sup:`32`\  - 1
     :def:	0 sec
     :desc:	Maximal difference in seconds between received time-tagged control command and the internal time.
		If this attribute is used, time-tag of the received control command is checked and command will be discarded if it has been substantially delayed.
		Value 0 disables time-tagged command validation and any incoming control command will be accepted.


.. include-file:: sections/Include/table_flags8.rstinc "" "tabid-IEC104slAsduFlags" "IEC60870-5-104 Slave ASDU flags" ":ref:`xmlattr-IEC104slAsduFlags`" "ASDU flags"

.. include-file:: sections/Include/IEC10xsl_ASDUflags.rstinc
