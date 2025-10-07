import re
import phonenumbers
from phonenumbers.phonenumberutil import region_code_for_country_code


def main():
    number = input("Number: ")

    # Match +971 or 00971 etc., followed by digits (spaces or dashes optional)
    pattern = r"^(?:\+|00)(?P<country_code>\d{1,3})[\s-]?\d+"

    match = re.search(pattern, number)
    if not match:
        print("Invalid number format (missing country code prefix)")
        return

    code_str = match.group("country_code")
    try:
        code_int = int(code_str)
        region = region_code_for_country_code(code_int)

        if not region:
            print("Unknown country code")
            return

        parsed = phonenumbers.parse(number, None)

        if phonenumbers.is_valid_number(parsed):
            country = region_name(region)
            print(f"This code is from: {country} (+{code_str})")
            print("✅ This is a valid phone number format.")
        else:
            print(f"This code is from: {region_name(region)} (+{code_str})")
            print("❌ Invalid phone number format for this country.")

    except Exception:
        print("Invalid or unrecognized number.")


def region_name(region):
    """Return full country name from ISO 2-letter region code."""
    import pycountry
    try:
        country = pycountry.countries.get(alpha_2=region)
        return country.name if country else region
    except Exception:
        return region


if __name__ == "__main__":
    main()
