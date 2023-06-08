
.. _xmlgroup-SpabusmaDI: lelabel=DITable
.. _xmlelem-SpabusmaDI: lelabel=DI

DITable group
-------------

.. include-file:: sections/Include/ma_DIAI_table.rstinc "" ":ref:`xmlgroup-SpabusmaDI`" ":ref:`xmlelem-SpabusmaDI`" ":numref:`tabid-SpabusmaDI`" ":ref:`docref-IEC10xslDI`" "DI" "status information" "IED"

Please see sample :ref:`xmlgroup-SpabusmaDI` group and :ref:`xmlelem-SpabusmaDI` elements below.
There are 5 status information objects defined with 4 :ref:`xmlelem-SpabusmaDI` elements.

.. code-block:: none

   <DITable>
	<DI Index="0" PollMsg="1" DataPos="1" OnValue="2" OffValue="1" Total="2"/>
	<DI Index="2" Request="120V1" OnValue="2" OffValue="1" IndetValue="3" InterDelay="0"/>
	<DI Index="3" Request="10V1/2" DataPos="1/2 OnValue="0/1" OffValue="1/0"/>
	<DI Index="4" Request="10/11V1" DataPos="1/2 OnValue="0/1" OffValue="1/0"/>
   </DITable>

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-SpabusmaDI`"

.. code-block:: none

   <DI Index="0" PollMsg="1" DataPos="1" Request="120V1" Qualifier="0x00" OnValues="2" OffValues="1" InterValue="0" IndetValue="3" OnEvent="10E1" OffEvent="10E2" InterEvent="10E0" IndetEvent="10E3" InterDelay="0" IndetDelay="0" OnDelay="0" OffDelay="0" Total="1" Name="CB position" />

.. include-file:: sections/Include/tip_order.rstinc "" ":ref:`xmlelem-SpabusmaDI`"

DI attributes
^^^^^^^^^^^^^

.. include-file:: sections/Include/table_attrs.rstinc "" "tabid-SpabusmaDI" "Spabus Master DI attributes" ":spec: |C{0.14}|C{0.14}|C{0.1}|S{0.62}|"

.. include-file:: sections/Include/ma_Index.rstinc "" "DI"

.. include-file:: sections/Include/Spabusma_PollMsg.rstinc ""
		Value 0 means no poll message is selected, :ref:`xmlattr-SpabusmaDIRequest` attribute must be used to specify the message.
		:inlinetip:`This attribute has higher priority than` :ref:`xmlattr-SpabusmaDIRequest`\ :inlinetip:`, if both attributes are specified` :ref:`xmlattr-SpabusmaDIPollMsg` :inlinetip:`will be used.`

   * :attr:	:xmlattr:`DataPos`
     :val:	1...16 or 1...16/1...16
     :def:	1
     :desc:	Data position in the received message.
		This attribute supports 2 positions e.g. :lemonobgtext:`1/2` for double status information that is reported with 2 different Spabus channel or data numbers.

   * :attr:	:xmlattr:`Request`
     :val:	see description
     :def:	n/a
     :desc:	| Spabus request to poll data from outstation. Attribute has the following format [:lemonobgtext:`Channel`][:lemonobgtext:`Category`][:lemonobgtext:`Data Number`].
		| Range of [:lemonobgtext:`Channel`] values 0..999
		| [:lemonobgtext:`Category`] is one of :lemonobgtext:`I`, :lemonobgtext:`M`, :lemonobgtext:`O`, :lemonobgtext:`S`, :lemonobgtext:`V`
		| Range of [:lemonobgtext:`Data Number`] values 1..999999
		| This attribute supports channel and data number ranges for double status information that is reported with 2 different Spabus channels or data numbers e.g. [:lemonobgtext:`First Channel`]/[:lemonobgtext:`Last Channel`][:lemonobgtext:`Category`][:lemonobgtext:`Data Number`] or [:lemonobgtext:`Channel`][:lemonobgtext:`Category`][:lemonobgtext:`First Data Number`]/[:lemonobgtext:`Last Data Number`]
		| Examples :ref:`xmlattr-SpabusmaDIRequest`\ ="\ :lemonobgtext:`15I2`" or :ref:`xmlattr-SpabusmaDIRequest`\ ="\ :lemonobgtext:`15/16I2`" or :ref:`xmlattr-SpabusmaDIRequest`\ ="\ :lemonobgtext:`15I2/4`"
		| :inlineimportant:`Only one range can be used at a time i.e. either channel range or data number range.`
		| :inlinetip:`Attribute is optional if` :ref:`xmlattr-SpabusmaDIPollMsg` :inlinetip:`is used.`

.. include-file:: sections/Include/Qualifier.rstinc "" ":numref:`tabid-SpabusmaDIQualifier`"

.. include-file:: sections/Include/Spabusma_doubleValue.rstinc "" ":xmlattr:`OnValues`" ":ref:`xmlattr-SpabusmaDIOnValues`" "1" "ON"

.. include-file:: sections/Include/Spabusma_doubleValue.rstinc "" ":xmlattr:`OffValues`" ":ref:`xmlattr-SpabusmaDIOffValues`" "0" "OFF"

.. include-file:: sections/Include/Spabusma_singleValue.rstinc "" ":xmlattr:`InterValue`" "0" "Intermediate"

.. include-file:: sections/Include/Spabusma_singleValue.rstinc "" ":xmlattr:`IndetValue`" "3" "Indeterminate (error)"

.. include-file:: sections/Include/Spabusma_Event.rstinc "" ":xmlattr:`OnEvent`" "ON"

.. include-file:: sections/Include/Spabusma_Event.rstinc "" ":xmlattr:`OffEvent`" "OFF"

.. include-file:: sections/Include/Spabusma_Event.rstinc "" ":xmlattr:`InterEvent`" "Intermediate"

.. include-file:: sections/Include/Spabusma_Event.rstinc "" ":xmlattr:`IndetEvent`" "Indeterminate (error)"

.. include-file:: sections/Include/DI_Idelays.rstinc ""

.. include-file:: sections/Include/DI_Odelays.rstinc ""

.. include-file:: sections/Include/Total.rstinc "" ":ref:`xmlattr-SpabusmaDIIndex` and :ref:`xmlattr-SpabusmaDIDataPos`" ":ref:`xmlelem-SpabusmaDI`" "254"

.. include-file:: sections/Include/Name.rstinc ""

DI.Qualifier
^^^^^^^^^^^^

.. include-file:: sections/Include/table_flags8.rstinc "" "tabid-SpabusmaDIQualifier" "Spabus Master DI internal qualifier" ":ref:`xmlattr-SpabusmaDIQualifier`" "DI internal qualifier"

   * :attr:	Bit 0
     :val:	xxxx.xxx0
     :desc:	DI object **will not** be inverted (ON = 1; OFF = 0)

   * :(attr):
     :val:	xxxx.xxx1
     :desc:	DI object **will** be inverted (ON = 0; OFF = 1)

   * :attr:	Bit 3
     :val:	xxxx.0xxx
     :desc:	**Use original** timetag when event is received from outstation

   * :(attr):
     :val:	xxxx.1xxx
     :desc:	**Substitute timetag** with local time when event is received from outstation

   * :attr:	:bitdef:`4`
     :val:	xxx0.xxxx
     :desc:	**Exclude** DI request from continuous polling.
		This option only applies if DI data values are requested only during IED initialization i.e. :ref:`bitref-SpabusmaAppFlagsBit0`\ |bittrue| in :ref:`xmlelem-SpabusmaApp`.\ :ref:`xmlattr-SpabusmaAppFlags`.

   * :(attr):
     :val:	xxx1.xxxx
     :desc:	**Poll this DI continuously** even if DI values are requested only during IED initialization i.e. :ref:`bitref-SpabusmaAppFlagsBit0`\ |bittrue| in :ref:`xmlelem-SpabusmaApp`.\ :ref:`xmlattr-SpabusmaAppFlags`.

   * :attr:	:bitdef:`5`
     :val:	xx0x.xxxx
     :desc:	Use time tag of the **last** event if Intermediate state of the Double Point object was not reported (because Intermediate state didn't exceed :ref:`xmlattr-SpabusmaDIInterDelay`). e.g. in transition ON->INTER->OFF time tag of the INTER->OFF event will be used.

   * :(attr):
     :val:	xx1x.xxxx
     :desc:	Use time tag of the **first** event if Intermediate state of the Double Point object was not reported (because Intermediate state didn't exceed :ref:`xmlattr-SpabusmaDIInterDelay`). e.g. in transition ON->INTER->OFF time tag of the ON->INTER event will be used.

   * :attr:	Bit 7
     :val:	0xxx.xxxx
     :desc:	DI is **enabled** and will be processed when received

   * :(attr):
     :val:	1xxx.xxxx
     :desc:	DI is **disabled** and will be discarded when received

   * :attr:	Bits 1,2,6
     :val:	Any
     :desc:	Bits reserved for future use

