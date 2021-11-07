public class LinkedStack {
    private int N;
    private Node top;

    public LinkedStack() {
        N = 0;
        top = null;
    }

    public boolean isEmpty() {
        return N == 0;
    }

    public int size() {
        return N;
    }

    public int pop() {
        if (!isEmpty()) {
            int result = top.getData();
            top = top.getNext();
            return result;
        }
        return 0;
    }

    public boolean push(int item) {
        Node n = new Node(item);
        if (isEmpty()) {
            top = n;
        } else {
            n.setNext(top);
            top = n;
        }
        N++;
        return true;
    }

    public void display() {

    }
}
