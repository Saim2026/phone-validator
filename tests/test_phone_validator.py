
import phonenumbers
from phone_validator import region_name

# Optional: `tests/test_phone_validator.py`


def test_region_name():
    assert region_name("US") == "United States"
    assert region_name("GB") == "United Kingdom"
