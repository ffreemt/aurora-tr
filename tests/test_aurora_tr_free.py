"""
Test aurora_tr selector="free".

run `rye run pytest`
"""
import dotenv
import platform
import pytest
import stamina
from aurora_tr import aurora_tr


@pytest.fixture(autouse=True, scope="session")
def deactivate_retries():
    stamina.set_active(False)


def test_aurora_tr_free_empty_input():
    """Test aurora_tr empty input."""
    _ = aurora_tr("  ", selector="free")
    assert _.get("translation").startswith(" ")


def test_aurora_tr_free_url():
    """Test aurora_tr url."""
    _ = aurora_tr("https://www.baidu.com", selector="free")
    assert _.get("translation").startswith("http")


def test_aurora_tr_free_dw_text():
    """Test aurora_tr digital twin text."""
    text = "A digital twin is a virtual model or representation of an object, component, or system that can be updated through real-time data via sensors, either within the object itself or incorporated into the manufacturing process."

    # api_key = dotenv.dotenv_values().get("OPENAI_API_KEY_UUCI")
    # _ = aurora_tr(text, selector="free", api_key=api_key)

    # may need to turn this off when the free quota runs out
    if True:
        _ = aurora_tr(text, selector="free")
        _ = _.get("translation")
        assert "数字" in _ or "实时" in _ or "更新" in _
