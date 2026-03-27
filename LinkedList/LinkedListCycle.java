package CodeInterview_catolicasc.LinkedList;

public class LinkedListCycle {

    public static class ListNode {
        int value;
        public ListNode next;
        public Integer val;
        
        ListNode(int x) {
          value = x;
          next = null;
      }
    }

    public boolean hasCycle(ListNode head) {
        ListNode slow = head;
        ListNode fast = head;

        while(fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;

            if (fast == slow) {
                return true;
            }
        }

        return false;
    }

    public static void main(String[] args) {
        LinkedListCycle.ListNode n1 = new LinkedListCycle.ListNode(3);
        LinkedListCycle.ListNode n2 = new LinkedListCycle.ListNode(2);
        LinkedListCycle.ListNode n3 = new LinkedListCycle.ListNode(0);
        LinkedListCycle.ListNode n4 = new LinkedListCycle.ListNode(-4);

        n1.next = n2;
        n2.next = n3;
        n3.next = n4;
        n4.next = n2;

        LinkedListCycle response = new LinkedListCycle();
        boolean result = response.hasCycle(n1);

        System.out.println(result);
    }
}