def file_stats(filename):
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()

    lines = text.splitlines()
    words = text.split()
    characters = len(text)

    return {
        "lines": len(lines),
        "words": len(words),
        "characters": characters
    }


stats = file_stats("example.txt")

print(stats
                )
