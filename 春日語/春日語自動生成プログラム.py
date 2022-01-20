# -----------------------------------------+
# Kasuga_language                          |
# Gak Roppongi                             |
# Last Modified: 6/15, 2021                |
# -----------------------------------------+
## ---------------------------------------------------------------------------------------------------------------------
def translator(sentence):
    input_file = ("春日語一覧.csv")
    file = open(input_file, "r")
    file.readline()

    for each_line in file:
        each_line = each_line.strip()
        row = each_line.split(",")

        if row[0] in sentence:
            sentence.replace(row[0])
            print(sentence)



def main():
    sentence = input("翻訳したい日本語の文章を入力してください: ")
    translator(sentence)

main()