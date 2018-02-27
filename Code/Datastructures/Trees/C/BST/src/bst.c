#include <stdlib.h>
#include <stdio.h>
#include <assert.h>



#include "bst.h" //Inner function declarations
#include "../incl/bst.h"//public functions

#define remove remove_from_bst
static void	__destroy_empty_node(bst*node){
	free(node->children);
	free(node);
}
static void __set_val(bst*tree, int key,void*data){
	tree->val = data;
	tree->key = &tree->keyVal;
	*tree->key = key;

	if (tree->children != NULL){

		if (!tree->children[0])
			tree->children[0] = __create_bst_internal(tree);
		
		if (!tree->children[1])
			tree->children[1] = __create_bst_internal(tree);
	
	}

}

void insert(bst *tree, int key, void*data){
	
	bst * n = NULL;
	n = __find_internal(tree,key);
	
	if (n == NULL)
		return;

	__set_val(n,key,data);

	return;

}

int  contains(bst*tree,int key){
	bst*res = __find_internal(tree,key);
	return res!=NULL && res->key;
}

void* retrieve(bst*tree,int key){
	return __find_internal(tree,key)->val;
}

static bst* __find_internal(bst*tree,int key){

	if (!tree) return NULL;
	
	if (tree->keyVal == key || !tree->key) return tree;
	
	int next = (unsigned)(tree->keyVal-key) >> 31 ;
	
	return __find_internal(tree->children[ next ], key);
}

void *remove(bst *tree, int key){

	bst *node = __find_internal(tree,key);
	if (!node) return NULL;

	int subtrees = __non_empty_subtrees(node);
	void *data;

	if (subtrees==0){
		data = node->val;
		node->val = NULL;
		node->key = NULL;
	}

	if (subtrees == 1){
		// Checking if we are on root by checking the parent of the node;
		// 		if we are at root, we swap the values between this and the next node
		//			and then we remove that node by calling remove again.
		if (node->parent){
			
			int side = (unsigned)(node->parent->key - node->key) >> 31 ;
			int nextChild = !(node->children[0]->key!=NULL);
			
			node->parent->children[side] = node->children[nextChild];
			node->children[nextChild]->parent = node->parent;
			data = node -> val;
			
			__destroy_empty_node(node->children[!nextChild]);
			__destroy_empty_node(node);
			
		}else{

			int side = !(node->children[0]->key!=NULL);
			bst* next = node->children[side];
			__node_swap(node,next);

			return remove(next,key);
		}
	
	}

	return data;

}

bst* createBst(){
	return __create_bst_internal(NULL);
}

static int 	__non_empty_subtrees(bst*t){	
	return (t->children[0]->key!=NULL) + (t->children[1]->key!= NULL);
}

static bst* __create_bst_internal(bst*parent){
	
	bst* t = malloc(sizeof(bst));
	t->children = malloc(2*sizeof(bst*));
	t->children[0] = NULL;
	t->children[1] = NULL;
	t->val = NULL;
	t->key = NULL;
	t->keyVal = 0;
	t->parent = parent;
	return t;
}

void destroyBst(bst*t){
	
	if (t==NULL) return;
	
	destroyBst(t->children[0]);
	destroyBst(t->children[1]);
	if (t->children)
		free(t->children);
	if (t->val)
		free(t->val);
	
	free(t);

}
void __node_swap(bst*alpha,bst*beta){

	void* temp;

	//swapping keys;
	
	*alpha->key += *beta->key;
	*beta ->key  = *alpha->key - *beta->key;
	*alpha->key  = *alpha->key - *beta->key;
	//Swapping data;
	temp = alpha->val;
	alpha->val = beta->val;
	beta->val = temp;

}



#ifdef DEBUG

int main(void){

	bst *u = createBst();
	
	int*o = malloc(sizeof(int*));
	*o = 15;
	insert(u,0,o);
	
	o = malloc(sizeof(int*));
	*o = 25;
	insert(u,1,o  );

	o = malloc(sizeof(int*));
	*o = 35;
	insert(u,2,o  );

	
	printf("contains 0: %d\n", contains(u,0));
	printf("contains 1: %d\n", contains(u,1));
	printf("contains 2: %d\n", contains(u,2));
	printf("contains -1: %d\n", contains(u,2));
	free(remove(u,1));
	printf("contains 1 after removing: %d\n", contains(u,1));
	destroyBst(u);
	printf("cleaned\n");


	u = createBst();
	printf("Creating a new tree, will insert and remove and reinsert");
	
	o = malloc(sizeof(int*));
	*o = 35;
	insert(u,2,o  );
	printf("inserted 2, check contains: %d\n", contains(u,2));
	free(remove(u,2));
	printf("removed 2, check contains: %d\n", contains(u,2));
	
	o = malloc(sizeof(int*));
	*o = 35;
	insert(u,2,o);
	printf("inserted 2, check contains: %d\n", contains(u,2));
	free(remove(u,2));
	printf("removed 2, check contains: %d\n", contains(u,2));

	destroyBst(u);

}

#endif