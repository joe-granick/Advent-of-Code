public class Wrapping {
    public static void main (String[] args)
    {
        int sum = 0;
        while(!StdIn.isEmpty())
        {
            String readDim = StdIn.readString();
            //System.out.println(readDim);
            String[] dimensions = readDim.split("x");
            //System.out.println(dimensions.length);
            
            int l = Integer.parseInt(dimensions[0]);  
            int w = Integer.parseInt(dimensions[1]);
            int h = Integer.parseInt(dimensions[2]);
            int side1 = l*w;
            int side2 = w*h;
            int side3 = h*l;
            int min = side1;
            if(side2 < min) min = side2;
            if(side3 < min) min = side3;

            sum+= ((2*side1) + (2*side2) + (2*side3) + min) ;
        }
        System.out.println(sum);
    }
}