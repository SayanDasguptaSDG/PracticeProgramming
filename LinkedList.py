class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList:
	def __init__(self):
		self.head = None

	def insertAtBeginning(self, data):
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
			return
		else:
			new_node.next = self.head
			self.head = new_node

	def insertAtEnd(self, data):
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
			return
		current_node = self.head
		while current_node.next:
			current_node = current_node.next
		current_node.next = new_node

	def insertAtIndex(self, data, index):
		new_node = Node(data)
		current_node = self.head
		position = 0
		if position == index:
			self.insertAtBeginning()
		else:
			while current_node is not None and position + 1 != index:
				position += 1
				current_node = current_node.next
			if current_node is not None:
				new_node.next = current_node.next
				current_node.next = new_node
			else:
				print("Index not present")

	def updateNode(self, value, index):
		current_node = self.head
		position = 0

		if position == index:
			current_node.data = value
		else:
			while current_node is not None and position != index:
				position += 1
				current_node = current_node.next
			if current_node is not None:
				current_node.data = value
			else:
				print("Index not present")

	def deleteAtFirst(self):
		if self.head is None:
			return
		self.head = self.head.next

	def deleteFromLast(self):
		if self.head is None:
			return
		current_node = self.head
		while current_node.next.next:
			current_node = current_node.next
		current_node.next = None

	def deleteFromIndex(self, index):
		if self.head is None:
			return
		current_node = self.head
		position = 0

		if position == index:
			self.deleteAtFirst()
		else:
			while current_node is not None and position + 1 != index:
				position += 1
				current_node = current_node.next

			if current_node is not None:
				current_node.next = current_node.next.next
			else:
				print("Index not present")

	def deleteForValue(self, data):
		current_node = self.head
		if current_node.data == data:
			self.deleteAtFirst()
			return
		while current_node is not None and current_node.next.data != data:
			current_node = current_node.next

		if current_node is None:
			return
		else:
			current_node.next = current_node.next.next

	def sizeOfLinkedList(self):
		size = 0
		if self.head:
			current_node = self.head
			while current_node:
				size += 1
				current_node = current_node.next
			return size
		else:
			return 0

	def printLinkedList(self):
		current_node = self.head
		while current_node:
			print(current_node.data)
			current_node = current_node.next


linkedList = LinkedList()
linkedList.insertAtBeginning('a')
linkedList.insertAtBeginning('b')
linkedList.insertAtEnd('c')
linkedList.insertAtEnd('d')
linkedList.insertAtBeginning('e')
linkedList.insertAtIndex('f', 3)
linkedList.updateNode('g', 5)
linkedList.deleteAtFirst()
linkedList.deleteFromLast()
linkedList.deleteFromIndex(3)
linkedList.deleteForValue('a')
linkedList.printLinkedList()
size = linkedList.sizeOfLinkedList()
print(size)
