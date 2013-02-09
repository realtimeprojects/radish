# -*- coding: utf-8 -*-

import re
from datetime import datetime
from lxml import etree

from radish.config import Config


class ReportWriter(object):
    REPORT_FILENAME = "radishtests.xml"

    def __init__(self, endResult):
        self.endResult = endResult

    def generate(self):
        testsuite = etree.Element(
            "testsuite",
            name="radish",
            hostname="localhost",
            tests=str(self.endResult.total_steps),
            errors="0",
            failures=str(self.endResult.failed_steps),
            timestamp=datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
        )

        total_duration = 0

        for feature in self.endResult.Features:
            for scenario in feature.Scenarios:
                for step in scenario.Steps:
                    testcase = etree.Element(
                        "testcase",
                        classname="%s : %s" % (feature.Sentence, scenario.Sentence),
                        name=step.Sentence,
                        time=str(step.Duration)
                    )
                    if step.passed is False:
                        failure = etree.Element(
                            "failure",
                            type=step.fail_reason.Name,
                            message=self.stripAnsiText(step.fail_reason.Reason)
                        )
                        failure.text = etree.CDATA(self.stripAnsiText(step.fail_reason.Traceback))
                        testcase.append(failure)
                    testsuite.append(testcase)
                    total_duration += (step.Duration if step.Duration > 0 else 0)
        testsuite.attrib["time"] = str(total_duration)
        return etree.ElementTree(testsuite)

    def write(self):
        doc = self.generate()
        f = open(Config().xunit_file or ReportWriter.REPORT_FILENAME, "w")
        f.write(etree.tostring(doc, pretty_print=True, xml_declaration=True, encoding="utf-8"))
        f.close()

    def stripAnsiText(self, text):
        pattern = re.compile("(\\033\[\d+(?:;\d+)*m)")
        return pattern.sub("", text)
