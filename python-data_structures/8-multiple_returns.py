def multiple_returns(sentence):
    if len(sentence) == 0:
        return (0, None)
    return (len(sentence), sentence[0])
print(multiple_returns("Python"))
print(multiple_returns(""))
