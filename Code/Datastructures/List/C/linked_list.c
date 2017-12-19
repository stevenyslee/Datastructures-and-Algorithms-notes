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

int destroy_linked_list(linked_list *list,int count, int destroy_elements){
    void* start = list;
    for(;count>0;count--){
        while(list->head){
            ll_node *_to_del = list->head;
            list -> head = list -> head -> next;
            if (destroy_elements) free(_to_del->element);
            free(_to_del);
        }
        list++;
    }
    free(start);

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
int remove_linked_list( const linked_list *list, void *element, int (comp)(const void*, const void*)){

    return 0;
}
int find_linked_list( const linked_list *list, void *element, int (comp)(const void*, const void*)){

    return 0;
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