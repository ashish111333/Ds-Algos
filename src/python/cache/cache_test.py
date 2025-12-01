from cache import Dll,CacheItem,Node,LruCache


def test_dll():
    new_dll=Dll()
    cach_items=[CacheItem(3),CacheItem(2),CacheItem(1)]
    nodes=[]
    for ci in cach_items:
        nodes.append(new_dll.insert(ci)) 
        head_node=new_dll.head 
        assert ci.value==head_node.data.value
    
    assert  new_dll.size==len(cach_items)
    assert new_dll.tail is nodes[0]
    assert new_dll.head is nodes[2] 
    new_dll.delete(nodes[2])
    assert new_dll.head is nodes[1]
    new_dll.delete(nodes[0])
    assert new_dll.size==1 
    
    cache_items2=[CacheItem(4),CacheItem(5),CacheItem(6)]
    dll2=Dll()
    nodes=[dll2.insert(ci) for ci in cache_items2]
    assert nodes[0] is dll2.tail
    assert nodes[2] is dll2.head
    assert dll2.size==3
    
    # test shift_to_head

    dll2.shift_to_head(nodes[0])
    assert dll2.head is nodes[0]
    assert dll2.tail is nodes[1]
    assert dll2.size==3
    
    dll2.shift_to_head(dll2.tail)
    assert dll2.head is nodes[1]
    assert dll2.tail is nodes[2]
    assert dll2.size==3 
    dll2.shift_to_head(dll2.tail)
    assert dll2.head is nodes[2]
    assert dll2.tail is nodes[0]
    assert dll2.size==3
    
    
def test_lru_Cache():
    new_cache=LruCache(3)
    new_cache.set("a",1)
    new_cache.set("b",2)
    new_cache.set("c",3)
    assert new_cache.size==3
    assert new_cache.max_size==3
    assert new_cache.get("a")==1
    assert new_cache.get("b")==2
    assert new_cache.get("c")==3

    
    

    

    
    
    


           