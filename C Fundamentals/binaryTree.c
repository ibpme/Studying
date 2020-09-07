#include <stdlib.h>
#include <stdio.h>

typedef struct node
{
    int number;
    struct node* left;
    struct node* right;
}node;

void insert(node* tree,char leftOrRight,int num)
{

    node* t = malloc(sizeof(node));
    if (t != NULL)
    {
        t->number=num;
        t->left=NULL;
        t->right=NULL;
    };
    if(leftOrRight =='l')
    {
        tree->left = t;

    }
    else if(leftOrRight =='r')
    {
        tree->right = t;
    }
    
}

int main()
{
    node* tree = NULL;
    node* t = malloc(sizeof(node));
    if (t != NULL)
    {
        t->number=50;
        t->left=NULL;
        t->right=NULL;
    }
    else
    {
        return 1;
    };
    tree=t;    

    insert(tree,'l',25);
    insert(tree,'r',75);
    insert(tree->left,'l',10);
    insert(tree->left,'r',40);
    insert(tree->right,'l',60);
    insert(tree->right,'r',90);

    printf("Main %i\n",tree->number);
    printf("Left %i\n",tree->left->number);
    printf("Right %i\n",tree->right->number);
    printf("Left Left %i\n",tree->left->left->number);
    printf("Left Right %i\n",tree->left->right->number);
    printf("Right Left %i\n",tree->right->left->number);
    printf("Right RIght %i\n",tree->right->right->number);

    //Free Memory
    // while(tree != NULL)
    // {
    //     node* tmpLeft = tree->left;
    //     node* tmpRight = tree->right;
    //     free(tree);
    //     tree->left = tmpLeft;
    //     tree->right = tmpRight;
    // }
     
    return 0;
}
