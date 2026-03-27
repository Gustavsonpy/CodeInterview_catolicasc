package CodeInterview_catolicasc.Stack;

import java.util.Stack;
import CodeInterview_catolicasc.LinkedList.LinkedListCycle.ListNode;

public class PalindromeLinkedList {
    public boolean isPalindrome(ListNode head) {
        Stack<Integer> stack = new Stack<>();
        ListNode temp = head;

        while (temp != null) {
            stack.push(temp.val);
            temp = temp.next;
        }

        while (head != null) {
            if (head.val != stack.pop()) {
                return false;
            }
            head = head.next;
        }

        return true;
    }
}