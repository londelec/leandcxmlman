.. _ref-IEC61850clScsmSettings:

ScsmSettings
^^^^^^^^^^^^

Specific Communication Service Mapping settings can be specified using attributes of :ref:`<ref-IEC61850clScsmSettings>` element node.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`<ref-IEC61850clScsmSettings>`"

.. code-block:: none

 <ScsmSettings Bdyndsname="dynb" Udyndsname="dynu" BOptFlds="0x0001" UOptFlds="0x0000" Flags="0x03"/>


.. _docref-IEC61850clScsmSettingsAttab:

.. include-file:: sections/Include/table_attrs.rstinc "" "IEC61850 Client ScsmSettings attributes"

   * :attr:     :xmlref:`Bdyndsname`
     :val:      Max 16 chars
     :def:      dynb
     :desc:     Name for dynamic datasets that are going to be linked to Buffered Report Blocks.

   * :attr:     :xmlref:`Udyndsname`
     :val:      Max 16 chars
     :def:      dynu
     :desc:     Name for dynamic datasets that are going to be linked to Unbuffered Report Blocks.

   * :attr:     .. _ref-IEC61850clScsmBOptFlds:

		:xmlref:`BOptFlds`
     :val:      0x0000...0xFFFF
     :def:      0x0001
     :desc:     Optional Fields for Buffered Report Control Blocks.
		[OptFlds] of all used Report Control Blocks will be set to this value.
		Applies to all Report Control Blocks - defined in SCL and received from IED during initialization.
		See table :numref:`docref-IEC61850clScsmOptFldsBits` for description.

   * :attr:     .. _ref-IEC61850clScsmUOptFlds:

		:xmlref:`UOptFlds`
     :val:      0x0000...0xFFFF
     :def:      0x0000
     :desc:     Optional Fields for Unbuffered Report Control Blocks.
		[OptFlds] of all used Report Control Blocks will be set to this value.
		Applies to all Report Control Blocks - defined in SCL and received from IED during initialization. 
		See table :numref:`docref-IEC61850clScsmOptFldsBits` for description.

   * :attr:     .. _ref-IEC61850clScsmFlags:

                :xmlref:`Flags`
     :val:      0...255 or 0x00...0xFF
     :def:      0x00
     :desc:     Miscellaneous Specific Communication Service Mapping settings.
		See table :numref:`docref-IEC61850clScsmFlagsBits` for description.


.. _docref-IEC61850clScsmOptFldsBits:

.. field-list-table:: [OptFlds] of Report Control Blocks
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.20}|C{0.20}|S{0.50}|
   :header-rows: 1

   * :attr,10: Bits
     :val,10:  Value
     :desc,80: Description

   * :attr:     :ref:`<ref-IEC61850clScsmBOptFlds>` and :ref:`<ref-IEC61850clScsmUOptFlds>` [xxxx.xxxx.xxxx.xxxx]
     :val:      0x0000...0xFFFF
     :desc:     [OptFlds] is 16 bit encoded variable. Decimal 0...65535 and hex 0x0000...0xFFFF values supported

   * :attr:     Bit 0
     :val:      xxxx.xxxx.xxxx.xxx0
     :desc:     **Exclude** [entryID] field from Reports (default value)

   * :(attr):
     :val:      xxxx.xxxx.xxxx.xxx1
     :desc:     **Include** [entryID] field in Reports

   * :attr:     Bit 1
     :val:      xxxx.xxxx.xxxx.xx0x
     :desc:     **Exclude** [buffer-overflow] field from Reports (default value)

   * :(attr):
     :val:      xxxx.xxxx.xxxx.xx1x
     :desc:     **Include** [buffer-overflow] field in Reports

   * :attr:     Bit 2
     :val:      xxxx.xxxx.xxxx.x0xx
     :desc:     **Exclude** [data-reference] field from Reports (default value)

   * :(attr):
     :val:      xxxx.xxxx.xxxx.x1xx
     :desc:     **Include** [data-reference] field in Reports

   * :attr:     Bit 3
     :val:      xxxx.xxxx.xxxx.0xxx
     :desc:     **Exclude** [data-set-name] field from Reports (default value)

   * :(attr):
     :val:      xxxx.xxxx.xxxx.1xxx
     :desc:     **Include** [data-set-name] field in Reports

   * :attr:     Bit 4
     :val:      xxxx.xxxx.xxx0.xxxx
     :desc:     **Exclude** [reason-for-inclusion] field from Reports (default value)

   * :(attr):
     :val:      xxxx.xxxx.xxx1.xxxx
     :desc:     **Include** [reason-for-inclusion] field in Reports

   * :attr:     Bit 5
     :val:      xxxx.xxxx.xx0x.xxxx
     :desc:     **Exclude** [report-time-stamp] field from Reports (default value)

   * :(attr):
     :val:      xxxx.xxxx.xx1x.xxxx
     :desc:     **Include** [report-time-stamp] field in Reports

   * :attr:     Bit 6
     :val:      xxxx.xxxx.x0xx.xxxx
     :desc:     **Exclude** [sequence-number] field from Reports (default value for Unbuffered Reports)

   * :(attr):
     :val:      xxxx.xxxx.x1xx.xxxx
     :desc:     **Include** [sequence-number] field in Reports (default value for Buffered Reports)

   * :attr:     Bit 15
     :val:      0xxx.xxxx.xxxx.xxxx
     :desc:     **Exclude** [conf-revision] field from Reports (default value)

   * :(attr):
     :val:      1xxx.xxxx.xxxx.xxxx
     :desc:     **Include** [conf-revision] field in Reports

   * :attr:     Bits 8...14
     :val:      Any
     :desc:     Bits reserved for future use


.. _docref-IEC61850clScsmFlagsBits:

.. include-file:: sections/Include/table_flags.rstinc "" "Specific Communication Service Mapping flags" ":ref:`<ref-IEC61850clScsmFlags>`" "Specific Communication Service Mapping flags"

   * :attr:     Bit 0
     :val:      xxxx.xxx0
     :desc:     **Use** leading 0 (zero) in dynamic dataset names with number less than 10. Dynamic datasets will have name e.g. 'dynb01'
		Dynamic dataset numbers are assigned automatically or specified with :ref:`DI<ref-IEC61850clDI>`.\ :ref:`<ref-IEC61850clDIDSnum>` \ or :ref:`AI<ref-IEC61850clAI>`.\ :ref:`<ref-IEC61850clAIDSnum>` attribute. (default value)

   * :(attr):
     :val:      xxxx.xxx1
     :desc:     **Omit** leading 0 (zero) in dynamic dataset names with number less than 10. Dynamic datasets will have name e.g. 'dynb1'
		Dynamic dataset numbers are assigned automatically or specified with :ref:`DI<ref-IEC61850clDI>`.\ :ref:`<ref-IEC61850clDIDSnum>` \ or :ref:`AI<ref-IEC61850clAI>`.\ :ref:`<ref-IEC61850clAIDSnum>` attribute.

   * :attr:     Bit 1
     :val:      xxxx.xx0x
     :desc:     **Don't set** [PurgeBuf] bit if [EntryID] setting fails during Report Control Block initialization (default value)

   * :(attr):
     :val:      xxxx.xx1x
     :desc:     **Set** [PurgeBuf] bit if [EntryID] setting fails during Report Control Block initialization.
		Setting [PurgeBuf] bit will remove all Buffererd reports including those that might have not been sent to Client.

   * :attr:     Bits 2...7
     :val:      Any
     :desc:     Bits reserved for future use
