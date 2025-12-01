# LRU cache 

from typing import Any,Dict

class CacheItem():
    def __init__(self,value: Any,ttl: int=None):
        self.value=value
        self.ttl=ttl



    
class Node():
    def __init__(self,data: CacheItem):
        self.data=data
        self.l_ptr: Node=None
        self.r_ptr: Node=None
    

# doubly linked list        
class Dll:
    size: int=0
    def __init__(self):
        self.head: Node=None
        self.tail: Node=None
    
    def insert(self,data: Any):
        if not self.head:
            new_node=Node(data)
            self.head=new_node
            self.tail=self.head
            self.size+=1
            return new_node
        
        new_node=Node(data)
        new_node.l_ptr=self.head
        self.head.r_ptr=new_node
        self.head=new_node
        self.size+=1
        return new_node
    
    
    def delete(self,node: Node):
        if node is self.head:
            l_node=self.head.l_ptr
            l_node.r_ptr=None
            self.head=l_node
            self.size-=1
            return 
        if node is self.tail:
            r_node=self.tail.r_ptr
            r_node.l_ptr=None
            self.tail=r_node
            self.size-=1
            return
 
        l_node=node.l_ptr
        r_node=node.r_ptr
        l_node.r_ptr=r_node
        r_node.l_ptr=l_node
        node.l_ptr=None
        node.r_ptr=None
        self.size-=1
    
    def clear(self):
        self.head=None
        self.tail=None
        self.size=0
        
    # move a existing node to head, useful for LRU.
    def shift_to_head(self,node: Node):
        if node is self.tail:
            r_node=node.r_ptr
            r_node.l_ptr=None
            self.tail.l_ptr=self.head
            self.tail.r_ptr=None
            self.tail=r_node
            self.head=node
        if  node is self.head:
            return
            
            
        l_node=node.l_ptr
        r_node=node.r_ptr
        l_node.r_ptr=r_node
        r_node.l_ptr=l_node
        node.r_ptr=None
        node.l_ptr=self.head
        self.head=node
        

    @property
    def is_empty(self)->bool:
        if not self.size:
            return True
    

            
    
    
# Lru cache 
# key is mapped to a ddl node each node will have cacheItem (see the implementation above) as data.
# Time complexity of accessing any cache item will be O(1) same for deletion

class LruCache():
    
    max_size=None
    
    def __init__(self,max_size: int):
        self.cache_data: Dict[any,Node]={}
        self.max_size=max_size
        self.ddl=Dll()
    
    def set(self,key: Any,ci: CacheItem):
        node=self.ddl.insert(ci)
        self.cache_data[key]=node
            
        
    def get(self,key: Any):
        
        return self.cache_data.get(key)

        
    def delete(self,key: Any):
       self.cache_data.pop(key) 
        
    def empty_cache(self):
        self.cache_data.clear()
        self.ddl.clear()
    
    @property
    def size(self):
        return len(self.cache_data)
    