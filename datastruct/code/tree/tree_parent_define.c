//
//  tree_define.c
//  
//
//  Created by Nomansky on 2019/5/21.



/* The parent representation of tree*/
#define MAX_TREE_SIZE  100
typedef int TElemType; /* Define the data type of tree to int*/
typedef struct PTNode   /*Struct of nodes*/
{
    TElemType data;     /*Node's data*/
    int parent;         /* Node's parent */
} PTNode;
typedef struct {        /* Sturct of tree*/
    PTNode nodes[MAX_TREE_SIZE]; /*Array of nodes*/
    int r,n;
} PTree;
