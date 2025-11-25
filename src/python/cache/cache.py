# LRU cache and MRU cache 

from typing import Any,Dict

class CacheItem:
    def __init(self,value: Any,ttl: int):
        self.value=value
        self.ttl=ttl
    

# doubly linked list        
class Dll:
    size=0
    def __init__(self):
        self.head=None
        self.tail=None
    
    def insert(self,data: Any):
        if not self.size:
            self.head=Node(data)
            self.tail=self.head
        new_node=Node(data)
        new_node.l_ptr=self.head
        self.head.r_ptr=new_node
        self.head=new_node
        
        
            
            
         
    def delete():
        pass
    @property
    def is_empty(self)->bool:
        if not self.size:
            return True
    
            
            
    
    
    
class Node:
    def __init__(self,data: Any):
        self.data=data
        self.l_ptr: Node=None
        self.r_ptr: Node=None
        
class LruCache:
    ignore_ttl=True
    default_size=10
    size=0
    def __init__(self,size: int | None):
        self.cache_data: Dict[any,CacheItem]={}
        self.size=size
    

       
    