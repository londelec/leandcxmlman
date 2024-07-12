# -*- coding: utf-8 -*-
#
# LeandcXmlManual build configuration file.
#

# General information about the project.
project = u'Leandc series XML configuration manual'

# The full version, including alpha/beta/rc tags.
release = u'V44 FW V5.09'

numfig = True
numfig_format = {'table': 'Table %s', 'figure': 'Figure %s', 'code-block': '%s'}

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = [
	'sections/Annexes/*',
	'sections/communicationCfg/*',
	'sections/HardwareCfg/*',
	'sections/IEC10xma/*',
	'sections/IEC10xsl/*',
	'sections/IEC101ma/*',
	'sections/IEC101sl/*',
	'sections/IEC103ma/*',
	'sections/IEC104ma/*',
	'sections/IEC104sl/*',
	'sections/IEC61850cl/*',
	'sections/Include/*',
	'sections/internalCfg/*',
	'sections/Modbusma/*',
	'sections/Spabusma/*',
	'sections/supervisionCfg/*']
