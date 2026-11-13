DIGITS = "0123456789"


def format_player_name(name):
    """
    Title-cases a player name and cuts it to 10 characters for the scoreboard.
    Returns an empty string for non-string input (None, numbers, etc.).
    """
    if not isinstance(name, str):
        return ""
    return name.strip().title()[:10]


def parse_frame(text):
    """
    Converts frame notation into pins knocked down: 'X' -> (10, 0),
    '7/' -> (7, 3), '45' -> (4, 5).
    Returns None for anything that is not a valid frame.
    """
    if not isinstance(text, str):
        return None
    text = text.strip().upper()
    if text == 'X':
        return 10, 0
    if len(text) != 2:
        return None
    if text[0] not in DIGITS:
        return None
    first = int(text[0])
    if text[1] == '/':
        return first, 10 - first
    if text[1] not in DIGITS:
        return None
    second = int(text[1])
    if first + second > 10:
        return None
    return first, second


def parse_scoreboard(text):
    """
    Parses 'Asha:150,Ravi:132' into a {name: score} dictionary.
    Malformed entries (missing colon, empty name, non-numeric score,
    score outside 0-300) are skipped. Non-string input gives an empty dict.
    """
    scores = {}
    if not isinstance(text, str):
        return scores
    for entry in text.split(','):
        parts = entry.split(':')
        if len(parts) != 2:
            continue
        name = parts[0].strip()
        if not name:
            continue
        try:
            score = int(parts[1].strip())
        except ValueError:
            continue
        if score < 0 or score > 300:
            continue
        scores[name] = score
    return scores


def main():
    print("==== Running format_player_name ====")
    value = input("Enter a player name for the scoreboard: ")
    print("Scoreboard name:", format_player_name(value))

    print("\n==== Running parse_frame ====")
    value = input("Enter a frame as X (strike), 7/ (spare) or two digits (e.g. 45): ")
    print("Pins (first roll, second roll):", parse_frame(value))

    print("\n==== Running parse_scoreboard ====")
    value = input("Enter scores as NAME:SCORE separated by commas (e.g. Asha:150,Ravi:132): ")
    print("Scoreboard:", parse_scoreboard(value))

if __name__ == "__main__":
    main()

