.. include:: global.roles

.. _docref-hwio:
.. _xmlgroup-hwioConfig: lelabel=hwioConfig

Hardware IO
===========

This section contains details of IO object tables that represents General Purpose Inputs and Outputs (GPIO) of the Industrial PC.
Number of Inputs/Outputs depends on the hardware the |leandcapp| is running on and
IO tables that represents these Inputs/Outputs are created automatically.
Automatically created Digital Input and Output objects will have default settings as described in this section and
in most cases there is no need to define tables manually.
However IO tables can be created manually as described below if user wishes to change any of the settings.

Name and location path of the XML configuration file is not predefined, it can be chosen freely.
File name 'hwio.xml' is used as a sample.
Enter name of the XML file in :ref:`xmlelem-gphwio`.\ :ref:`xmlattr-gphwioXMLpath` attribute of the PLC instance created in |leandcxml| as follows:
:ref:`xmlattr-gphwioXMLpath` \ ="hwio.xml" .
Location path doesn't have to be specified if the XML file is located in the default directory (|leandcdir|).

| Configuration file (e.g. 'hwio.xml') must have a root node :ref:`xmlgroup-hwioConfig` which cosists of:
| 1 mandatory group :ref:`xmlelem-VersionControl`;
| 1 optional Digital Input group :ref:`xmlgroup-hwioDI`.
| 1 optional Digital Output group :ref:`xmlgroup-hwioDO`.
| Please see the sample below.

.. code-block:: none

 <hwioConfig xmlns="http://www.londelec.com/xmlschemas/leandc/hwio" … version="1.00">
   <VersionControl conf="1.00" date="2022-10-24" time="12:00:13"/>
   <DITable>
     <DI Index="0" Qualifier="0" ChatterFilter="50" Name="DI1"/>
         …
   </DITable>
   <DOTable>
     <DO Index="0" Qualifier="0" Name="DO1"/>
         …
   </DOTable>
 </hwioConfig>


.. _xmlgroup-hwioDI: lelabel=DITable
.. _xmlelem-hwioDI: lelabel=DI

DITable group
-------------

| :ref:`xmlgroup-hwioDI` group and its elements :ref:`xmlelem-hwioDI` are used to define DI information objects.
  Each :ref:`xmlelem-hwioDI` element can be linked to DI information objects (one or more) defined in the IO table of a Slave protocol instance.
| Please refer to the :ref:`docref-IEC10xslDI` section of a Slave protocol instance for more information on how to link DI information objects.

Please see sample :ref:`xmlgroup-hwioDI` group and :ref:`xmlelem-hwioDI` elements below.
There are 3 information objects defined with 2 :ref:`xmlelem-hwioDI` elements.

.. code-block:: none

 <DITable>
   <DI Index="0" Qualifier="0x00" ChatterFilter="50" Name="DI1"/>
   <DI Index="1" Qualifier="0x00" ChatterFilter="50" Total="2" Name="DI2..3"/>
 </DITable>

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-hwioDI`"

.. code-block:: none

   <DI Index="0" Qualifier="0x00" ChatterFilter="50" Total="1" Name="DI1"/>

.. include-file:: sections/Include/tip_order.rstinc "" ":ref:`xmlelem-hwioDI`"

DI attributes
^^^^^^^^^^^^^

.. include-file:: sections/Include/table_attrs.rstinc "" "tabid-hwioDI" "Hardware DI attributes" ":spec: |C{0.12}|C{0.14}|C{0.12}|S{0.62}|"

.. include-file:: sections/Include/ma_Index.rstinc "" "DI"

.. include-file:: sections/Include/Qualifier.rstinc "" ":numref:`tabid-hwioDIQualifier`"

   * :attr:	:xmlattr:`ChatterFilter`
     :val:	30...65535
     :def:	50 msec
     :desc:	Chatter filter in milliseconds for Digital Inputs.
		State change of the digital input will be reported only if it remains stable for the period that exceeds configured filter.

.. include-file:: sections/Include/Total.rstinc "" ":ref:`xmlattr-hwioDIIndex`" ":ref:`xmlelem-hwioDI`" "16"

.. include-file:: sections/Include/Name.rstinc ""

DI.Qualifier
^^^^^^^^^^^^

.. include-file:: sections/Include/table_flags8.rstinc "" "tabid-hwioDIQualifier" "Hardware DI internal qualifier" ":ref:`xmlattr-hwioDIQualifier`" "DI internal qualifier"

   * :attr:	Bit 0
     :val:	xxxx.xxx0
     :desc:	DI object **will not** be inverted (ON = 1; OFF = 0)

   * :(attr):
     :val:	xxxx.xxx1
     :desc:	DI object **will** be inverted (ON = 0; OFF = 1)

   * :attr:	Bit 7
     :val:	0xxx.xxxx
     :desc:	DI is **enabled**, GPIO Input state changes will be processed

   * :(attr):
     :val:	1xxx.xxxx
     :desc:	DI is **disabled**, GPIO Input state changes will be ignored

   * :attr:	Bits 1..6
     :val:	Any
     :desc:	Bits reserved for future use


.. _xmlgroup-hwioDO: lelabel=DOTable
.. _xmlelem-hwioDO: lelabel=DO

DOTable group
-------------

| :ref:`xmlgroup-hwioDO` group and its elements :ref:`xmlelem-hwioDO` are used to define DO information objects.
  Each :ref:`xmlelem-hwioDO` element can be linked to DO information objects (one or more) defined in the IO table of a Slave protocol instance.
| Please refer to the :ref:`docref-IEC10xslDO` section of a Slave protocol instance for more information on how to link DO information objects.

Please see sample :ref:`xmlgroup-hwioDO` group and :ref:`xmlelem-hwioDO` elements below.
There are 3 information objects defined with 2 :ref:`xmlelem-hwioDO` elements.

.. code-block:: none

 <DOTable>
   <DO Index="0" Qualifier="0x00" PulseDuration="1500" Name="DO1"/>
   <DO Index="1" Qualifier="0x00" PulseDuration="1500" Total="2" Name="DO2..3"/>
 </DOTable>

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-hwioDO`"

.. code-block:: none

   <DO Index="0" Qualifier="0x00" PulseDuration="50" Total="1" Name="DO1"/>

.. include-file:: sections/Include/tip_order.rstinc "" ":ref:`xmlelem-hwioDO`"

DO attributes
^^^^^^^^^^^^^

.. include-file:: sections/Include/table_attrs.rstinc "" "tabid-hwioDO" "Hardware DO attributes" ":spec: |C{0.12}|C{0.14}|C{0.12}|S{0.62}|"

.. include-file:: sections/Include/ma_Index.rstinc "" "DO"

.. include-file:: sections/Include/Qualifier.rstinc "" ":numref:`tabid-hwioDOQualifier`"

   * :attr:	:xmlattr:`PulseDuration`
     :val:	10...65535
     :def:	1500 msec
     :desc:	Digital output pulse duration in milliseconds.
		Digital output will be activated when command is received and automatically released after configured number of milliseconds.

.. include-file:: sections/Include/Total.rstinc "" ":ref:`xmlattr-hwioDOIndex`" ":ref:`xmlelem-hwioDO`" "16"

.. include-file:: sections/Include/Name.rstinc ""

DO.Qualifier
^^^^^^^^^^^^

.. include-file:: sections/Include/table_flags8.rstinc "" "tabid-hwioDOQualifier" "Hardware DO internal qualifier" ":ref:`xmlattr-hwioDOQualifier`" "DO internal qualifier"

   * :attr:	Bit 7
     :val:	0xxx.xxxx
     :desc:	DO is **enabled**, GPIO Output will be activated

   * :(attr):
     :val:	1xxx.xxxx
     :desc:	DO is **disabled**, GPIO Output will not be activated

   * :attr:	Bits 1..7
     :val:	Any
     :desc:	Bits reserved for future use

