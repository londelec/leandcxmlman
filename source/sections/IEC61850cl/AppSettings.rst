.. _ref-IEC61850clAppSettings:

AppSettings
^^^^^^^^^^^

Application layer settings can be specified using attributes of :ref:`<ref-IEC61850clAppSettings>` element node.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`<ref-IEC61850clAppSettings>`"

.. code-block:: none

 <AppSettings IgnoreTimetags="1" AIDeadband="2" AIPercent="0.5" DIEventStartup="1" AIEventStartup="1" ForwardGI="1" bufTime="0" Flags="0x00"/>


.. _docref-IEC61850clAppSettingsAttab:

.. include-file:: sections/Include/table_attrs.rstinc "" "IEC61850 Client AppSettings attributes"

.. include-file:: sections/Include/ma_IgnoreTimetags.rstinc

.. include-file:: sections/Include/AI_ThresholdsCmn.rstinc "" ".. _ref-IEC61850clAppSettingsAIDeadband:" ".. _ref-IEC61850clAppSettingsAIPercent:" ":ref:`AI<ref-IEC61850clAI>`" ":ref:`<ref-IEC61850clAIDeadband>`" ":ref:`<ref-IEC61850clAIPercent>`"

.. include-file:: sections/Include/IEC60870_ASDU_EventStartup.rstinc

.. include-file:: sections/Include/IEC60870_ForwardGI.rstinc

   * :attr:     :xmlref:`bufTime`
     :val:      0...2\ :sup:`32`\  - 2
     :def:      0 msec
     :desc:     Interval in milliseconds for the buffering of internal notifications before Information Report is generated [IEC61850-7-2:2010].
		Value 0 disables buffering and Information Reports are generated instantly.

   * :attr:     .. _ref-IEC61850clAppFlags:

                :xmlref:`Flags`
     :val:      0...255 or 0x00...0xFF
     :def:      0x00
     :desc:     Miscellaneous settings of the Application layer.
		See table :numref:`docref-IEC61850clAppFlagsBits` for description.


.. _docref-IEC61850clAppFlagsBits:

.. include-file:: sections/Include/table_flags.rstinc "" "Application layer flags" ":ref:`<ref-IEC61850clAppFlags>`" "Application layer flags"

   * :attr:     Bit 0
     :val:      xxxx.xxx0
     :desc:     **Don't read** the LD directory [GetLogicalDeviceDirectory] when station goes online if IED supports only static datasets (default value)

   * :(attr):
     :val:      xxxx.xxx1
     :desc:     **Read** the LD directory [GetLogicalDeviceDirectory] when station goes online even if IED supports only static datasets.
		IED initialization will take longer if this bit is enabled, however it offers extra checks.
		Object directory received from IED will be matched against SCL file and any inconsistencies will be reported.

   * :attr:     Bit 1
     :val:      xxxx.xx0x
     :desc:     **Process** reports generated after Enhanced security command completion (default value)

   * :(attr):
     :val:      xxxx.xx1x
     :desc:     **Ignore** reports generated after Enhanced security command completion.
		This bit has to be used only for IEDs that doesn't generate a report when Enhanced security Direct or SBO command is complete.
		If not set command will be removed only after Application timeout expiration.

   * :attr:     Bits 2...7
     :val:      Any
     :desc:     Bits reserved for future use
