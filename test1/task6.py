BAD_WORDS = [
    "fuck",
    "shit",
    "bullshit",
    "bastard",
    "bitch",
    "whore",
    "damn",
]


def censored(text):
    x=[]
    text = text.split()
    for i in text:
        if i.lower() in BAD_WORDS:
            i='*' * len(i)
        x.append(i)
    x = " ".join(x)
    return x

# Tests:
assert censored("this line should not be censored at all") == "this line should not be censored at all"
assert censored("fuck this bitch") == "**** this *****"
assert censored("This task is UTTER BULLshit") == "This task is UTTER ********", "be careful with the case!"
assert censored("") == ""