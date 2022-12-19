
.. _xmlelem-gphwio:

HWIO
^^^^

Some Industrial PC models have General Purpose Inputs and Outputs (GPIO).
These can be accessed and controlled by utilizing :ref:`xmlelem-gphwio` instance.
Supported Industrial PC models with GPIOs are shown in the :numref:`tabid-HwioHardwares` below:

.. field-list-table:: Supported hardwares with GPIOs
   :class: table table-condensed table-bordered table-left table-center-all
   :name: tabid-HwioHardwares
   :header-rows: 1
   :spec: |C{0.14}|C{0.11}|C{0.11}|C{0.11}|C{0.11}|C{0.11}|C{0.11}|C{0.11}|C{0.11}|

   * :hw,30:	Hardware
     :di,7:	Inputs
     :do,7:	Outputs

   * :hw:	UNO-1372G (LEANDC-4/4)
     :di:	4
     :do:	4

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-gphwio`"

.. code-block:: none

   <HWIO Index="99" XMLpath="hwio.xml" Name="Advantech GPIO"/>


.. field-list-table:: HWIO attributes
   :class: table table-condensed table-bordered longtable
   :name: tabid-hwio
   :spec: |C{0.20}|C{0.25}|S{0.55}|
   :header-rows: 1

   * :attr,10,center:	Attribute
     :val,15,center:	Values or range
     :desc,75:		Description

   * :attr:	:xmlattr:`Index`
     :val:	|gpindexrange|
     :desc:	Index is a unique identifier of the HWIO instance.
		It is used to reference Industrial PC GPIOs from other configuration files e.g. IO object tables
		(please see :ref:`xmlelem-IEC10xslDI`.\ :ref:`xmlattr-IEC10xslDIDevice`\; :ref:`xmlelem-IEC10xslAI`.\ :ref:`xmlattr-IEC10xslAIDevice`\; :ref:`xmlelem-IEC10xslDO`.\ :ref:`xmlattr-IEC10xslDODevice`\; :ref:`xmlelem-IEC10xslAO`.\ :ref:`xmlattr-IEC10xslAODevice` \ attributes of the Slave protocol instance).
		:inlineimportant:`Make sure the selected value doesn't overlap with communication protocol instance indexes.`

   * :attr:	:xmlattr:`XMLpath`
     :val:	Max 100 chars
     :desc:	XML configuration file name and path.
		This file contains Industrial PC GPIO table and other settings.
		Path may be omitted if the XML file is stored in the default directory (|leandcdir|)
		:inlineimportant:`Attribute is case sensitive, observe case of the path and file name when specifying.`

.. include-file:: sections/Include/Name_wodef.rstinc ""

Industrial PC GPIO table is defined in a separate XML file specified in :ref:`xmlattr-gphwioXMLpath` attribute.
Contents of this XML file are described in the section :ref:`docref-hwio`.
