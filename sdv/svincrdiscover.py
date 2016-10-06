#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-

##################################
#  @program        synda
#  @description    climate models data transfer program
#  @copyright      Copyright “(c)2009 Centre National de la Recherche Scientifique CNRS. 
#                             All Rights Reserved”
#  @license        CeCILL (https://raw.githubusercontent.com/Prodiguer/synda/master/sdt/doc/LICENSE)
##################################

"""This script contains UAT test for incremental discovery."""

import argparse
import re
import time
from fabric.api import task
from svtestutils import fabric_run, task_exec
import svtestcommon as tc

def run():

    task_exec(tc.stop) 
    task_exec(tc.disable_download) 
    task_exec(tc.reset) 
    task_exec(tc.configure_task) 
    task_exec(tc.execute_basic_command)
    task_exec(tc.check_version)

    print 'At T1, a normal (full) discovery is performed'
    task_exec(normal_discovery)
    task_exec(check_normal_discovery_result)

    print 'A few weeks pass, without any discovery being run..'
    time.sleep(15)

    print 'At T1, a normal (full) discovery is performed'
    time.sleep(2)

@task
def normal_discovery():
    fabric_run('synda install -y %s to=%s'%(parameter,date_t1))

@task
def check_normal_discovery_result():
    fabric_run('test $(synda list limit=0 -f | wc -l) -eq 2473')

@task
def normal_discovery():
    fabric_run('synda install -i -y %s from=%s'%(parameter,date_t1))

@task
def check_dataset_version():
    fabric_run('synda remove -y CMIP5 MPI-M MPI-ESM-LR decadal1995 mon baresoilFrac')

@task
def check_dataset_version():
    fabric_run('test ! -f /srv/synda/sdt/data/cmip5/output1/MPI-M/MPI-ESM-LR/decadal1995/mon/land/Lmon/r2i1p1/v20120529/baresoilFrac/baresoilFrac_Lmon_MPI-ESM-LR_decadal1995_r2i1p1_199601-200512.nc')

# init.
parameter='CMIP5 output1 MOHC HadGEM2-ES rcp85 mon atmos Amon r1i1p1'
date_t1='2015-11-01T01:00:00Z'

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    run()