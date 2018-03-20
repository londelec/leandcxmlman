.. _ref-IEC61850clScsmSettings:

ScsmSettings
^^^^^^^^^^^^

Specific Communication Service Mapping settings can be specified using attributes of :ref:`<ref-IEC61850clScsmSettings>` element node.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`<ref-IEC61850clScsmSettings>`"

.. code-block:: none

 <ScsmSettings Bdyndsname="dynb" Udyndsname="dynu" BOptFlds="0x0001" UOptFlds="0x0000" Flags="0x0003"/>


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
     :val:      0...65535 or 0x00...0xFFFF
     :def:      0x0000
     :desc:     Miscellaneous Specific Communication Service Mapping settings.
		See table :numref:`docref-IEC61850clScsmFlagsBits` for description.

.. include-file:: sections/Include/hidden_InfoLogFlags.rstinc "internal"

.. _docref-IEC61850clScsmOptFldsBits:

.. include-file:: sections/Include/table_flags16bit.rstinc "" "[OptFlds] of Report Control Blocks" ":ref:`<ref-IEC61850clScsmBOptFlds>` and :ref:`<ref-IEC61850clScsmUOptFlds>`" "[OptFlds]"

   * :attr:     Bit 0
     :val:      xxxx.xxxx xxxx.xxx0
     :desc:     **Exclude** [:lectext1:`entryID`] field from Reports (default value)

   * :(attr):
     :val:      xxxx.xxxx xxxx.xxx1
     :desc:     **Include** [:lectext1:`entryID`] field in Reports

   * :attr:     Bit 1
     :val:      xxxx.xxxx xxxx.xx0x
     :desc:     **Exclude** [:lectext1:`buffer-overflow`] field from Reports (default value)

   * :(attr):
     :val:      xxxx.xxxx xxxx.xx1x
     :desc:     **Include** [:lectext1:`buffer-overflow`] field in Reports

   * :attr:     Bit 2
     :val:      xxxx.xxxx xxxx.x0xx
     :desc:     **Exclude** [:lectext1:`data-reference`] field from Reports (default value)

   * :(attr):
     :val:      xxxx.xxxx.xxxx.x1xx
     :desc:     **Include** [:lectext1:`data-reference`] field in Reports

   * :attr:     Bit 3
     :val:      xxxx.xxxx xxxx.0xxx
     :desc:     **Exclude** [:lectext1:`data-set-name`] field from Reports (default value)

   * :(attr):
     :val:      xxxx.xxxx xxxx.1xxx
     :desc:     **Include** [:lectext1:`data-set-name`] field in Reports

   * :attr:     Bit 4
     :val:      xxxx.xxxx xxx0.xxxx
     :desc:     **Exclude** [:lectext1:`reason-for-inclusion`] field from Reports (default value)

   * :(attr):
     :val:      xxxx.xxxx xxx1.xxxx
     :desc:     **Include** [:lectext1:`reason-for-inclusion`] field in Reports

   * :attr:     Bit 5
     :val:      xxxx.xxxx xx0x.xxxx
     :desc:     **Exclude** [:lectext1:`report-time-stamp`] field from Reports (default value)

   * :(attr):
     :val:      xxxx.xxxx xx1x.xxxx
     :desc:     **Include** [:lectext1:`report-time-stamp`] field in Reports

   * :attr:     Bit 6
     :val:      xxxx.xxxx x0xx.xxxx
     :desc:     **Exclude** [:lectext1:`sequence-number`] field from Reports (default value for Unbuffered Reports)

   * :(attr):
     :val:      xxxx.xxxx x1xx.xxxx
     :desc:     **Include** [:lectext1:`sequence-number`] field in Reports (default value for Buffered Reports)

   * :attr:     Bit 15
     :val:      0xxx.xxxx xxxx.xxxx
     :desc:     **Exclude** [:lectext1:`conf-revision`] field from Reports (default value)

   * :(attr):
     :val:      1xxx.xxxx xxxx.xxxx
     :desc:     **Include** [:lectext1:`conf-revision`] field in Reports

   * :attr:     Bits 8...14
     :val:      Any
     :desc:     Bits reserved for future use

.. _docref-IEC61850clScsmFlagsBits:

.. include-file:: sections/Include/table_flags16bit.rstinc "" "Specific Communication Service Mapping flags" ":ref:`<ref-IEC61850clScsmFlags>`" "Specific Communication Service Mapping flags"

   * :attr:     Bit 0
     :val:      xxxx.xxxx xxxx.xxx0
     :desc:     **Add** leading 0 (zero) to dynamic dataset names with number less than 10. Dynamic datasets will have name e.g. 'dynb01'
		Dynamic dataset numbers are assigned automatically or specified with :ref:`DI<ref-IEC61850clDI>`.\ :ref:`<ref-IEC61850clDIDSnum>` \ or :ref:`AI<ref-IEC61850clAI>`.\ :ref:`<ref-IEC61850clAIDSnum>` attribute. (default value)

   * :(attr):
     :val:      xxxx.xxxx xxxx.xxx1
     :desc:     **Omit** leading 0 (zero) from dynamic dataset names with number less than 10. Dynamic datasets will have name e.g. 'dynb1'
		Dynamic dataset numbers are assigned automatically or specified with :ref:`DI<ref-IEC61850clDI>`.\ :ref:`<ref-IEC61850clDIDSnum>` \ or :ref:`AI<ref-IEC61850clAI>`.\ :ref:`<ref-IEC61850clAIDSnum>` attribute.

   * :attr:     Bit 1
     :val:      xxxx.xxxx xxxx.xx0x
     :desc:     **Don't set** [:lectext1:`PurgeBuf`] bit if [:lectext1:`EntryID`] setting fails during Report Control Block initialization (default value)

   * :(attr):
     :val:      xxxx.xxxx xxxx.xx1x
     :desc:     **Set** [:lectext1:`PurgeBuf`] bit if [:lectext1:`EntryID`] setting fails during Report Control Block initialization.
		Setting [:lectext1:`PurgeBuf`] bit will remove all Buffererd reports including those that might have not been sent to Client.

   * :attr:     Bit 2
     :val:      xxxx.xxxx xxxx.x0xx
     :desc:     Read Basic Types of **objects that don't exist in SCL** when station goes online.
		In case IEC61850 server has any objects that don't appear in CID/SCD, Basic Types of those objects will be read with [:lectext1:`GetDataDirectory`] (default value)

   * :(attr):
     :val:      xxxx.xxxx xxxx.x1xx
     :desc:     Read Basic Types of **all** objects when station goes online with [:lectext1:`GetDataDirectory`]
		
   * :attr:     Bits 3...15
     :val:      Any
     :desc:     Bits reserved for future use

.. include-file:: sections/Include/hidden_InfoLogFlagTable.rstinc "internal"
