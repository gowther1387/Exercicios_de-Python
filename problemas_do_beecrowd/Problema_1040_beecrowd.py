nota_aluno1 = float(input("qual foi a primeira nota?")) 
nota_aluno2 = float(input("qual foi a segunda nota?"))
nota_aluno3 = float(input("qual foi a terceira nota?"))
nota_aluno4 = float(input("qual foi a quarta nota?"))


media = round((((nota_aluno1 * 2) + (nota_aluno2 * 3) + (nota_aluno3 * 4) + (nota_aluno4 * 1))/10), 2)


if media < 5.0 : 
    print("aluno reprovado")
    print("media final:" , media)

elif  5 <= media <= 6.9 :
    print("Aluno em exame.")
    nota_exame = float(input("qual a nota do exame?"))
    media_exame = round(((media + nota_exame ) / 2), 2)
    print("aprovado") 
    print("Media:" , media)

    if(media_exame >=4.9) :
        print("aluno reprovado")
        print("media final:" , media_exame)
    else : 
        print("aluno reprovado")
        print("media final:" , media_exame)         

else :
    print("media:", media)
    print("aluno aprovado")