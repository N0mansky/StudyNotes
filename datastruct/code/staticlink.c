# define MAXSIZE 1000

typedef struct
{
    ElemType data;
    int cur;    /*Cursor,Present 0 when no point*/
} Component,StaticLinkList[MAXSIZE]

/* Linking all backup link of space array to a back linklist */
/* space[0].cur is null point,"0" means null point */
Status InitList(StaticLinkList space){
    int i;
    for (i=0;i<MAXSIZE-1;i++)
        space[i].cur = i+1
    space[MAXSIZE-1].cur=0 /* At present static linklist is null,the last cur of element is 0*/
}

int Malloc_SLL(StaticLinkList space){
    /* Get first idle backup linktable's index*/
    int i = space[0].cur; /* First element cursor value of current array*/
    if (space[0].cur)
        space[0].cur = space[i].cur;
    return i
}

Status ListInsert(StaticLinkList L,int i,Element e){
    int j,k,l;  /*Declare three var,j:index of idel element,k:index of start element,l:loop's step var*/
    k = MAX_SIZE -1; /*Beware the 'k' is last element's index at first*/
    if (i<1 || i>ListLength(L) + 1) /*If the insert index greater or lesser than current position,return ERROR*/
        return ERROR;
    j = Malloc_SSL(L); /*Get the idle position of current array*/
    if(j){
        L[j].data = e; /* Assignment would be insert value to idle position*/
        for(l=1;l<i;l++) /* Traversing array to get before insert value's index*/
            k=L[k].cur;
        L[j].cur = L[k].cur; /* Assigning previous cursor to new element cursor*/
        L[k].cur = j; /* Assigning new element's cursor to previous element's cursor*/
        return OK;
    }
    return ERROR;
}

Status ListInsert(StaticLinkList L,int i){
    int j,k;
    if (i<1 || i > ListLength(L))
        return ERROR;
    k = MAX_SIZE -1;
    for(j=1;j<i;j++)
        k = L[k].cur;
    j = L[k].cur;
    L[k].cur=L[j].cur;
    Free_SSL(L,j);
    return OK;
}

void Free_SSL(StaticLinkList space,int k){
    space[k].cur = space[0].cur;
    space[0].cur = k;
}


int ListLength(StaticLinkList L){
    int j=0;
    int i=L[MAXSIZE-1].cur;
    while(i){
        i=L[i].cur;
        j++;
    }
    return j;
}







