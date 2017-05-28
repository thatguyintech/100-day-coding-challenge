VOWELS = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])

def changeOfVowelsInCycle(cycle, text):
    rearranged = list(text)[::-1]
    vowelIndexes = [i for i, c in enumerate(rearranged) if c in VOWELS]
   
    numVowels = len(vowelIndexes) 
    if numVowels > 1:
        
        i = 0

        saved = [rearranged[vowelIndexes[j]] for j in xrange(cycle % numVowels)]
        while i < numVowels:
            vowelIndex = vowelIndexes[(i + cycle) % numVowels]
            saved.append(rearranged[vowelIndex])
            rearranged[vowelIndex] = saved.pop(0)

            i += 1
        
    return "".join(rearranged)

def testChangeOfVowelsInCycle():
    assert changeOfVowelsInCycle(1, "potato") == "ototap"
    assert changeOfVowelsInCycle(3, "this test is of potato") == "itetip fo sa tsot soht"
    assert changeOfVowelsInCycle(45, "aa bb cc dd ee ff gg hh ii jj") == "jj ea hh gg ff ai dd cc bb ie"
    assert changeOfVowelsInCycle(1, "abc") == "cba"
    assert changeOfVowelsInCycle(350, "a true magic is a potato think") == "knaht otatip i sa cegum airt o"
    assert changeOfVowelsInCycle(9, "CodeFights") == "sthgiFedoC"
    assert changeOfVowelsInCycle(10, "Ojf lsnelI UFlsn Eeiuo nnky Ynak jhA") == "ahj konY yknn uieEU nslFI elOnsl fjA"
    assert changeOfVowelsInCycle(28, "Once upon a time there lived three little foxes") == "sexif elttel eirht davol ureht Omet o nepi ecne"

def main():
    testChangeOfVowelsInCycle()

if __name__ == "__main__":
    main()

