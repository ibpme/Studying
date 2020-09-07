#include <stdlib.h>
#include <stdio.h>
//LINKED LIST

//Create a node consisting of a number and a pointer
typedef struct node{
    int number;
    struct node *next;
}node;

//Function to push a number into a linked list
void push(node* listPointerToNode,int num){
 
    while(listPointerToNode->next != NULL)//Iterates to each node on the list and assigns each node pointer(next) to the next node in the list until it reached the end of the list
    {
        listPointerToNode = listPointerToNode->next; //The linkedList pointer doesn't change in main function because it is only changed in this stack, because we only get a copy of the list pointer variable and didn't derefrence the address(pointer) of the pointer
//^^ We didn't actually change the pointer reference ^^ Remember this is (*listPointerToNode).next
    };

    node* n = malloc(sizeof(node));
    if (n != NULL) 
    {
        n->number=num; 
        n->next=NULL; 
    }
    listPointerToNode->next = n; 

};

//Function to push a number into a linked list index
node* pushTo(node* listPointerToNode,int num,int index)
{
    node* originList = listPointerToNode;

    if(index==0)
    {
        node* n = malloc(sizeof(node));
        if (n != NULL) 
        {
            n->number=num; 
            n->next=listPointerToNode; 
        }
        return n;
    }
    for (int i = 0; i < index-1; i++)
    {
        if(listPointerToNode->next == NULL){
            break;
        };
        
        listPointerToNode = listPointerToNode->next;
    }

    node* n = malloc(sizeof(node));
    if (n != NULL) 
    {
        n->number=num; 
        n->next=listPointerToNode->next; 
    }
    listPointerToNode->next = n; 

    return originList;

};

//Remove the last element of the list
void pop(node* listPointerToNode)
{
    while(listPointerToNode->next->next != NULL)
    {
        listPointerToNode = listPointerToNode->next; 
    };
    node *n = listPointerToNode->next;
    listPointerToNode->next = NULL;
    free(n);
};

// Returns a new list and remove a list from an index
node* removeFrom(node* listPointerToNode,int index)
{
    node* originList = listPointerToNode;
    if(index==0)
    {
        originList=listPointerToNode->next;
        return originList;
    }
    for (int i = 0; i < index-1; i++)
    {
        listPointerToNode=listPointerToNode->next;
    }
   listPointerToNode->next = listPointerToNode->next->next;
   //Memory Loss here
   return originList;

};

int main(int argc, char const *argv[])
{
    //Intializing an empty list
    node* list = NULL;

    // Creating a new node for the number 1 in a temporary variable called n
    node* n = malloc(sizeof(node)); // Allocate memory for node n
    if (n != NULL) // Check if n is allocated in memory
    {
        n->number=0; // Acessing number property of n Equivalent to (*n).number=1
        n->next=NULL; // Creating  placeholder for the pointer and denoting th end of a list
    }
    else
    {
        return 1;
    };
    list=n; // Make the list point to the first node so that we can make a new node.
    //Add number 2 to a list 
    n = malloc(sizeof(node));
    if (n != NULL) 
    {
        n->number=1; 
        n->next=NULL; 
    }
    else
    {
        return 1;
    };
    list->next = n; //Make the first node point to second node we have just declared

    //Add number 3 to a list 
    n = malloc(sizeof(node));
    if (n != NULL) 
    {
        n->number=2; 
        n->next=NULL; 
    }
    else
    {
        return 1;
    };
    list->next->next = n; //Make the second node point to third node we have just declared
    push(list,3);
    push(list,4);
    push(list,6);
    push(list,7);
    list = pushTo(list,10,1);
    list = removeFrom(list,2);
    pop(list);
   

    for (node *tmp = list; tmp != NULL; tmp=tmp->next)
    {
        printf("%i\n",tmp->number);
    };

    // //Free Memory
    while (list != NULL)
    {
        node *tmp  = list->next;
        free(list);
        list=tmp;
    }
    return 0;
}
