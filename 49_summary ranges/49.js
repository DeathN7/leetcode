var summaryRanges = function(nums) {
    const result = [];
    for (let i = 0; i < nums.length; i++) {
        let start = nums[i];
        while (i + 1 < nums.length && nums[i + 1] - nums[i] === 1) {
            i++;
        }
        if (start !== nums[i]) {
            result.push(`${start}->${nums[i]}`);
        } else {
            result.push(`${start}`);
        }
    }
    return result;
};