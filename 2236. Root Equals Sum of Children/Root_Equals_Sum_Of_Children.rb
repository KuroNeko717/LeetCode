# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val = 0, left = nil, right = nil)
#         @val = val
#         @left = left
#         @right = right
#     end
# end
# @param {TreeNode} root
# @return {Boolean}
def check_tree(root)
    return root.val == root.left.val + root.right.val;
    # or 
    #root.val == root.left.val + root.right.val

end