
.. _xmlgroup-HmiCfg: lelabel=HmiCfg

HmiCfg group node
-----------------

Group object node :ref:`xmlgroup-HmiCfg` is used to configure web access to leandc application.

.. code-block:: none

   <HmiCfg>
	<SCADA XMLpath="db.xml" Name="SCADA instance"/>
   </HmiCfg>

At the moment :ref:`xmlgroup-HmiCfg` group can have only one element node :ref:`xmlelem-SCADA` and its configuration is described in the following paragraph.
More element nodes will be added in the future.

.. _xmlelem-SCADA:

SCADA
^^^^^

Leandc application in conjuction with web server 'lehmi' provides SCADA functionality.
SCADA settings are stored in a separate XML file and this file is defined in :ref:`xmlelem-SCADA` node.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-SCADA`"

.. code-block:: none

   <SCADA XMLpath="db.xml" Name="SCADA instance"/>


.. field-list-table:: Leandc SCADA node
   :class: table table-condensed table-bordered longtable
   :name: tabid-SCADA
   :spec: |C{0.20}|C{0.25}|S{0.55}|
   :header-rows: 1

   * :attr,10:	Attribute
     :val,15:	Values or range
     :desc,75:	Description

   * :attr:	:xmlattr:`XMLpath`
     :val:	Max 100 chars
     :desc:	XML configuration file name and path.
		This file contains webscada settings and is used by 'lehmi' binary.
		File path may be omitted if XML file is stored in the default directory (|leandcapp|)
		:inlineimportant:`Attribute is case sensitive, observe case of the path and file name when specifying.`

.. include-file:: sections/Include/Name_wodef.rstinc ""

