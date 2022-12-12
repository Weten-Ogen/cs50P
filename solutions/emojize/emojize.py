from emoji import emojize
def main():
    text = input("input a string ").strip()
    print(moji(text))

def moji(txt):
    txt = txt.lower()
    return emojize(f":{txt}:")









if __name__ == "__main__":
    main()