var isBalanced = function(root) {
    var height = function(node) {
        if (node === null) return 0;
        return Math.max(height(node.left), height(node.right)) + 1;
    };
    
    var helper = function(node) {
        if (node === null) return true;
        if (Math.abs(height(node.left) - height(node.right)) > 1) return false;
        return helper(node.left) && helper(node.right);
    };
    
    return helper(root);
};