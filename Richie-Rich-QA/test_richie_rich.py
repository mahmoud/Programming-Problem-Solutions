
import a_richie_rich as arr


def _a_helper():
    return False


def test_pass():
    assert True


def test_basic_comp():
    res_lines = arr.comp('4', '1', '3943')

    res = res_lines[0]

    assert res == '3993'
