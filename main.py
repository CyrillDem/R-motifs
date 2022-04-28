import regex
import re



def find_complex_motifs(string):
    complex_pattern = r"(R([A-Z]{0,2}R){2,})"
    motifs = []
    for match in re.finditer(complex_pattern, string):
        motifs.append([match.span(), match.group()])
    return motifs
    # complex_motifs = re.findall(complex_pattern, string)
    # return [groups[0] for groups in complex_motifs]


def overlap(a, b):
    return a[1] >= b[0] and a[0] <= b[1]


def count_R(string):
    R_number = string.count('R')
    return R_number


def find_all_motifs(string):
    found = []
    for i in range(3):
        pattern = r"R[A-Z]{" + str(i) + r"}R"
        for match in regex.finditer(pattern, string, overlapped=True):
            found.append([match.span(), match.group()])
        # found += regex.findall(pattern, string, overlapped=True)
    return found
    # print("Substrings: ", len(found))
    # print(found)


def main(string):
    message = ""
    counter = 1
    complex_motifs = find_complex_motifs(string)
    message += f'{string}, R: {count_R(string)}, TOTAL: {len(string)}\n\n'
    for item in find_all_motifs(string):
        message += f"Motif {counter}: {item[1]}, pos: ({item[0][0]+1}, {item[0][1]+1}), length: {len(item[1])}, R: {count_R(item[1])}"
        for complex_motif in complex_motifs:
            if overlap(complex_motif[0], item[0]):
                length = complex_motif[0][1] - complex_motif[0][0]
                message += f" | Substring of a COMPLEX motif {complex_motif[1]} (Pos: ({complex_motif[0][0]+1}, {complex_motif[0][1]+1}), Length: {length}, R: {count_R(complex_motif[1])})"
                break
        message += '\n'
        # if item[0]
        # print(f"Substring {counter}: {found[counter-1]}, Amino Acids: {len(found[counter-1])}, R: {found[counter-1].count('R')} ")
        counter += 1
    return message


with open("input.txt", 'r') as inp:
    lines = inp.readlines()
    with open("output.txt", 'w+') as output:
        for line in lines:
            string = line.strip()
            protein, seq = string.split()
            message = main(seq)
            output.write(f"{protein} - {message}")
            output.write('============================\n')

        
