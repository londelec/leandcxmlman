
.. _xmlgroup-SpabusmaDO: lelabel=DOTable
.. _xmlelem-SpabusmaDO: lelabel=DO

DOTable group
-------------

.. include-file:: sections/Include/ma_DOAO_table.rstinc "" ":ref:`xmlgroup-SpabusmaDO`" ":ref:`xmlelem-SpabusmaDO`" ":numref:`tabid-SpabusmaDO`" ":ref:`docref-IEC10xslDO`" "DO" "control" "IED"

Please see sample :ref:`xmlgroup-SpabusmaDO` group and :ref:`xmlelem-SpabusmaDO` element nodes below.
There are 3 control commands defined in this sample.

.. code-block:: none

   <DOTable>
	<DO Index="0" OnCtrlMsg="1" OffCtrlMsg="1" OnValue="1" OffValue="2"/>
	<DO Index="1" OnRequest="120V4" OffRequest="120V5" OnValue="0" OffValue="1" />
	<DO Index="2" OnRequest="120V4" OffRequest="120V5" Qualifier="0x01" FollowCtrlMsg="2"/>
   </DOTable>

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-SpabusmaDO`"

.. code-block:: none

   <DO Index="0" OnCtrlMsg="2" OffCtrlMsg="4" OnRequest="120V4" OffRequest="120V5" Qualifier="0x00" OnValue="1" OffValue="2" FollowCtrlMsg="2" Name="CB command" />

.. include-file:: sections/Include/tip_order.rstinc "" ":ref:`xmlelem-SpabusmaDO`"

DO attributes
^^^^^^^^^^^^^

.. include-file:: sections/Include/table_attrs.rstinc "" "tabid-SpabusmaDO" "Spabus Master DO attributes" ":spec: |C{0.14}|C{0.14}|C{0.1}|S{0.62}|"

.. include-file:: sections/Include/ma_Index.rstinc "" "DO"

.. include-file:: sections/Include/Spabusma_CtrlMsg.rstinc "" :xmlattr:`OnCtrlMsg` "ON"
		Value 0 means no control message is selected., :ref:`xmlattr-SpabusmaDOOnRequest` attribute must be used to specify the message.
		:inlinetip:`This attribute has higher priority than` :ref:`xmlattr-SpabusmaDOOnRequest`\ :inlinetip:`, if both attributes are specified` :ref:`xmlattr-SpabusmaDOOnCtrlMsg` :inlinetip:`will be used.`

.. include-file:: sections/Include/Spabusma_CtrlMsg.rstinc "" :xmlattr:`OffCtrlMsg` "OFF"
		Value 0 means no control message is selected., :ref:`xmlattr-SpabusmaDOOffRequest` attribute must be used to specify the message.
		:inlinetip:`This attribute has higher priority than` :ref:`xmlattr-SpabusmaDOOffRequest`\ :inlinetip:`, if both attributes are specified` :ref:`xmlattr-SpabusmaDOOffCtrlMsg` :inlinetip:`will be used.`

.. include-file:: sections/Include/Spabusma_DOAO_Request.rstinc "" :xmlattr:`OnRequest` "ON"
		| Example :ref:`xmlattr-SpabusmaDOOnRequest`\ ="\ :lemonobgtext:`120V4`"
		| :inlinetip:`Attribute is optional if` :ref:`xmlattr-SpabusmaDOOnCtrlMsg` :inlinetip:`is used.`

.. include-file:: sections/Include/Spabusma_DOAO_Request.rstinc "" :xmlattr:`OffRequest` "OFF"
		| Example :ref:`xmlattr-SpabusmaDOOffRequest`\ ="\ :lemonobgtext:`120V5`"
		| :inlinetip:`Attribute is optional if` :ref:`xmlattr-SpabusmaDOOffCtrlMsg` :inlinetip:`is used.`

.. include-file:: sections/Include/Qualifier.rstinc "" ":numref:`tabid-SpabusmaDOQualifier`"

.. include-file:: sections/Include/Spabusma_DO_Value.rstinc "" :xmlattr:`OnValue` "1" "ON"

.. include-file:: sections/Include/Spabusma_DO_Value.rstinc "" :xmlattr:`OffValue` "0" "OFF"

.. include-file:: sections/Include/serma_FollowCtrlMsg.rstinc ""

.. include-file:: sections/Include/Name.rstinc ""

DO.Qualifier
^^^^^^^^^^^^

.. include-file:: sections/Include/table_flags8.rstinc "" "tabid-SpabusmaDOQualifier" "Spabus Master DO internal qualifier" ":ref:`xmlattr-SpabusmaDOQualifier`" "DO internal qualifier"

   * :attr:	Bit 0
     :val:	xxxx.xxx0
     :desc:	DO object **will not** be inverted (ON = 1; OFF = 0)

   * :(attr):
     :val:	xxxx.xxx1
     :desc:	DO object **will** be inverted (ON = 0; OFF = 1)

   * :attr:	Bit 7
     :val:	0xxx.xxxx
     :desc:	DO is **enabled**, command will be sent to outstation

   * :(attr):
     :val:	1xxx.xxxx
     :desc:	DO is **disabled**, command will not be sent to outstation

   * :attr:	Bits 1..6
     :val:	Any
     :desc:	Bits reserved for future use

