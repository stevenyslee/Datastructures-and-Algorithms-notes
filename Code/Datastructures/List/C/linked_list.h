//
// Created by Stelios on 05/01/2018.
//

#ifndef DS_AL_LINKED_LIST_H
#define DS_AL_LINKED_LIST_H

/**
 * next -> next element
 * element -> the current element in the node
 */
typedef struct ll_node{
    struct ll_node *next;
    void *element;
}ll_node;

int create_ll_node(ll_node *node, int _);

typedef struct{
    ll_node * head;
    int count;
}linked_list;

int   create_linked_list( linked_list *list,int count);
int   insert_linked_list( linked_list *list, void *element);
void* remove_linked_list( linked_list *list, void *element, int (comp)(const void*, const void*));
void* find_linked_list( const linked_list *list, void *element, int (comp)(const void*, const void*));
int   destroy_linked_list(linked_list *list, int destroy_elements);

#endif //DS_AL_LINKED_LIST_H
