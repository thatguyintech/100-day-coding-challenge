def validateIP(ip):
    ipv4 = ip.split(".")
    ipv6 = ip.split(":")
    if len(ipv4) == 4 and validateIPv4(ipv4):
        return "IPv4"
    elif len(ipv6) == 8 and validateIPv6(ipv6):
        return "IPv6"
    else:
        return "Neither"

def validateIPv4(segments):
    digits = set("1234567890")
    for s in segments:
        # segment too long or too short
        if len(s) > 3 or len(s) == 0:
            return False

        # segment has leading 0
        if len(s) > 1 and s[0] == "0":
            return False

        # segment contains non-numeric digits
        if not set(s) < digits:
            return False

        # segment is not an int between 0 and 255 inclusive
        if int(s) > 255 or int(s) < 0:
            return False
    return True

def validateIPv6(segments):
    hexDigits = set("1234567890abcdefABCDEF")
    for s in segments:
        # segment too long or too short
        if len(s) > 4 or len(s) == 0:
            return False

        # segment contains non-hexadecimal digits
        if not set(s) < hexDigits:
            return False
    return True

def testValidateIPv4():
    assert validateIPv4(["172", "16", "254", "1"])
    assert not validateIPv4(["172", "16", "254", "01"])
    assert not validateIPv4(["172", "16", "256", "1"])
    assert not validateIPv4(["1e1", "4", "5", "6"])
    assert not validateIPv4(["1e1", "", "5", "6"])

def testValidateIPv6():
    assert validateIPv6(["2001", "0db8", "85a3", "0000", "0000", "8a2e", "0370", "7334"])
    assert validateIPv6(["2001", "db8", "85a3", "0", "0", "8A2E", "0370", "7334"])
    assert not validateIPv6(["2001", "0db8", "85a3", "", "", "8A2E", "0370", "7334"])
    assert not validateIPv6(["02001", "0db8", "85a3", "0000", "0000", "8a2e", "0370", "7334"])
    assert not validateIPv6(["GGGG", "0db8", "85a3", "0000", "0000", "8a2e", "0370", "7334"])

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
    testValidateIPv4()
    testValidateIPv6()
    testValidateIP()

if __name__ == "__main__":
    main()
