def Google():
    print("Don't be evil")

second,*first,top = ["www","baidu","aaa","com"]
print(second)
print(first)
print(top)


url = {
    "Google":"Google.com",
    "Youtube":"Youtube.com",
    "Facebook":"Facebook.com",
    "GitHub":"GitHub.com",
}

print(max(zip(url.keys(),url.values())))

print(sorted(zip(url.keys(),url.values())))




class Enemy:
    life = 3

    def attack(self):
        print("掉一滴血")
        self.life -=1


    def check_life(self):
        if self.life <= 0:
            print("死了")
        else:
            print("还活着，你过来呀！")


enemy = Enemy()
enemy.attack()
enemy.check_life()
enemy.attack()
enemy.check_life()
enemy.attack()
enemy.check_life()


class work:
    def  __init__(self):
        print("构造函数被调用！")

    def oxox(self):
        print("oxox被调用")

www = work()
www.oxox()


class Girl:
    gender = '0'
    def __init__(self,name):
        self.name = name

oxox = Girl("oxox")

work = Girl("work")

print(oxox.name)
print(work.name)



#继承

class Parten():
    def print_last_name(self):
        print("Zou")


class Child(Parten):
    def print_first_name(self):
        print("Janus")

    def print_last_name(self):
        print(" aaa")

work = Child()
work.print_first_name()
work.print_last_name()


class Mario():
    def move(self):
        print("我在移动")

class BigMario():
    def eat_mushroom(self):
        print("我变大了")

class ShootMario(Mario,BigMario):
    def Shoot(self):
        print("我在射击")

shoot = ShootMario();

shoot.move()
shoot.eat_mushroom()
shoot.Shoot()