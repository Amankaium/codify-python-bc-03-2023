res = {i:i**2 for i in range(5)}
print(res)

profile = {
    "name": "Kaium",
    "age": 28,
    "code": "python",
    "kotlin": 0
}

boolean_profile = {key: bool(value) for key, value in profile.items()}
print(boolean_profile)
