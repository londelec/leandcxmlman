
.. _xmlgroup-SpabusmaAO: lelabel=AOTable
.. _xmlelem-SpabusmaAO: lelabel=AO

AOTable group
-------------

.. include-file:: sections/Include/ma_DOAO_table.rstinc "" ":ref:`xmlgroup-SpabusmaAO`" ":ref:`xmlelem-SpabusmaAO`" ":numref:`tabid-SpabusmaAO`" ":ref:`docref-IEC10xslAO`" "AO" "setpoint" "IED"

Please see sample :ref:`xmlgroup-SpabusmaAO` group and :ref:`xmlelem-SpabusmaAO` element nodes below.
There are 2 setpoint commands defined in this sample.

.. code-block:: none

   <AOTable>
	<AO Index="0" CtrlMsg="1"/>
	<AO Index="1" Request="120V4" Coeff="2" FollowCtrlMsg="2"/>
   </AOTable>

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-SpabusmaAO`"

.. code-block:: none

   <AO Index="0" CtrlMsg="2" Request="120V4" Qualifier="0x00" Coeff="1.1" FollowCtrlMsg="2" Name="Setpoint" />

.. include-file:: sections/Include/tip_order.rstinc "" ":ref:`xmlelem-SpabusmaAO`"

AO attributes
^^^^^^^^^^^^^

.. include-file:: sections/Include/table_attrs.rstinc "" "tabid-SpabusmaAO" "Spabus Master AO attributes" ":spec: |C{0.14}|C{0.14}|C{0.1}|S{0.62}|"

.. include-file:: sections/Include/ma_Index.rstinc "" "AO"

.. include-file:: sections/Include/Spabusma_CtrlMsg.rstinc "" :xmlattr:`CtrlMsg` "setpoint"
		Value 0 means no control message is selected., :ref:`xmlattr-SpabusmaAORequest` attribute must be used to specify the message.
		:inlinetip:`This attribute has higher priority than` :ref:`xmlattr-SpabusmaAORequest`\ :inlinetip:`, if both attributes are specified` :ref:`xmlattr-SpabusmaAOCtrlMsg` :inlinetip:`will be used.`

.. include-file:: sections/Include/Spabusma_DOAO_Request.rstinc "" :xmlattr:`Request` "setpoint"
		| Example :ref:`xmlattr-SpabusmaAORequest`\ ="\ :lemonobgtext:`120V4`"
		| :inlinetip:`Attribute is optional if` :ref:`xmlattr-SpabusmaAOCtrlMsg` :inlinetip:`is used.`

.. include-file:: sections/Include/Qualifier.rstinc "" ":numref:`tabid-SpabusmaAOQualifier`"

.. include-file:: sections/Include/AO_Coeff.rstinc ""

.. include-file:: sections/Include/serma_FollowCtrlMsg.rstinc ""

.. include-file:: sections/Include/Name.rstinc ""

AO.Qualifier
^^^^^^^^^^^^

.. include-file:: sections/Include/table_flags8.rstinc "" "tabid-SpabusmaAOQualifier" "Spabus Master AO internal qualifier" ":ref:`xmlattr-SpabusmaAOQualifier`" "AO internal qualifier"

   * :attr:	Bit 7
     :val:	0xxx.xxxx
     :desc:	AO is **enabled**, command will be sent to outstation

   * :(attr):
     :val:	1xxx.xxxx
     :desc:	AO is **disabled**, command will not be sent to outstation

   * :attr:	Bits 0..6
     :val:	Any
     :desc:	Bits reserved for future use

