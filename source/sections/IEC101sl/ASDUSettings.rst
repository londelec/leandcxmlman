.. _ref-IEC101slASDUSettings:

ASDUSettings
^^^^^^^^^^^^

Application layer settings can be specified using attributes of :ref:`<ref-IEC101slASDUSettings>` element node.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`<ref-IEC101slASDUSettings>`"

.. code-block:: none

   <ASDUSettings COTSize="1" CAASize="1" IOASize="2" InvalidEvent="1" SUthroughoutDST="1" DIEventType="2" AIEventType="14" DOType="46" AOType="50" DIInterDelay="8000" DIIndetDelay="3500" DIEventStartup="1" AIEventStartup="1" TimeSync="1" TranspTypes="1" ForwardGI="1" />


.. _docref-IEC101slASDUSettingsAttab:

.. include-file:: sections/Include/table_attrs.rstinc "" "IEC60870-5-101 Slave ASDUSettings attributes"

.. include-file:: sections/Include/IEC60870_ASDUsizes.rstinc "" ".. _ref-IEC101slASDUSettingsCOTSize:" ".. _ref-IEC101slASDUSettingsCAASize:" ".. _ref-IEC101slASDUSettingsIOASize:"

.. include-file:: sections/Include/IEC60870_InvalidEvent.rstinc

.. include-file:: sections/Include/IEC60870_SUthroughoutDST.rstinc

   * :attr:     :xmlref:`DIEventType`
     :val:      See table :numref:`ref-IEC10xslDITypeIDValues`
     :def:      2 [M_SP_TA_1]
     :desc:     Use this ASDU type to send DI events which don't have :ref:`DI<ref-IEC10xslDI>`.\ :ref:`<ref-IEC10xslDITypeID>` \ attribute specified in their element node. This setting also affects ASDU type of the static data (e.g. Single or Double status information) reported to a General Interrogation request. (default value 2 – 'Single-point Information', DI event will be sent using ASDU type 2 [M_SP_TA_1], **CP24time2A**, msec and min)

   * :attr:     :xmlref:`AIEventType`
     :val:      See table :numref:`ref-IEC10xslAITypeIDValues`
     :def:      14 [M_ME_TC_1]
     :desc:     Use this ASDU type to send AI events which don't have :ref:`AI<ref-IEC10xslAI>`.\ :ref:`<ref-IEC10xslAITypeID>` \ attribute specified in their element node. This setting also affects ASDU type of the static data (e.g. Normalized, Scaled, Short floating point) reported to a General Interrogation request. (default value 14 – 'Short floating point', AI event will be sent using ASDU type 14 [M_ME_TC_1], **CP24time2A**, msec and min)

.. include-file:: sections/Include/IEC10xsl_ASDU.rstinc "" ".. _ref-IEC101slASDUSettingsTranspTypes:"

.. include-file:: sections/Include/IEC60870_ForwardGI.rstinc
