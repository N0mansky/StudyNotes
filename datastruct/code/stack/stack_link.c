typedef struct StackNode{
    SElemType data;
    struct StackNode *next;
} StackNode,*LinkStackPtr;

typedef struct LinkStack{
    LinkStackPtr top;
    int count;
} LinkStack;

Status Push(LinkStack *S,SElemType e){
    LinkStackPtr s =()malloc(sizeof(StackNode));
    s->data=e;
    s->next=S->top;
    S->top=s;
    s->count++;
}

Status Pop(LinkStack *S,SElemType *e){
    LinkStackPtr p;
    if(StackEmpy(*S))
        return ERROR;
    *e=S->top->data;
    p=S->top;
    S->top=S->top->next;
    free(p);
    S->count--;
    return OK;
}
