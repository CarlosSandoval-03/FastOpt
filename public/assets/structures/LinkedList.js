class LinkedList {
	constructor() {
		this.head = null;
		this.tail = null;
		this.length = 0;
	}

	isEmpty() {
		return this.length === 0;
	}

	getLength() {
		return this.length;
	}

	toString() {
		let current = this.head;

		let representation = "[";
		while (current !== null) {
			representation += current.data + ",";
			current = current.next;
		}
		representation = representation.slice(0, -1);
		representation += "]";
		return representation;
	}

	print() {
		console.log(this.toString());
	}

	pushFront(data) {
		let newNode = new Node(data);
		newNode.next = this.head;
		this.head = newNode;

		if (this.tail === null) {
			this.tail = this.head;
		}
		this.length++;
	}

	topFront() {
		return this.head.data;
	}

	popFront() {
		if (this.isEmpty()) {
			console.error("EMPTY LIST");
			return null;
		}
		this.head = this.head.next;
		if (this.head === null) {
			this.tail = null;
		}
		this.length--;
	}

	pushBack(data) {
		let newNode = new Node(data);
		if (this.tail === null) {
			this.head = newNode;
			this.tail = this.head;
		} else {
			this.tail.next = newNode;
			this.tail = newNode;
		}
		this.length++;
	}

	topBack() {
		return this.tail.data;
	}

	popBack() {
		if (this.isEmpty()) {
			console.error("EMPTY LIST");
			return null;
		}
		if (this.head === this.tail) {
			this.head = null;
			this.tail = null;
		} else {
			let current = this.head;
			while (current.next.next !== null) {
				current = current.next;
			}
			current.next = null;
			this.tail = current;
		}
		this.length--;
	}

	find(data) {
		let current = this.head;

		while (current !== null) {
			if (current.data === data) {
				return true;
			}
			current = current.next;
		}
		return false;
	}

	findNode(data) {
		let current = this.head;
		while (current !== null) {
			if (current.data === data) {
				return current;
			}
			current = current.next;
		}
		return null;
	}

	findPos(data) {
		let current = this.head;
		let pos = 0;
		while (current !== null) {
			if (current.data === data) {
				return pos;
			}
			current = current.next;
			pos++;
		}
		return -1;
	}

	read(pos) {
		let current = this.head;
		for (let i = 0; i < pos; i++) {
			current = current.next;
		}
		return current.data;
	}

	insert(pos, data) {
		if (pos === 0) {
			this.pushFront(data);
		} else if (pos === this.length) {
			this.pushBack(data);
		} else {
			let current = this.head;
			let prev = null;
			for (let i = 0; i < pos; i++) {
				prev = current;
				if (current.next !== null) {
					current = current.next;
				}
			}
			prev.next = new Node(data);
			prev.next.next = current;
			this.length++;
		}
	}
}
