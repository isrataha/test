meme_dict = {
    "CRINGE" : "Garip ya da utandırıcı bir şey",
    "LOL" : "Komik bir şeye verilen cevap",
    "ROFL" : "bir şakaya karşılık cevap",
    "SHEESH" : "onaylamamak",
    "CREEPY" : "korkunç",
    "AGRRO" : "agrasifleşmek/sinirlenmek"
}

word = input("Anlamadığınız kelime varsa yazınız: ").upper()

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("Bu kelimeyi bilmiyorum")
