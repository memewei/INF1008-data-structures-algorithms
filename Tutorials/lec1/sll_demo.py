from singlylinkedlist import SinglyLinkedList
from singlylinkedlist import SinglyListNode

aList = SinglyLinkedList()
aNode = SinglyListNode(15)
aList.insertAtHead(aNode)
aNode2 = SinglyListNode(30)
aList.insertAtHead(aNode2)
aNode3 = SinglyListNode(40)
aList.insertAtHead(aNode3)
aList.printList()

aList.delete(30)
aList.printList()
aList.delete(3)
