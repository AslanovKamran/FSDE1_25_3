def make_length_validator (min_length, max_length):
    def validator(str):
        return min_length <= len(str) <= max_length
    return validator

validator = make_length_validator(3,6)

print(validator("hi"))
print(validator("hello"))
print(validator("salam aleykum"))

