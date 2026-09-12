import sys

if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    new_size: int = 0
    for arg in sys.argv[1:]:
        try:
            int(arg)
            new_size += 1
        except ValueError:
            continue

    new_list = [0] * new_size
    index = 0

    for arg in sys.argv[1:]:
        try:
            int(arg)
            new_list[index] = int(arg)
            index += 1
        except ValueError:
            print(f"Invalid parameter: '{arg}'")
            continue

    if new_size == 0:
        print(
            "No scores provided. Usage: python3 "
            "ft_score_analytics.py <score1> <score2> ..."
        )
    else:
        print(f"Scores processed: {new_list}")
        print(f"Total players: {len(new_list)}")
        print(f"Total score: {sum(new_list)}")
        print(f"Average score: {sum(new_list) / len(new_list)}")
        print(f"High score: {max(new_list)}")
        print(f"Low score: {min(new_list)}")
        print(f"Score range: {max(new_list) - min(new_list)}")
