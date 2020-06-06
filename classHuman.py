class Human:
    name=""
    HP=300
    MP=100

    @classmethod
    def meet(cls):
        print('| 이름:{} | HP:{} | MP:{} | 안녕하세요 |'.format(cls.name,cls.HP,cls.MP))

class Player(Human):
    name="haeun"

    def __init__(self,AD):
        self.AD=AD 

    def att(self,enemy):
        enemy.HP -= (self.AD - enemy.DP) # 한 번 공격시 HP -50
        return enemy.HP

class Npc(Human):
    name="computer"

class Enemy(Human):
    name="enemy"

    def __init__(self,DP):
        self.DP=DP 

player=Player(60) # 공격력 AD
npc=Npc()
enemy=Enemy(10) # 방어력 DP

def init():
    while True :
        print('--------------------------------------------------')
        print('1. 인사말 + 캐릭터 상태\n2. attack 공격\n')
        user=input('선택하세요>> ')
        if user=='1':
            player.meet()
            npc.meet()
        elif user=='2':
            enemyHP = player.att(enemy)
            print("공격!!")
            if enemyHP>0:
                print("\n현재 enemy HP:",enemyHP)
            else :
                print("\n적이 죽었습니다. 게임이 종료되었습니다.\n")
                break

init()

