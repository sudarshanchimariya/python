paragraph = "tar rat arc car elbow below state taste cider cried dusty got hurt my chin"

paraSplit = paragraph.split()
def findAnagram(paraSplit):
    dict = {}
    for word in paraSplit:
        key = ''.join(sorted(word))

        if key in dict.keys():
            dict[key].append(word)
        else:
            dict[key] = []
            dict[key].append(word)
        output = ""
        for key, value in dict.items():
            if len(value) > 1:
                output = output + ' '.join(value) + ' '

    return output


print(findAnagram(paraSplit))
