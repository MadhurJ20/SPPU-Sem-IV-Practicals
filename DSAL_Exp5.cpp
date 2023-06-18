/*
Madhur Jaripatke
Roll No. 55
SE A Computer
RMDSSOE, Warje, Pune
*/
/*
A book consists of chapters, chapters consist of sections and sections consist of
subsections. Construct a tree and print the nodes. Find the time and space requirements
of your method.
*/
# include <iostream>
using namespace std;
struct node
{
	char label[50];
	int ch_count;
	int sub_count;
	struct node *child[10];
}*root;
class Tree
{
	public:
		void create_tree();  
 		void display(node * r1);
 		Tree()
 		{
			root = NULL;
		}
};
void Tree::create_tree()
{
	int tbooks,tchapters,i,j,k;
	root = new node;
	cout<<"Enter Name of Book ";
	cin>>root->label;
	cout<<"Enter number of Chapters in Book ";
	cin>>tchapters; 
	root->ch_count = tchapters;
	for(i=0;i<tchapters;i++)
	{
		root->child[i] = new node;
		cout<<"Enter Chapter "<<i+1<<" Name ";
		cin>>root->child[i]->label;   
		cout<<"Enter no. of sections in Chapter "<<root->child[i]->label<<" ";
		cin>>root->child[i]->ch_count;
		for(j=0;j<root->child[i]->ch_count;j++)
		{
			root->child[i]->child[j] = new node;
			cout<<"Enter Section "<<j+1<<" Name\n";
			cin>>root->child[i]->child[j]->label;   
			cout<<"Enter no. of Subsections in "<<root->child[i]->child[j]->label<<" ";
			cin>>root->child[i]->sub_count;
		}
	}
}
void Tree::display(node * r1)
{
	int i,j,k,tchapters;
	if(r1!=NULL)
	{
		cout<<"\n\nBook Hierarchy Tree\n\n";
		cout<<"\nBook Title: "<<r1->label;
		tchapters = r1->ch_count;
		cout<<"\nChapters:";
		for(i=0;i<tchapters;i++)
		{
			cout<<"\nChapter "<<i+1<<":";
			cout<<" "<<r1->child[i]->label;   
			cout<<"\nSections:";
			for(j=0;j<r1->child[i]->ch_count;j++)
			{
				cout<<"\n"<<r1->child[i]->child[j]->label;
				cout<<"\nSubsections: "<<r1->child[i]->sub_count;
			}
			
		}
 }
}
int main()
{
	int ch;
	Tree t1;
	while (true)
	{
		cout<<"\nPlease Enter Your Choice:\n1. New Entry\t2. Display\n3. Quit ";
		cin>>ch;
		switch(ch)
		{
			case 1:
				t1.create_tree();
				break;
			case 2:
				t1.display(root);
				break;
			case 3:
				exit(0);
			default:
				cout<<"Invalid Choice"<<endl;
		}
	}
}
