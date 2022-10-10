# Semantic cube

SEMANTICA = {
    int: {
        int: {
            '*' : int,
            '/' : int,
            '+' : int,
            '-' : int,
            '>' : bool,
            '<' : bool,
            '<=' : bool,
            '>=' : bool,
            '==' : bool,
            '!=' : bool
        },
        float: {
            '*' : float,
            '/' : float,
            '+' : float,
            '-' : float,
            '>' : bool,
            '<' : bool,
            '<=' : bool,
            '>=' : bool,
            '==' : bool,
            '!=' : bool
        }
    },

    float:{
        int:{
            '*' : float,
            '/' : float,
            '+' : float,
            '-' : float,
            '>' : bool,
            '<' : bool,
            '<=' : bool,
            '>=' : bool,
            '==' : bool,
            '!=' : bool
        },
        float: {
            '*' : float,
            '/' : float,
            '+' : float,
            '-' : float,
            '>' : bool,
            '<' : bool,
            '<=' : bool,
            '>=' : bool,
            '==' : bool,
            '!=' : bool
        }
    },

    bool: {
        bool: {
            '&&' : bool,
            '||' : bool,
            '!'  : bool
        }
    }
}