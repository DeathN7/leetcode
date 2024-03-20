var isValid = function(s) {
    const stack = [];
    const map = {
        "(": ")",
        "[": "]",
        "{": "}"
    };
    for (let i = 0; i < s.length; i++) {
        if (map[s[i]]) {
            stack.push(s[i]);
        } else {
            const last = stack.pop();
            if (s[i] !== map[last]) {return false;}
        }
    }
    if (stack.length !== 0) {return false;}
    return true;
};