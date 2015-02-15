.. _docref-IEC104slMiscellaneousAttr:

Miscellaneous attributes
^^^^^^^^^^^^^^^^^^^^^^^^

Miscellaneous and project-specific settings can be specified using attributes of :ref:`Miscellaneous<ref-IEC104slMiscellaneous>` element node.

Please see sample :ref:`Miscellaneous<ref-IEC104slMiscellaneous>` node and the table listing all available attributes below.

.. code-block:: none

   <Miscellaneous LegacyAIEVinitdelay="2" />

.. _docref-IEC104slMiscellaneousAttab:

.. field-list-table:: IEC 60870-5-104 Slave Miscellaneous attributes
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.20}|C{0.25}|S{0.55}|
   :header-rows: 1

   * :attr,10: Attribute
     :val,15:  Values or range
     :desc,75: Description
     
   * :attr:    :xmlref:`LegacyAIEVinitdelay`
     :val:     0...2\ :sup:`32`\  - 1
     :desc:    Attribute enables specially marked (legacy spontaneous-only) AI object initialization after configured number of seconds on leandc startup. This feature applies only to AI objects that have Legacy bit [2] set in Master's :ref:`AI<ref-IEC10xmaAI>`.\ :ref:`qualifier<ref-IEC10xmaAIqualifier>` \. Legacy AI objects will be reported spontaneously with a last value from the internal database whenever downstream outstation comes online e.g. after a communication loss or when Enabled using Service command. AI events will not have either Invalid [IV] or Not Topical [NT] bits set, with exception on leandc startup when Ai events will have value 0 and Invalid bit [IV] set. This behaviour is not affected by the use of the :xmlref:`LegacyAIEVinitdelay` attribute and always applies if a particular AI object has Legacy bit [2] set in Master's :ref:`AI<ref-IEC10xmaAI>`.\ :ref:`qualifier<ref-IEC10xmaAIqualifier>` \. This attribute extends functionality by providing mechanism to remove Invalid [IV] bit after configured number of seconds when legacy AI events have been sent to upstream station for the first time on leandc startup. AI objects with 0 value and cleared Invalid [IV] bit will be sent using Background scan message(s) after number of seconds configured in :xmlref:`LegacyAIEVinitdelay` attribute. This ensures an upstream station (e.g. SCADA) will have a valid legacy AI object with 0 value in the database and station is ready to process first genuine AI event when it arrives.
