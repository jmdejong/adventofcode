
inp.match(/mul\(\d\d?\d?,\d\d?\d?\d?\)|do\(\)|don't\(\)/g).map(l=>l[0]!='m'?l:l.split("(")[1].split(")")[0].split(",").map(s=>Number.parseInt(s))).reduce((acc, curr) =>{ if (curr==="do()"){return [true, acc[1]]} else if (curr == "don't()") {return [false, acc[1]]} else if (acc[0]){return [true, acc[1] + curr[0] * curr[1]]}else{return acc} }, [true, 0])
