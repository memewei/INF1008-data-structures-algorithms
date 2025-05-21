from doublylinkedlist import DoublyLinkedList
from doublylinkedlist import DoublyListNode

aList = DoublyLinkedList()
aNode = DoublyListNode(15)
aList.insertAtHead(aNode)
aNode2 = DoublyListNode(30)
aList.insertAtHead(aNode2)
aNode3 = DoublyListNode(40)
aList.insertAtHead(aNode3)
aList.printList()

aList.delete(30)
aList.printList()
aList.delete(3)
