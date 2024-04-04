function digitSquareSum(n) {
    let sum = 0;
    while (n) {
        let digit = n % 10;
        sum += digit * digit;
        n = Math.floor(n / 10);
    }
    return sum;
}

var isHappy = function(n) {
    let slow = n;
    let fast = n;
    do {
        slow = digitSquareSum(slow);
        fast = digitSquareSum(fast);
        fast = digitSquareSum(fast);
    } while (slow !== fast);
    return slow === 1;
};