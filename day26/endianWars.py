def endianWar(expression):
    a, _ = expression.split("+")
    b, c = _.split("=")
    return int(a[::-1]) + int(b[::-1]) == int(c[::-1])

def testEndianWar():
    # little endian
    assert endianWar("73+42=16")
    assert endianWar("10+20=30")
    assert endianWar("11+44=55")
    assert endianWar("2466+7=9466")
    assert endianWar("2+19=39")
    assert endianWar("4+3=7")
    assert endianWar("714+8=524")
    assert endianWar("47+17=541")
    assert endianWar("99+54962=44072")

    # not little endian
    assert not endianWar("8861+81209=90070")
    assert not endianWar("5+8=13")
    assert not endianWar("649+68072=68721")
    assert not endianWar("65+72825=72890")
    assert not endianWar("930+70374=71304")

def main():
    testEndianWar()

if __name__ == "__main__":
    return main()
    