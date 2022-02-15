'''
1-Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir. 
Örnek olarak:
    input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
    output: [1,'a','cat',2,3,'dog',4,5]
'''
emptyList = []
    
def flat(l):
    for i in l:
        if type(i) == list:
            flat(i)
        else:
            emptyList.append(i)

flat([[1,'a',['cat'],2],[[[3]],'dog'],4,5])
print(emptyList)

'''
2-Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün. 
Örnek olarak:
    input: [[1, 2], [3, 4], [5, 6, 7]]
    output: [[[7, 6, 5], [4, 3], [2, 1]]
'''
x = [[11, 22], [33, 44], [5, 6]]
empty = []

def tersCevir(l):
    for i in l:
        if type(i)==list:
            empty.append(list(reversed(i)))

tersCevir([[11, 22], [33, 44], [5, 6]])
print(list(reversed(empty)))
