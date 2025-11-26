# LRU cache and MRU cache 

from typing import Any,Dict

class CacheItem:
    def __init(self,value: Any,ttl: int):
        self.value=value
        self.ttl=ttl



    
class Node:
    def __init__(self,data: Any):
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
        if not self.size:
            self.head=Node(data)
            self.tail=self.head
            self.size+=1
        new_node=Node(data)
        new_node.l_ptr=self.head
        self.head.r_ptr=new_node
        self.head=new_node
        self.size+=1
        return new_node
    
    
    def delete(self,node: Node):
        l_node=node.l_ptr
        r_node=node.r_ptr
        l_node.r_ptr=r_node
        r_node.l_ptr=l_node
        node.l_ptr=None
        node.r_ptr=None
        
    @property
    def is_empty(self)->bool:
        if not self.size:
            return True
    
            
            
    
    
# Lru cache 
# key is mapped to a ddl node 
# each node will have cacheItem (see the implementation above) as data
# Time complexity of accessing any cache item will be O(1) same for deletion
# for set operation will add other item to head of ddl
        
class LruCache:
    ignore_ttl=True
    max_size=None
    size=0
    def __init__(self,max_size: int):
        self.cache_data: Dict[any,Node]={}
        self.max_size=max_size
        self.ddl=Dll()
    
    def set(self,key: any,ci: CacheItem):
        pass
        
       
    