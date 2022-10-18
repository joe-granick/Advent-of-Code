public class Day1_1
{
    public static void main(String[] args)
    {
        int floor = 0;
        int count = 0;
        int up = 0;
        int down = 0;
        while(!StdIn.isEmpty())
        {
            char par = StdIn.readChar();
            //System.out.print(par);
            if (par == '(') up++;
            if (par == ')') down++;
            count++;
        }
        System.out.println(up);
        System.out.println(down);
        System.out.println(up - down);
        System.out.println(count);
    }
}