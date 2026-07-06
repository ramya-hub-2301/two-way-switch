import pytest
from app.twowayswitch import TwoWaySwitch


class TestTwoWaySwitch:

    @pytest.mark.tcid("TC-001")
    @pytest.mark.smoke
    def test_initial_state(self, switch):
        assert switch.switch1 == 0
        assert switch.switch2 == 0
        assert switch.light_on is True

    @pytest.mark.tcid("TC-002")
    @pytest.mark.smoke
    def test_toggle_switch1_changes_light(self, switch):
        switch.toggle_switch1()
        assert switch.light_on is False

    @pytest.mark.tcid("TC-003")
    @pytest.mark.smoke
    def test_toggle_switch2_changes_light(self, switch):
        switch.toggle_switch2()
        assert switch.light_on is False

    @pytest.mark.tcid("TC-004")
    @pytest.mark.smoke
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