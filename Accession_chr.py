#!/user/bin/env/python3

#refGene.txtの読み込み
with open("refGene.txt","r")as file:
    with open("Accession_chr.txt", "w")as output:
   

    #1行ずつ読み込む
        for line in file:

        # columnsに要素を取り出す際の処理を明示
            columns = line.strip().split("\t")         # 空白を除去してタブ区切り

        # 必要な要素をカラムに入れていく
            Accession = columns[1]
            chr = columns[2]
            output.write("{}\t{}\n".format(Accession, chr))
