
.. _ref-IEC10xslAUTOCfg:
.. _ref-IEC10xslAUTO:

AUTOCfg group and AUTO node
---------------------------

Group node :ref:`AUTOCfg<ref-IEC10xslAUTOCfg>` and element nodes :ref:`AUTO<ref-IEC10xslAUTO>` enable automatic object linking without individually defining 
each DI/AI/DO/AO object in the table. All DI/AI/DO/AO objects of the Master protocol instance can be 
automatically linked to Slave protocol instance without individual defining each object in Slave protocol 
instance's object table. Objects can be automatically linked simply by using Master protocol instance's Index in 
the Source attribute. By default DI/AI/DO/AO object information addresses will be the same as defined in 
Master protocol instance's object table. It is also possible to override automatic information address initialization 
and have them initialized sequentially using :ref:`DIInfAddr<ref-IEC10xslAUTODIInfAddr>`; :ref:`AIInfAddr<ref-IEC10xslAUTOAIInfAddr>`; :ref:`DOInfAddr<ref-IEC10xslAUTODOInfAddr>`; :ref:`AOInfAddr<ref-IEC10xslAUTOAOInfAddr>` attributes. The first 
object will have information address as specified in corresponding :ref:`DIInfAddr<ref-IEC10xslAUTODIInfAddr>`; :ref:`AIInfAddr<ref-IEC10xslAUTOAIInfAddr>`; :ref:`DOInfAddr<ref-IEC10xslAUTODOInfAddr>`; :ref:`AOInfAddr<ref-IEC10xslAUTOAOInfAddr>` 
attribute and remaining objects will be initialized sequentially. :ref:`AUTOCfg<ref-IEC10xslAUTOCfg>` group node can have multiple 
:ref:`AUTO<ref-IEC10xslAUTO>` nodes as shown in the sample below.

.. code-block:: none

   <AutoCfg> 
 	<AUTO Source="1"  Name="RTU1" />
	<AUTO Source="2"  Name="RTU2" />
	<AUTO Name="RTU3" />
   </AutoCfg>
   
Please see sample :ref:`AUTO<ref-IEC10xslAUTO>` element node below listing all available attributes.
            
.. code-block:: none
            
   <AUTO Source="1"
	 DIInfAddr="1001"
         AIInfAddr="2001"
         DOInfAddr="4001"
         AOInfAddr="5001"
         DIqual="0x00"
         AIqual="0x00"
         DOqual="0x00"
         AOqual="0x00"
         DIGroupMask="0x0001"
         AIGroupMask="0x0002"
         Policy="0"
         CommsOnlineAddr="1"
         Name="Auto configuration" />
      
.. tip:: Attributes of the :ref:`AUTO<ref-IEC10xslAUTO>` element node can be arranged in any order, it will not affect the XML file validation.         

.. _ref-IEC10xslAUTOAttributes:

.. field-list-table:: IEC 60807-5-101/104 Slave AUTO attributes
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.22}|C{0.23}|S{0.55}|
   :header-rows: 1

   * :attr,10: Attribute
     :val,15:  Values or range
     :desc,75: Description

   * :attr:    .. _ref-IEC10xslAUTOSource:
               
               :xmlref:`Source`
     :val:     1...255
     :desc:    Source communication protocol instance. Any Master protocol instance listed in :ref:`CommunicationCfg<ref-CommunicationCfg>` group can be used as a source. Use value of the Master protocol instance :ref:`Index<ref-IEC101maIndex>` attribute in order to link to it. :inlinetip:`Attribute is optional and doesn't have to be included in configuration, value of the` :ref:`IEC101sl<ref-IEC101sl>`.\ :ref:`Source<ref-IEC101slSource>` \ or :ref:`IEC104sl<ref-IEC104sl>`.\ :ref:`Source<ref-IEC104slSource>` \ :inlinetip:`attributes will be used if omitted.`

   * :attr:    .. _ref-IEC10xslAUTODIInfAddr:
   
               :xmlref:`DIInfAddr`
     :val:     1...16777215
     :desc:    Base DI information object address, DI objects will be initialized sequentially starting with this information address. :inlinetip:`Attribute is optional and doesn't have to be included in configuration, DI objects will have the same information addresses as defined in source communication protocol object table.`

   * :attr:    .. _ref-IEC10xslAUTOAIInfAddr:
   
               :xmlref:`AIInfAddr`
     :val:     1...16777215
     :desc:    Base AI information object address, AI objects will be initialized sequentially starting with this information address. :inlinetip:`Attribute is optional and doesn't have to be included in configuration, AI objects will have the same information addresses as defined in source communication protocol object table.`

   * :attr:    .. _ref-IEC10xslAUTODOInfAddr:
   
               :xmlref:`DOInfAddr`
     :val:     1...16777215
     :desc:    Base DO information object address, DO objects will be initialized sequentially starting with this information address. :inlinetip:`Attribute is optional and doesn't have to be included in configuration, DO objects will have the same information addresses as defined in source communication protocol object table.`

   * :attr:    .. _ref-IEC10xslAUTOAOInfAddr:
   
               :xmlref:`AOInfAddr`
     :val:     1...16777215
     :desc:    Base AO information object address, AO objects will be initialized sequentially starting with this information address. :inlinetip:`Attribute is optional and doesn't have to be included in configuration, AO objects will have the same information addresses as defined in source communication protocol object table.`

   * :attr:    .. _ref-IEC10xslAUTODIqual:
   
               :xmlref:`DIqual`
     :val:     See table :numref:`ref-IEC10xslDIqualifierBits` for description
     :desc:    Internal DI object qualifier to enable customized data processing. See table :numref:`ref-IEC10xslDIqualifierBits` for internal object qualifier description. (default value 0) :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:    .. _ref-IEC10xslAUTOAIqual:
   
               :xmlref:`AIqual`
     :val:     See table :numref:`ref-IEC10xslAIqualifierBits` for description
     :desc:    Internal AI object qualifier to enable customized data processing. See table :numref:`ref-IEC10xslAIqualifierBits` for internal object qualifier description. (default value 0) :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:    .. _ref-IEC10xslAUTODOqual:
   
               :xmlref:`DOqual`
     :val:     See table :numref:`ref-IEC10xslDOqualifierBits` for description
     :desc:    Internal DO object qualifier to enable customized data processing. See table :numref:`ref-IEC10xslDOqualifierBits` for internal object qualifier description. (default value 0) :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:    .. _ref-IEC10xslAUTOAOqual:
   
               :xmlref:`AOqual`
     :val:     See table :numref:`ref-IEC10xslAOqualifierBits` for description
     :desc:    Internal AO object qualifier to enable customized data processing. See table :numref:`ref-IEC10xslAOqualifierBits` for internal object qualifier description. (default value 0) :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:    .. _ref-IEC10xslAUTODIGroupMask:
   
               :xmlref:`DIGroupMask`
     :val:     0...0xFFFF
     :desc:    Include DI objects in Interrogation group/groups. Each bit of the group mask attribute needs to be set in order to include object in a particular interrogation group. Please refer to the table :numref:`ref-IEC10xslGroupMask` for more information. (default value 0) :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:    .. _ref-IEC10xslAUTOAIGroupMask:
   
               :xmlref:`AIGroupMask`
     :val:     0...0xFFFF
     :desc:    Include AI objects in Interrogation group/groups. Each bit of the group mask attribute needs to be set in order to include object in a particular interrogation group. Please refer to the table :numref:`ref-IEC10xslGroupMask` for more information. (default value 0) :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:    .. _ref-IEC10xslAUTOPolicy:
   
               :xmlref:`Policy`
     :val:     0...255
     :desc:    Command execution policy, see table :numref:`ref-IEC10xslPolicy` for description. (default value 0) :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:    .. _ref-IEC10xslAUTOCommsOnlineAddr:
   
               :xmlref:`CommsOnlineAddr`
     :val:     1...16777215
     :desc:    Information address to report service DI – peer station communication (Online/Offline) status. :inlinetip:`Attribute is optional and doesn't have to be included in configuration, communication status will not be reported if omitted.`

   * :attr:    .. _ref-IEC10xslAUTOName:
   
               :xmlref:`Name`
     :val:     Max 100 chars
     :desc:    Freely configurable name, just for reference. :inlinetip:`Name attribute is optional and doesn't have to be included in configuration.`
   
