import pytest
from app.twowayswitch import TwoWaySwitch

@pytest.fixture
def switch():
    """Provides a fresh TwoWaySwitch instance for every test."""
    return TwoWaySwitch()


class TestTwoWaySwitch:

    def test_initial_state(self, switch):
        assert switch.switch1 == 0
        assert switch.switch2 == 0
        assert switch.light_on is True

    def test_toggle_switch1_changes_light(self, switch):
        switch.toggle_switch1()
        assert switch.light_on is False

    def test_toggle_switch2_changes_light(self, switch):
        switch.toggle_switch2()
        assert switch.light_on is False

    @pytest.mark.parametrize("s1,s2,expected", [
        (0, 0, True),
        (1, 1, True),
        (0, 1, False),
        (1, 0, False),
    ])
    def test_light_state_truth_table(self, switch, s1, s2, expected):
        switch.switch1 = s1
        switch.switch2 = s2
        switch.update_light()
        assert switch.light_on is expected