
.. _xmlelem-gpspabusma:

Spabusma
^^^^^^^^

General settings of the Spabus Master communication protocol instance.
.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-gpspabusma`"

.. code-block:: none

   <Spabusma Index="10" HWIndex="2" XMLpath="IED1.xml" Address="5" CommsFlags="0x80" Name="Protection IED"/>


.. include-file:: sections/Include/table_gp.rstinc "" "tabid-gpspabusma" "Spabusma"

.. include-file:: sections/Include/gp_ma_Index.rstinc "" 

.. include-file:: sections/Include/gp_HWIndex.rstinc "" ":ref:`xmlelem-uart`.\ :ref:`xmlattr-UARTIndex`"
		:inlinetip:`Multiple` :ref:`xmlelem-gpspabusma` :inlinetip:`instances can share the same hardware node.`

.. include-file:: sections/Include/gp_XMLpath.rstinc ""

   * :attr:	:xmlattr:`Address`
     :val:	1...899
     :desc:	SPA device address.
		Address of the connected SPA Slave station (e.g. IED) must be the same.

.. include-file:: sections/Include/gp_CommsFlags.rstinc ""

.. include-file:: sections/Include/Name_wodef.rstinc ""

.. include-file:: sections/Include/gp_section.rstinc "" ":ref:`xmlattr-gpspabusmaXMLpath`" ":ref:`docref-Spabusma`"
