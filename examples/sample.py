import searchClosest


def read_sample(filename):
    with open(filename) as document:
        dict = {}
        for line in document:
            if line.strip():  # non-empty line?
                key, value = line.split(";", 1)
                dict[key] = value.split(";",-1)
    document.close()
    return dict


def find_answer(word, dict):
    word = word.strip()
    word = word.lower()
    for key in dict:
        if word in dict[key]:
            return key
    else:
        ans = searchClosest.search_the_closest(word, r"E:\Програмування\fbchat\examples\nedovyb.txt")
        k = ""
        if ans != "Sorry, can You repeat, please?":
            k = find_answer(ans, dict)
            return k
        else:
            return ans
