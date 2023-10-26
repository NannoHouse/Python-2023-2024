def find_shortest_and_longest_words(words, letter):
    words = [word for word in words if word.startswith(letter)]
    minn = min(words,key=len)
    maxx = max(words,key=len)
    return (minn,maxx)

assert find_shortest_and_longest_words(["abracadabra", "banana", "kugelschreiber", "ant", "almost", "thisshouldbeaverylongword"], "a") == ("ant", "abracadabra")
assert find_shortest_and_longest_words(["abracadabra", "banana", "kugelschreiber", "ant", "almost", "thisshouldbeaverylongword"], "b") == ("banana", "banana")
