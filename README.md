# Linked Lists

## Overview

  In contrast to an ordered list where the position of each item can be known by the position one is in the list, unordered lists cannot. The position of items are only known by the link between items and so that link determines the position of the next time and the position of each item can be known in that way. But the first item of the list must be known so we can determine where to go from there. The first item is referred to as the head. We also need the last item to know that there are no more items after it. 

  Linked lists are made using a Node object or a instance of the class Node. A node holds two pieces of information, the list item itself (the data field) and a reference to the next node. 

## The Node Class

Each position in an unordered list can be referred to as a Node. A Node as two primary characteristics, it contains data and a reference to the next Node.  The first Node in an unordered list is referred to as the Head. The Head doesn't have a prior Node link and could have a link to a subsequent Node. The last Node in an unordered list doesn't have a next Node but does is connected to a prior Node. 

The Node class contain methods associated with this structure. So there is a constructor method that sets (initially) the data value and next reference. The next reference is initially described as None as an unordered list doesn't yet exist. 

The class continues with methods for data and next as well as setting both data and next. 

## The LinkedList Class

The LinkedList Class contains methods for both traversing the list (a feat made simple by the next methods in the Node class), and for manipulating the list. As with index-determined lists, this class contains methods such as deleting, adding, and finding. Where the contrast between deterministic (in the sense of index) and unordered lists is apparent, is in keeping track of Node and next when adding and removing Nodes. For example, in adding a new item to the list, the item that was the head is now the next item and the new item is the head. 