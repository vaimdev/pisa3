# -*- coding: ISO-8859-1 -*-
#############################################
## (C)opyright by Dirk Holtwick, 2002-2007 ##
## All rights reserved                     ##
#############################################

__reversion__ = "$Revision: 238 $"
__author__    = "$Author: holtwick $"
__date__      = "$Date: 2008-06-26 20:06:02 +0200 (Do, 26 Jun 2008) $"

REQUIRED_INFO = """
****************************************************
IMPORT ERROR!
%s
****************************************************

The following Python packages are required for PISA:
- ReportlabToolkit>=2.1 <http://www.reportlab.org/>
- HTML5lib>=0.11.1 <http://code.google.com/p/html5lib/>

Optional packages:
- pyPDF <http://pybrary.net/pyPdf/>
- PIL <http://www.pythonware.com/products/pil/>

""".lstrip()

try:
    #from pisa import *
    from .pisa import *
#except ImportError , e:
except ImportError as e:
    import sys
    sys.stderr.write(REQUIRED_INFO % e)
    raise

__version__   = VERSION
