#define remove remove_from_bst
#define bst_h


/** 
 * The structure of the bst allows it to trade space for reduced indivitual free and malloc calls; 
 */
typedef struct node{
	struct node	**children;
	void		*val;
	int			*key;
	int			keyVal;
	struct node *parent;
}bst;


static void 	__set_val(bst*tree, int key,void*data);
static bst		*__find_internal(bst*tree,int key);
static bst		*__create_bst_internal(bst*parent);
static int 		__non_empty_subtrees(bst*t);
static void		__node_swap(bst*,bst*);
static void		__destroy_empty_node(bst*);