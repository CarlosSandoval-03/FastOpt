class LinkedStack extends LinkedList {
	constructor() {
		super();
	}

	push(data) {
		super.pushFront(data);
	}

	top() {
		return super.topBack();
	}

	pop() {
		let tempValue = super.topBack();
		super.popBack();
		return tempValue;
	}
}
