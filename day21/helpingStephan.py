def helpingStephan(x, y):
    xSplit = str(x).split(".")
    ySplit = str(y).split(".")
    
    XdigitsAfterDecimal = "0"
    if len(xSplit) > 1:
        XdigitsAfterDecimal = xSplit[1]
        
    YdigitsAfterDecimal = "0"
    if len(ySplit) > 1:
        YdigitsAfterDecimal = ySplit[1]
                                      
                                  
    digitsAfterDecimal = max(len(XdigitsAfterDecimal), len(YdigitsAfterDecimal))
                
    x *= 10**digitsAfterDecimal
    y *= 10**digitsAfterDecimal

    a = max(x, y)
    b = min(x, y)
     
    r = -1
    while r != 0:
        r = round(a % b, 6) * 1.0
        a = b
        b = r
        
    return a / 10**digitsAfterDecimal

def main():
    assert helpingStephan(2.4, 4.8) == 2.4
    assert helpingStephan(36.21, 4.19) == 0.01
    assert helpingStephan(4, 6) == 2
    assert helpingStephan(2.43, 4.899) == 0.003
    assert helpingStephan(47.804, 11.8683) == 0.0001
    assert helpingStephan(17.27568, 49.90752) == 1.91952
    assert helpingStephan(22.14728, 11.07364) == 11.07364

if __name__ == "__main__":
    main()
