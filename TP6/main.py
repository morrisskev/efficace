import sys

nb_notes = 0
seq_len = 0
freq = []
freq_raw = []
seq = []
eq_multiplier = 0

# Inequality =
# NbNotes * raw freq * eq_multiplier - eq_multiplier <
# eq_multiplayer < NbNotes * raw freq * eq_multiplier + eq_multiplier

# IMPORTANT : ARRAY STARTS AT 0 BUT NOT AT 1


def note_possible(note: int) -> bool:

    pass


def best_note():
    pass


def parse():
    with open("ex1.in", "r") as f:
        data = f.read()
        data = data.split("\n")
        nb_notes, seq_len = data[0].split(" ")
        freq_raw = [int(x) for x in data[1].split(" ")]
        eq_multiplier = sum(freq_raw)
        for i in range(0, len(freq_raw)):
            freq.append(freq_raw[i] / eq_multiplier)

        seq = [int(x) for x in data[2].split(" ")]

        print("nb_notes: " + str(nb_notes))
        print("seq_len: " + str(seq_len))
        print("freq raw: " + str(freq_raw))
        print("freq: " + str(freq))
        print("seq: " + str(seq))
        print("eq multiplier: " + str(eq_multiplier))
        f.close()


def solve():

    pass


def main():
    parse()
    solve()


if __name__ == "__main__":
    main()
