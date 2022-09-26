.. _xmlelem-SpabusmaApp:

AppSettings
^^^^^^^^^^^

Application layer settings can be specified using attributes of the :ref:`xmlelem-SpabusmaApp` element.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-SpabusmaApp`"

.. code-block:: none

 <AppSettings IgnoreTimetags="0" AIDeadband="2" AIPercent="0.5" RatioP0="2" RatioL="3" DnumRangeMax="16" ChannelRangeMax="8" ForwardGI="1" TimetagFBrange="2" Flags="0x00"/>


.. include-file:: sections/Include/table_attrs.rstinc "" "tabid-SpabusmaApp" "Spabus Master AppSettings attributes" ":spec: |C{0.18}|C{0.14}|C{0.1}|S{0.58}|"

.. include-file:: sections/Include/ma_IgnoreTimetags.rstinc "" ":ref:`xmlelem-SpabusmaDI`.\ :ref:`xmlattr-SpabusmaDIQualifier` attribute can be used to disable timetag processing for each DI."

.. include-file:: sections/Include/AI_ThresholdsCmn.rstinc "" ":ref:`xmlelem-SpabusmaAI`" ":ref:`xmlattr-SpabusmaAIDeadband`" ":ref:`xmlattr-SpabusmaAIPercent`"

.. include-file:: sections/Include/serma_RatioP0.rstinc "" ":ref:`xmlattr-SpabusmaPollMsgPriority`"

   * :attr:	:xmlattr:`RatioL`
     :val:	1...255
     :def:	3
     :desc:	Polling ratio between poll messages and Event request :lemonobgtext:`R0L`.
		Default value 3 means Event request :lemonobgtext:`R0L` will be sent after every three poll messages.
		This attribute doesn't take into account message :ref:`xmlattr-SpabusmaPollMsgPriority` value, all poll messages are being accounted together
		i.e. if :ref:`xmlattr-SpabusmaAppRatioP0` attribute has a default value 2, the poll sequence will be: two Priority 0 messages, one Priority 1 message and Event request :lemonobgtext:`R0L`.
		If IED response conatains any Events, the :lemonobgtext:`R0L` request will be repeated immediately until all Events are read from IED.
		Only then normal Priority 0 and 1 polling will resume.

   * :attr:	:xmlattr:`DnumRangeMax`
     :val:	1...255
     :def:	16
     :desc:	Maximal number of SPA data numbers that can be consolidated in one request message.
		Consider situation when one :ref:`xmlelem-SpabusmaDI` has :ref:`xmlattr-SpabusmaDIRequest`\ ="\ :lemonobgtext:`10V2`" and another :ref:`xmlelem-SpabusmaDI` has :ref:`xmlattr-SpabusmaDIRequest`\ ="\ :lemonobgtext:`10V3`".
		These 2 separate messages can be consolidated into a single :ref:`xmlattr-SpabusmaDIRequest`\ ="\ :lemonobgtext:`10V2/3`".
		Default value 16 ensures no more than 16 SPA data numbers are requested in one message.
		:inlinetip:`Data number consolidation applies only to messages created automatically from` :ref:`xmlelem-SpabusmaDI`.\ :ref:`xmlattr-SpabusmaDIRequest` :inlinetip:`and` :ref:`xmlelem-SpabusmaAI`.\ :ref:`xmlattr-SpabusmaAIRequest`
		:inlinetip:`attributes. Messages defined within` :ref:`xmlgroup-SpabusmaPollMessages` :inlinetip:`group will not be consolidated.`

   * :attr:	:xmlattr:`ChannelRangeMax`
     :val:	1...255
     :def:	8
     :desc:	Maximal number of SPA channel numbers that can be consolidated in one request message.
		Consider situation when one :ref:`xmlelem-SpabusmaDI` has :ref:`xmlattr-SpabusmaDIRequest`\ ="\ :lemonobgtext:`10V2`" and another :ref:`xmlelem-SpabusmaDI` has :ref:`xmlattr-SpabusmaDIRequest`\ ="\ :lemonobgtext:`11V2`".
		These 2 separate messages can be consolidated into a single :ref:`xmlattr-SpabusmaDIRequest`\ ="\ :lemonobgtext:`10/11V2`".
		Default value 8 ensures no more than 8 SPA channel numbers are requested in one message.
		:inlinetip:`Channel number consolidation applies only to messages created automatically from` :ref:`xmlelem-SpabusmaDI`.\ :ref:`xmlattr-SpabusmaDIRequest` :inlinetip:`and` :ref:`xmlelem-SpabusmaAI`.\ :ref:`xmlattr-SpabusmaAIRequest`
		:inlinetip:`attributes. Messages defined within` :ref:`xmlgroup-SpabusmaPollMessages` :inlinetip:`group will not be consolidated.`

   * :attr:	:xmlattr:`ForwardGI`
     :val:	0
     :def:	1
     :desc:	**Don't use** General Interrogation command received from upstream station (e.g. SCADA) to request DI values.
		This option only applies if DI data values are requested only during IED initialization i.e. :ref:`bitref-SpabusmaAppFlagsBit0`\ |bittrue| in :ref:`xmlelem-SpabusmaApp`.\ :ref:`xmlattr-SpabusmaAppFlags`.

   * :(attr):
     :val:	1
     :(def):
     :desc:	**Use** General Interrogation command received from upstream station (e.g. SCADA) to request DI values.
		This option only applies if DI data values are requested only during IED initialization i.e. :ref:`bitref-SpabusmaAppFlagsBit0`\ |bittrue| in :ref:`xmlelem-SpabusmaApp`.\ :ref:`xmlattr-SpabusmaAppFlags`.

   * :attr:	:xmlattr:`TimetagFBrange`
     :val:	0...30
     :def:	1 sec
     :desc:	Received event time-tag minute forward-backward adjustment range.
		If the time-tag of the event received from IED is closer to full minute (0 secs) than the specified range in seconds, the minute value of the resulting timestamp will be automatically adjusted.
		This functionality ensures correct minute value is attached to the SPA time-tag, as it carries only seconds and milliseconds, if event arrived late.
		Minute, hour, day, month and year values are taken from internal system time.
		If the time value of the event time-tag is just before a full minute (e.g. sec.msec = 59:580) and there is a delay in communication channel,
		there is a chance the event is received only after internal minute has already changed (e.g. min:sec.msec = 30:01.000).
		This will lead to incorrect minute (min = 30) being applied to the resulting timestamp, although it is most likely the event was generated before the minute change (e.g. generated at min:sec.msec = 29:59.580).
		:ref:`xmlattr-SpabusmaAppTimetagFBrange` attribute ensures the minute of the resulting timestamp is automatically decremented if the time of the received time-tag falls within a forward-backward adjustment range and internal minute has recently changed.
		Similar functionality applies if the time of the received time-tag appears to be in the future, but the internal minute hasn't changed yet.
		In this case minute of the resulting timestamp is automatically incremented.
		Default value 1 will adjust received event time-tags sec.msec = 59.000...00.999 if they arrive when internal time is min:sec.msec = 29:59.000...30:00.999

   * :attr:	:xmlattr:`Flags`
     :val:	|flags8range|
     :def:	0x00
     :desc:	Settings to customize data polling algorithm.
		See :numref:`tabid-SpabusmaAppFlags` for description.


.. include-file:: sections/Include/table_flags8.rstinc "" "tabid-SpabusmaAppFlags" "Polling algorithm flags" ":ref:`xmlattr-SpabusmaAppFlags`" "Application flags"

   * :attr:	:bitdef:`0`
     :val:	xxxx.xxx0
     :desc:	Request DI data values **continuously** (default value).

   * :(attr):
     :val:	xxxx.xxx1
     :desc:	Request DI data values **only on startup** during IED initialization i.e. whenever IED goes online after a communication loss.
		Event buffer and AI values will be polled continuously.
		DI position changes are based on received Events.
		This setting only applies to DI requests created automatically i.e. :ref:`xmlelem-SpabusmaDI`.\ :ref:`xmlattr-SpabusmaDIRequest` attribute **is** used and :ref:`xmlelem-SpabusmaDI`.\ :ref:`xmlattr-SpabusmaDIPollMsg` attribute **is not** used.
		:ref:`xmlelem-SpabusmaDI` also must have :ref:`xmlattr-SpabusmaDIOnEvent` and :ref:`xmlattr-SpabusmaDIOffEvent` attributes in order for the request to be excluded from continuous polling.
		If these attributes are missing or :ref:`bitref-SpabusmaDIQualifierBit4`\ |bittrue| in :ref:`xmlelem-SpabusmaDI`.\ :ref:`xmlattr-SpabusmaDIQualifier`, the particular DI request will be sent continuously.

   * :attr:	Bit 1
     :val:	xxxx.xx0x
     :desc:	**Don't send** clear Event buffer :lemonobgtext:`WC` message on startup. (default value)

   * :(attr):
     :val:	xxxx.xx1x
     :desc:	**Always send** clear Event buffer :lemonobgtext:`WC` message when establishing communication to IED.
		Clear Event buffer will be the first message sent to IED on startup and whenever IED goes online after a communication loss.

   * :attr:	Bit 2
     :val:	xxxx.x0xx
     :desc:	**Use** initialization state.

   * :(attr):
     :val:	xxxx.x1xx
     :desc:	**Don't use** initialization state.
		This option is only used for testing.

   * :attr:	Bits 3...7
     :val:	Any
     :desc:	Bits reserved for future use
