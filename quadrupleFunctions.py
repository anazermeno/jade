def validateOperator(operatorNew, operatorStack):
    # Validate for operator * and /
    if operatorNew == "*" or operatorNew == "/":
        if operatorStack == "*" or operatorStack == "/":
            return True
        else:
            return False
    elif operatorNew == "+" or operatorNew == "-":
        if operatorStack == "*" or operatorStack == "/" or operatorStack == "+" or operatorStack == "-":
            return True
        else:
            return False
    elif operatorNew == "<" or operatorNew == ">" or operatorNew == "<=" or operatorNew == ">=" or operatorNew == "!=" or operatorNew == "==":
        if operatorStack == "*" or operatorStack == "/" or operatorStack == "+" or operatorStack == "-" or operatorStack == "<" or operatorStack == ">" or operatorStack == "<=" or operatorStack == ">=" or operatorStack == "!=" or operatorStack == "==":
            return True
        else:
            return False
    elif operatorNew == "=":
        if operatorStack == "=" or operatorStack == "*" or operatorStack == "/" or operatorStack == "+" or operatorStack == "-" or operatorStack == "<" or operatorStack == ">" or operatorStack == "<=" or operatorStack == ">=" or operatorStack == "!=" or operatorStack == "==":
            return True
        else:
            return False
    else:
        return False