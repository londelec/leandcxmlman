.. _docref-IEC103maCommsSettingsAttr:

CommsSettings attributes
^^^^^^^^^^^^^^^^^^^^^^^^

Communication state reporting and related delays can be specified using attributes of :ref:`CommsSettings<ref-IEC103maCommsSettings>` 
element node.

Please see sample :ref:`CommsSettings<ref-IEC103maCommsSettings>` node and the table listing all available attributes below.

.. code-block:: none

   <CommsSettings NoRespCount="5" DegradedRetries="5" DegradedTimeout="600" ControlLockTimer="20" OfflineDelay="10" PostOfflineDelay="1000" OnlineGIDelay="10" />

.. _docref-IEC103maCommsSettingsAttab:

.. field-list-table:: IEC 60870-5-103 Master CommsSettings attributes
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.20}|C{0.25}|S{0.55}|
   :header-rows: 1

   * :attr,10: Attribute
     :val,15:  Values or range
     :desc,75: Description

.. include-file:: sections/Include/serma_CommsSettings.rstinc "" ".. _ref-IEC103maCommsSettingsNoRespCount:" ".. _ref-IEC103maCommsSettingsDegradedRetries:" ".. _ref-IEC103maCommsSettingsDegradedTimeout:"

.. include-file:: sections/Include/IEC10xma_ControlLockTimer.rstinc "" ".. _ref-IEC103maCommsSettingsControlLockTimer:"

.. include-file:: sections/Include/serma_OfflineDelay.rstinc "" ".. _ref-IEC103maCommsSettingsOfflineDelay:"

.. include-file:: sections/Include/PostOfflineDelay.rstinc "" ".. _ref-IEC103maCommsSettingsPostOfflineDelay:" ":ref:`OfflineDelay<ref-IEC103maCommsSettingsOfflineDelay>`"

.. include-file:: sections/Include/IEC10xma_OnlineGIDelay.rstinc "" ".. _ref-IEC103maCommsSettingsOnlineGIDelay:"
