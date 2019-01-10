# -*- coding: utf-8 -*-
#
# LeandcXmlManual build configuration file.
#

# General information about the project.
project = u'Leandc series XML configuration manual'

# The full version, including alpha/beta/rc tags.
release = u'V35'

# Override default css styles specified in SphinxBuild/conf_html.py
#html_numref_color = '#333'
#html_numref_font_weight = 'bold'
#html_numref_text_decoration = 'underline'

#html_docref_color = '#333'
#html_docref_font_weight = 'bold'
#html_docref_text_decoration = 'underline'

numfig = True
numfig_format = {'table': '%s', 'figure': '%s', 'code-block': '%s'}

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = [
	'sections/Annexes/*',
	'sections/communicationCfg/*',
	'sections/HardwareCfg/*',
	'sections/hmiCfg/*',
	'sections/IEC10xma/*',
	'sections/IEC10xsl/*',
	'sections/IEC101ma/*',
	'sections/IEC101sl/*',
	'sections/IEC103ma/*',
	'sections/IEC104ma/*',
	'sections/IEC104sl/*',
	'sections/IEC61850cl/*',
	'sections/Include/*',
	'sections/Modbusma/*',
	'sections/supervisionCfg/*']
