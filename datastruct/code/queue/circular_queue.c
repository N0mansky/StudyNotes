typedef int QElemType; /* The type of QElemType was defined by actual situation,In there was presumed as int*/

/* The linear storage structure of circular queue */

typedef struct{
    QElemType data[MAXSIZE];
    int front; /* Head point */
    int rear; /* Rear point,if queue is not empty,this is indexed last position*/
} SqQueue;

/* Initialize an empty queue */
Status InitQueue(SqQueue *Q){
    Q->front=0;
    Q->rear=0;
    return OK;
}

/* Get the number of elements in Q,that is the current length of queue */
int QueueLength(SqQueue Q){
    return (Q.rear - Q.front+MAXSIZE)%MAXSIZE
}

/* If queue isn't full,append e to Q */
Status EnQueue(SqQueue *Q,QElemType *e){
    /* Checking whether Q is full */
    if((Q->rear+1)%MAXSIZE == Q->front)
        return ERROR;
    Q->data[Q->rear] = e;
    Q->rear=(Q->rear+1)%MAXSIZE; /* Backward point to next position */
    return OK;
}

Status DeQueue(SqQueue *Q,QElemType *e){
    if (Q->front==Q->rear)
        return ERROR;
    *e=Q->data[Q->rear];
    Q->front = (Q->front+1)%MAXSIZE;
    return OK;
}
