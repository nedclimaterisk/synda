#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-

##################################
#  @program        synda
#  @description    climate models data transfer program
#  @copyright      Copyright “(c)2009 Centre National de la Recherche Scientifique CNRS. 
#                             All Rights Reserved”
#  @license        CeCILL (https://raw.githubusercontent.com/Prodiguer/synda/master/sdt/doc/LICENSE)
##################################

"""This module contains 'upgrade' routines."""

import sdsearch
import sdinstall
import sdexception
import sdlog
from sdtools import print_stderr

def run(selections,args):

    # BEWARE: tricky statement
    #
    # 'upgrade' is a multi-selections 'subcommand' which do the same as the
    # mono-selection 'install' subcommand, but for many selections.  What we do
    # here is replace 'upgrade' subcommand with 'install' subcommand, so that we can,
    # now that we are in 'upgrade' func/context, 
    # come back to the existing mono-selection func,
    # for each selection, with 'install' subcommand.
    #
    args.subcommand='install'

    # force non-interactive mode
    args.yes=True

    for selection in selections:
        try:
            sdlog.info("SDUPGRAD-003","Process %s.."%selection.filename,stderr=True)
            install(args,selection)
        except sdexception.IncorrectParameterException,e:
            sdlog.info("SDUPGRAD-004","Error occurs while processing %s (%s)"%(selection.filename,str(e)),stderr=True)

def install(args,selection):

    # TODO: maybe force type=file here, in case the selection file have 'type=Dataset'

    if not args.dry_run:
        sdlog.info("SDUPGRAD-001","Retrieve metadata from ESGF..")
        metadata=sdsearch.run(selection=selection)
        sdlog.info("SDUPGRAD-002","Install files..")
        (status,newly_installed_files_count)=sdinstall.run(args,metadata)