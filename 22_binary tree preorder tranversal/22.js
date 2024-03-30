var preorderTraversal = function(root) {
    if (root === null) return [];
    return [root.val].concat(preorderTraversal(root.left), preorderTraversal(root.right));
};