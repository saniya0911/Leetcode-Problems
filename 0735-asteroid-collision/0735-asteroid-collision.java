class Solution {
    public int[] asteroidCollision(int[] asteroids) {
        Stack<Integer> stack = new Stack<>();
        int f =0;
        for(int i=0;i<asteroids.length;i++)
        {
            int a = asteroids[i];
            if(a>0)
            f++;
            if(f==0|| a>0)
            stack.add(a);
            else
            {
                int flag =0;
                if(stack.peek()+a>0)
                    continue;
                while(!stack.isEmpty() && stack.peek()*a<0)
                {
                    if(stack.peek()+a<0)
                    stack.pop();
                    else if(stack.peek()+a>0)
                    {
                        flag=1;
                        break;
                    }
                    else
                    {
                        stack.pop();
                        flag=1;
                        break;
                    }
                }
                if(flag==0)
                stack.add(a);
            }
            if(stack.isEmpty())
            f=0;
        }
        int ans[]=new int[stack.size()];
        for(int j =stack.size()-1;j>=0;j--)
        ans[j]=stack.pop();

        return ans;
    }
}