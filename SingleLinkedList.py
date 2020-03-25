


'''Here all the operations on single linked lists are mentiond try out with your inputs '''


class LinkedList:
  def __init__(self):
    self.head=None                                      #Creating the linked list  Class
  def printing(self):                                      
    temp=self.head
    while(temp):
      print(temp.data)                                  #Printing the data in linkedlist
      temp=temp.next

class Node:
  def __init__(self,data):
    self.data=data                                        #creating the node Class
    self.next=None

glist=LinkedList()

glist.head=Node(10)
second=Node(12)
Third=Node(14)
Fourth=Node(16)

glist.head.next=second
second.next=Third
Third.next=Fourth

glist.printing()

class Node:
  def __init__(self,data):
    self.data=data
    self.next=None

class LinkedList:
  def __init__(self):
    self.head=None


  def append(self,data):
    new_node=Node(data)
    if self.head is None:
      self.head=new_node                                        # Appending the element to the linkedlist
      return
    last_node=self.head
    while last_node.next:
      last_node=last_node.next
    last_node.next=new_node

  def printing(self):
    current_node=self.head
    while current_node:                                         # Printing the elements of a linkedlist
      print(current_node.data,end=' ')
      current_node=current_node.next
  
  def length(self):
    current_node=self.head
    count=0
    while current_node:                                         # Length of a Linkedlist
      count=count+1
      current_node=current_node.next
    return count

  def prepend(self,data):
    new_node=Node(data)                                         # prepending the elements in a linkedlist
    new_node.next=self.head                         
    self.head=new_node
 
  def insert(self,prev_node,data):
    new_node=Node(data)
    new_node.next=prev_node.next                                # insert into Linkedlist by passing the node
    prev_node.next=new_node

  def inserti(self,index,data):
    current_node=self.head
    new_node=Node(data)
    i=0                                                         # inserting into a index position of a linkedlist
    while i<index-1:
      current_node=current_node.next
      i=i+1
    new_node.next=current_node.next
    current_node.next=new_node
  
  def deletenode(self,key):
    current_node=self.head
    if current_node and current_node.data==key:
      self.head=current_node.next
      current_node=None                                         # deleting the specified node
      return
    while current_node and current_node.data!=key:
      prev=current_node
      current_node=current_node.next
    if current_node is None:
      return
    prev.next=current_node.next
    current_node=None
  
  def deletenode_at_pos(self,ind):
    current_node=self.head
    count=0
    prev=None
    while current_node and count!=ind:                          # deleting node at a sepcified index
      prev=current_node
      count=count+1
      current_node=current_node.next
    prev.next=current_node.next
    current_node=None
  
  def swap_nodes(self,key1,key2):
    prev_1=None
    curr_1=self.head
    while curr_1 and curr_1.data!=key1:
      prev_1=curr_1
      curr_1=curr_1.next                                        # swapping the nodes
    
    prev_2=None
    curr_2=self.head
    while curr_2 and curr_2.data!=key2:
      prev_2=curr_2
      curr_2=curr_2.next
    if not curr_1 or not curr_2:
      return

    if prev_1:
      prev_1.next=curr_2
    else:
      self.head=curr_2
    if prev_2:
      prev_2.next=curr_1
    else:
      self.head=curr_1
    curr_1.next,curr_2.next=curr_2.next,curr_1.next
  

  def reverse_iterative(self):
    prev=None
    curr=self.head
    while curr:
      nxt=curr.next
      curr.next=prev                                            # Reversing the LinkedList

      prev=curr
      curr=nxt
    self.head=prev
  
  def remove_dup(self):
    curr=self.head
    glist=[]
    while curr:
      if curr.data in glist:
        prev.next=curr.next                                         #removing duplicates in a single linked list
      else:
        glist.append(curr.data)
        prev=curr  
      curr=curr.next

  def merge_sorted_list(self,llist):
    p=self.head
    q=llist.head
    s=None

    if not p:
      return q
    if not q:
      return p

    if p and q:
      if p.data<=q.data:
        s=p
        p=s.next
      else:
        s=q
        q=s.next
      new_head=s

    while p and q:
      if p.data<=q.data:
        s.next=p
        s=p
        p=s.next
      
      else:
        s.next=q
        s=q
        q=s.next
    if not p:
      s.next=q
    if not q:
      s.next=p
    return new_head



