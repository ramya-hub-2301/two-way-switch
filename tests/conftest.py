import pytest


@pytest.fixture
def switch():
    from app.twowayswitch import TwoWaySwitch
    return TwoWaySwitch()


# ---- pytest-html: add Test Case ID and Tags columns ----

def pytest_html_results_table_header(cells):
    cells.insert(1, "<th>Test Case ID</th>")
    cells.insert(2, "<th>Tags</th>")


def pytest_html_results_table_row(report, cells):
    cells.insert(1, f"<td>{getattr(report, 'tcid', '')}</td>")
    cells.insert(2, f"<td>{getattr(report, 'tags', '')}</td>")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    tcid_marker = item.get_closest_marker("tcid")
    report.tcid = tcid_marker.args[0] if tcid_marker else ""

    tags = [m.name for m in item.iter_markers() if m.name not in ("tcid", "parametrize")]
    report.tags = ", ".join(tags)