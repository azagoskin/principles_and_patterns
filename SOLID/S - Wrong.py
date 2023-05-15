# Single Responsibility Principle
# WRONG EXAMPLE

# the class contains two different objects and you need to make two separate classes
class LionAndTiger:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def show_lion(self):
        ascii_lion = """
            |\_                \|\||            
          -' | `.             -- ||||/
         /7      `-._        /7   |||||/
        /            `-.____/    |||||||/`-.____________
        \-'_                \-' |||||||||               `-._
         -- `-.              -/||||||||\                `` -`.
               |\              /||||||\             \_  |   `\\
               | \  \_______...-//|||\|________...---'\  \    \\
               |  \  \            ||  |  \ ``-.__--. | \  |    ``-.__--.
               |  |\  \          / |  |\  \   ``---'/ / | |       ``---'
             _/  / _|  )      __/_/  / _|  )     __/ / _| |
        :   /,__/ /,__/      /,_/,__/_/,__/     /,__/ /,__/       
        """
        print(ascii_lion)

    def show_tiger(self):
        ascii_tiger = """
                      __,,,,_
          _ __..-;''`--/'/ /.',-`-.
      (`/' ` |  \ \ \\ / / / / .-'/`,_
     /'`\ \   |  \ | \| // // / -.,/_,'-,
    /<7' ;  \ \  | ; ||/ /| | \/    |`-/,/-.,_,/')
   /  _.-, `,-\,__|  _-| / \ \/|_/  |    '-/.;.\'
   `-`  f/ ;      / __/ \__ `/ |__/ |
        `-'      |  -| =|\_  \  |-' |
              __/   /_..-' `  ),'  //
          fL ((__.-'((___..-'' \__.'
        """
        print(ascii_tiger)

l = LionAndTiger('lion', 100)
l.show_lion()

t = LionAndTiger('tiger', 100)
t.show_tiger()
