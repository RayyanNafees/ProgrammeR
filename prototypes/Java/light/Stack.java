class Stacks{
    int[] stack;
    int items;
    int length;
   Stacks(int ln) {
       this.length = ln;
       stack = new int[ln];
       items = -1;

   }

    void push(int item){
        if (items<this.length-1)
            stack[++items] = item;
        else 
            System.out.println("Stack full");
    }

    int pop(){
        if (items > 0){
            return stack[items--];
        }

        System.out.println("Stack overflow");
        return 0;
    }

    void all(){
        for (int i=0; i<stack.length; i++)
            System.out.println(stack[i]);
    }

}

class Stack{
    public static void main(String args[]){
        Stacks x = new Stacks(10);
        for (int i=0; i<12; i++){
            x.push(i);
            System.out.println("pushed "+i);
        }

        for (int i=0; i<12; i++){
           System.out.println("popped"+ x.pop());
        }

        x.all();
        int y = () -> 2*2*2;
        System.out.println("lambda: "+y())
    }
}