public class Solution {
    // Function to check if a linked list has a cycle
    public boolean hasCycle(ListNode head) {
        // Create a HashSet to store visited nodes
        HashSet<ListNode> visitedNodes = new HashSet<>();
        
        // Start at the head of the linked list
        ListNode currentNode = head;
        
        // Traverse the linked list
        while (currentNode != null) {
            // If the current node has been visited before, it means there is a cycle
            if (visitedNodes.contains(currentNode)) {
                return true; // Return true to indicate the presence of a cycle
            }
            
            // Add the current node to the set of visited nodes
            visitedNodes.add(currentNode);
            
            // Move to the next node in the linked list
            currentNode = currentNode.next;
        }
        
        // If the end of the linked list is reached without finding a cycle, return false
        return false;
    }
}
