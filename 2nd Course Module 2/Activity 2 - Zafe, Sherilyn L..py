groceries = {"chicken": 8, "apples": 6, "cucumber": 3, "milk": 2, "oranges": 4}
remove = groceries.pop("oranges")
print(groceries)

speaker = {"Sir Rafael": 54, "Ms. Joan": 33, "Ms. Dana": 67}
name = speaker.keys()
print(name)

tryout_result = {"Carl": "passed", "Quentin": "failed",
                 "John Y.": "passed", "Peter": "failed",
                 "Max T.": "passed", "Joseph": "passed",
                 "Jone": "failed", "Jorge": "failed",
                 "George": "passed", "Ben": "passed",
                 "Jerome": "passed", "Rick": "failed",
                 "Max G.": "failed", "John P.": "failed",
                 "Vince": "passed"}
print(tryout_result.get("Jorge"))