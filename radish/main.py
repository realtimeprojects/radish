#!/usr/bin/python
# -*- coding: utf-8 -*-

import radish

import os
import sys
import time
import optparse


def xunit_file_callback(option, opt_str, value, parser):
    value = radish.ReportWriter.REPORT_FILENAME
    if parser.rargs:
        value = parser.rargs[0]
        del parser.rargs[0]
    setattr(parser.values, option.dest, value)


def main():
    parser = optparse.OptionParser(
        description="radish is a smart 'Test-Driven Developement'-Tool",
        epilog="(C) Copyright 2012 by Timo Furrer <tuxtimo@gmail.com>"
    )
    parser.add_option(
        "-b", "--basedir",
        dest="basedir",
        default=os.path.join(os.getcwd(), "radish"),
        help="The basedir is used to locate the steps.py and terrain.py"
    )
    parser.add_option(
        "-a", "--abort-fail",
        dest="abort_fail",
        action="store_true",
        help="If one feature file fails this option will stop the execution"
    )
    parser.add_option(
        "-v", "--verbosity",
        dest="verbosity",
        default=4,
        help="The verbosity level for the output"
    )
    parser.add_option(
        "-m", "--marker",
        dest="marker",
        default=int(time.time()),
        help="A specific marker for the step loggings"
    )
    parser.add_option(
        "-d", "--dry-run",
        dest="dry_run",
        action="store_true",
        help="Executes a dry run to validate steps"
    )
    parser.add_option(
        "-x", "--xunit-file",
        dest="xunit_file",
        action="callback",
        default=None,
        callback=xunit_file_callback,
        help="Location where to write to JUnit xml report file"
    )

    options, args = parser.parse_args()

    exitCode = 0
    try:
        # initialize config object
        cf = radish.Config()
        cf.SetBasedir(radish.FileSystemHelper.expand(options.basedir))
        cf.feature_files = args
        cf.abort_fail = options.abort_fail
        cf.verbosity = options.verbosity
        cf.marker = options.marker
        cf.dry_run = options.dry_run
        cf.xunit_file = options.xunit_file

        # parse feature files
        fp = radish.FeatureParser()
        fp.parse()

        # load terrain and steps
        loader = radish.Loader(fp.Features)
        loader.load()

        # run the features
        runner = radish.Runner(fp.Features)
        endResult = runner.run()

        # report writer
        if cf.xunit_file:
            rw = radish.ReportWriter(endResult)
            rw.write()

        exitCode = 0 if endResult.all_passed else 1
    except radish.RadishError, e:
        print("%s %s" % (radish.colorful.bold_red("radish error:"), e))
        exitCode = 2

    sys.exit(exitCode)

if __name__ == "__main__":
    main()
