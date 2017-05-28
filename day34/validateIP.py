import re

def validateIP(ip):
    ipv4 = ip.split(".")
    ipv6 = ip.split(":")
    if len(ipv4) == 4 and isValidIPv4(ip):
        return "IPv4"
    elif len(ipv6) == 8 and isValidIPv6(ip):
        return "IPv6"
    else:
        return "Neither"

def isValidIPv4(ip):
    for s in ip.split("."):
        numDigits = len(s)

        if not 1 <= numDigits <= 3:
            return False

        if s.startswith("0"):
            return False

        if not re.match("[1234567890]{{{}}}".format(numDigits), s):
            return False

        if not 0 <= int(s) <= 255:
            return False
    return True

def isValidIPv6(ip):
    for s in ip.split(":"):
        numDigits = len(s)

        if not 1 <= numDigits <= 4:
            return False

        if not re.match("[1234567890abcdefABCDEF]{{{}}}".format(numDigits), s):
            return False
    return True

def testIsValidIPv4():
    assert isValidIPv4("172.16.254.1")
    assert not isValidIPv4("172.16.254.01")
    assert not isValidIPv4("172.16.256.1")
    assert not isValidIPv4("1e1.4.5.6")
    assert not isValidIPv4("1e1..5.6")

def testIsValidIPv6():
    assert isValidIPv6("2001:0db8:85a3:0000:0000:8a2e:0370:7334")
    assert isValidIPv6("2001:db8:85a3:0:0:8A2E:0370:7334")
    assert not isValidIPv6("2001:0db8:85a3:::8A2E:0370:7334")
    assert not isValidIPv6("02001:0db8:85a3:0000:0000:8a2e:0370:7334")
    assert not isValidIPv6("GGGG:0db8:85a3:0000:0000:8a2e:0370:7334")

def testValidateIP():
    assert validateIP("172.16.254.1") == "IPv4"
    assert validateIP("172.16.254.01") == "Neither"
    assert validateIP("172.16.254.01") == "Neither"
    assert validateIP("172.16.256.1") == "Neither"

    assert validateIP("2001:0db8:85a3:0000:0000:8a2e:0370:7334") == "IPv6"
    assert validateIP("2001:db8:85a3:0:0:8A2E:0370:7334") == "IPv6"
    assert validateIP("2001:0db8:85a3:::8A2E:0370:7334") == "Neither"
    assert validateIP("02001:db8:85a3:0:0:8A2E:0370:7334") == "Neither"

def main():
    testIsValidIPv4()
    testIsValidIPv6()
    testValidateIP()

if __name__ == "__main__":
    main()
