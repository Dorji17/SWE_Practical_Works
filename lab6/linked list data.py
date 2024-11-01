1#middle element

class linkedlist:
    # ...(previous code)

    def find_middle(self):
        slow = self.head
        fast = self.hesd
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow.data if slow else None
    
    2#detect a cycle

    class linkedlist:
        # ...(previous code)

        def has_cycles(self):
            slow = self.head
            fast = self.head
            while fast and fast.next:
                slow = slow.next
                fast =fast.next.next
                if slow == fast:
                    return True
                return False
            

            