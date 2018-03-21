
.. _ref-IEC10xslAUTOCfg:
.. _ref-IEC10xslAUTO:

AUTOCfg group and AUTO node
---------------------------

Group node :ref:`AUTOCfg<ref-IEC10xslAUTOCfg>` and element nodes :ref:`AUTO<ref-IEC10xslAUTO>` enable automatic object linking without a need to create 
DI/AI/DO/AO object table.
All DI/AI/DO/AO objects of the Master protocol instance are automatically linked to Slave protocol instance if this feature is used.
Easiest way to enable automatic linking is by specifying value of the :ref:`<ref-IEC101maIndex>` attribute of any Master protocol instance in the :ref:`<ref-IEC10xslAUTOSource>` attribute. 
By default information addresses of DI/AI/DO/AO objects will be the same as defined in Master protocol instance's object table.
It is also possible to override automatic information address initialization and have them initialized sequentially using :ref:`<ref-IEC10xslAUTODIInfAddr>`; :ref:`<ref-IEC10xslAUTOAIInfAddr>`; :ref:`<ref-IEC10xslAUTODOInfAddr>`; :ref:`<ref-IEC10xslAUTOAOInfAddr>` attributes.
The first object will have information address as specified and following objects will be initialized sequentially.
:ref:`AUTOCfg<ref-IEC10xslAUTOCfg>` group can have multiple :ref:`AUTO<ref-IEC10xslAUTO>` nodes as shown in the sample below.

.. code-block:: none

   <AutoCfg> 
 	<AUTO Source="1"  Name="RTU1" />
	<AUTO Source="2"  Name="RTU2" />
	<AUTO Name="RTU3" />
   </AutoCfg>

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`AUTO<ref-IEC10xslAUTO>`"

.. code-block:: none

   <AUTO Source="1" DIInfAddr="1001" AIInfAddr="2001" DOInfAddr="4001" AOInfAddr="5001" DIqual="0x00" AIqual="0x00" DOqual="0x00" AOqual="0x00" DIGroupMask="0x0001" AIGroupMask="0x0002" Policy="0" CommsOnlineAddr="1" Name="Auto configuration" />

.. tip:: Attributes of the :ref:`AUTO<ref-IEC10xslAUTO>` element node can be arranged in any order, it will not affect the XML file validation.         

.. _ref-IEC10xslAUTOAttributes:

.. include-file:: sections/Include/table_attrs.rstinc "" "IEC60870-5-101/104 Slave AUTO attributes"

   * :attr:     .. _ref-IEC10xslAUTOSource:

                :xmlref:`Source`
     :val:      1...255
     :def:      n/a
     :desc:     Source communication protocol instance.
		Any Master protocol instance listed in :ref:`CommunicationCfg<ref-CommunicationCfg>` group can be used as a source.
		Use value of the :ref:`<ref-IEC101maIndex>` attribute in order to select Master protocol instance as source.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, value of the` :ref:`<ref-IEC101sl>`.\ :ref:`<ref-IEC101slSource>` \ :inlinetip:`or` :ref:`<ref-IEC104sl>`.\ :ref:`<ref-IEC104slSource>` \ :inlinetip:`attributes will be used if omitted.`

   * :attr:     .. _ref-IEC10xslAUTODIInfAddr:

                :xmlref:`DIInfAddr`
     :val:      1...16777215
     :def:      n/a
     :desc:     Base DI information object address. Addresses of DI objects will be initialized sequentially starting with this value.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, objects will have the same information addresses as defined in source communication protocol object table.`

   * :attr:     .. _ref-IEC10xslAUTOAIInfAddr:

                :xmlref:`AIInfAddr`
     :val:      1...16777215
     :def:      n/a
     :desc:     Base AI information object address. Addresses of AI objects will be initialized sequentially starting with this value.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, objects will have the same information addresses as defined in source communication protocol object table.`

   * :attr:     .. _ref-IEC10xslAUTODOInfAddr:

                :xmlref:`DOInfAddr`
     :val:      1...16777215
     :def:      n/a
     :desc:     Base DO information object address. Addresses of DO objects will be initialized sequentially starting with this value.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, objects will have the same information addresses as defined in source communication protocol object table.`

   * :attr:     .. _ref-IEC10xslAUTOAOInfAddr:

                :xmlref:`AOInfAddr`
     :val:      1...16777215
     :def:      n/a
     :desc:     Base AO information object address. Addresses of AO objects will be initialized sequentially starting with this value.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, objects will have the same information addresses as defined in source communication protocol object table.`

   * :attr:     .. _ref-IEC10xslAUTODIqual:

                :xmlref:`DIqual`
     :val:      0...255 or 0x00...0xFF
     :def:      0x00
     :desc:     Internal DI object qualifier to enable customized data processing.
		See table :numref:`ref-IEC10xslDIqualifierBits` for internal object qualifier description.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:     .. _ref-IEC10xslAUTOAIqual:

                :xmlref:`AIqual`
     :val:      0...255 or 0x00...0xFF
     :def:      0x00
     :desc:     Internal AI object qualifier to enable customized data processing.
		See table :numref:`ref-IEC10xslAIqualifierBits` for internal object qualifier description.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:     .. _ref-IEC10xslAUTODOqual:

                :xmlref:`DOqual`
     :val:      0...255 or 0x00...0xFF
     :def:      0x00
     :desc:     Internal DO object qualifier to enable customized data processing.
		See table :numref:`ref-IEC10xslDOqualifierBits` for internal object qualifier description.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:     .. _ref-IEC10xslAUTOAOqual:

                :xmlref:`AOqual`
     :val:      0...255 or 0x00...0xFF
     :def:      0x00
     :desc:     Internal AO object qualifier to enable customized data processing.
		See table :numref:`ref-IEC10xslAOqualifierBits` for internal object qualifier description.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:     .. _ref-IEC10xslAUTODIGroupMask:

                :xmlref:`DIGroupMask`
     :val:      0...65535 or 0x0000...0xFFFF
     :def:      0x0000
     :desc:     Include DI objects in Interrogation group/groups.
		Each bit of the group mask attribute needs to be set in order to include object in a particular interrogation group.
		Please refer to the table :numref:`ref-IEC10xslGroupMask` for more information.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:     .. _ref-IEC10xslAUTOAIGroupMask:

                :xmlref:`AIGroupMask`
     :val:      0...65535 or 0x0000...0xFFFF
     :def:      0x0000
     :desc:     Include AI objects in Interrogation group/groups.
		Each bit of the group mask attribute needs to be set in order to include object in a particular interrogation group.
		Please refer to the table :numref:`ref-IEC10xslGroupMask` for more information.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:     .. _ref-IEC10xslAUTOPolicy:

                :xmlref:`Policy`
     :val:      0...255
     :def:      0
     :desc:     Command execution policy, see table :numref:`ref-IEC10xslPolicy` for description.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:     .. _ref-IEC10xslAUTOCommsOnlineAddr:

                :xmlref:`CommsOnlineAddr`
     :val:      1...16777215
     :def:      n/a
     :desc:     Information address to report service DI – peer station communication (Online/Offline) status.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, communication status will not be reported if omitted.`

.. include-file:: sections/Include/Name.rstinc ""
