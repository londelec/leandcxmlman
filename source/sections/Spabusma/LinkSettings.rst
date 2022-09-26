.. _xmlelem-SpabusmaLink:

LinkSettings
^^^^^^^^^^^^

Spabus message settings can be specified using attributes of the :ref:`xmlelem-SpabusmaLink` element.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-SpabusmaLink`"

.. code-block:: none

   <LinkSettings Flags="0x00" />


.. include-file:: sections/Include/table_attrs.rstinc "" "tabid-SpabusmaLink" "Spabus Master LinkSettings attributes" ":spec: |C{0.12}|C{0.12}|C{0.1}|S{0.66}|"

   * :attr:	:xmlattr:`Flags`
     :val:	|flags8range|
     :def:	0x00
     :desc:	Miscellaneous Spabus message settings.
		See :numref:`tabid-SpabusmaLinkFlags` for description.


.. include-file:: sections/Include/table_flags8.rstinc "" "tabid-SpabusmaLinkFlags" "Message format flags" ":ref:`xmlattr-SpabusmaLinkFlags`" "Message format flags"

   * :attr:	Bit 0
     :val:	xxxx.xxx0
     :desc:	**Include** channel number in Event request mesage :lemonobgtext:`R0L` (default value)

   * :(attr):
     :val:	xxxx.xxx1
     :desc:	**Omit** channel number from Event request mesage :lemonobgtext:`RL`

   * :attr:	Bits 1...7
     :val:	Any
     :desc:	Bits reserved for future use
