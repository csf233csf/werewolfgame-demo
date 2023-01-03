import random

class werewolfkill():
    def __init__(self):
        self.player = 12
        ## 预女猎白 预言家，女巫，猎人，白痴
        ## 4狼
        self.card = ['预言家','女巫','猎人','白痴','狼人','狼人','狼人','狼人','村民','村民','村民','村民']
        self.cure = True
        self.poison = True
        self.day = False
        self.daycount = 0
        self.poisoned = None
        self.prekill = None
        
    def distribute(self):
        identity = {}
        for n in range(1,13):
            random.shuffle(self.card)
            identity[f'player {n}'] = self.card.pop()
        return identity
    
    def prophet(self, identity, num):
        if identity[f'player {num}'] == '狼人':
            return False
        else:
            return True
    
    def witch(self, dead):
        if self.cure:
            answer = input(f'昨晚{dead}号玩家死亡, 请问是否使用解药 1是使用/2是不用: ')
            if answer == 1:
                self.cure = False
                return True
            else:
                self.cure = True

        elif self.poison:
            answer = input('请问是否使用毒药 1是使用/2是不用: ')
            if answer == 1:
                num = input('你要毒谁,输入1-12数字: ')
                return num
    
    def hunter(self):
        answer = input('请问想要射杀的玩家,请输入1-12: ')
        return answer
    
    def gamestart(self):
        identity = werewolfkill.distribute()
        print(identity)
        while True:
            if self.day:
                exenum = input('请输入被处决的玩家1-12: ')
                del identity[f'player {exenum}']
                print(f'player {exenum} 被处决')
                self.day = False
            else:
                if '预言家' in identity.values():
                    if werewolfkill.prophet(identity, num = input('预言家,请输入你要查验的玩家号码: ')):
                        print('你查验的玩家是好人')
                    else:
                        print('你查验的玩家是狼人')
                
                if '狼人' in identity.values():
                    self.prekill = input('请选择你要刀的玩家: ')
                    
                if '女巫' in identity.values():
                    if werewolfkill.witch(self.prekill):
                        self.prekill = None
                    else:
                        self.poisoned = werewolfkill.witch(self.prekill)
                
                if self.poisoned != None:
                    del identity[f'player {self.poisoned}']
                
                if self.prekill != None:
                    del identity[f'player {self.prekill}']
                
                print(f'昨晚, player {self.poisoned} and player {self.prekill} 死亡')
                
                self.day = True
                
            if '村民' not in identity.values():
                print('游戏结束,狼人胜利')
                break
            if '狼人' not in identity.values():
                print('游戏结束,好人胜利')
                break
            if '预言家' and '女巫' and '猎人' and '白痴' not in identity.values():
                print('游戏结束,狼人胜利')
                break
            
            print(identity)
                
    
if __name__ == "__main__":
    werewolfkill = werewolfkill()
    werewolfkill.gamestart()
