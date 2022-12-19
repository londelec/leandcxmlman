.. _xmlelem-IEC61850clAcsi:

AcsiSettings
^^^^^^^^^^^^

Abstract Communication Service Interface (IEC61850-7-x ACSI) settings can be specified using attributes of :ref:`xmlelem-IEC61850clAcsi` element node.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-IEC61850clAcsi`"

.. code-block:: none

 <AcsiSettings Bdyndsname="dynb" Udyndsname="dynu" Maxdynds="10" BOptFlds="0x0001" UOptFlds="0x0000" orCat="3" orIdent="LEANDC" bufTime="0" Flags="0x0003" RCBFlags="0x0000" DSFlags="0x0000" LogFlags="0x0000"/>


.. include-file:: sections/Include/table_attrs.rstinc "" "tabid-IEC61850clAcsi" "IEC61850 Client AcsiSettings attributes" ":spec: |C{0.14}|C{0.18}|C{0.1}|S{0.58}|"

.. include-file:: sections/Include/IEC61850cl_dyndsname.rstinc "" ":xmlattr:`Bdyndsname`" "dynb" "Buffered"

.. include-file:: sections/Include/IEC61850cl_dyndsname.rstinc "" ":xmlattr:`Udyndsname`" "dynu" "Unbuffered"

   * :attr:	:xmlattr:`Maxdynds`
     :val:	0...255
     :def:	20
     :desc:	Maximal number of dynamic datasets that can be created.
		Datasets linked to Buffered and Unbuffered Report Blocks are accounted separately.
		Default value 20 means 20 (Buffered) + 20 (Unbuffered) dynamic datasets can be created.

   * :attr:	:xmlattr:`BOptFlds`
     :val:	0x0000...0xFFFF
     :def:	0x0001
     :desc:	Optional Fields for Buffered Report Control Blocks.
		[OptFlds] of all used Report Control Blocks will be set to this value.
		Applies to all Report Control Blocks - defined in the SCL and received from IED during initialization.
		See :numref:`tabid-IEC61850clAcsiOptFlds` for description.

   * :attr:	:xmlattr:`UOptFlds`
     :val:	0x0000...0xFFFF
     :def:	0x0000
     :desc:	Optional Fields for Unbuffered Report Control Blocks.
		[OptFlds] of all used Report Control Blocks will be set to this value.
		Applies to all Report Control Blocks - defined in the SCL and received from IED during initialization.
		See :numref:`tabid-IEC61850clAcsiOptFlds` for description.

   * :attr:	:xmlattr:`orCat`
     :val:	1...8
     :def:	3
     :desc:	Originator category value for outgoing commands [IEC61850-7-3:2011].
		Default value 3 = [:lemonobgtext:`remote-control`]

   * :attr:	:xmlattr:`orIdent`
     :val:	1...64 chars
     :def:	LEANDC
     :desc:	Originator identification value for outgoing commands [IEC61850-7-3:2011].

   * :attr:	:xmlattr:`bufTime`
     :val:	0...2\ :sup:`32`\  - 2
     :def:	0 msec
     :desc:	Interval in milliseconds for buffering internal notifications before Information Report is generated [IEC61850-7-2:2010].
		Value 0 disables buffering and Information Reports are generated instantly.

   * :attr:	:xmlattr:`Flags`
     :val:	|flags16range|
     :def:	0x0000
     :desc:	Miscellaneous Abstract Communication Service Interface settings.
		See :numref:`tabid-IEC61850clAcsiFlags` for description.

   * :attr:	:xmlattr:`RCBFlags`
     :val:	|flags16range|
     :def:	0x0000
     :desc:	Report Control Block settings.
		See :numref:`tabid-IEC61850clAcsiRCBFlags` for description.

   * :attr:	:xmlattr:`DSFlags`
     :val:	|flags16range|
     :def:	0x0000
     :desc:	Dataset settings.
		See :numref:`tabid-IEC61850clAcsiDSFlags` for description.

.. include-file:: sections/Include/IEC61850_LogFlags16.rstinc "" ":numref:`tabid-IEC61850clAcsiLogFlags`"


.. include-file:: sections/Include/table_flags16.rstinc "" "tabid-IEC61850clAcsiOptFlds" "[OptFlds] of Report Control Blocks" ":ref:`xmlattr-IEC61850clAcsiBOptFlds` and :ref:`xmlattr-IEC61850clAcsiUOptFlds`" "[OptFlds]"

   * :attr:	Bit 0
     :val:	xxxx.xxxx xxxx.xxx0
     :desc:	**Exclude** [:lemonobgtext:`entryID`] field from Reports (default value)

   * :(attr):
     :val:	xxxx.xxxx xxxx.xxx1
     :desc:	**Include** [:lemonobgtext:`entryID`] field in Reports

   * :attr:	Bit 1
     :val:	xxxx.xxxx xxxx.xx0x
     :desc:	**Exclude** [:lemonobgtext:`buffer-overflow`] field from Reports (default value)

   * :(attr):
     :val:	xxxx.xxxx xxxx.xx1x
     :desc:	**Include** [:lemonobgtext:`buffer-overflow`] field in Reports

   * :attr:	Bit 2
     :val:	xxxx.xxxx xxxx.x0xx
     :desc:	**Exclude** [:lemonobgtext:`data-reference`] field from Reports (default value)

   * :(attr):
     :val:	xxxx.xxxx xxxx.x1xx
     :desc:	**Include** [:lemonobgtext:`data-reference`] field in Reports

   * :attr:	Bit 3
     :val:	xxxx.xxxx xxxx.0xxx
     :desc:	**Exclude** [:lemonobgtext:`data-set-name`] field from Reports (default value)

   * :(attr):
     :val:	xxxx.xxxx xxxx.1xxx
     :desc:	**Include** [:lemonobgtext:`data-set-name`] field in Reports

   * :attr:	Bit 4
     :val:	xxxx.xxxx xxx0.xxxx
     :desc:	**Exclude** [:lemonobgtext:`reason-for-inclusion`] field from Reports (default value)

   * :(attr):
     :val:	xxxx.xxxx xxx1.xxxx
     :desc:	**Include** [:lemonobgtext:`reason-for-inclusion`] field in Reports

   * :attr:	Bit 5
     :val:	xxxx.xxxx xx0x.xxxx
     :desc:	**Exclude** [:lemonobgtext:`report-time-stamp`] field from Reports (default value)

   * :(attr):
     :val:	xxxx.xxxx xx1x.xxxx
     :desc:	**Include** [:lemonobgtext:`report-time-stamp`] field in Reports

   * :attr:	Bit 6
     :val:	xxxx.xxxx x0xx.xxxx
     :desc:	**Exclude** [:lemonobgtext:`sequence-number`] field from Reports (default value for Unbuffered Reports)

   * :(attr):
     :val:	xxxx.xxxx x1xx.xxxx
     :desc:	**Include** [:lemonobgtext:`sequence-number`] field in Reports (default value for Buffered Reports)

   * :attr:	Bit 15
     :val:	0xxx.xxxx xxxx.xxxx
     :desc:	**Exclude** [:lemonobgtext:`conf-revision`] field from Reports (default value)

   * :(attr):
     :val:	1xxx.xxxx xxxx.xxxx
     :desc:	**Include** [:lemonobgtext:`conf-revision`] field in Reports

   * :attr:	Bits 7...14
     :val:	Any
     :desc:	Bits reserved for future use


.. include-file:: sections/Include/table_flags16.rstinc "" "tabid-IEC61850clAcsiFlags" "Abstract Communication Service Interface flags" ":ref:`xmlattr-IEC61850clAcsiFlags`" "ACSI flags"

   * :attr:	:bitdef:`0`
     :val:	xxxx.xxxx xxxx.xxx0
     :desc:	**Don't read** directory when station goes online. (default value)
		This setting applies only if IED doesn't support Dynamic datasets.
		If IED supports Dynamic datasets, directory will always be read regardless of this setting.

   * :(attr):
     :val:	xxxx.xxxx xxxx.xxx1
     :desc:	| **Always read** directory when station goes online.
		  IED initialization will take longer, however this offers extra checks.
		  Directory received from IED will be matched against the SCL tree and any inconsistencies will be reported. ACSI services:
		| [:lemonobgtext:`GetServerDirectory`] 
		| [:lemonobgtext:`GetLogicalDeviceDirectory`] 
		| [:lemonobgtext:`GetLogicalNodeDirectory`] [:lemonobgtext:`ACSIClass`]="Data,BRCB,URCB,LCB,SGCB"

   * :attr:	Bit 1
     :val:	xxxx.xxxx xxxx.xx0x
     :desc:	| Read Basic Types of **elements that don't exist in SCL** when station goes online. (default value)
		  If any new elements have been discovered in directory response that don't exist in the SCL tree, Basic Types of those will be requested with [:lemonobgtext:`GetDataDefinition`].
		| It will happen only in one of these situations:
		| > IED supports Dynamic datasets;
		| > IED doesn't support Dynamic datasets, but directory read is enabled with :ref:`bitref-IEC61850clAcsiFlagsBit0`\ |bittrue|.

   * :(attr):
     :val:	xxxx.xxxx xxxx.xx1x
     :desc:	Read Basic Types of **all** elements when station goes online with [:lemonobgtext:`GetDataDefinition`].
		It will only happen in 2 situations described above.

   * :attr:	:bitdef:`2`
     :val:	xxxx.xxxx xxxx.x0xx
     :desc:	**Don't read** Basic Types of elements which are required for data acquisition (linked to DI/AI) when station goes online. (default value)

   * :(attr):
     :val:	xxxx.xxxx xxxx.x1xx
     :desc:	| **Read** Basic Types of elements which are required for data acquisition (linked to DI/AI) when station goes online.
		| It will happen only in one of these situations:
		| > IED supports Dynamic datasets;
		| > IED doesn't support Dynamic datasets, but directory read is enabled with :ref:`bitref-IEC61850clAcsiFlagsBit0`\ |bittrue|.
		| > IED doesn't support Dynamic datasets and Report Blocks are included in the SCL file.

   * :attr:	Bit 4
     :val:	xxxx.xxxx xxx0.xxxx
     :desc:	**Process** [:lemonobgtext:`CommandTermination`] received after Enhanced security command completion. (default value)

   * :(attr):
     :val:	xxxx.xxxx xxx1.xxxx
     :desc:	**Ignore** missing [:lemonobgtext:`CommandTermination`] after Enhanced security commands.
		This setting has to be used only if IED doesn't generate [:lemonobgtext:`CommandTermination`] when Enhanced security Direct or SBO command is complete.
		If there is no termination and this setting is not used, the command will only be completed after Application timeout expiration.

   * :attr:	Bit 5
     :val:	xxxx.xxxx xx0x.xxxx
     :desc:	**Ignore** millisecond accuracy of timetags received from IED (default value)

   * :(attr):
     :val:	xxxx.xxxx xx1x.xxxx
     :desc:	**Use** millisecond accuracy of timetags received from IED.
		Some IEDs report lower accuracy if the IED is not synchronized.
		Enabling this setting will result in rounding of milliseconds based on the received accuracy and the timetag may appear different than record in IED's internal event list.

   * :attr:	Bits 3;6...15
     :val:	Any
     :desc:	Bits reserved for future use


.. include-file:: sections/Include/table_flags16.rstinc "" "tabid-IEC61850clAcsiRCBFlags" "Report Control Block flags" ":ref:`xmlattr-IEC61850clAcsiRCBFlags`" "Report Control Block flags"

   * :attr:	Bit 0
     :val:	xxxx.xxxx xxxx.xxx0
     :desc:	**Don't set** [:lemonobgtext:`PurgeBuf`] bit if [:lemonobgtext:`EntryID`] setting fails during Report Control Block initialization (default value)

   * :(attr):
     :val:	xxxx.xxxx xxxx.xxx1
     :desc:	**Set** [:lemonobgtext:`PurgeBuf`] bit if [:lemonobgtext:`EntryID`] setting fails during Report Control Block initialization.
		Setting [:lemonobgtext:`PurgeBuf`] bit will remove all Buffered reports including those that might not have been sent to Client.

   * :attr:	Bit 1
     :val:	xxxx.xxxx xxxx.xx0x
     :desc:	**Observe** [:lemonobgtext:`Resv`] attribute value of the Unbufferred Report Control Block received from IED (default value)
		We will try to reserve only those Unbuffered Report Control Blocks not already reserved by another client.

   * :(attr):
     :val:	xxxx.xxxx xxxx.xx1x
     :desc:	**Ignore** [:lemonobgtext:`Resv`] attribute value of the Unbufferred Report Control Block received from IED.
		We will try to reserve all Unbuffered Report Control Blocks even if already reserved by another client.


.. include-file:: sections/Include/table_flags16.rstinc "" "tabid-IEC61850clAcsiDSFlags" "Dataset flags" ":ref:`xmlattr-IEC61850clAcsiDSFlags`" "Dataset flags"

   * :attr:	Bit 0
     :val:	xxxx.xxxx xxxx.xxx0
     :desc:	**Add** leading 0 (zero) to dynamic dataset names with a number less than 10. Dynamic dataset will have a name e.g. 'dynb01'.
		Numbers are added to dynamic dataset names created from :ref:`xmlattr-IEC61850clAcsiBdyndsname` or :ref:`xmlattr-IEC61850clAcsiUdyndsname` attributes. (default value)

   * :(attr):
     :val:	xxxx.xxxx xxxx.xxx1
     :desc:	**Omit** leading 0 (zero) from dynamic dataset names with a number less than 10. Dynamic dataset will have a name e.g. 'dynb1'.
		Numbers are added to dynamic dataset names created from :ref:`xmlattr-IEC61850clAcsiBdyndsname` or :ref:`xmlattr-IEC61850clAcsiUdyndsname` attributes.

   * :attr:	Bit 1
     :val:	xxxx.xxxx xxxx.xx0x
     :desc:	**Delete** dynamic datasets that are not created by us. (default value)
		This means datasets with names other than :ref:`xmlattr-IEC61850clAcsiBdyndsname` or :ref:`xmlattr-IEC61850clAcsiUdyndsname` (e.g. 'dynb01', 'dynu01')
		and names not defined by :ref:`xmlelem-IEC61850clDI`.\ :ref:`xmlattr-IEC61850clDIDSref` and :ref:`xmlelem-IEC61850clAI`.\ :ref:`xmlattr-IEC61850clAIDSref` attributes.
		This setting applies only if IED supports Dynamic dataset creation.

   * :(attr):
     :val:	xxxx.xxxx xxxx.xx1x
     :desc:	**Don't delete** dynamic datasets that are not created by us.
		This setting applies only if IED supports Dynamic dataset creation.

   * :attr:	Bit 8
     :val:	xxxx.xxx0 xxxx.xxxx
     :desc:	Initialize only those Report Blocks with linked datasets that are **required for data acquisition** of DI/AI objects. (default value)
		This setting applies only if IED doesn't support Dynamic datasets.
		If IED supports Dynamic datasets, we will check and rebuild datasets according to configured DI/AIs.

   * :(attr):
     :val:	xxxx.xxx1 xxxx.xxxx
     :desc:	Initialize **all** available Report Blocks that are linked to datasets.
		This setting applies only if IED doesn't support Dynamic datasets.
		If IED supports Dynamic datasets, we will check and rebuild datasets according to configured DI/AIs.

   * :attr:	:bitdef:`9`
     :val:	xxxx.xx0x xxxx.xxxx
     :desc:	Dynamic dataset functionality is **enabled** if IED supports Dynamic dataset creation. (default value)

   * :(attr):
     :val:	xxxx.xx1x xxxx.xxxx
     :desc:	Dynamic dataset functionality is **disabled**.
		Only static datasets will be used even if IED supports Dynamic dataset creation.

   * :attr:	Bits 2...7;10...15
     :val:	Any
     :desc:	Bits reserved for future use


.. include-file:: sections/Include/table_flags16.rstinc "" "tabid-IEC61850clAcsiLogFlags" "ACSI informative logger flags" ":ref:`xmlattr-IEC61850clAcsiLogFlags`" "Logger flags"

   * :attr:	Bit 0
     :val:	xxxx.xxxx xxxx.xxx0
     :desc:	LD/LN/RCB/DO/DA element validation **will not be** recorded.

   * :(attr):
     :val:	xxxx.xxxx xxxx.xxx1
     :desc:	| LD/LN/RCB/DO/DA element validation **will be** recorded. ACSI services:
		| [:lemonobgtext:`GetServerDirectory`]
		| [:lemonobgtext:`GetLogicalDeviceDirectory`]
		| [:lemonobgtext:`GetLogicalNodeDirectory`] [:lemonobgtext:`ACSIClass`]="Data,BRCB,URCB,LCB,SGCB"

   * :attr:	Bit 1
     :val:	xxxx.xxxx xxxx.xx0x
     :desc:	DS and FCDA validation **will not be** recorded.

   * :(attr):
     :val:	xxxx.xxxx xxxx.xx1x
     :desc:	| DS and FCDA validation **will be** recorded. ACSI services:
		| [:lemonobgtext:`GetLogicalNodeDirectory`] [:lemonobgtext:`ACSIClass`]="DATA-SET"
		| [:lemonobgtext:`GetDataSetDirectory`]

   * :attr:	Bit 2
     :val:	xxxx.xxxx xxxx.x0xx
     :desc:	Basic Types **will not be** recorded.

   * :(attr):
     :val:	xxxx.xxxx xxxx.x1xx
     :desc:	| Basic Types **will be** recorded. ACSI services:
		| [:lemonobgtext:`GetDataDirectory`]
		| [:lemonobgtext:`GetDataDefinition`]

   * :attr:	Bit 3
     :val:	xxxx.xxxx xxxx.0xxx
     :desc:	Data values **will not be** recorded.

   * :(attr):
     :val:	xxxx.xxxx xxxx.1xxx
     :desc:	| Data values **will be** recorded. ACSI services:
		| [:lemonobgtext:`GetDataValues`]
		| [:lemonobgtext:`SetDataValues`]
		| [:lemonobgtext:`GetDatasetValues`]
		| [:lemonobgtext:`SetDatasetValues`]
		| [:lemonobgtext:`GetBRCBValues`]
		| [:lemonobgtext:`SetBRCBValues`]
		| [:lemonobgtext:`GetURCBValues`]
		| [:lemonobgtext:`SetURCBValues`]
		| and all command services

   * :attr:	Bit 4
     :val:	xxxx.xxxx xxx0.xxxx
     :desc:	Dynamically created/removed LD/LN/RCB/DO/DA elements **will not be** recorded.

   * :(attr):
     :val:	xxxx.xxxx xxx1.xxxx
     :desc:	| Dynamically created/removed LD/LN/RCB/DO/DA elements **will be** recorded. These are differences between current SCL tree and ACSI services:
		| [:lemonobgtext:`GetServerDirectory`]
		| [:lemonobgtext:`GetLogicalDeviceDirectory`]
		| [:lemonobgtext:`GetLogicalNodeDirectory`] [:lemonobgtext:`ACSIClass`]="Data,BRCB,URCB,LCB,SGCB"

   * :attr:	Bit 5
     :val:	xxxx.xxxx xx0x.xxxx
     :desc:	Dynamically created/deleted datasets and differences in dataset contents **will not be** recorded.

   * :(attr):
     :val:	xxxx.xxxx xx1x.xxxx
     :desc:	| Dynamically created/deleted datasets and differences in dataset contents **will be** recorded. These are differences between current SCL tree and ACSI services:
		| [:lemonobgtext:`CreateDataSet`]
		| [:lemonobgtext:`DeleteDataSet`]
		| [:lemonobgtext:`GetLogicalNodeDirectory`] [:lemonobgtext:`ACSIClass`]="DATA-SET"
		| [:lemonobgtext:`GetDataSetDirectory`]

   * :attr:	Bit 6
     :val:	xxxx.xxxx x0xx.xxxx
     :desc:	Differences in Basic Types **will not be** recorded.

   * :(attr):
     :val:	xxxx.xxxx x1xx.xxxx
     :desc:	| Differences in Basic Types **will be** recorded. These are differences between current SCL tree and ACSI services:
		| [:lemonobgtext:`GetDataDirectory`]
		| [:lemonobgtext:`GetDataDefinition`]

   * :attr:	Bit 8
     :val:	xxxx.xxx0 xxxx.xxxx
     :desc:	Progress of the main state machine **will not be** recorded.

   * :(attr):
     :val:	xxxx.xxx1 xxxx.xxxx
     :desc:	Progress of the main state machine **will be** recorded (Application).

   * :attr:	Bit 11
     :val:	xxxx.0xxx xxxx.xxxx
     :desc:	Created FCDAs **will not be** recorded.

   * :(attr):
     :val:	xxxx.1xxx xxxx.xxxx
     :desc:	Created FCDAs **will be** recorded (Application).


   * :attr:	Bit 12
     :val:	xxx0.xxxx xxxx.xxxx
     :desc:	Report Control Block (RCB) initialziation process **will not be** recorded.

   * :(attr):
     :val:	xxx1.xxxx xxxx.xxxx
     :desc:	Report Control Block (RCB) initialziation process **will be** recorded (Application).

   * :attr:	Bit 13
     :val:	xx0x.xxxx xxxx.xxxx
     :desc:	Dataset validation against DI/AI objects **will not be** recorded.

   * :(attr):
     :val:	xx1x.xxxx xxxx.xxxx
     :desc:	Dataset validation against DI/AI objects **will be** recorded (Application). This means FCDAs required, FCADs missing and FCDAs no longer required.

   * :attr:	Bit 14
     :val:	x0xx.xxxx xxxx.xxxx
     :desc:	Dataset initialization process **will not be** recorded.

   * :(attr):
     :val:	x1xx.xxxx xxxx.xxxx
     :desc:	Dataset initialization process **will be** recorded (Application).

   * :attr:	Bits 7;9;10;15
     :val:	Any
     :desc:	Bits reserved for future use
