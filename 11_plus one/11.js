var plusOne = function(digits) {
    let i = digits.length - 1;
    while (i >= 0) {
        if (digits[i] === 9) {
            digits[i] = 0;
            i--;
        } else {
            digits[i]++;
            return digits;
        }
    }
    digits.unshift(1);
    return digits;
};