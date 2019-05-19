typedef int SElementType;
typedef struct{
    SElementType data[MAXSIZE];
    int top;
} SqStack;

Status push(SqStack *S,SElementType e){
    if(S->top == MAXSIZE -1){ /* Stack full*/
        return ERROR;
    }
    S->top++;
    S->data[S->top]=e;
    return OK;
}

SElementType pop(SqStack *S){
    if(S->top == -1){ /* Stack emtpy */
        return ERROR;
    }
    return S->data[S->top--];
}

/* Double stack share store space */
typedef struct{
    SElementType data[MAXSIZE];
    int topf=-1;
    int topl=MAXSIZE;
} SrStack;

Status Srpush(SrStack *s,int type,SElementType e){
    if(s->topf+1==s->topl){ /* Stack full*/
        return ERROR;
    }
    if(type==0){
        s->data[++s->topf]=e;
    }else{
        s->data[--s->topl]=e;
    }
    return OK;
}

Status Srpop(SrStack *s,SElementType *e,int type){
    if(type==0){
        if(s->topf==-1){ /*First statck is empty */
            return ERROR;
        }
        *e = s->data[s->topf--];
    }else{
        if(s->topl==MAXSIZE){ /*Last statck is empty */
            return ERROR;
        }
        *e = s->data[s->topl++];
    }
    return OK;
}
