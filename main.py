
def ispalindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

def main():
    mots = [
        "radar", "kayak", "level", "rotor", "civique", "deifie",
        "bonjour", "python", "été", "ressasser"
    ]
    for s in mots:
        print(f"{s} : {ispalindrome(s)}")


if __name__ == "__main__":
    main()
