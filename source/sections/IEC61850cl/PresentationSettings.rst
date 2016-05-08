.. _ref-IEC61850clPresentationSettings:

PresentationSettings
^^^^^^^^^^^^^^^^^^^^

Settings of the Presentation layer (ISO8823) can be specified using attributes of :ref:`<ref-IEC61850clPresentationSettings>` 
element node.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`<ref-IEC61850clPresentationSettings>`"

.. code-block:: none

   <PresentationSettings CallingPSEL="1" />


.. _docref-IEC61850clPresentationSettingsAttab:

.. include-file:: sections/Include/table_attrs.rstinc "" "IEC61850 Client PresentationSettings attributes"

   * :attr:     :xmlref:`CallingPSEL`
     :val:      1...2\ :sup:`32`\  - 1
     :def:      1
     :desc:     Calling Presentation Selector used for outgoing [CP PPDU] message
