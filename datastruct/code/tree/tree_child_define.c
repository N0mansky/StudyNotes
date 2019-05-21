//
//  tree_child_define.c
//  
//
//  Created by Nomansky on 2019/5/21.
//

#include <stdio.h>
/* The child representation of tree struct */
#define MAX_TREE_SIZE 100
typedef struct CTNode /* Child node */
{
    int child;
    struct CTNode *next;
} *ChildPtr;

typedef struct {    /* Defination of table head */
    TElemType data;
    ChildPtr firstchild;
} CTBox;

typedef struct {
    CTBox nodes[MAX_TREE_SIZE] /* Numbers of node */
    int r,n     /* Positon of root and nodes' count */
} CTree;

