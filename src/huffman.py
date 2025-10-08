def char_count(text):
    count_dict = {}
    for character in set(text):
        count_dict[character] = text.count(character)
    count = sorted(count_dict.items(), key=lambda item: item[1], reverse=True)
    return dict(count)

