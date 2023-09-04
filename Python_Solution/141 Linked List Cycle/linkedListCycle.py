class Solution:
    # Function to check if a linked list has a cycle
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Create a set to store visited nodes
        visited_nodes = set()
        
        # Start at the head of the linked list
        current_node = head
        
        # Traverse the linked list
        while current_node:
            # If the current node has been visited before, it means there is a cycle
            if current_node in visited_nodes:
                return True  # Return True to indicate the presence of a cycle
            
            # Add the current node to the set of visited nodes
            visited_nodes.add(current_node)
            
            # Move to the next node in the linked list
            current_node = current_node.next
        
        # If the end of the linked list is reached without finding a cycle, return False
        return False
