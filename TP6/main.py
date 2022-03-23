import sys

nb_notes = 0
seq_len = 0
freq = []
freq_raw = []
seq = []
eq_multiplier = 0
total_notes_played = 0
notes_played = []

# Inequality =
# NbNotes * raw freq * eq_multiplier - eq_multiplier <
# eq_multiplayer < NbNotes * raw freq * eq_multiplier + eq_multiplier

# IMPORTANT : ARRAY STARTS AT 0 BUT NOT AT 1


def compute_seq():
    global notes_played
    global seq_len
    notes_played = [0] * nb_notes
    for n in seq:
        notes_played[n-1] += 1


def note_possible(i):
    global nb_notes
    global seq_len
    global freq
    global freq_raw
    global seq
    global eq_multiplier
    global total_notes_played
    global notes_played
    if (notes_played[i] + 1) * eq_multiplier < (total_notes_played + 1) * eq_multiplier * freq_raw[i] + eq_multiplier:
        for j in range(0, nb_notes):
            if j == i:
                continue
            if (total_notes_played + 1) * eq_multiplier * freq_raw[i] + eq_multiplier < notes_played[i] * eq_multiplier:
                return False
        return True
    return False


def notes_possible():
    global nb_notes
    global seq_len
    global freq
    global freq_raw
    global seq
    global eq_multiplier
    global total_notes_played
    global notes_played
    res = []
    for i in range(0, nb_notes):
        if (note_possible(i)):
            res.append(i)
    return res


def best_note():
    global nb_notes
    global seq_len
    global freq
    global freq_raw
    global seq
    global eq_multiplier
    global total_notes_played
    global notes_played
    max = -1
    max_index = -1
    for i in range(0, nb_notes):
        if (notes_played[i] + 1) * eq_multiplier < (total_notes_played + 1) * eq_multiplier * freq_raw[i] + eq_multiplier:
            for j in range(0, nb_notes):
                if j == i:
                    continue

                cur = notes_played[j] * eq_multiplier - (
                    (total_notes_played + 1) * eq_multiplier * freq_raw[j] - eq_multiplier)
                print("cur: " + str(cur))
                if cur < 0:
                    print("cur < 0")
                    break
                if cur > max:
                    max = cur
                    max_index = j
    return max_index


def parse():
    global nb_notes
    global seq_len
    global freq
    global freq_raw
    global seq
    global eq_multiplier
    global total_notes_played
    global notes_played
    with open("ex1.in", "r") as f:
        data = f.read()
        data = data.split("\n")
        nb_notes, seq_len = [int(x) for x in data[0].split(" ")]
        freq_raw = [int(x) for x in data[1].split(" ")]
        eq_multiplier = sum(freq_raw)
        for i in range(0, len(freq_raw)):
            freq.append(freq_raw[i] / eq_multiplier)

        seq = [int(x) for x in data[2].split(" ")]

        compute_seq()

        total_notes_played = seq_len

        print("nb_notes: " + str(nb_notes))
        print("seq_len: " + str(seq_len))
        print("freq raw: " + str(freq_raw))
        print("freq: " + str(freq))
        print("seq: " + str(seq))
        print("eq multiplier: " + str(eq_multiplier))
        print("notes played: " + str(notes_played))
        f.close()


def solve():
    global nb_notes
    global seq_len
    global freq
    global freq_raw
    global seq
    global eq_multiplier
    global total_notes_played
    global notes_played

    notes = notes_possible()
    print("notes_possible: " + str(notes))
    return

    best_note_index = best_note()
    while(best_note_index != -1):
        best_note_readable = (best_note_index + 1)
        print("Best note is : " + str(best_note_readable))
        notes_played[best_note_index] += 1
        total_notes_played += 1
        seq.append(best_note_readable)
        best_note_index = best_note()


def main():
    parse()
    solve()


if __name__ == "__main__":
    main()
