all_card_type = "♥♠♣♦"
all_card_text = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]

for t in all_card_type:
    # print(t)
    for t2 in all_card_text:
        # print(t2,end='')  #52个数据
        ca = [t,t2]
        # print(ca)   #52个列表，4个花色各13个

#['♥', 'A']
# ['♥', 'K']
# ['♥', 'Q']
# ['♥', 'J']
# ['♥', '10']
#。。。。。

for t3 in all_card_text:
    # print(t3,end='')
    for t4 in all_card_type:
        # print(t4,end='')
        ca2 = [t3,t4]
        # print(ca2)    #52个列表，13个值各四个花色

#['A', '♥']
# ['A', '♠']
# ['A', '♣']
# ['A', '♦']
#....