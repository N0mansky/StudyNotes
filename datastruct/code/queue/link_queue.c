typedef int QElemType;

typedef struct QNode{ /* The structure of nodes */
    QElemType data;
    struct QNode *next;
} QNode,*QueuePtr;

typedef struct{ /* The linktable structure of queue*/
    QueuePtr front,rear;
}LinkQueue;

/* Insert element e to Q */
Status EnQueue(LinkQueue *Q,QElemType e){
    QueuePtr s=(QueuePtr)malloc(sizeof(QNode));
    if(!s){
        exit(OVERFLOW);
    }
    s->data=e;
    s->next=NULL;
    Q->rear->next=s;
    Q->rear=s;
    return OK;
}

Status Dequeue(LinkQueue *Q,QElemType *e){
    QueuePtr p;
    if(Q->front==Q->rear){
        return ERROR;
    }
    p=Q->front->next; /* Store the head node to p*/
    *e=p->data;
    Q->front->next=p->next
    if(Q->rear==p){
        Q->rear=Q->front;
    }
    free(p);
    return OK;
}
