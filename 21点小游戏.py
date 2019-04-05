import random
import sys
import time


class Card:
    """定义扑克牌类。每个对象代表一张扑克牌。
    """
    def __init__(self, card_type, card_text, card_value):
        """初始化方法。
        card_type : str
            牌的类型。（红桃，黑桃，梅花，方片）
        card_text : str
            牌面显示的文本。（A，K，Q，J）
        card_value : int
            牌面真实的点数。（如A为1点或11点。K为10点等）
        """
        self.card_type = card_type
        self.card_text = card_text
        self.card_value = card_value

# s = Card('♣','2','2')
# print(s.card_value)

class Role:
    """定义角色类，用来表示电脑（庄家）与我们用户（玩家）。"""
    def __init__(self):
        """初始化方法"""
        # 定义列表，用来保存当前角色手中的牌。初始牌为空。
        self.cards = []

    def show_card(self):
        """向控制台打印手中所有的牌。"""
        for card in self.cards:
            print(card.card_type, card.card_text, sep="", end="")
        # 打印当前角色手中所有牌之后，再进行一个换行。
        print()

    def get_value(self, min_or_max):
        """获得当前角色手中牌的点数。（分为最小值与最大值）。
        min_or_max : str，值为min或max。
            当值为min时，返回的是最小点数。即所有的A当成是1时的点数。（用来判断是否爆牌的情况。）
            当值为max时，返回在不爆牌的前提下，可表示的最大点数。此时A可能表示为11，也可能表示为1。

        value : int
            返回手中牌的点数。（最小点数或最大点数。）
        """
        # 总的点数
        sum2 = 0
        # 牌面中A的数量。（有几张A）
        A = 0
        for card in self.cards:
            # 累计相加牌面所有的点数
            sum2 += card.card_value
            #  累计A的数量
            if card.card_text == "A":
                A += 1
        if min_or_max == "max":
            # 逐渐减少A的数量，选择一个小于等于21点的最大值。
            for i in range(A):
                # 在总的点数上减去10，相当于将A当成1点看待。（减去几个10，就相当于
                # 是将几个A当成1点来看待。）
                value = sum2 - i * 10
                if value <= 21:
                    return value
        # 如果把所有的A都当成1，则最大值与最小值是相同的。
        return sum2 - A * 10

    def burst(self):
        """判断是否爆牌，是返回True，否则返回False。
        b : bool
            是否爆牌，爆牌返回True，否则返回False。
        """
        # 判断是否爆牌，只需要判断最小值是否大于21点即可。
        # print('ok')
        return self.get_value("min") > 21

# r = Role()
# # print(r)    #<__main__.Role object at 0x00000121FADCEB00>
# r.burst()
# r.get_value('min')
# r.show_card()

class CardManager:
    """扑克牌管理类。管理一整副扑克牌，并且能够进行发牌。"""
    def __init__(self):
        """初始化方法"""
        # 定义列表，用来保存一整副扑克牌（52张）
        self.cards = []
        # 定义所有牌的类型。
        all_card_type = "♥♠♣♦"
        # 定义所有牌面显示的文本
        all_card_text = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
        # 定义牌面文本对应的真实点数
        all_card_value = [11, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2]
        # 对牌面类型与牌面文本进行嵌套循环。
        for card_type in all_card_type:
            # print(card_type)
            for index, card_text in enumerate(all_card_text):
                # 创建Card类型的对象。（一张扑克牌）,调用Card扑克牌类方法
                card = Card(card_type, card_text, all_card_value[index])
                # 将创建好的card对象加入到整副扑克牌cards列表当中。
                self.cards.append(card)
        # 洗牌操作
        random.shuffle(self.cards)

    def send_card(self, role, num=1):
        """给电脑或者玩家发牌。
        role : Role
            电脑或玩家对象。
        num ： int
            发牌的张数。默认为1。
        """
        for i in range(num):
            card = self.cards.pop()  #发牌后，cards列表少一张牌card，玩家或电脑多一张牌card
            role.cards.append(card)

# cm = CardManager()
# print(cm.cards)
# print(len(cm.cards))  52张牌（52个列表）总共，打乱顺序
# for i in cm.cards:
#     print(i.card_text,end='')


# 创建扑克牌管理器类
cards = CardManager()
# 创建电脑角色对象
computer = Role()
# 创建玩家角色对象
player = Role()
# 初始时，给庄家发一张牌，给玩家发两张牌。
cards.send_card(computer)
cards.send_card(player, 2)
# 显示庄家与玩家手中牌。
computer.show_card()
player.show_card()
# 询问玩家是否要牌，要则继续发牌，否则停牌。
while True:
    # 询问玩家是否要牌，y：要牌，n：停牌。
    choice = input("是否再要一张牌？【y/n】")
    # 玩家选择要牌
    if choice == "y":
        # 向玩家发牌
        cards.send_card(player)
        # 发牌后，显示庄家与玩家手中的牌。
        computer.show_card()
        player.show_card()
        # 判断每次玩家要牌后，是否爆牌。如果爆牌，则玩家负。
        # 如果没有爆牌，则继续向玩家询问是否要牌。
        if player.burst():
            print("爆牌，您输了！")
            # 退出程序
            sys.exit()
    # 否则，没有要牌，则退出循环。（停牌）
    else:
        break
# 玩家停牌之后，庄家发牌。庄家在小于17点时，必须一直要牌。在大于等于17点，小于等于21点时，必须停牌。
while True:
    print("庄家发牌中……")
    # 因为庄家发牌不需要向玩家那样进行询问，所以没有停顿时间。程序会显示非常快速。
    # 为了能有一个很好的间隔性，我们在每次发牌时，暂停1秒。
    time.sleep(1)
    # 向庄家发牌
    cards.send_card(computer)
    # 更新显示庄家与玩家手中的牌。
    computer.show_card()
    player.show_card()
    # 判断庄家是否爆牌。如果爆牌，则庄家负。
    if computer.burst():
        print("庄家爆牌，您赢了！")
        sys.exit()
    # 如果没有爆牌，则判断庄家的牌面值是否达到17点，如果达到17点，则庄家必须停牌，否则，庄家必须继续要牌。
    elif computer.get_value("max") >= 17:
        break
# 如果庄家与玩家都没有爆牌，则根据手中的牌面点数，比价大小。
# 获取在不爆牌的前提下，可表示的最大点数。
player_value = player.get_value("max")
computer_value = computer.get_value("max")
# 比较点数大小，多者胜出。如果一样大，则平局。
if player_value > computer_value:
    print("您赢了！")
elif player_value == computer_value:
    print("平均")
else:
    print("您输了")

