#讀取檔案
def read_file(filename):
    lines = []
    with open(filename, "r", encoding="utf-8-sig") as f:
        for line in f:
            lines.append(line.strip())
    return lines
#轉換排版
def convert(file):
    new = []
    person = None
    for line in file:
        if line == "Allen":
            person = "Allen"
            continue
        elif line == "Viki":
            person = "Viki"
            continue
        if person:
            new.append(person + ":" + line)
    return new
#寫入新檔案
def write_file(filename, file):
    with open(filename, "w", encoding="utf-8") as f:
        for line in file:
            f.write(line + "\n")
#encoding= utf-8, utf-8-sig, cp950

def main():
    lines = read_file("input.txt") # 3 steps
    lines = convert(lines) # 3 steps
    write_file("output.txt", lines) # 2 steps

main()





