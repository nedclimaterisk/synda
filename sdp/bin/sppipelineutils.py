#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-

##################################
#  @program        synchro-data
#  @description    climate models data transfer program
#  @copyright      Copyright “(c)2009 Centre National de la Recherche Scientifique CNRS. 
#                             All Rights Reserved”
#  @license        CeCILL (http://dods.ipsl.jussieu.fr/jripsl/synchro_data/LICENSE)
##################################

"""Contains post-processing pipeline job argument builder.

Note
    - 'sppparg' means 'Synda Post-Processing Pipeline ARGument'
"""
import spconfig

TODO_CHECK

def remove_first_facet(path):
    """Remove first item in path

    path sample
        CMIP5/*/MIROC/MIROC5/historical/day/atmos/day/r2i1p1/v20120710
    """
    path=path.strip('/') # if leading and/or trailing slash exist, remove them

    li=path.split('/')

    li=li[1:]

    return '/'.join(li)

def replace_product_facet(dataset_pattern):
    return dataset_pattern.replace('/*/','/merge/')

def get_variable_full_path(prefix,dataset_pattern,variable):
    return '%s/%s/%s/%s/'%(spconfig.data_folder,prefix,dataset_pattern,variable)

def build_user_path(**generic_args):
    """Build end-user path.

    Sample
        /prodigfs/project/CMIP5/main/CNRM-CM5/historicalGHG/fx/atmos/fx/...
    """

    # Remove project facet. WARNING: we assume all datasets start with 'project'
    # facet (but this is not the case for some projects, e.g. obs4MIPs /
    # RMBE.ARMBE_Wind_Direction)
    dataset_pattern=remove_first_facet(dataset_pattern)

    # Remove product facet
    dataset_pattern=remove_first_facet(dataset_pattern) if project in ['CMIP5','CORDEX'] else dataset_pattern

    prefix='%s/%s/%s/%s'%(spconfig.data_folder,'project',project,'main')

    path=get_variable_full_path(prefix,dataset_pattern,variable)

    return path

def build_mirror_path(**generic_args):
    path=sppipelineutils.get_variable_full_path('esgf/mirror',dataset_pattern,variable)
    return path

def build_process_path(**generic_args):
    dataset_pattern=sppipelineutils.replace_product_facet(dataset_pattern) if project=='CMIP5' else dataset_pattern # product coalesce hack
    path=sppipelineutils.get_variable_full_path('esgf/process',dataset_pattern,variable)
    return path