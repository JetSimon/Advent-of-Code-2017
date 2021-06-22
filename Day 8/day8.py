instructions = open('input.txt', 'r') 
reg = {}
best = 0

for inst in instructions:
    key = inst.split(" ")[0]
    reg[key] = 0 if key not in reg else reg[key]
    testcase = inst.split(" ", 4)[4]
    var = testcase.split(" ")[0]
    reg[var] = 0 if var not in reg else reg[var]
    testcase = testcase.replace(var, str(reg[var]))
    works = eval(testcase)

    if works:
        temp = reg[key]
        result = inst.split("if")[0]
        result = result.replace("inc", "+=").replace("dec", "-=").replace(key, "temp")
        result = compile(result,"<string>", "single")
        eval(result, locals())
        reg[key] = temp
        if temp > best:
            best = temp

print(best)