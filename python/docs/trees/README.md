# Trees
A BT is a DS that has Nodes that have a left and right value

A BST is where values are stored in a way that makes finding and adding values very fast, structured so that values to the left are lesser than its parent node and values on the right are greater

## Challenge
write a post_order,pre_order, and in_order methods for a BT and an add and contains method for a BST

## Approach & Efficiency
for the BST methods it has a Time of O(log n) because while it does depend on the size of the input, the way the BST is structured makes it much faster. The methods have a Space of O(n) because it depends on the size of its input

## API
BT: post_order returns a list that has been appended in the following order: Left, Right, Root
    pre_order returns a list that has been appended in the following order: Root, Left, Right
    in_order returns a list that has been appended in the following order: Left, Root, Right

BST: add adds a value following the structure of a BST
     contains returns a boolean if the input value is in the BST
