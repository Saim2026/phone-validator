# 🌍 Global Phone Number Validator

A simple Python script that identifies the country of a phone number (e.g. `+971` or `00971`)  
and validates whether the number is in a correct format using Google’s `libphonenumber`.

---

## 🚀 Features

- Detects country from international dialing code (`+` or `00` prefix)
- Validates phone number format per country rules
- Supports all countries worldwide
- Uses [phonenumbers](https://pypi.org/project/phonenumbers/) and [pycountry](https://pypi.org/project/pycountry/)

---

## 🧩 Example Usage

```bash
$ python phone_validator.py
Number: +971 50 123 4567
This code is from: United Arab Emirates (+971)
✅ This is a valid phone number format.

OR 

``` python
$ python phone_validator.py

Number: +91 123 123 1236 2546
This code is from: India (+91)
❌ Invalid phone number format for this country.

