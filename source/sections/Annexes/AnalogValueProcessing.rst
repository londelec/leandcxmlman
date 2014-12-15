.. include:: global.roles

.. _docref-AIProcessing:

Analog value processing
=======================

This annex contains additional information on incoming AI processing, scaling options and application examples.

.. _docref-AIScalingWithoutStartOffset:

AI scaling without StartOffset enabled
--------------------------------------

Flowchart on the right shows scaling sequence when leandc receives AI value from outstation or before sending 
AI value to upstream station depending on used communication protocol. Scaling sequence shown below is 
used if :xmlref:`StartOffset` is **not enabled** (attribute :ref:`AI<ref-IEC10xslAI>`.\ :ref:`StartOffset<ref-IEC10xslAIStartOffset>` \ = 0 or excluded). Sample values before and after 
each step are listed in the following tables. Please note there is no relation between values shown in different 
tables. Tables are used to illustrate functionality of each step separately not the complete operation of the 
scaling sequence.

.. figure:: ../_images/AI_processing_0.*
   :figclass: figure-right
   
   AI scaling without StartOffset enabled

.. field-list-table:: AI.ZeroDeadband processing sample
   :class: table table-condensed table-bordered table-left table-center-all
   :spec: |C{0.28}|C{0.28}|
   :header-rows: 1

   * :val1,50: Value before
     :val2,50: Value after (:ref:`AI<ref-IEC10xslAI>`.\ :ref:`ZeroDeadband<ref-IEC10xslAIZeroDeadband>` \ = 2)

   * :val1:    -10
     :val2:    -10

   * :val1:    -2.1
     :val2:    -2.1

   * :val1:    -2
     :val2:    0

   * :val1:    -1
     :val2:    0

   * :val1:    0
     :val2:    0

   * :val1:    1
     :val2:    0

   * :val1:    2
     :val2:    0

   * :val1:    2.1
     :val2:    2.1

   * :val1:    10
     :val2:    10

.. field-list-table:: AI.Offset processing sample
   :class: table table-condensed table-bordered table-left table-center-all
   :spec: |C{0.28}|C{0.28}|
   :header-rows: 1

   * :val1,50: Value before
     :val2,50: Value after 
               (:ref:`AI<ref-IEC10xslAI>`.\ :ref:`Offset<ref-IEC10xslAIOffset>` \ = 5)

   * :val1:    -10
     :val2:    -5

   * :val1:    -2
     :val2:    3

   * :val1:    -1
     :val2:    4

   * :val1:    0
     :val2:    5

   * :val1:    1
     :val2:    6

   * :val1:    2
     :val2:    7

   * :val1:    10
     :val2:    15

.. field-list-table:: AI.OffsetDeadband processing sample
   :class: table table-condensed table-bordered table-left table-center-all
   :spec: |C{0.28}|C{0.28}|
   :header-rows: 1

   * :val1,50: Value before
     :val2,50: Value after (:ref:`AI<ref-IEC10xslAI>`.\ :ref:`OffsetDeadband<ref-IEC10xslAIOffsetDeadband>` \ = 2)

   * :val1:    -10
     :val2:    -10

   * :val1:    -2.1
     :val2:    -2.1

   * :val1:    -2
     :val2:    0

   * :val1:    -1
     :val2:    0

   * :val1:    0
     :val2:    0

   * :val1:    1
     :val2:    0

   * :val1:    2
     :val2:    0

   * :val1:    2.1
     :val2:    2.1

   * :val1:    10
     :val2:    10

.. field-list-table:: AI.NonZeroOffset processing sample
   :class: table table-condensed table-bordered table-left table-center-all
   :spec: |C{0.28}|C{0.28}|
   :header-rows: 1

   * :val1,50: Value before
     :val2,50: Value after (:ref:`AI<ref-IEC10xslAI>`.\ :ref:`NonZeroOffset<ref-IEC10xslAINonZeroOffset>` \ = 5)

   * :val1:    -10
     :val2:    -15

   * :val1:    -2
     :val2:    -7

   * :val1:    -1
     :val2:    -6

   * :val1:    0
     :val2:    0

   * :val1:    1
     :val2:    6

   * :val1:    2
     :val2:    7

   * :val1:    10
     :val2:    15

.. field-list-table:: AI.Coeff processing sample
   :class: table table-condensed table-bordered table-left table-center-all
   :spec: |C{0.28}|C{0.28}|
   :header-rows: 1

   * :val1,50: Value before
     :val2,50: Value after (:ref:`AI<ref-IEC10xslAI>`.\ :ref:`Coeff<ref-IEC10xslAICoeff>` \ = 2.5)

   * :val1:    -10
     :val2:    -25

   * :val1:    -2
     :val2:    -5

   * :val1:    -1
     :val2:    -2.5

   * :val1:    0
     :val2:    0

   * :val1:    1
     :val2:    2.5

   * :val1:    2
     :val2:    5

   * :val1:    10
     :val2:    25

.. _docref-AIScalingWithStartOffset:

AI scaling with StartOffset enabled
-----------------------------------     
     
Flowchart on the right shows scaling sequence when leandc receives AI value from outstation or before sending 
AI value to upstream station depending on used communication protocol. Scaling sequence shown below is 
used if :xmlref:`StartOffset` **is enabled** (attribute :ref:`AI<ref-IEC10xslAI>`.\ :ref:`StartOffset<ref-IEC10xslAIStartOffset>` \ > 0). Sample values before and after each step are listed 
in the following tables. Please note there is no relation between values shown in different tables. Tables are 
used to illustrate functionality of each step separately not the complete operation of the scaling sequence.

.. figure:: ../_images/AI_processing_1.*
   :figclass: figure-right
   
   AI scaling with StartOffset enabled

.. field-list-table:: AI.ZeroDeadband processing sample
   :class: table table-condensed table-bordered table-left table-center-all
   :spec: |C{0.28}|C{0.28}|
   :header-rows: 1

   * :val1,50: Value before
     :val2,50: Value after 
               (:ref:`AI<ref-IEC10xslAI>`.\ :ref:`StartOffset<ref-IEC10xslAIStartOffset>` \ = 6554)
               (:ref:`AI<ref-IEC10xslAI>`.\ :ref:`ZeroDeadband<ref-IEC10xslAIZeroDeadband>` \ = 1)

   * :val1:    -6556
     :val2:    -6556

   * :val1:    -6555
     :val2:    0

   * :val1:    -6554
     :val2:    0

   * :val1:    -6553
     :val2:    0

   * :val1:    -6552
     :val2:    0 & Invalid [IV]

   * :val1:    -1
     :val2:    0 & Invalid [IV]

   * :val1:    0
     :val2:    0 & Invalid [IV]

   * :val1:    1
     :val2:    0 & Invalid [IV]

   * :val1:    6552
     :val2:    0 & Invalid [IV]

   * :val1:    6553
     :val2:    0

   * :val1:    6554
     :val2:    0

   * :val1:    6555
     :val2:    0

   * :val1:    6556
     :val2:    6556
     
.. field-list-table:: AI.StartOffset processing sample
   :class: table table-condensed table-bordered table-left table-center-all
   :spec: |C{0.28}|C{0.28}|
   :header-rows: 1

   * :val1,50: Value before
     :val2,50: Value after 
               (:ref:`AI<ref-IEC10xslAI>`.\ :ref:`StartOffset<ref-IEC10xslAIStartOffset>` \ = 6554)

   * :val1:    -32767
     :val2:    -26213

   * :val1:    -6555
     :val2:    -1

   * :val1:    -6554
     :val2:    0

   * :val1:    -6553
     :val2:    0 & Invalid [IV]

   * :val1:    -1
     :val2:    0 & Invalid [IV]

   * :val1:    0
     :val2:    0 & Invalid [IV]

   * :val1:    1
     :val2:    0 & Invalid [IV]

   * :val1:    6553
     :val2:    0 & Invalid [IV]

   * :val1:    6554
     :val2:    0

   * :val1:    6555
     :val2:    1

   * :val1:    32767
     :val2:    26213
     
.. _docref-ReceivedAIProcessing:
     
Received AI processing
----------------------

Flowchart below shows AI value processing when IEC 60870-5-101/103/104 Master protocol instance receives 
AI object from outstation. This processing takes place after AI scaling has been completed, refer to previous 
annexes for additional information on AI scaling.

.. figure:: ../_images/AI_processing_2.*
   :align: center
   
   Received AI processing flowchart

The figure below shows how a real time value received from outstation will be processed if :ref:`AI<ref-IEC10xmaAI>`.\ :ref:`Deadband<ref-IEC10xmaAIDeadband>` \ 
attribute is enabled. Internal database will be updated and AI event will get generated every time a real time 
value exceeds 'static deadband'. Thresholds of the 'static deadband' are calculated based on previous value 
stored in the database. Attribute :ref:`AI<ref-IEC10xmaAI>`.\ :ref:`Deadband<ref-IEC10xmaAIDeadband>` \ = 2 is used as an example.

.. figure:: ../_images/AI_processing_3.*
   :align: center

   :xmlref:`AI.Deadband` processing sample

The figure below shows how a real time value received from outstation will be processed if :ref:`AI<ref-IEC10xmaAI>`.\ :ref:`Percent<ref-IEC10xmaAIPercent>` \ attribute 
is enabled. Internal database will be updated and AI event will get generated every time a real time value 
exceeds 'dynamic deadband'. Thresholds of the 'dynamic deadband' are calculated based on previous value 
stored in the database. Attribute :ref:`AI<ref-IEC10xmaAI>`.\ :ref:`Percent<ref-IEC10xmaAIPercent>` \ = 20 is used as an example.   

.. figure:: ../_images/AI_processing_4.*
   :align: center

   :xmlref:`AI.Percent` processing sample

0-20mA transducers
------------------

AIMs use 16bit Signed Integer variables for analogue value reporting. Lowest integer value 0 represents 0mA at 
AIM's input and the highest integer value 32767 represents 20mA at AIM's input.

Following formulas allow Integer value evaluation from Current at the AIM's input and vice versa.

Formula for evaluating current mA value is: 

.. math::

   mA = \frac{Integer}{32767} * 20

example

.. math::

   \frac{2000}{32767} * 20 = 1.2207mA

Formula for evaluating Integer value is:

.. math::

   Integer = \frac{mA}{20} * 32767

example

.. math::

   \frac{2.2}{20} * 32767 = 3604
   
Sample values are summarized in the table :numref:`ref-AISampleValuesIf0-20maRangeUsed` below and it is assumed **1A/0-20mA** current transducer is 
connected to the AIM. Current values at the transducer input are listed in the third column.   

.. _ref-AISampleValuesIf0-20maRangeUsed:

.. field-list-table:: AI sample values if 0-20mA input range is used
   :class: table table-condensed table-bordered table-left table-center-all
   :spec: |C{0.28}|C{0.28}|C{0.28}|
   :header-rows: 1

   * :val1: mA value
     :val2: Integer value
     :val3: Current at (1A) transducer input 

   * :val1:    0mA
     :val2:    0
     :val3:    0A
      
   * :val1:    1mA
     :val2:    1638
     :val3:    0.05A

   * :val1:    2mA
     :val2:    3277
     :val3:    0.1A

   * :val1:    3mA
     :val2:    4915
     :val3:    0.15A

   * :val1:    4mA
     :val2:    6553
     :val3:    0.2A

   * :val1:    5mA
     :val2:    8192
     :val3:    0.25A

   * :val1:    8mA
     :val2:    13107
     :val3:    0.4A

   * :val1:    12mA
     :val2:    19660
     :val3:    0.6A

   * :val1:    16mA
     :val2:    26214
     :val3:    0.8A

   * :val1:    20mA
     :val2:    32767
     :val3:    1A
     
4-20mA transducers     
------------------     
     
It is common to use 4-20mA output range transducers as there is an option of detecting transducer failure if 
current at the AIM input drops below 4mA. However additional calculation is required to compensate the 4mA 
offset at the AIM input created because of this increased functionality.

AIMs will still use 16bit Signed Integer variables for analogue value reporting, but unlike the previous 
paragraph, full range can't be used and the 4mA offset needs to be taken into consideration. There is an option 
to automatically adjust 4mA offset and it can be enabled by setting Bit [0] of the Slave AI internal qualifier 
(attribute :ref:`AI<ref-IEC10xslAI>`.\ :ref:`qualifier<ref-IEC10xslAIqualifier>` \ please refer to the table :numref:`ref-IEC10xslAIqualifierBits`). Setting Bit[0] to '1' will enables automatic adjustment by 
subtracting 6554 from the received Integer value.

Offset 6554 is equal to 4mA current value (as per table :numref:`ref-AISampleValuesIf0-20maRangeUsed` above) which means after subtraction Integer will 
be 0 when there are 4mA at AIM's input and Integer will be **26213** when there are 20mA at AIM's input. 

.. tip::

   Leandc unit will report Integer '0' with Invalid [IV] flag set if the current at AIM input is less than 4mA 
   (Integer is less than '6554'). This is an extended functionality for detecting transducer failure.

Following formulas allow Integer value evaluation from Current at the AIM's input and vice versa.     
     
Formula for evaluating current mA value is:
  
.. math::

   mA = \left(\frac{Integer}{26213} * 16\right) + 4

example

.. math::

   \left(\frac{2000}{26213} * 16\right) + 4 = 5.2208mA

Formula for evaluating Integer value is:

.. math::

   Integer = \frac{(mA - 4)}{16} * 26213

example

.. math::

   \frac{(5.2 - 4)}{16} * 26213 = 1966

Sample values are listed in the table :numref:`ref-AISampleValuesIf4-20maRangeUsed` below, those are calculated assuming **1A/4-20mA** current transducer 
is connected to the AIM. Current values at the transducer input are listed in the third column.

.. _ref-AISampleValuesIf4-20maRangeUsed:

.. field-list-table:: AI sample values if 4-20mA input range is used
   :class: table table-condensed table-bordered table-left table-center-all
   :spec: |C{0.28}|C{0.28}|C{0.28}|
   :header-rows: 1

   * :val1: mA value
     :val2: Integer value
     :val3: Current at (1A) transducer input 

   * :val1:    0mA
     :val2:    0 & INVALID
     :val3:    Transducer not connected

   * :val1:    1mA
     :val2:    0 & INVALID
     :val3:    Transducer not connected

   * :val1:    4mA
     :val2:    0
     :val3:    0A

   * :val1:    5mA
     :val2:    1638
     :val3:    0.0625A

   * :val1:    6mA
     :val2:    3276
     :val3:    0.125A

   * :val1:    7mA
     :val2:    4914
     :val3:    0.1875A

   * :val1:    8mA
     :val2:    6553
     :val3:    0.25A

   * :val1:    12mA
     :val2:    13106
     :val3:    0.5A

   * :val1:    16mA
     :val2:    19660
     :val3:    0.75A

   * :val1:    20mA
     :val2:    26213
     :val3:    1A

Special transducers
-------------------

There are specific types of transducers that have offset at their input and this paragraph explains how to 
configure LEANDC unit to compensate measurement offset created by such transducers. A specific voltage 
transducer with input range 75-125V and output 4-20mA will be used as an example. Now in addition to the 
fixed 4mA output offset compensation described in the previous paragraph, there is another offset required to 
compensate 75V voltage offset at the transducer's input. Both offset compensation adjustment requires 3 
separate steps as follow:

* 4mA compensation can be enabled by setting Bit [0] of the Slave AI internal qualifier attribute 
  AI.qualifier as described in the previous paragraph. After 6554 offset subtraction Integer will be 0 when 
  there are 4mA at AIM's input and Integer will be 26213 when there are 20mA the same as before.
  
* It is necessary to select a deadband to filter a noise around 4mA using AI.ZeroDeadband attribute. The 
  AI.ZeroDeadband attribute has to be selected carefully to ensure a value exceeding the deadband is 
  valid measurement (not a noise) and represents voltage above 75V at transducer's input. AI value 
  fluctuations around 4mA that doesn't exceed deadband configured in the AI.ZeroDeadband attribute 
  will be forced to 0.
  
* The final step is to compensate a 75V offset at transducer's input using AI.NonZeroOffset attribute. 
  Please note AI.NonZeroOffset will be applied only to Integer values exceeding AI.ZeroDeadband. It is 
  necessary to calculate an integer offset that is proportional to 75V. The following formula can be used, 
  divide scaled Integer range (26213, after 4mA offset compensation) by actual transducer input range 
  (75-125V, actual range after subtracting 75 is 50) and multiply by offset at the transducer's input (75V).

.. math::

   Integer Offset = \frac{Integer range}{input range} * input offset

example

.. math::

   \frac{26213}{50} * 75 = 39320

The proportional Integer offset is **39320** and following formulas can be used to evaluate Integer value from 
Current at the AIM's input and vice versa.

Formula for evaluating Current mA value from Integer is:

.. math::

   mA = \left(\frac{(Integer - 39320)}{26213} * 16\right) + 4

example

.. math::

   \left(\frac{(40000 - 39320)}{26213} * 16\right) + 4 = 4.415mA

Formula for evaluating Integer from Current mA is:

.. math::

   Integer = \left(\frac{(mA - 4)}{16} * 26213\right) + 39320

example

.. math::

   \left(\frac{(5.7 - 4)}{16} * 26213\right) + 39320 = 42105

Formula for evaluating Current mA value from Voltage is:

.. math::

   mA = \left(\frac{(Voltage - 75)}{50} * 16\right) + 4

example

.. math::

   \left(\frac{(79.3 - 75)}{50} * 16\right) + 4 = 5.376mA

Formula for evaluating Integer from Voltage is:   

.. math::

   Integer = \left(\frac{(Voltage - 75)}{50} * 26213\right) + 39320

example

.. math::

   \left(\frac{(82.4 - 75)}{50} * 26213\right) + 39320 = 43200
   
Following formulas allow Voltage evaluation from Current at the AIM's input or Integer.   
   
Formula for evaluating Voltage from Integer is:   
   
.. math::

   Voltage = \left(\frac{(Integer - 39320)}{26213} * 50\right) + 75

example

.. math::

   \left(\frac{(40200 - 39320)}{26213} * 50\right) + 75 = 76.678V
   
Formula for evaluating Voltage from Current mA is:   
   
.. math::

   Voltage = \left(\frac{(mA - 4)}{16} * 50\right) + 75

example

.. math::

   \left(\frac{(5.9 - 4)}{16} * 50\right) + 75 = 80.936V
   
Sample values at various conversion stages based on **75-125V/4-20mA** voltage transducer are summarized in 
the table :numref:`ref-AISampleValuesIf75-125V4-20mARangeUsed` below. Integer values after 4mA offset subtraction are listed in column 2. :ref:`AI<ref-IEC10xslAI>`.\ :ref:`ZeroDeadband<ref-IEC10xslAIZeroDeadband>` \
attribute value of 2 is used for this example resulting Integer values 1 and 2 being forced to 0, functionality is 
shown in column 3. Integer values after :ref:`AI<ref-IEC10xslAI>`.\ :ref:`NonZeroOffset<ref-IEC10xslAINonZeroOffset>` \ adjustment are listed in the column 4. Voltage values 
at the transducer input are listed in the column 5.   

.. _ref-AISampleValuesIf75-125V4-20mARangeUsed:

.. field-list-table:: AI sample values if 75-125V/4-20mA transducer is used
   :class: table table-condensed table-bordered table-center-all
   :spec: |C{0.2}|C{0.2}|C{0.2}|C{0.2}|C{0.2}|
   :header-rows: 1

   * :val1,20: mA value
     :val2,20: Integer value before 75V offset
     :val3,20: ZeroDeadband active
     :val4,20: Integer value after 75V offset
     :val5,20: Voltage at (75-125V) transducer Input

   * :val1:    0mA
     :val2:    0 & INVALID
     :val3:    No
     :val4:    0 & INVALID
     :val5:    Transducer not connected

   * :val1:    1mA
     :val2:    0 & INVALID
     :val3:    No
     :val4:    0 & INVALID
     :val5:    Transducer not connected

   * :val1:    4mA
     :val2:    0
     :val3:    No
     :val4:    0
     :val5:    0V...75V

   * :val1:    4.0006mA
     :val2:    1
     :val3:    Yes, forcing to 0
     :val4:    0
     :val5:    75.002V

   * :val1:    4.0012mA
     :val2:    2
     :val3:    Yes, forcing to 0
     :val4:    0
     :val5:    75.004V

   * :val1:    4.0018mA
     :val2:    3
     :val3:    No
     :val4:    39323
     :val5:    75.006V

   * :val1:    5mA
     :val2:    1638
     :val3:    No
     :val4:    40958
     :val5:    78.125V

   * :val1:    6mA
     :val2:    3276
     :val3:    No
     :val4:    42596
     :val5:    81.25V

   * :val1:    7mA
     :val2:    4914
     :val3:    No
     :val4:    44234
     :val5:    84.375V

   * :val1:    8mA
     :val2:    6553
     :val3:    No
     :val4:    45873
     :val5:    87.5V

   * :val1:    12mA
     :val2:    13106
     :val3:    No
     :val4:    52426
     :val5:    100V

   * :val1:    16mA
     :val2:    19660
     :val3:    No
     :val4:    58980
     :val5:    112.5V

   * :val1:    20mA
     :val2:    26213
     :val3:    No
     :val4:    65533
     :val5:    125V
     