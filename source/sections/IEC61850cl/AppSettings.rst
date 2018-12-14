.. _ref-IEC61850clAppSettings:

AppSettings
^^^^^^^^^^^

Application layer settings can be specified using attributes of :ref:`<ref-IEC61850clAppSettings>` element node.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`<ref-IEC61850clAppSettings>`"

.. code-block:: none

 <AppSettings IgnoreTimetags="1" AIDeadband="2" AIPercent="0.5" DIEventStartup="1" AIEventStartup="1" ForwardGI="1" bufTime="0" orCat="3" orIdent="LEANDC" Flags="0x0000"/>


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

   * :attr:     :xmlref:`orCat`
     :val:      1...8
     :def:      3
     :desc:     Originator category value for outgoing commands [IEC61850-7-3:2011].
		Default value 3 = [:lectext1:`remote-control`]

   * :attr:     :xmlref:`orIdent`
     :val:      64 chars
     :def:      LEANDC
     :desc:     Originator identification value for outgoing commands [IEC61850-7-3:2011].

   * :attr:     .. _ref-IEC61850clAppFlags:

                :xmlref:`Flags`
     :val:      0...65535 or 0x00...0xFFFF
     :def:      0x0000
     :desc:     Miscellaneous settings of the Application layer.
		See table :numref:`ref-IEC61850clAppFlagsBits` for description.


.. _ref-IEC61850clAppFlagsBits:

.. include-file:: sections/Include/table_flags16bit.rstinc "" "Application layer flags" ":ref:`<ref-IEC61850clAppFlags>`" "Application layer flags"

   * :attr:     Bit 0
     :val:      xxxx.xxxx xxxx.xxx0
     :desc:     **Don't read** the LD directory [:lectext1:`GetLogicalDeviceDirectory`] when station goes online if IED supports only static datasets (default value)

   * :(attr):
     :val:      xxxx.xxxx xxxx.xxx1
     :desc:     **Read** the LD directory [:lectext1:`GetLogicalDeviceDirectory`] when station goes online even if IED supports only static datasets.
		IED initialization will take longer if this bit is enabled, however it offers extra checks.
		Object directory received from IED will be matched against SCL file and any inconsistencies will be reported.

   * :attr:     Bit 1
     :val:      xxxx.xxxx xxxx.xx0x
     :desc:     **Process** reports generated after Enhanced security command completion (default value)

   * :(attr):
     :val:      xxxx.xxxx xxxx.xx1x
     :desc:     **Ignore** reports generated after Enhanced security command completion.
		This bit has to be used only for IEDs that doesn't generate a report when Enhanced security Direct or SBO command is complete.
		If not set command will be removed only after Application timeout expiration.

   * :attr:     Bit 2
     :val:      xxxx.xxxx xxxx.x0xx
     :desc:     **Ignore** millisecond accuracy of timetags received from IED (default value)

   * :(attr):
     :val:      xxxx.xxxx xxxx.x1xx
     :desc:     **Use** millisecond accuracy of timetags received from IED.
		Some IEDs report lower accuracy if the IED is not synchronized.
		Enabling this setting will result in rounding of milliseconds based on the accuracy and the timetag may appear different from the value IED has recorded in the internal event list.

   * :attr:     Bit 4
     :val:      xxxx.xxxx xxx0.xvxx
     :desc:     **Use** [:lectext1:`Resv`] attribute value of the Unbufferred report control block received from IED (default value)
		IEC61850 client tries to reserve only unbuffered report control blocks that are not already reserved by another client.

   * :(attr):
     :val:      xxxx.xxxx xxx1.xxxx
     :desc:     **Ignore** [:lectext1:`Resv`] attribute value of the Unbufferred report control block received from IED.
		IEC61850 client tries to reserve unbuffered report control blocks even if already reserved by another client.

   * :attr:     Bit 8
     :val:      xxxx.xxx0 xxxx.xxxx
     :desc:     Enable only Report Blocks with linked static datasets that contain **defined DI/AI objects** (default value)

   * :(attr):
     :val:      xxxx.xxx1 xxxx.xxxx
     :desc:     Enable **all** Report Blocks that exist in the SCL file.
		This setting applies only to Report Blocks that are defined in the SCL file.

.. include-file:: sections/Include/hidden_IEC61850clAppFlagsBit8.rstinc "internal"

   * :attr:     Bits 3;5...7;9...15
     :val:      Any
     :desc:     Bits reserved for future use
