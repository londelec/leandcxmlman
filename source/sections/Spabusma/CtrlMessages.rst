
.. _xmlgroup-SpabusmaCtrlMessages: lelabel=CtrlMessages
.. _xmlelem-SpabusmaCtrlMsg: lelabel=MSG

CtrlMessages group
------------------

Group node :ref:`xmlgroup-SpabusmaCtrlMessages` and child element nodes :ref:`xmlelem-SpabusmaCtrlMsg` contain messages for writing data to outstation.
Use :ref:`xmlelem-SpabusmaDO` node to specify which control message has to be sent to outstation when command is received.

.. tip:: \ :ref:`xmlgroup-SpabusmaCtrlMessages` group and :ref:`xmlelem-SpabusmaCtrlMsg` nodes are optional :ref:`xmlelem-SpabusmaDO`.\ :ref:`xmlattr-SpabusmaDOOnRequest` and :ref:`xmlelem-SpabusmaDO`.\ :ref:`xmlattr-SpabusmaDOOffRequest` attributes are used. In this case messages required to send data will be created automatically.

Please see sample :ref:`xmlgroup-SpabusmaCtrlMessages` group and :ref:`xmlelem-SpabusmaCtrlMsg` child element nodes below.
There are 2 Spabus messages configured using 2 :ref:`xmlelem-SpabusmaCtrlMsg` element nodes.

.. code-block:: none

   <CtrlMessages>
	<MSG CtrlMsg="1" Channel="120" Category="V" DataNumber="4" />
	<MSG CtrlMsg="2" Channel="120" Category="V" DataNumber="5" />
   </CtrlMessages>

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-SpabusmaCtrlMsg`"

.. code-block:: none

   <MSG CtrlMsg="1" Channel="120" Category="V" DataNumber="4" Value="11" FollowCtrlMsg="2" Name="CB Open" />

.. tip:: Attributes of the :ref:`xmlelem-SpabusmaCtrlMsg` element node can be arranged in any order, it will not affect XML file validation.

Ctrl MSG attributes
^^^^^^^^^^^^^^^^^^^

.. include-file:: sections/Include/table_attrs.rstinc "" "tabid-SpabusmaCtrlMsg" "Spabus Master Control message attributes" ":spec: |C{0.16}|C{0.16}|C{0.1}|S{0.58}|"

.. include-file:: sections/Include/serma_Msgid.rstinc "" ":xmlattr:`CtrlMsg`"

   * :attr:	:xmlattr:`Channel`
     :val:	0...999
     :def:	n/a
     :desc:	Spabus channel number.
		This attribute does not support channel range e.g. :lemonobgtext:`10/12`.

   * :attr:	:xmlattr:`Category`
     :val:	I, M, O, S, V
     :def:	n/a
     :desc:	Spabus Category value.

   * :attr:	:xmlattr:`DataNumber`
     :val:	1...999999
     :def:	n/a
     :desc:	Spabus data number.
		This attribute does not support data number range e.g. :lemonobgtext:`10/12`.

   * :attr:	:xmlattr:`Value`
     :val:	0...65535
     :def:	n/a
     :desc:	Data value to send with this message.
		:inlinetip:`Attribute is optional and can be omitted. Value of` 
		:ref:`xmlelem-SpabusmaDO`.\ :ref:`xmlattr-SpabusmaDOOnValue` :inlinetip:`or` 
		:ref:`xmlelem-SpabusmaDO`.\ :ref:`xmlattr-SpabusmaDOOffValue` :inlinetip:`or received` 
		:ref:`xmlelem-SpabusmaAO` :inlinetip:`will be used if this attribute is not specified.`

.. include-file:: sections/Include/serma_FollowCtrlMsg.rstinc ""

.. include-file:: sections/Include/Name.rstinc ""

