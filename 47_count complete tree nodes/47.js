var countNodes = function(root) {
    if (!root) return 0;
    let left = root.left;
    let right = root.right;
    let leftHeight = 1;
    let rightHeight = 1;
    while (left) {
        left = left.left;
        leftHeight++;
    }
    while (right) {
        right = right.right;
        rightHeight++;
    }
    if (leftHeight === rightHeight) {
        return Math.pow(2, leftHeight) - 1;
    }
    return 1 + countNodes(root.left) + countNodes(root.right);
};