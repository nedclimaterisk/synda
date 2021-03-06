#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-

##################################
#  @program        synda-pp
#  @description    climate models data transfer program
#  @copyright      Copyright “(c)2009 Centre National de la Recherche Scientifique CNRS. 
#                             All Rights Reserved”
#  @license        CeCILL (https://raw.githubusercontent.com/Prodiguer/synda/master/sdp/doc/LICENSE)
##################################

"""Pipeline loader.

Note
    'sppipeline' stands for 'Synda Post-processing pipeline'
"""

import os
import sys
import copy
import imp
import spconfig
from spexception import SPException

sys.path.insert(0, spconfig.pipeline_folder) # this is because of sdpipelineutils.py. TODO: try to find a better way to prevent doing that

def get_pipeline(name):
    if name not in pipelines:
        pipeline_definition_file='%s/%s.py'%(spconfig.pipeline_folder,name)
        
        if not os.path.exists(pipeline_definition_file):
            raise SPException("SPPPIPEL-001","Pipeline definition file not found (%s)"%pipeline_definition_file)

        pipeline_definition_module=imp.load_source(name, pipeline_definition_file)
        pipelines[name]=pipeline_definition_module.get_pipeline()

    return copy.deepcopy(pipelines[name])

# init.

pipelines={}
