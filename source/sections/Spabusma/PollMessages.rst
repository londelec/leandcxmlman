
.. _xmlgroup-SpabusmaPollMessages: lelabel=PollMessages
.. _xmlelem-SpabusmaPollMsg: lelabel=MSG

PollMessages group
------------------

Group node :ref:`xmlgroup-SpabusmaPollMessages` and child element nodes :ref:`xmlelem-SpabusmaPollMsg` contain messages that are being sent to continuously poll outstation data.
All defined messages are sent to outstation in a sequential order.
Data received from outstation can be mapped using :ref:`xmlelem-SpabusmaDI` and :ref:`xmlelem-SpabusmaAI` nodes.

.. tip:: \ :ref:`xmlgroup-SpabusmaPollMessages` group and :ref:`xmlelem-SpabusmaPollMsg` nodes are optional if :ref:`xmlelem-SpabusmaDI`.\ :ref:`xmlattr-SpabusmaDIRequest` and :ref:`xmlelem-SpabusmaAI`.\ :ref:`xmlattr-SpabusmaAIRequest` attributes are used. In this case messages required to poll data will be created automatically.

Please see sample :ref:`xmlgroup-SpabusmaPollMessages` group and :ref:`xmlelem-SpabusmaPollMsg` child element nodes below.
There are 3 Spabus messages configured using 3 :ref:`xmlelem-SpabusmaPollMsg` element nodes.

.. code-block:: none

   <PollMessages>
	<MSG PollMsg="1" Channel="120" Category="V" DataNumber="1/4" Priority="0"/>
	<MSG PollMsg="2" Channel="120/121" Category="V" DataNumber="1" Priority="0"/>
	<MSG PollMsg="3" Channel="10" Category="I" DataNumber="15" Priority="1"/>
   </PollMessages>

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-SpabusmaPollMsg`"

.. code-block:: none

   <MSG PollMsg="1" Channel="120" Category="V" DataNumber="1/4" Priority="0" Name="CB position message" />

.. tip:: Attributes of the :ref:`xmlelem-SpabusmaPollMsg` element node can be arranged in any order, it will not affect XML file validation.

Poll MSG attributes
^^^^^^^^^^^^^^^^^^^

.. include-file:: sections/Include/table_attrs.rstinc "" "tabid-SpabusmaPollMsg" "Spabus Master Poll message attributes" ":spec: |C{0.1}|C{0.16}|C{0.1}|S{0.64}|"

.. include-file:: sections/Include/serma_Msgid.rstinc "" ":xmlattr:`PollMsg`"

   * :attr:	:xmlattr:`Channel`
     :val:	0...999 or 0...999/1...999
     :def:	n/a
     :desc:	Spabus channel number.
		This attribute supports channel range e.g. :lemonobgtext:`10/12`, where 10 is the first and 12 is the last channel requested.
		:inlinetip:`Range can be specified only in one of the attributes` :ref:`xmlattr-SpabusmaPollMsgChannel` :inlinetip:`or` :ref:`xmlattr-SpabusmaPollMsgDataNumber`. :inlinetip:`Therefore if channel range is used` :ref:`xmlattr-SpabusmaPollMsgDataNumber` :inlinetip:`attribute can't have a range.`

   * :attr:	:xmlattr:`Category`
     :val:	I, M, O, S, V
     :def:	n/a
     :desc:	Spabus Category value.

   * :attr:	:xmlattr:`DataNumber`
     :val:	1...999999 or 1...999999/1...999999
     :def:	n/a
     :desc:	Spabus data number.
		This attribute supports data number range e.g. :lemonobgtext:`10/12`, where 10 is the first and 12 is the last data number requested.
		:inlinetip:`Range can be specified only in one of the attributes` :ref:`xmlattr-SpabusmaPollMsgChannel` :inlinetip:`or` :ref:`xmlattr-SpabusmaPollMsgDataNumber`. :inlinetip:`Therefore if data number range is used` :ref:`xmlattr-SpabusmaPollMsgChannel` :inlinetip:`attribute can't have a range.`

.. include-file:: sections/Include/serma_MsgPriority.rstinc "" ":ref:`xmlattr-SpabusmaAppRatioP0`"

.. include-file:: sections/Include/Name.rstinc ""

