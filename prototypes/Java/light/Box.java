class Box1{
    double width, height, length;

    Box1(int w, int h, int b){
        this.width  = w;
        this.height = h;
        this.length = b;
    }

    int volume(){
        return (int) (this.width*this.height*this.length);
    }


}

class Box{
    public static void main(String[] args){
        Box1 vol = new Box1(2,2,3);
        System.out.println("Volume is "+vol.volume());
    }

    protected void finalize(){
        System.out.println("\nClass finalised");
    }
}