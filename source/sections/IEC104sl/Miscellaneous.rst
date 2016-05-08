.. _ref-IEC104slMiscellaneous:

Miscellaneous
^^^^^^^^^^^^^

Miscellaneous and project-specific settings can be specified in this node.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`<ref-IEC104slMiscellaneous>`"

.. code-block:: none

   <Miscellaneous LegacyAIEVinitdelay="2" />


.. _docref-IEC104slMiscellaneousAttab:

.. include-file:: sections/Include/table_attrs.rstinc "" "IEC60870-5-104 Slave Miscellaneous attributes"

   * :attr:     :xmlref:`LegacyAIEVinitdelay`
     :val:      0...2\ :sup:`32`\  - 1
     :def:      0 sec
     :desc:     Attribute enables specially marked (legacy spontaneous-only) AI object initialization after configured number of seconds on leandc startup.
		Feature applies only to AI objects that have Legacy bit [2] set in :ref:`AI<ref-IEC10xmaAI>`.\ :ref:`<ref-IEC10xmaAIqualifier>` \.
		Legacy AI objects will be reported spontaneously with a last known value from the internal database whenever downstream outstation goes online e.g. after a communication loss or when Enabled with a Service command. 
		In this case AI events will not have either Invalid [IV] nor Not Topical [NT] bits set, with the exception on leandc startup.
 		AI events will have value 0 and Invalid bit [IV] set when initialized for the first time on leandc startup.
		This functionality is not affected by the use of the :xmlref:`LegacyAIEVinitdelay` attribute and applies always if a particular AI object has Legacy bit [2] set in :ref:`AI<ref-IEC10xmaAI>`.\ :ref:`<ref-IEC10xmaAIqualifier>` \. 
		:xmlref:`LegacyAIEVinitdelay` attribute extends functionality by providing a mechanism to remove Invalid [IV] bit after configured number of seconds.
		(The Invalid [IV] bit was set when legacy AI events had been sent to the upstream station for the first time on leandc startup.)
		AI objects with 0 value and cleared Invalid [IV] bit will be sent using Background scan message(s) after number of seconds configured in :xmlref:`LegacyAIEVinitdelay` attribute.
		This ensures upstream station (e.g. SCADA) will have a valid legacy AI object with 0 value in the database.
		As a result upstream station will be ready to process first genuine AI event when it arrives.
