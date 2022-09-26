.. _xmlelem-IEC101slAsdu:

ASDUSettings
^^^^^^^^^^^^

Application layer settings can be specified using attributes of :ref:`xmlelem-IEC101slAsdu` element node.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-IEC101slAsdu`"

.. code-block:: none

   <ASDUSettings COTSize="1" CAASize="1" IOASize="2" InvalidEvent="1" SUthroughoutDST="1" DIEventType="2" AIEventType="14" DOType="46" AOType="50" DIInterDelay="8000" DIIndetDelay="3500" DIEventStartup="1" AIEventStartup="1" TimeSync="1" TranspTypes="1" Flags="0x00" ForwardGI="1" />


.. include-file:: sections/Include/table_attrs.rstinc "" "tabid-IEC101slAsdu" "IEC60870-5-101 Slave ASDUSettings attributes" ":spec: |C{0.19}|C{0.12}|C{0.14}|S{0.55}|"

.. include-file:: sections/Include/IEC60870_ASDUsizes.rstinc ""

.. include-file:: sections/Include/IEC60870_InvalidEvent.rstinc ""

.. include-file:: sections/Include/IEC60870_SUthroughoutDST.rstinc ""

   * :attr:	:xmlattr:`DIEventType`
     :val:	See :numref:`tabid-IEC10xslDITypeID`
     :def:	2 [:lemonobgtext:`M_SP_TA_1`]
     :desc:	Use this ASDU type to send DI events which don't have :ref:`xmlelem-IEC10xslDI`.\ :ref:`xmlattr-IEC10xslDITypeID` \ attribute specified in their element node.
		This setting also affects ASDU type of the static data (e.g. Single or Double status information) reported to a General Interrogation request.
		(default value 2 – 'Single-point Information', DI event will be sent using ASDU type 2 [:lemonobgtext:`M_SP_TA_1`], **CP24time2A**, msec and min)

   * :attr:	:xmlattr:`AIEventType`
     :val:	See :numref:`tabid-IEC10xslAITypeID`
     :def:	14 [:lemonobgtext:`M_ME_TC_1`]
     :desc:	Use this ASDU type to send AI events which don't have :ref:`xmlelem-IEC10xslAI`.\ :ref:`xmlattr-IEC10xslAITypeID` \ attribute specified in their element node.
		This setting also affects ASDU type of the static data (e.g. Normalized, Scaled, Short floating point) reported to a General Interrogation request.
		(default value 14 – 'Short floating point', AI event will be sent using ASDU type 14 [:lemonobgtext:`M_ME_TC_1`], **CP24time2A**, msec and min)

.. include-file:: sections/Include/IEC10xsl_ASDU.rstinc "" ":numref:`tabid-IEC101slAsduFlags`"

.. include-file:: sections/Include/IEC60870_ForwardGI.rstinc ""


.. include-file:: sections/Include/table_flags8.rstinc "" "tabid-IEC101slAsduFlags" "IEC60870-5-101 Slave ASDU flags" ":ref:`xmlattr-IEC101slAsduFlags`" "ASDU flags"

.. include-file:: sections/Include/IEC10xsl_ASDUflags.rstinc
