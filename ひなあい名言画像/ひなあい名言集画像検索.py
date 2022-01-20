#　ひなあい名言集画像を検索してリターン
from PIL import Image
import numpy as np

# 元となる画像の読み込み
def dictionary(dict,choice):
    if choice in dict:
        img = Image.open(dict[choice])
        img.show()
        main()

    if choice not in dict:
        print("タイプミスの可能性があります")
        print("もう一度入力してみてください")
        print(" ")
        main()

def main():
    print("以下のリストから表示する画像の番号を選んでください：")
    print(" ")
    print("1：ありがとな（春日）")
    print("2：いいね（KAWADAさん）")
    print("3：お前許さないからな！（若様）")
    print("4：お客様は常識を知っていますか？（斎藤京子）")
    print("5：ケチ！（ささく）")
    print("6：しゃああああ！（若様）")
    print("7：それは持ってるで！（まなふぃー）")
    print("8：なきゃここに座ってませんよ！（春日）")
    print("9：はい？（KAWADAさん）")
    print("10：やるよ！（春日）")
    print("11：元気田支店長（ひなの）")
    print("12：公式ど変態（べみほ）")
    print("13：君がNo.1！（井口真緒）")
    print("14：払うよ！（春日）")
    print("15：聞かせてやるよ〜（若様）")
    print(" ")
    print("終了するときは「done」をタイプしてください")
    print(" ")

    choice = int(input(print("どの画像を出しますか？ 番号を選んでください:")))
    #image(choice)

    dict = {1:"ありがとなって思っちゃう.jpg", 2:"いいね.jpg", 3:"お前許さないからな！.jpg", 4:"お客様は常識を知っていますか？.jpg",
            5:"ケチ！.jpg", 6:"シャアああ.jpg", 7:"それは盛ってるで！.jpg", 8:"なきゃここに座ってませんよ.jpg", 9:"はい？.jpg",
            10:"やるよ！.jpg", 11:"元気田店長.jpg", 12:"公式ど変態.jpg", 13:"君がNo.1.jpg",
            14:"払うよ！.jpg", 15:"聞かせてやるよ〜.jpg"}
    dictionary(dict,choice)

main()

# ありがとなって思っちゃう.jpg
# いいね.jpg
# お前許さないからな！.jpg
# お客様は常識を知っていますか？.jpg
# ケチ！.jpg
# シャアああ.jpg
# それは盛ってるで！.jpg
# なきゃここに座ってませんよ.jpg
# はい？.jpg
# やるよ！.jpg
# 元気田店長.jpg
# 公式ど変態.jpg
# 君がNo.1.jpg
# 払うよ！.jpg
# 聞かせてやるよ〜.jpg
