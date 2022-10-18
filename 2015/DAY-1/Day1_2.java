public class Day1_2
{
    public static void main(String[] args)
    {
        int floor = 0;
        int count = 0;
        int up = 0;
        int down = 0;
        while(!StdIn.isEmpty())
        {
            count++;
            char par = StdIn.readChar();
            //System.out.print(par);
            if (par == '(') floor++;
            if (par == ')') 
            {
            floor--;
            if (floor < 0) break;
            }
            
        }
        System.out.println(floor);
        System.out.println(count);
    }
}