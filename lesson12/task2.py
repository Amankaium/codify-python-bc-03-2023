def show_info(**kwargs):
    if "name" in kwargs:
        print(kwargs["name"])
    if "code" in kwargs:
        print(kwargs["code"])
    # v1
    if "mark_1" in kwargs:
        print(kwargs["mark_1"], end=" ")
    if "mark_2" in kwargs:
        print(kwargs["mark_2"])
    # v2
    if "mark_1" in kwargs and "mark_2" in kwargs:
        print(kwargs["mark_1"], kwargs["mark_2"])

show_info(name="Kaium", code="python", mark_1=77, mark_2=88)
# Kaium
# python
# 77 88

