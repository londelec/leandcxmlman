
.. _xmlgroup-IEC10xslAuto: lelabel=AutoCfg
.. _xmlelem-IEC10xslAuto: lelabel=AUTO

AUTOCfg group
-------------

Group node :ref:`xmlgroup-IEC10xslAUTO` and element nodes :ref:`xmlelem-IEC10xslAuto` enable automatic object linking without a need to create 
DI/AI/DO/AO object table.
All DI/AI/DO/AO objects of the Master protocol instance are automatically linked to Slave protocol instance if this feature is used.
Easiest way to enable automatic linking is by specifying value of the :ref:`xmlattr-gp101maIndex` attribute of any Master protocol instance in the :ref:`xmlattr-IEC10xslAUTOSource` attribute. 
By default information addresses of DI/AI/DO/AO objects will be the same as defined in Master protocol instance's object table.
It is also possible to override automatic information address initialization and have them initialized sequentially using :ref:`xmlattr-IEC10xslAUTODIInfAddr`; :ref:`xmlattr-IEC10xslAUTOAIInfAddr`; :ref:`xmlattr-IEC10xslAUTODOInfAddr`; :ref:`xmlattr-IEC10xslAUTOAOInfAddr` attributes.
The first object will have information address as specified and following objects will be initialized sequentially.
:ref:`xmlgroup-IEC10xslAUTO` group can have multiple :ref:`xmlelem-IEC10xslAuto` nodes as shown in the sample below.

.. code-block:: none

   <AutoCfg> 
 	<AUTO Source="1" Name="RTU1" />
	<AUTO Source="2" Name="RTU2" />
	<AUTO Name="RTU3" />
   </AutoCfg>

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-IEC10xslAuto`"

.. code-block:: none

   <AUTO Source="1" DIInfAddr="1001" AIInfAddr="2001" DOInfAddr="4001" AOInfAddr="5001" DIqual="0x00" AIqual="0x00" DOqual="0x00" AOqual="0x00" DIGroupMask="0x0001" AIGroupMask="0x0002" Policy="0" CommsOnlineAddr="1" Name="Auto configuration" />

.. tip:: Attributes of the :ref:`xmlelem-IEC10xslAuto` element node can be arranged in any order, it will not affect the XML file validation.         


.. include-file:: sections/Include/table_attrs.rstinc "" "tabid-IEC10xslAuto" "IEC60870-5-101/104 Slave AUTO attributes" ":spec: |C{0.20}|C{0.16}|C{0.1}|S{0.54}|"

.. include-file:: sections/Include/IEC10xsl_Device.rstinc "" ":xmlattr:`Source`" "source" "Source"

.. include-file:: sections/Include/IEC10xsl_Auto_IOA.rstinc "" ":xmlattr:`DIInfAddr`" "DI"

.. include-file:: sections/Include/IEC10xsl_Auto_IOA.rstinc "" ":xmlattr:`AIInfAddr`" "AI"

.. include-file:: sections/Include/IEC10xsl_Auto_IOA.rstinc "" ":xmlattr:`DOInfAddr`" "DO"

.. include-file:: sections/Include/IEC10xsl_Auto_IOA.rstinc "" ":xmlattr:`AOInfAddr`" "AO"

.. include-file:: sections/Include/IEC10xsl_Auto_Qualifier.rstinc "" ":xmlattr:`DIqual`" ":numref:`tabid-IEC10xslDIqualifier`" "DI"

.. include-file:: sections/Include/IEC10xsl_Auto_Qualifier.rstinc "" ":xmlattr:`AIqual`" ":numref:`tabid-IEC10xslAIqualifier`" "AI"

.. include-file:: sections/Include/IEC10xsl_Auto_Qualifier.rstinc "" ":xmlattr:`DOqual`" ":numref:`tabid-IEC10xslDOqualifier`" "DO"

.. include-file:: sections/Include/IEC10xsl_Auto_Qualifier.rstinc "" ":xmlattr:`AOqual`" ":numref:`tabid-IEC10xslAOqualifier`" "AO"

.. include-file:: sections/Include/IEC10xsl_GroupMask.rstinc "" ":xmlattr:`DIGroupMask`" "DI objects"

.. include-file:: sections/Include/IEC10xsl_GroupMask.rstinc "" ":xmlattr:`AIGroupMask`" "AI objects"

.. include-file:: sections/Include/IEC10xsl_Policy.rstinc ""

   * :attr:	:xmlattr:`CommsOnlineAddr`
     :val:	1...16777215
     :def:	n/a
     :desc:	Information address to report service DI – peer station communication (Online/Offline) status.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, communication status will not be reported if omitted.`

.. include-file:: sections/Include/Name.rstinc ""
