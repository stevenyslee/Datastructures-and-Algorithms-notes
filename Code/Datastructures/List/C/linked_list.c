//
// Created by Stelios on 05/01/2018.
//

#include "linked_list.h"
#include "common.h"
#include <stdlib.h>
#include <assert.h>


int create_linked_list(linked_list *list,int count){
    assert(count >= 0);

    for(;count>0;count--){
        list -> count = 0;
        _new((list->head),ll_node);
        list++;
    }

    return 0;
}

int create_ll_node(ll_node *node, int _){
    node -> element = 0x0;
    node -> next = 0x0;
    return 0;
}

int destroy_linked_list(linked_list *list, int destroy_elements){
    
    while(list->head){
        ll_node *_to_del = list->head;
        list -> head = list -> head -> next;
        if (destroy_elements) 
            free(_to_del->element);
        free(_to_del);
    }
    free(list);

    return 0;
}

int insert_linked_list( linked_list *list, void *element){
    assert(list);

    ll_node *new;
    _new(new,ll_node);

    new->next = list->head;
    new->element = element;

    list -> head = new;
    list -> count ++;

    return 0;
}
/**
 * Create an indivitual node that is outside the list and points to a node in the list.
 * This allows us to traverse the list, from the beginning to the end with less
 * cases to check.
 */
void* remove_linked_list(linked_list *list, void *element, int (comp)(const void*, const void*)){

    struct holder{
        ll_node* next;
        ll_node* current;
        void* element;
    } curr = {list->head,NULL, NULL};

    while(curr.next && !curr.element){
        curr.element = comp(element,curr.next->element)? NULL: curr.next -> element;
        curr.current = curr.element? curr.current: curr.next;
        curr.next = curr.element? curr.next: curr.next -> next;
    }
    
    // no next
    // we found element.
    // if we found element

    
    list -> count -= curr.element != NULL;

    return curr.element;
}

/**
 * Return pointer/null if found/not found
 */
void* find_linked_list( const linked_list *list, void *element, int (comp)(const void*, const void*)){

    linked_list l = {list->head,0};
    int flag = 1;
    while (l.head && flag){
        flag = comp(l.head,element);
        l.head = flag? l.head -> next : l.head;
    }

    return flag? NULL : l.head;
}


#ifdef DEBUG
int main(void)
{
    linked_list* list;
    void* elems[2] = {malloc(30),malloc(30)};
    _new(list, linked_list);
    insert(list,linked_list,elems[0]);
    insert(list,linked_list,elems[1]);
    destroy(list,linked_list,1);
}
#endif