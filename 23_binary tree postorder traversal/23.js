var postorderTraversal = function(root) {
    if (root === null) return [];
    return postorderTraversal(root.left).concat(postorderTraversal(root.right), [root.val]);
};