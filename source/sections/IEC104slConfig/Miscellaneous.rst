
Miscellaneous attributes
^^^^^^^^^^^^^^^^^^^^^^^^

Miscellaneous and project-specific settings can be specified using attributes of :ref:`Miscellaneous<ref-IEC104slMiscellaneous>` element node.

Please see sample :ref:`Miscellaneous<ref-IEC104slMiscellaneous>` node and the table listing all available attributes below.

.. code-block:: none

   <Miscellaneous LegacyAIEVinitdelay="20" />

.. _ref-IEC104slMiscellaneousAttributes:

.. field-list-table:: IEC 60807-5-104 Slave Miscellaneous attributes
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.20}|C{0.25}|S{0.55}|
   :header-rows: 1

   * :attr,10: Attribute
     :val,15:  Values or range
     :desc,75: Description
     
   * :attr:    :xmlref:`LegacyAIEVinitdelay`
     :val:     0...2\ :sup:`32`\  - 1
     :desc:    Attribute enables specially marked (legacy spontaneous-only) AI object post-initialization after configured number of seconds when downstream outstation goes online. This functionality is enabled for AI objects which have Legacy bit [2] set in Master's :ref:`AI<ref-IEC10xmaAI>`.\ :ref:`qualifier<ref-IEC10xmaAIqualifier>` \. If an AI has Invalid [IV] bit set, its Invalid [IV] bit will be cleared and object will be sent upstream after number of seconds configured in :xmlref:`LegacyAIEVinitdelay` on system startup and whenever downstream outstation goes online. AI value will remain unchanged, being 0 on system startup and previous value from internal database when outstation goes online.
     