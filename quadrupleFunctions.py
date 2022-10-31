def validateOperator(operatorNew, operatorStack):
    # Validate for operator * and /
    print("op new:", operatorNew)
    print("op stack:", operatorStack)
    if operatorNew == "*" or operatorNew == "/":
        if operatorStack == "*" or operatorStack == "/":
            return True
    elif operatorNew == "+" or operatorNew == "-":
        if operatorStack == "*" or operatorStack == "/" or operatorStack == "+" or operatorStack == "-":
            return True
    elif operatorNew == "<" or operatorNew == ">" or operatorNew == "<=" or operatorNew == ">=" or operatorNew == "!=" or operatorNew == "==":
        if operatorStack == "*" or operatorStack == "/" or operatorStack == "+" or operatorStack == "-" or operatorStack == "<" or operatorStack == ">" or operatorStack == "<=" or operatorStack == ">=" or operatorStack == "!=" or operatorStack == "==":
            return True
    elif operatorNew == "=":
        if operatorStack == "=" or operatorStack == "*" or operatorStack == "/" or operatorStack == "+" or operatorStack == "-" or operatorStack == "<" or operatorStack == ">" or operatorStack == "<=" or operatorStack == ">=" or operatorStack == "!=" or operatorStack == "==":
            return True
    else:
        return False