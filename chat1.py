#讀取檔案
def read_file(filename):
    lines = []
    with open(filename, "r", encoding="utf-8-sig") as f:
        for line in f:
            lines.append(line.strip())
    return lines

#計數
def convert(file):
    allen_word = 0
    allen_sticker = 0
    allen_image = 0
    viki_word = 0
    viki_sticker = 0
    viki_image = 0
    for line in file:
        s = line.split(" ")
        time = s[0] 
        name = s[1]
        if name == "Allen":
            if s[2] == "貼圖":
                allen_sticker += 1
            elif s[2] == "圖片":
                allen_image += 1
            else:
                for w in s[2:]:
                    allen_word += len(w)
        elif name == "Viki":
            if s[2] == "貼圖":
                viki_sticker += 1
            elif s[2] == "圖片":
                viki_image += 1
            else:
                for w in s[2:]:
                    viki_word += len(w)
    print("Allen說了", allen_word,"個字,", "傳了", allen_sticker, "個貼圖以及", allen_image, "張圖片")
    print("Viki說了", viki_word,"個字,", "傳了", viki_sticker, "個貼圖以及", viki_image, "張圖片")

#寫入新檔案
def write_file(filename, file):
    with open(filename, "w", encoding="utf-8") as f:
        for line in file:
            f.write(line + "\n")
#encoding= utf-8, utf-8-sig, cp950

def main():
    lines = read_file("LINE-Viki.txt") # 3 steps
    lines = convert(lines) # 3 steps
    #write_file("output.txt", lines) # 2 steps


main()