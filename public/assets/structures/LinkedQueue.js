class LinkedQueue extends LinkedList {
	constructor() {
		super();
	}

	enqueue(data) {
		this.pushBack(data);
	}

	dequeue() {
		let tempValue = this.topFront();
		this.popFront();
		return tempValue;
	}
}
