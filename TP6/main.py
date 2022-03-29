import sys

nb_notes = 0
seq_len = 0
freq = []
freq_raw = []
seq = []
eq_multiplier = 0
total_notes_played = 0
notes_played = []
file_name = ""

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


def parse(path):
    global nb_notes
    global seq_len
    global freq
    global freq_raw
    global seq
    global eq_multiplier
    global total_notes_played
    global notes_played
    with open(path, "r") as f:
        data = f.read()
        data = data.split("\n")
        nb_notes, seq_len = [int(x) for x in data[0].split(" ")]
        freq_raw = [int(x) for x in data[1].split(" ")]
        eq_multiplier = sum(freq_raw)
        for i in range(0, len(freq_raw)):
            freq.append(freq_raw[i] / eq_multiplier)

        seq = [] if data[2] == "" else [int(x) for x in data[2].split(" ")]

        compute_seq()

        total_notes_played = seq_len

        f.close()


def testonleft(notes_played, total_notes_played, freq, nb_notes, i):
    for j in range(0, nb_notes):
        if not j == i and (not (total_notes_played+1)*freq[j]-1 < notes_played[j]):
            return False
    return True


def bestNote(notes_played, total_notes_played, freq, nb_notes):
    min = 10000
    indice = -1
    for i in range(0, nb_notes):
        r = notes_played[i]-(total_notes_played*freq[i]-1)
        if r > 0 and min > r:
            if (notes_played[i]+1 < (total_notes_played+1)*freq[i]+1) and testonleft(notes_played, total_notes_played, freq, nb_notes, i):
                min = r
                indice = i
    return indice


def solve():
    global nb_notes
    global seq_len
    global freq
    global freq_raw
    global seq
    global eq_multiplier
    global total_notes_played
    global notes_played
    global file_name

    compt = 0
    sequence_add = []
    while(compt < 100):
        indice = bestNote(notes_played, total_notes_played, freq, nb_notes)
        if(indice == -1):
            break
        else:
            notes_played[indice] += 1
            total_notes_played += 1
            compt = compt+1
            sequence_add.append(indice+1)

    if (compt >= 100):
        print("resultat="+str(compt))
        print("infini")
    else:
        print("resultat="+str(compt))
    file_name = file_name.replace(".in", ".out")
    print("file_name="+file_name)
    with open(file_name, "w") as f:
        f.write(str(compt)+"\n")
        f.write(" ".join(str(x) for x in sequence_add))


def main():
    global nb_notes
    global seq_len
    global freq
    global freq_raw
    global seq
    global eq_multiplier
    global total_notes_played
    global notes_played
    global file_name
    for i in range(3, 84):
        path = "0" + str(i) + ".in" if i < 10 else str(i) + ".in"
        print("TESTING FILE " + path)
        print("------------------")
        file_name = path
        parse(path)
        solve()
        nb_notes = 0
        seq_len = 0
        freq = []
        freq_raw = []
        seq = []
        eq_multiplier = 0
        total_notes_played = 0
        notes_played = []
        file_name = ""
        print("------------------\n")


if __name__ == "__main__":
    main()
