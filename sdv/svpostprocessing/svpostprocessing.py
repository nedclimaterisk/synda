#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-

##################################
#  @program        synda
#  @description    climate models data transfer program
#  @copyright      Copyright “(c)2009 Centre National de la Recherche Scientifique CNRS. 
#                             All Rights Reserved”
#  @license        CeCILL (https://raw.githubusercontent.com/Prodiguer/synda/master/sdt/doc/LICENSE)
##################################

"""This script contains user acceptance testing (UAT) routines."""

import sys
import argparse
import re
import time
import fabric.api
from fabric.api import task

sys.path.append("..")

from testlib.svtestutils import fabric_run, task_exec, Testset, title
import testlib.svtestcommon as tc

def run():

    # check env.
    task_exec(tc.execute_basic_sdt_command)
    task_exec(tc.execute_basic_sdp_command)
    task_exec(tc.check_sdt_version)
    task_exec(tc.check_sdp_version)

    task_exec(tc.pause)

    # stop daemons
    task_exec(tc.stop_sdt)
    task_exec(tc.stop_sdp)
    task_exec(tc.stop_sdw)

    task_exec(tc.reset_all)
    task_exec(install_CMIP5)
    TODO

    task_exec(tc.reset_all)
    task_exec(install_CORDEX)
    TODO

    task_exec(tc.reset_all)
    task_exec(install_CMIP5)
    task_exec(trigger_CDF)

    # discovery
    task_exec(install_CMIP5)
    task_exec(check_CMIP5_installation_result)
    task_exec(install_CORDEX)
    task_exec(check_CORDEX_installation_result)

    # download
    task_exec(tc.start_sdt)
    time.sleep(300) # give some time for the file to be downloaded
    task_exec(check_download_result)

    # pexec
    task_exec(trigger_CDF)
    task_exec(check_CDF_trigger_result)

    # transfer events from SDT to SDP
    task_exec(tc.start_sdp)
    time.sleep(50) # give some time for pp events to be transfered from SDT to SDP
    task_exec(check_pp_events_transfer_result)

    # start pp pipelines
    task_exec(start_pp_pipelines)
    task_exec(check_pp_pipelines_result)

    print 'Test complete successfully !'

@task
def install_CMIP5():
    fabric_run('sudo synda install -s 20160503_test_CMIP5.txt')

@task
def install_CORDEX():
    fabric_run('sudo synda install -s 20160503_test_CORDEX.txt')

@task
def trigger_CDF():
    fabric_run('sudo synda pexec cdf -s 20160503_test_CMIP5.txt')

@task
def start_pp_pipelines():
    fabric_run('synda_wo -x start')
    fabric_run('test -f /tmp/foobar')

@task
def fake():
    fabric_run('test ! -f /srv/synda/sdt/data/cmip5/output1/MPI-M/MPI-ESM-LR/decadal1995/mon/land/Lmon/r2i1p1/v20120529/baresoilFrac/baresoilFrac_Lmon_MPI-ESM-LR_decadal1995_r2i1p1_199601-200512.nc')

# init.

reset_script='./resource/reset.sh'
scripts_pp='./resource/scripts_pp'

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    run()
