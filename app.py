
# A very simple Flask Hello World app for you to get started with...
import math
from flask import Flask

app = Flask(__name__)

@app.route('/simath/<a>/<n>/<b>')
def UniS(a,n,b):
    match n:
        case "+":
            return str(float(a)+float(b))
        case "-":
            return str(float(a)-float(b))
        case "*":
            return str(float(a)*float(b))
        case "|":
            return str(float(a)/float(b))
        case "||":
            return str(float(a)//float(b))
        case "mod":
            return str(float(a)%float(b))

@app.route('/hamath/<name>/<a>/<b>/<meter>')
def UniH(name,a,b,meter):
    try:
        if (meter == "degrees"):
            match name:
                case "cos":
                    return str(math.cos(math.radians(float(a))))
                case "sin":
                    return str(math.sin(math.radians(float(a))))
                case "tan":
                    if float(a) % (math.pi / 2):
                        return "Unaccaptable number"
                    else:
                        return str(math.tan(math.radians(float(a))))
                case "pow":
                    bam = float(b)
                    am = float(a)
                    return str(math.pow(am,bam))
                case "sqrt":
                    if a < 0:
                        return "You can't get a square root out of negative number!"
                    else:
                        return str(math.sqrt(float(a)))
        elif (meter == "rads"):
            match name:
                case "cos":
                    af = float(a)
                    return str(math.cos(af))
                case "sin":
                    af = float(a)
                    return str(math.sin(af))
                case "tan":
                    af = float(a)
                    if af % (math.pi / 2):
                        return "Unaccaptable number"
                    return str(math.tan(af))
                case "pow":
                    bam = float(b)
                    am = float(a)
                    return str(math.pow(am,bam))
                case "sqrt":
                    if a < 0:
                        return "You can't get a square root out of negative number!"
                    else:
                        return str(math.sqrt(float(a)))
    except Exception as e:
        return "You've typed a wrong number, or letter! Try again"
