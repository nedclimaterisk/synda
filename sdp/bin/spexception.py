#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-

##################################
#  @program        synda-pp
#  @description    climate models data transfer program
#  @copyright      Copyright “(c)2009 Centre National de la Recherche Scientifique CNRS. 
#                             All Rights Reserved”
#  @license        CeCILL (https://raw.githubusercontent.com/Prodiguer/synda/master/sdp/doc/LICENSE)
##################################

"""This module contains exception classes.
"""

class SPException(Exception):
    def __init__(self, code=None, msg=None):
        self.code=code
        self.msg=msg
    def __str__(self):
        return "code=%s,message=%s"%(self.code,self.msg)

class NoPostProcessingTaskWaitingException(SPException):
    pass
class StateNotFoundException(SPException):
    pass
class PipelineRunningException(SPException):
    pass
