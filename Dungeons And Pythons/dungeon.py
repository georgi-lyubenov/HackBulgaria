import hero
import orc


class Dungeon():
    def __init__(self, path):
        self.path = path

    def print_map(self):
        f1 = open(self.path, "r")
        content = f1.read()
        print(content)
        f1.close()
        return True

    def spawn(self, player_name, entity):

        m = []
        f2 = open(self.path, "r")
        for lines in f2:
            for char in lines:
                m.append(char)
        for i in range(len(m) - 1):
                if m[i] == "S":
                    if isinstance(entity, hero.Hero):
                        m[i] = "H"
                        break
                    elif isinstance(entity, orc.Orc):
                        m[i] = "O"
                        break
                    else:
                        print("invalid input")
        f2.close()
        f2 = open(self.path, "w")
        for i in m:
            f2.write(i)
        f2.close()
        return True

    def move(self, player_name, direction):
        if direction in ("up", "down", "left", "right"):
            m = []
            current_position = 0
            f2 = open(self.path, "r")
            for lines in f2:
                for char in lines:
                    m.append(char)
            f2.close()
            for i in range(len(m) - 1):
                if m[current_position + 1] == ".":
                    m[current_position] = "."
                    m[current_position + 1] = "H"
                    break
            f2 = open(self.path, "w")
            for i in m:
                f2.write(i)
            f2.close()
            return True
        else:
            return ("invalid input")
