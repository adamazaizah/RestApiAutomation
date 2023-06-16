import datetime
import os
import pytest

from utils import helper


@pytest.hookimpl(trylast=True)
def pytest_sessionfinish(session, exitstatus):
    report_file = "../report.html"
    if not os.path.isfile(report_file):
        return
    config = helper.read_config()
    if not config:
        return
    REPORTS = config["REPORTS"]
    html_report = REPORTS['html_report']

    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    new_report_file = f"report_{current_date}.html"
    os.rename(report_file, f'{html_report}//{new_report_file}')