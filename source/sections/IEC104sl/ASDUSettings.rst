.. _ref-IEC104slASDUSettings:

ASDUSettings
^^^^^^^^^^^^

Application layer settings can be specified using attributes of :ref:`<ref-IEC104slASDUSettings>` element node.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`<ref-IEC104slASDUSettings>`"

.. code-block:: none

   <ASDUSettings InvalidEvent="1" SUthroughoutDST="1" DIEventType="31" AIEventType="36" DOType="46" AOType="50" DIInterDelay="8000" DIIndetDelay="3500" DIEventStartup="1" AIEventStartup="1" TimeSync="1" TranspTypes="1" ForwardGI="1" CommandLatency="300" />


.. _docref-IEC104slASDUSettingsAttab:

.. include-file:: sections/Include/table_attrs.rstinc "" "IEC60870-5-104 Slave ASDUSettings attributes"

.. include-file:: sections/Include/IEC60870_InvalidEvent.rstinc

.. include-file:: sections/Include/IEC60870_SUthroughoutDST.rstinc

   * :attr:     :xmlref:`DIEventType`
     :val:      See table :numref:`ref-IEC10xslDITypeIDValues`
     :def:      30 [M_SP_TB_1]
     :desc:     Use this ASDU type to send DI events which don't have :ref:`DI<ref-IEC10xslDI>`.\ :ref:`<ref-IEC10xslDITypeID>` \ attribute specified in their element node. This setting also affects ASDU type of the static data (e.g. Single or Double status information) reported to a General Interrogation request. (default value 30 – 'Single-point Information', DI event will be sent using ASDU type 30 [M_SP_TB_1], **CP56time2A**, full time)

   * :attr:     :xmlref:`AIEventType`
     :val:      See table :numref:`ref-IEC10xslAITypeIDValues`
     :def:      36 [M_ME_TF_1]
     :desc:     Use this ASDU type to send AI events which don't have :ref:`AI<ref-IEC10xslAI>`.\ :ref:`<ref-IEC10xslAITypeID>` \ attribute specified in their element node. This setting also affects ASDU type of the static data (e.g. Normalized, Scaled, Short floating point) reported to a General Interrogation request. (default value 36 – 'Short floating point', AI event will be sent using ASDU type 36 [M_ME_TF_1], **CP56time2A**, full time)

.. include-file:: sections/Include/IEC10xsl_ASDU.rstinc "" ".. _ref-IEC104slASDUSettingsTranspTypes:"

.. include-file:: sections/Include/IEC60870_ForwardGI.rstinc

   * :attr:     :xmlref:`CommandLatency`
     :val:      0...2\ :sup:`32`\  - 1
     :def:      0 sec
     :desc:     Maximal difference in seconds between received time-tagged control command and the internal time.
		If this attribute is used, time-tag of the received control command is checked and command will be discarded if it has been substantially delayed.
		Value 0 disables time-tagged command validation and any incoming control command will be accepted.
